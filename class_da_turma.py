""" Exemplo de uma class construída coletivamente
"""


class Turma:
    def __init__(self, name='PythonIpea2022'):
        self.turma = name
        self.students = list()

    def add_student(self, name):
        self.students.append(name)

    def remove_student(self, name):
        self.students.remove(name)

    def count_std(self):
        return len(self.students)

    def list_std(self):
        for each in self.students:
            print(each)

    def __repr__(self):
        return f'{self.turma} tem {self.count_std()} alunos'


if __name__ == '__main__':
    a = Turma()
    print(type(a))
    print(a)

    a.list_std()

    print(a)
    b = Turma('PythonAdvanced')
    print(b)
