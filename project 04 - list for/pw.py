# make a password generator - used LIST in python 
import random

kata = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

angka = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbol = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+']

print(f"----------------------- Selamat Datang di Password Generator -----------------------")

jumlah_kata  = int(input(f"jumlah kata yang ingin kamu masukan : "))
jumlah_angka = int(input(f"jumlah angka yang ingin kamu masukan : "))
jumlah_simbol = int(input(f"jumlah simbol yang ingin kamu masukan : "))

total_password = jumlah_angka + jumlah_kata + jumlah_simbol
password = []

for i in range(1,jumlah_kata + 1) :
    password += random.choice(kata)


for i in range(1,jumlah_angka + 1) :
    password += random.choice(angka)
    
for i in range(1,jumlah_simbol + 1) :
    password += random.choice(simbol)

print(f"\n{password}")
random.shuffle(password)
print(password)

print(f"\n\npassword kamu berjumlah : {total_password}")
kunci = ""
for i in password :
    kunci += i

print(f"Your password is : {kunci}\n\n ===== TERIMAKASIH =====")
    