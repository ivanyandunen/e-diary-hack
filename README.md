# Скрипты для модификации электронного дневника школы

Файл scripts.py содержит следующие функции:

- `fix_marks` - Исправляет все оценки ученика ниже 4 на 5.

Например:
```
fix_marks('Фролов Иван')
```

- `remove_chastisements` - Удаляет все замечания ученика.

Например:
```
remove_chastisements('Фролов Иван')
```

- `create_commendation` - Добавляет похвалу от учителя ученику по выбранному предмету.

Например:
```
create_commendation('Фролов Иван', 'Музыка')
```

Скрипт не отработает, если найдено несколько учеников с одинаковыми именами или ни одного. Попробуйте уточнить имя (Например, указать отчество)

## Запуск

- Файл scripts.py необходимо скачать в каталог содержащий файл `manage.py`
- Запустить в терминале
```
python3 manage.py shell
```
- Импортировать необходимую функцию

Например:
```
from scripts import fix_marks
```
- Запустить функцию как в примерах выше.

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
