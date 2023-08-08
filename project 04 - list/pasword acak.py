import random

kata = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
angka = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbol = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print( f"================= selamat datang di pasword acak =================")


jumlah_kata = int(input(f"berapa kata yang ingin kamu masukan : "))
jumlah_angka = int(input(f"berapa angka yang ingin kamu masukan : "))
jumlah_simbol = int(input(f"berapa simbol yang ingin kamu masukan : "))


total_pw = jumlah_angka + jumlah_kata + jumlah_simbol

# pasword = ""

# for i in range(1, jumlah_kata+1) : 
#     pasword += random.choice(kata)

# for i in range(1, jumlah_angka+1) : 
#     pasword += random.choice(angka)

# for i in range(1, jumlah_simbol+1) : 
#     pasword += random.choice(simbol)


# print(f"pasword = {pasword}")


pasword = []

for i in range(1, jumlah_kata+1) : 
    pasword += random.choice(kata)

for i in range(1, jumlah_angka+1) : 
    pasword += random.choice(angka)

for i in range(1, jumlah_simbol+1) : 
    pasword += random.choice(simbol)


print(f"\n{pasword}")
random.shuffle(pasword)
print(pasword)

print(f"\n\npasword kamu berjumlah {total_pw}")
kunci = ""
for i in pasword :
  kunci += i

print(f"Your password is: {kunci}\n\n ====terimakasih====\n")


