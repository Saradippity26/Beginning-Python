print("Hello Python")
# scalar data types: Integers, Floating point
# Non, and Boolean
# supports binary notation
print("binary notation",0b0100)
#hex notation
print("hex notation", 0x0100)
#use the interger constructor int() -- can convert any integer
print(int("477"))
#option for base
print(int("1001",2))
#garbage collection is automatic in python, as soon as the object is out of scope it is wiped
#floating point: IEE-754
#x=3.7 and type(x) <class, float>
print("scientific Notation", 1.61e-35)
#undestands this directly
print("float construction float()", float("1.99"))
#tries to convert to float
#boolean
print("boolean const. bool()",bool(0))
#zero = false non zero = true even with fractions
print("boolean const. bool(42)", bool(42))
print("boolean const. bool(0.1)", bool(0.1))
#can test boolean on collections (like arrays)
print("boolean const. bool([])", bool([]))
print("boolean const. bool([1,2,3[)",bool([1,2,3]))
print("boolean const. bool("")",bool(""))
print("boolean const. bool('False')", bool("False"))
#will push this file to github: VCS > Import into Version control > share project on github >> no token change to password