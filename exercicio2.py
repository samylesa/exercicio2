def comparacao(lista):
    for i in range(0, 4):
        if(lista[i]>5):
            lista[i]=lista[i]
        else:
            lista[i]=lista[i]+10
    return lista   

def converter(numero):
    algarismo4= numero//1%10 
    algarismo3= numero//10%10 
    algarismo2= numero//100%10 
    algarismo1= numero//1000%10

    lista =[algarismo1, algarismo2, algarismo3, algarismo4]
    lista2 = comparacao(lista)

    for i in range(0, 4):
        lista2[i] = lista2[i]-6

    aux3 = lista2[0]
    aux4 = lista2[1]
    lista2[0]=lista2[2]
    lista2[1]=lista2[3]
    lista2[2]=aux3
    lista2[3]=aux4
    
    num =((lista2[0]*1000)+(lista2[1]*100)+(lista2[2]*10)+lista2[3])
    return num
def main():
    numero2 = int(input("Digite um número de quatro dígitos:"))
    if(numero2>9999 or numero2<999):
        while(numero2>9999 or numero2<999):
            numero2 = int(input("Digite um número de quatro dígitos:"))
    numero2 = converter(numero2)
    print("O número digitado descriptografado é:", numero2)
       
main()
