import random
def proses():

    try:
        print('Selamat datang dalam permainan batu gunting kertas')
        print('1.Gunting 2.Batu 3.Kertas')
        Rbot = random.randrange(1, 3)
        bot = int(Rbot)
        print(bot)
        jawaban = input('masukan tebakan anda ')

        if int(jawaban) == 1:
            if bot == 1:
                print('SERI')
            elif bot == 2:
                print('KALAH')
            elif bot == 3:
                print('MENANG')

        if int(jawaban) == 2:
            if bot == 2:
                print('SERI')
            elif bot == 3:
                print('KALAH')
            elif bot == 1:
                print('MENANG')

        if int(jawaban) == 3:
            if bot == 3:
                print('SERI')
            elif bot == 1:
                print('KALAH')
            elif bot == 2:
                print('MENANG')

        else:
            print('ERROR!!\n')
            proses()

    except:
        print('Jawaban tidak boleh kosong!\n')
        proses()

    x = input('Lanjut atau tidak (y/n) ')

    if x == 'y':
        print('\n')
        proses()
    elif x == 'n':
        exit()
proses()
