# print(dir(list))
class ImmuttableList(list):
    
    def __new__(cls,x:list):
        if all([type(i)==str for i in x])==False:
            raise ValueError(' all  values must be string ')
        else:
            return x


    
    def append(self, __object) -> None:
        if isinstance(__object,str):
            return super().append(__object)
        else:
            raise ValueError("expecting integer value")
    
    def extend(self, __iterable) -> None:
        if all([type(k)==str for k in __iterable ]):
            return super().extend(__iterable)
        else:
            raise ValueError("list must contain values of type string")

print(ImmuttableList([1,2,3]))

# c.extend(['a','b'])
# print(c.check_vals())
