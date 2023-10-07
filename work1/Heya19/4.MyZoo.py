class MyZoo:
    def __init__(self, animals=None):  # 它在对象创建时自动调用。
        print("My Zoo!")
        self.animals = animals if animals else {}
        # 在Python中，与许多其他编程语言（如Java或C++）不同，类的属性不需要在类定义中预先声明。
        # 相反，可以在任何方法中（通常是在__init__方法中）动态地为对象添加属性。

    def __str__(self):
        return ", ".join(f"{animal}: {count}" for animal, count in self.animals.items())

    def __eq__(self, other):
        return set(self.animals.keys()) == set(other.animals.keys())

    def __len__(self):
        return sum(self.animals.values())

'''
为MyZoo类定义了五个测试用例：
1.测试初始化是否正确。
2.测试字符串表示是否正确。
3.测试两个具有相同动物种类的MyZoo对象是否相等。
4.测试两个具有不同动物种类的MyZoo对象是否不相等。
5.测试len函数是否返回所有动物的总数。
'''
# 测试初始化
zoo = MyZoo({"pig": 5, "dog": 6})
assert str(zoo) == "pig: 5, dog: 6", f"Error: {zoo}" #assert语句用于测试表达式，如果表达式为False，则引发异常

# 测试字符串表示
zoo = MyZoo({"pig": 5, "dog": 6})
assert str(zoo) == "pig: 5, dog: 6", f"Error: {zoo}"

# 测试相等性
zoo1 = MyZoo({"pig": 1})
zoo2 = MyZoo({"pig": 5})
assert zoo1 == zoo2, f"Error: {zoo1} != {zoo2}"

# 测试不等性
zoo1 = MyZoo({"pig": 1})
zoo2 = MyZoo({"dog": 5})
assert zoo1 != zoo2, f"Error: {zoo1} == {zoo2}"

# 测试长度
zoo = MyZoo({"pig": 5, "dog": 6})
assert len(zoo) == 11, f"Error: len({zoo}) = {len(zoo)}"

print("All tests passed!")

