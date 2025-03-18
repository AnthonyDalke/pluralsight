from .abs_tree import AbsTree


class Tree(AbsTree):
    def __init__(self, name, members):
        self._name = name
        self._members = members

    def __iter__(self):
        return iter(self._members)

    @property
    def name(self):
        return self._name

    def accept(self, visitor):
        visitor.visit_tree(self)
        for node in self:
            node.accept(visitor)
