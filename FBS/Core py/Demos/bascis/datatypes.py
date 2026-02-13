####Numeric 
#1. int
# int x #varibale declaration

x = 10  #variable initialization 
print(type(x))

#2. float
x = 3.14
print(type(x))

#3.complex
x = 45 + 3j
print(type(x))

####Text 
#1.Str
x = "yash "
print(type(x))
x = "yash's'"
print(type(x))
x = '''Yash is a Man'''
print(type(x))

####Sequential
#1. list 
X = [10,20,30]
print(type(x))

#2. Tuple
x = (10,20,30)
print("tuple elements:",X)
print("First element:", x[2])
print("length of tuple:", len(x))

#3. range
x = range(1,10)
for x in range(5):
    print(x)

####SetType
#1.Set 
x = {10,20,30}

#2. frozenset
x = frozenset({10,20,30})

####Mapping
#1.dict
x = {1:'Python',2:'Java'}
print()
