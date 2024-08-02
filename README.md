Коллекция алгоритмов и структур данных 

## Управление зависимостями

Для управления зависимостями локально применяется poetry

* Установка [poetry](https://python-poetry.org/docs/#installation)

* Установка зависимостей
  ```shell
  poetry install
  ```

* Добавление зависимостей
  ```shell
  poetry add <package_name>
  ```
  
* Фиксация версий зависимостей
  ```shell
  poetry lock
  ```
  
* Экспорт зависимостей в requirements.txt и requirements-dev.txt
  ```shell
  poetry export --format requirements.txt -o requirements.txt --without-hashes --without-urls
  poetry export --format requirements.txt -o requirements-dev.txt --without-hashes --without-urls --with dev
  ```

## Тесты

Для тестов используется библиотека [pytest](https://docs.pytest.org)

### Выполнение тестов

Чтобы запустить тесты, необходимо в корневой папке проекта выполнить команду:

```shell
pytest
```

### Измерение покрытия
Покрытие кода тестами замеряется автоматически с помощью плагина [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/)

### HTML-отчет по покрытию

По окончании выполнения тестов HTML-отчет о покрытии можно найти в директории `./htmlcov`
