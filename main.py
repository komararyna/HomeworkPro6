import stu_2
import stu_3


class CountError(Exception):
    def __init__(self, mes):
        self.mes = mes


per1 = stu_2.Person('Ivan', 'Ivanov', 25)
per2 = stu_2.Student('Petr', 'Petrov', 23, 'math')

st1 = stu_2.Student('Ivan', 'Ivanov', 25, 'math')
st2 = stu_2.Student('Ivan', 'Petrov', 25, 'science')
st3 = stu_2.Student('Ivan', 'Markov', 25, 'history')
st4 = stu_2.Student('Ivan', 'Sidorov', 25, 'math')
st5 = stu_2.Student('Ivan', 'Vlasov', 25, 'science')
st6 = stu_2.Student('Maria', 'Ivanova', 25, 'math')
st7 = stu_2.Student('Maria', 'Petrova', 25, 'art')
st8 = stu_2.Student('Maria', 'Markova', 25, 'history')
st9 = stu_2.Student('Maria', 'Sidorova', 25, 'art')
st10 = stu_2.Student('Maria', 'Vlasova', 25, 'math')
st11 = stu_2.Student('Maria', 'Vlasova', 25, 'math')


group1 = stu_3.Group([st1, st2, st3, st4, st5, st6, st7, st8, st9, st10])

print(group1.student_search('Sidorova'))
print(per1)
print(per2)
print(group1)
