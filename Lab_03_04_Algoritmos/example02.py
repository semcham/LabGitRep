"""
Escribe un script en Python que muestre 
la siguiente tabla 
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
"""

def run():

    print("1 1 1 1 1")
    for i in range(2, 6):
        resultado = f"{i} 1 {i} {i*i} {i*i*i}"
        print(resultado)

if __name__ == "__main__":
    run()   