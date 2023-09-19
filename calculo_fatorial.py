print("Calculo de Fatorial")
def main():
    n=int(input("Valor de n:"))
    fat=1
    i=0
    if n<0:
       print("Erro")
    else:
      while i<n:
        fat=fat*n
        n=n-1
    print("O fatorial eh:",fat)
main() 