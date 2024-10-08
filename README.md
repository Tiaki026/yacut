# УаCut

![image](https://github.com/user-attachments/assets/bd8a0829-feac-4240-8749-d5912df93dc9)


# Оглавление
- [:page_with_curl: Описание](https://github.com/Tiaki026/yacut#page_with_curl-описание)
- [Процесс разработки, особенности и трудности](https://github.com/Tiaki026/yacut?tab=readme-ov-file#процесс-разработки-особенности-и-трудности)
  - [Было изучено](https://github.com/Tiaki026/yacut?tab=readme-ov-file#было-изучено)
  - [Трудности возникшие в работе](https://github.com/Tiaki026/yacut?tab=readme-ov-file#трудности-возникшие-в-работе)
- [:computer: Стек технологий](https://github.com/Tiaki026/yacut?tab=readme-ov-file#computer-стек-технологий)
- [:page_with_curl: Как воспользоваться проектом](https://github.com/Tiaki026/yacut#page_with_curl-как-воспользоваться-проектом)
- [Автор](https://github.com/Tiaki026/yacut?tab=readme-ov-file#автор)

## :page_with_curl: Описание
YaCut - сервис для укорачивания ссылок. Принцип работы прост, на сайте вас ждут всего два поля и одна кнопка. Первое поле - поле для вашей длинной ссылки, с которой будет вестись работа. Второе поле - поле, в котором будет вариант ссылки предложенный вами, либо ссылка сгенерируется автоматически.

## Процесс разработки, особенности и трудности
Проект по курсу "**Python-разработчик+**" [Яндекс Практикума](https://github.com/yandex-praktikum).

### Было изучено:
Flask - долго его игнорировал и вот наконец пришел к нему. Интересный, совсем не Django, но тоже хорошо. На некоторых работах хотят знание Flask, лишним не будет, быть может даже когда-то напишу на нем что-то еще, но мне кажется его съест FastAPI.
HTML - не отпускает меня HTML, надеюсь не съест.
SQLAlchemy - крутая БД, позволяет описывать структуры баз данных и способы взаимодействия с ними на языке Python без использования SQL.

### Трудности возникшие в работе
Работа не показалась легкой. На этапе узучения все казалось гораздо проще. Самое противное это тесты, которые требуют определенный вывод строк с ошибками, не люблю так. ~Пригорел.~ Гораздо приятнее видеть не роботизированные ошибки. Все остальное не вызывает особой сложности.

## :computer: Стек технологий
- ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
- ![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
- ![SQLAlchemy](https://camo.githubusercontent.com/002ee4ca516670df2b07f9fead4c132c71b7f367002ab21681a686c923c0acd6/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f73716c616c6368656d792d6662666266623f7374796c653d666f722d7468652d6261646765)
- ![Flask](https://camo.githubusercontent.com/caeca246a36e19149fde4f4bea527bd4b13ef7ed3ed059549d1cde0a5ff4abd8/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f666c61736b2d2532333030302e7376673f7374796c653d666f722d7468652d6261646765266c6f676f3d666c61736b266c6f676f436f6c6f723d7768697465)


## :page_with_curl: Как воспользоваться проектом
Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Tiaki026/yacut.git
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
создать бд и миграции
```
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```
запустить
```
flask run
```

## Автор:
  - [Колотиков Евгений](https://github.com/Tiaki026)
## 

  ## [:top: Путь наверх :top:](https://github.com/Tiaki026/yacut#оглавление)
