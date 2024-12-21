print('Selamat datang di program saya ini adalah program kalkulator sederhana')
number: int = input('Mohon masukan angka pertama ')
number2: int = input('masukan angka kedua ')
pilihan: int = input('masukan operasi matematika ')

try:
    if pilihan == '+':
        hasil = int(number2) + int(number2)
        print(hasil)

    elif pilihan == '-':
        hasil = int(number2) - int(number2)
        print(hasil)

    elif pilihan == '*':
        hasil = int(number2) * int(number2)
        print(hasil)

    elif pilihan == '/':
        hasil = int(number2) / int(number2)
        print(hasil)

except:
    print('Invalid Number')
