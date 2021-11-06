"""

only change encrypt() and decrypt() functions
both should accept a string and and return a string,  either encrypted or decrypted



"""


def contents(data):
    file_content = []
    for dat in data:
        file_content.append(dat) 
    return file_content

#rot 13

alpha_numeric = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = " ~`!@#$%^&*()_+-={}[]|\\:;\"'<>,.?/"
rot = 13
key = alpha_numeric + symbols
key_len = len(key)

def encrypt(data):
    
    encrypted = ""
    for letter in data:
        for pos in range(key_len):
            if key[pos] == letter:
                new_pos = pos + rot
                if new_pos < key_len:
                    encrypted += key[new_pos]
                else:
                    encrypted += key[new_pos - key_len]
    return encrypted
            

def decrypt(data):
    decrypted = ""
    for letter in data:
        for pos in range(key_len):
            if key[pos] == letter:
                new_pos = pos - rot
                if new_pos >= 0:
                    decrypted += key[new_pos]
                else:
                    decrypted += key[key_len + new_pos]
    return decrypted

def to_utf8(data):
    contents = []
    for line in data:
        contents.append(line.decode('utf-8'))
    return contents




def encrypted_text(data):
    encrypted = []
    for i in data:
        encrypted.append(encrypt(i) +'\n')
    return encrypted


def decrypted_text(data):
    decrypted = []
    for i in data:
        decrypted.append(decrypt(i) + '\n')
    return decrypted


a = ['hello\n', 'mowa\n']
with open('temp.txt', 'w') as temp_file:
    temp_file.writelines(encrypted_text(a))