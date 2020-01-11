# Скрипты для модификации электронного дневника школы

Файл scripts.py содержит следующие функции:

- fix_marks - Исправляет все оценки ученика ниже 4 на 5.

Например:
```
fix_marks('Фролов Иван')
```

- remove_chastisements - Удаляет все замечания ученика.

Например:
```
remove_chastisements('Фролов Иван')
```

- create_commendation - Добавляет похвалу от учителя ученику по выбранному предмету.

Например:
```
create_commendation('Фролов Иван', 'Музыка')
```

В том случае если скрипт находит несколько человек с подходящим именем или не находит ни одного, выдается соответствующее сообщение, и никаких действий выполнено не будет. Попробуйте уточнить имя (Например, указать отчество)

## Запуск

- Файл scripts.py необходимо скачать в корневой каталог содержащий сайт дневника
- Запустить python3 manage.py shell
- Импортировать необходимую функцию

Например:
```
from scripts import fix_marks
```
- Запустить функцию как в примерах выше.

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).