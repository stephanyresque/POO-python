#Atributos de classe

class A:
    vc = 123 #var da classe

    def __init__(self):
        self.vc = 321 #var de istância

a1 = A()
a2 = A()

#A.vc = 321 -> altero a variável da classe
#a1.vc = 321 #crio um atributo direto na instância

print(a1.vc)
print(a2.vc)
print(A.vc)

