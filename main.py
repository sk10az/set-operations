import random


# This class defines a Set data structure with methods for performing set operations like
# intersection, union, symmetric difference, and subtraction.
class Set:
    def __init__(self, *args) -> None:
        self.elements = set(args)

    def intersection(self, other_set: 'Set') -> 'Set':
        intersection_set = Set(*[i for i in self.elements if i in other_set.elements])
        return intersection_set

    def union(self, other_set: 'Set') -> 'Set':
        union_set = Set(*list(self.elements))
        for i in other_set.elements:
            if i not in union_set.elements:
                union_set.elements.add(i)
        return union_set

    def symmetric_difference(self, other_set: 'Set') -> 'Set':
        symmetric_diff_set = Set(*list([i for i in self.elements if i not in other_set.elements] + [i for i in other_set.elements if i not in self.elements]))
        return symmetric_diff_set

    def subtract(self, other_set: 'Set') -> 'Set':
        subtracted_set = Set(*list([i for i in self.elements if i not in other_set.elements]))
        return subtracted_set

    def __str__(self):
        return "{" + ", ".join(map(str, self.elements)) + "}"

    def __repr__(self):
        return self.__str__()

s1 = Set(1, 2, 3)
s2 = Set(2, 3, 4)

print("Intersection:", s1.intersection(s2))