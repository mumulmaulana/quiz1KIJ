#Muhammad Farhan Maulana
#5114100055
#KIJ A

from operator import xor

def encrypt(plaintext, scrt_key):
    print "\nENCRYPT TEXT"
    crypt = [None] * len(plaintext)
    crypt_str = [None] * len(plaintext)

    #Menentukan K0 dan K1
    K0 = [None] * 4
    K1 = [None] * 4
    for i in range(0,4):
        K0[i] = scrt_key[i]
        K1[i] = scrt_key[i+4]

    #Melakukan XOR untuk P dan K0
    idx = 0
    count_block = len(plaintext) / 4
    for i in range(0, count_block):
        for j in range(0, 4):
            crypt[idx] = xor(plaintext[idx],K0[j])
            idx += 1

    #Melakukan ADD dengan K1, kemudian MOD 256
    idx = 0
    for i in range(0, count_block):
        for j in range(0, 4):
            crypt[idx] = crypt[idx] + K1[j]
            crypt[idx] = crypt[idx] % 256
            idx += 1

    #Mengubah ke string kembali
    for i in range(0,len(plaintext)):
        crypt_str[i] = chr(crypt[i])
    print "ASCII_NUM: ", crypt
    print "ENCRYPTED: ", crypt_str

    return crypt_str


def decrypt(encrypted, scrt_key):
    print "\nDECRYPT TEXT"

    c_ascii = [None] * len(encrypted)
    for i in range(0, len(encrypted)):
        c_ascii[i] = ord(encrypted[i])

    #Menentukan K0 dan K1
    K0 = [None] * 4
    K1 = [None] * 4
    for i in range(0, 4):
        K0[i] = scrt_key[i]
        K1[i] = scrt_key[i + 4]

    #Melakukan pengurangan C dengan K1
    C = [None] * len(encrypted)
    idx = 0
    count_block = len(encrypted) / 4
    for i in range(0, count_block):
        for j in range(0, 4):
            C[idx] = c_ascii[idx] - K1[j]
            idx += 1

    #Melakukan XOR
    temp_XOR = [None] * len(encrypted)
    idx = 0
    for i in range(0, count_block):
        for j in range(0, 4):
            temp_XOR[idx] = xor(C[idx], K0[j])
            idx += 1

    #Mengubah dari ASCII ke string
    decrypt = [None] * len((encrypted))
    for i in range(0, len(encrypted)):
        decrypt[i] = chr(temp_XOR[i])

    print "ENCRYPTED: ", encrypted
    print "DECRYPTED: ", decrypt

    return decrypt


#Secret key
secret = "maulanaa"

#Konversi secret ke ASCII
asciisecret = [None] * len(secret)
for i in range(0, len(secret)):
    asciisecret[i] = ord(secret[i])

#Masukkan Plaintext
text = raw_input("Masukkan Pesan: ")
panjang = len(text)
panjangdata = panjang

#Menentukan panjang karakter yang akan diproses, membuatnya sesuai dengan 32 bit block
if panjang % 4 > 0:
    sisa = 4 - (panjang % 4)
    panjangdata = panjang + sisa
textdata = [None] * panjangdata
for i in range(0, panjangdata):
    if i < panjang:
        textdata[i] = text[i]
    else:
        textdata[i] = " "

#Mengonversikan string ke ascii
asciitext = [None] * panjangdata
for i in range(0, panjangdata):
    asciitext[i] = ord(textdata[i])

print "PLAINTEXT: ", text

hasil = encrypt(asciitext, asciisecret)
hasil_decrypt = decrypt(hasil, asciisecret)

input()
