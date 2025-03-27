from .abs_visitor import Visitor
from trees.null_person import NullPerson


class GetOldestVisitor(Visitor):
    def __init__(self):
        self.oldest = NullPerson()
        self.oldest_name = None
        self.oldest_birthday = self.oldest.birthdate

    def visit_person(self, person):
        if person.birthdate < self.oldest.birthdate:
            self.oldest = person

    def visit_tree(self, tree):
        pass
