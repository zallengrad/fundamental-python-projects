""" make a Rock, paper, scissors game ( membuat permainan batu, gunting, kertas [ pingsut ]  - if else ) """

# pertama import ascii gambar batu gunting kertas dari web agar tampilan permainan lebih menarik

batu = """ 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___) 
 """

kertas = """ 
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

"""

gunting = """ 
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

"""
import random

gambar = [batu, gunting, kertas]


print("========== Selamat datang di permainan batu, gunting, kertas ========== ")

user_choices = int(input("ketik 0 untuk memilih batu \nketik 1 untuk memilih gunting \nketik 2 untuk memilih kertas\n:"))
print(f"pilihan anda, {gambar[user_choices]}")

com_choices =  random.randint(0, 2)
print(f"pilihan komputer, {gambar[com_choices]}")

# ===================== IF ELSE ==============================

if user_choices >= 3 or user_choices < 0 :
    print(("angka yang kamu masukan tidak valid, KAMU KALAH"))
elif user_choices == 0 and com_choices == 2 :
    print("Kamu Menanggg,, Horeeee!!!!")
elif com_choices == 0 and user_choices == 1 :
    print("KAMU KALAH!")
elif user_choices > com_choices :
     print("Kamu Menanggg,, Horeeee!!!!")
elif com_choices > user_choices :
    print("KAMU KALAH!")
elif user_choices == com_choices:
    print("DRAWWWW!!, sama kuat , kalian imbang ")
