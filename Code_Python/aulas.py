
def primo(x):
    fator = 2
    while x % fator !=0 and fator < x/2:
        fator = fator + 1
    if x % fator == 0:
        return False
    else:
        return True

limite = int(input("limite máximo"))

n = 2
primos = []
while n < limite:
    if primo(n):
        primos.append(n)
    n = n + 1

print(primos) 