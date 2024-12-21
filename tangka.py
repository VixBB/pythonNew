import random

ans = random.randrange(1,100)
print(ans)
guess = input('masukan tebakan anda')

if int(guess) == ans:
    print('jawaban anda benar')
else:
    print('jawaban anda salah')
