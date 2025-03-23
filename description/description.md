# Lab description

1) Настройка CI \ CD:

Скрипт:
```yaml
name: Combined CI/CD

on:
  push:
    branches: ["main", "development"]
  pull_request:
    branches: ["main", "development"]

jobs:
  build-app:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.x"

      - name: Install dependencies
        run: |
          pip install -r requirements.txt -r requirements-dev.txt

      - name: Run tests
        run: pytest

  build-docs:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.x"

      - name: Install documentation dependencies
        run: pip install -r requirements-dev.txt

      - name: Build documentation
        run: mkdocs build

      - name: Deploy to GitHub Pages
        # if: github.ref == 'refs/heads/main'
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./site
          keep_files: false
          user_name: "ariinabel"
          user_email: "arina_belyakova04@mail.ru"

  automerge:
    needs: [build-app, build-docs]
    runs-on: ubuntu-latest
    # if: |
    #   github.event_name == 'pull_request' &&
    #   github.event.pull_request.user.login == 'dependabot[bot]'
    permissions:
      contents: write
      pull-requests: write
    steps:
      - name: Enable auto-merge
        uses: peter-evans/enable-pull-request-automerge@v3
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          pull-request-number: ${{ github.event.pull_request.number }}
          merge-method: squash
```

В репозитории:
![ci script](images/image.png)

2) workflow и их статус:

![ci script](images/image2.png)

Логи:

![ci script](images/image3.png)

3) Пример тестов:

```python
import pytest
from src.calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
])
def test_addition(calc, a, b, expected):
    assert calc.add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (7, 2, 5),
    (10, 10, 0),
    (-1, -1, 0),
])
def test_subtraction(calc, a, b, expected):
    assert calc.subtract(a, b) == expected
```

Лог запуска тестов:

![ci script](images/image4.png)

4) Новая функция из ветки `development`

![ci script](images/image5.png)

