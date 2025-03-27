from datetime import date
from trees.person import Person
from trees.tree import Tree

from visitors.get_oldest_visitor import GetOldestVisitor

hitchhikers = Tree(
    "Cast",
    [
        Person("Trillian", date(1970, 3, 14)),
        Person("Arthur", date(1965, 7, 4)),
        Person("Ford", date(1995, 2, 2)),
        Person("Zaphod", date(1997, 5, 1)),
    ],
)

singles = Tree(
    "Characters",
    [
        Person("Marvin", date(1991, 1, 1)),
        Person("Slarti", date(1993, 9, 9)),
    ],
)

loner = Person("Douglas", date(1952, 3, 11))

tree1 = Tree("Cast", [hitchhikers])
tree2 = Tree("Others", [singles, loner])
tree3 = Tree("Everyone", [tree1, tree2])

ov = GetOldestVisitor()
tree3.accept(ov)
name, age = ov.oldest_name, (ov.oldest_birthday - date.today()).days // 365
print(f"Oldest person in tree {tree3.name}: {name}; age: {age} years")
