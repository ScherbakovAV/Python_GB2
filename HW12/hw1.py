"""Создайте класс студента.
- Используя дескрипторы проверяйте ФИО на первую заглавную букву и
наличие только букв.
- Названия предметов должны загружаться из файла CSV при создании
экземпляра. Другие предметы в экземпляре недопустимы.
- Для каждого предмета можно хранить оценки (от 2 до 5) и результаты
тестов (от 0 до 100).
- Также экземпляр должен сообщать средний балл по тестам для каждого
предмета и по оценкам всех предметов вместе взятых."""

import csv


class WordsCapitalize:
    """Дескриптор для проверки слова на наличие только букв и первую заглавную букву"""

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    @staticmethod
    def validate(value):
        """Валидатор, проверяющий слово на наличие только букв и первую заглавную букву"""
        if not value.isalpha():
            raise TypeError(f'Параметры ФИО должны состоять только из букв!')
        if not value.istitle():
            raise ValueError(f'В параметрах ФИО первая буква должна быть большой!')


class NumberRange:
    """Проверка вхождения числа в диапазон"""

    def __init__(self, min_num: int = None, max_num: int = None):
        self._min_num = min_num
        self._max_num = max_num

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        """Валидатор, проверяющий вхождение числа в диапазон"""
        if not isinstance(value, int):
            raise TypeError(f'Значение {value} должно быть целым числом')
        if self._min_num is not None and value < self._min_num or self._max_num is not None and value > self._max_num:
            raise ValueError(f'Значение {value} должно быть в диапазоне от {self._min_num} до {self._max_num}')


class Student:
    """Класс, хранящий Ф.И.О., названия предметов, оценки и результаты тестов.\n
    Экземпляр класса сообщает средний балл по тестам для каждого предмета
    и по оценкам всех предметов вместе взятых."""
    _last_name = WordsCapitalize()
    _name = WordsCapitalize()
    _patronymic = WordsCapitalize()
    _grades = NumberRange(2, 5)
    _test_results = NumberRange(0, 100)

    def __init__(self, last_name: str, name: str, patronymic: str, file_name: str):
        self._last_name = last_name
        self._name = name
        self._patronymic = patronymic
        self._file_name = file_name
        self._subjects = self._subjects_from_scv()

    def __repr__(self):
        return f"Student('{self._last_name}', '{self._name}', '{self._patronymic}', '{self._file_name}')"

    @property
    def full_name(self):
        return f'{self._last_name} {self._name} {self._patronymic}'

    @property
    def subjects(self):
        return self._subjects

    @subjects.setter
    def subjects(self, value):
        if len(value) == 3:
            if value[0].capitalize() in self._subjects.keys():
                subj, grades, test_results = value
                if isinstance(grades, int):
                    self._grades = grades
                else:
                    for item in grades:
                        self._grades = item

                if isinstance(test_results, int):
                    self._test_results = test_results
                else:
                    for item in test_results:
                        self._test_results = item

                self._subjects.update({subj.capitalize():
                                       {'Оценки': grades if isinstance(grades, list)
                                        else [grades],
                                        'Результаты тестов': test_results if isinstance(test_results, list)
                                        else [test_results]}})
            else:
                print(f'Предмета {value[0]} нет у этого студента!')
        else:
            print('Неверное количество аргументов!')

    def _subjects_from_scv(self):
        """Метод, возвращающий словарь предметов из файла *.csv"""
        with open(self._file_name, encoding='utf-8') as file:
            csv_data = csv.DictReader(file, dialect='excel-tab', lineterminator='\n')
            subjects_list = [subject[0] for subject in csv_data.reader][1:]
            results = {subject: {'Оценки': [], 'Результаты тестов': []} for subject in subjects_list}
        return results

    def average_grade_results(self):
        """Метод, возвращающий словарь со средними оценками и средними результатами тестов для каждого предмета"""
        res = {}
        print('Средний балл по оценкам / тестам для каждого предмета:')
        for key, items in self._subjects.items():
            res.update({key: f'{sum(items.get("Оценки")) / len(items.get("Оценки"))} / '
                             f'{sum(items.get("Результаты тестов")) / len(items.get("Результаты тестов"))}'})
        return res

    def print_grade(self):
        """Метод печати общей успеваемости студента"""
        print(f'Успеваемость студента {self.full_name}:')
        for item in self._subjects.items():
            print(item)
        print()


if __name__ == '__main__':
    student_first = Student('Иванов', 'Андрей', 'Иванович', 'student1.csv')
    print(student_first.full_name)
    student_first.print_grade()
    student_first.subjects = 'Математика', 5, 70
    student_first.print_grade()
    student_first.subjects = 'Английский язык', 5, 85
    student_first.print_grade()
    student_first.subjects = 'Математика', [4, 3, 5, 5], [0, 86, 92, 58]
    student_first.subjects = 'Биология', [3, 4, 3, 3], [33, 45, 18]
    student_first.subjects = 'Химия', [3, 4, 5, 3], 46
    student_first.subjects = 'Русский язык', 2, [71, 28]
    student_first.print_grade()
    print(student_first.average_grade_results())
