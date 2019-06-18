class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'


obj = MyClass()
print(f'\nPrinting obj.method:\n\n', obj.method())
obj.classmethod()
print(f'\nPrinting obj.classmethod:\n\n', obj.classmethod())
obj.staticmethod()
print(f'\nPrinting obj.staticmethod:\n\n', obj.staticmethod())

print(MyClass.classmethod())
print(MyClass.staticmethod())
print(MyClass.method(obj))