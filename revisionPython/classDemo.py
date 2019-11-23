class ClassDemo:
    
    def summ(a):
        x = 12
        print(a + x)

    def add(a,b):
        return a+b
        
    def ret(a):
        print(ClassDemo.add(10,6))
        print(a)

ClassDemo.summ(3)
ClassDemo.ret(7)

def modless():
    print(f'what a {1-8} subtraction')

if __name__ == '__main__':
    ClassDemo.add(1,2)
    modless()

ClassDemo.ret(4)




