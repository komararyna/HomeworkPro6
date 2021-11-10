class CountError(Exception):
    def __init__(self, mes):
        self.mes = mes


class Group:
    def __init__(self, group: list):
        self.group = group
        if len(self.group) > 10:
            raise CountError('only 10 students can be in one group')

    def add_student(self, value):
        self.group.append(value)

    def remove_student(self, value):
        self.group.remove(value)

    def student_search(self, surname):
        res = []
        for stud in self.group:
            if stud.surname == surname:
                res.append(stud)
        return res or None

    def __iter__(self):
        return GroupIterator(self.group)

    def __str__(self):
        group_tmp = "\n".join(map(str, self.group))
        return f'{group_tmp}\n'


class GroupIterator:
    def __init__(self, group):
        self.group = group
        self.index = 0

    def __next__(self):
        if self.index < len(self.group):
            self.index = self.index + 1
            return self.group[self.index - 1]
        else:
            raise StopIteration

    def __iter__(self):
        return self
