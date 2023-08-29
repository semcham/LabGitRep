"""
Realiza lo siguiente utilizando métodos de formateo de cadenas:
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144 """

def run():
    a = 8
    b = 6
    print('{} + {} = {}'.format(a ,b ,a+b))
    print('{} - {} = {}'.format(a, b, a-b))
    print('{} * {} = {}'.format(a, b, a*b))
    print('{} / {} = {:.2f}'.format(a, b, a/b))
    print('{} % {} = {}'.format(a, b, a%b))
    print('{} // {} = {}'.format(a, b, a//b))
    print('{} ** {} = {}'.format(a, b, a**b))



if __name__ == "__main__":
    run()    