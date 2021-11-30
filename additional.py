"""

only change encrypt() and decrypt() functions
both should accept a string and and return a string,  either encrypted or decrypted



"""

sp="""abcdefghijklmnopqrstuv!"#$%&'()*+,-. MNOPQRSTUVWXYZ/:;<=>?@[\]^_`{|}~0123456789wxyzABCDEFGHIJKL"""

def encrypt(pat):
    newpat=""
    for i in range(len(pat)):
        if(pat[i] in sp):
            newpat += sp[(sp.index(pat[i]) + i) % len(sp)]
    return newpat

            
def decrypt(pat):
    newpat=""
    for i in range(len(pat)):
        if(pat[i] in sp):
            newpat += sp[(sp.index(pat[i]) - i) % len(sp)] 
    return newpat



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
