# Final work on the course "Autotests in Python. Basic part"
## Pizzeria website test automation project in Python


Demo: https://drive.google.com/file/d/1d3LH800oM9Gw_YJJXuf6UdMTfXcxOucL/view?usp=sharing

Site under test: http://pizzeria.skillbox.cc/ <br/>

Test cases: https://docs.google.com/spreadsheets/d/1Ms4yhNOKAkT6Z1eNObU9w9Xdl9DEHlI7TPmEhpo5LKo/edit?usp=sharing <br/>

Bug reports: https://docs.google.com/document/d/13F0pb54A9We7DKpHiS0LCqg7vxCNT0ECCyEKM4H4EhE/edit?usp=sharing <br/>

Task: https://drive.google.com/file/d/1e1R_tIH3qIVPTtwK4aIe-SB9qFjSRZhh/view?usp=sharing

### Repository structure

* **resource:** chromedriver.exe and test data
* **src.fixtures:** fixtures
* **src.locators:** modules with description of locators for searching elements on tested pages
* **src.pages:** modules describing methods (actions) that are performed on pages during tests
* **src.utils:** modules with helper functions
* **tests**: modules with test descriptions
* Configuration files:
   * **flake8:** configuration file for the flake8 linter
   * **conftest.py:** local plugin for fixtures and logging
   * **logging.ini:** pytest configuration file
   * **pytest.ini:** main pytest configuration file
* **requirements.txt:** libraries required for operation

### Technologies used

* Python (3.10)
* Selenium WebDriver
* selenium wire
* Pytest
* Allure Framework
* flake8

### Installation
Copy all content from the repository to a new directory.<br/>
Install all required libraries.
1. Selenium `pip install selenium`
2. Selenium Wire `pip install selenium-wire`
3. Pytest 'pip install pytest'
4. Flake8 `pip install flake8`
5.Allure <br/>
In a PowerShell terminal, run:
```command line
> Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
> irm get.scoop.sh | iex
```
Next in PowerShell run:
`scoop install allure`<br/>
Next, on the command line, run: `pip install allure-pytest`

Run tests from package **tests**






# Итоговая работа по курсу "Автотесты на Python. Базовая часть"
## Проект по автоматизации тестирования сайта Pizzeria на Python


Демо: https://drive.google.com/file/d/1d3LH800oM9Gw_YJJXuf6UdMTfXcxOucL/view?usp=sharing

Тестируемый сайт: http://pizzeria.skillbox.cc/ <br/>

Тест кейсы: https://docs.google.com/spreadsheets/d/1Ms4yhNOKAkT6Z1eNObU9w9Xdl9DEHlI7TPmEhpo5LKo/edit?usp=sharing <br/>

Баг репорты: https://docs.google.com/document/d/13F0pb54A9We7DKpHiS0LCqg7vxCNT0ECCyEKM4H4EhE/edit?usp=sharing <br/>

Задание: https://drive.google.com/file/d/1e1R_tIH3qIVPTtwK4aIe-SB9qFjSRZhh/view?usp=sharing


### Структура репозитория

* **resource:** chromedriver.exe и тестовые данные
* **src.fixtures:** фикстуры
* **src.locators:** модули с описанием локаторов для поиска элементов на тестируемых страницах
* **src.pages:** модули с описанием методов (действий), которые выполняются на страницах во время прохождения тестов
* **src.utils:** модули со вспомогательными функциями
* **tests**: модули с описанием тестов
* Конфигурационные файлы:
  * **flake8:** конфигурационный файл для линтера flake8
  * **conftest.py:** локальный плагин, подключающий фикстуры и логирование
  * **logging.ini:** конфигурационный файл pytest
  * **pytest.ini:** основной конфигурационный файл pytest
* **requirements.txt:** библиотеки, необходимые для работы

### Используемые технологии

* Python (3.10)
* Selenium WebDriver
* Selenium Wire
* Pytest
* Allure Framework
* Flake8

### Установка
Скопировать все содержимое из репозитория в новый каталог.<br/>
Установить все необходимые библиотеки.
1. Selenium `pip install selenium`
2. Selenium Wire `pip install selenium-wire`
3. Pytest 'pip install pytest' 
4. Flake8 `pip install flake8`
5. Allure <br/>
В терминале PowerShell запустить:
```commandline
> Set-ExecutionPolicy RemoteSigned -Scope CurrentUser 
> irm get.scoop.sh | iex
```
Далее в PowerShell выполнить:
`scoop install allure`<br/>
Далее в командной строке выполнить: `pip install allure-pytest`

Запустить тесты из пакета **tests**
