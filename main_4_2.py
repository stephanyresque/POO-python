#Atributos de classe

class A:
    vc = 123 #var da classe

    def __init__(self):
        pass

a1 = A()
a2 = A()

A.vc = 'Alterado em todos'

print(a1.vc)
print(a2.vc)
print(A.vc)

