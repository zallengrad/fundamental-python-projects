abjad = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

pilihan = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text= input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# def encrypt (plain_text, shift_amount):

#     cipher_text = ""

#     for i in plain_text :
#         posisi_awal = abjad.index(i)
#         posisi_baru = posisi_awal + shift_amount
#         kata_baru = abjad[posisi_baru]

#         cipher_text += kata_baru
#     print(f"The encoded text is {cipher_text}")

# def balik (plain_text, shift_amount):

#     cipher_text = ""

#     for i in plain_text :
#         posisi_awal = abjad.index(i)
#         posisi_baru = posisi_awal - shift_amount
#         kata_baru = abjad[posisi_baru]

#         cipher_text += kata_baru
#     print(f"The encoded text is {cipher_text}")



# if pilihan == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif pilihan == "decode":
#     balik(plain_text=text, shift_amount=shift)


def caesar (a_pilihan, a_text, a_shift):

    a_pilihan == pilihan
    a_text == text
    a_shift == shift
    
    cipher_text = ""

    
    for i in a_text :
        posisi_awal = abjad.index(i)
        posisi_baru = posisi_awal + a_shift
        kata_baru = abjad[posisi_baru]

        cipher_text += kata_baru
    print(f"The encoded text is : {cipher_text}")

caesar(pilihan, text, shift)