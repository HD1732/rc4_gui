def en_rc4(mes,key):
    S = []
    for i in range(256):
        S.append(i)
    j = 0
    message = mes
    K = key
    Keysize = len(K)
    for i in range(256):
        j = (j + S[i] + ord(K[i % Keysize])) % 256
        S[i], S[j] = S[j], S[i]
    i = 0
    j = 0
    # keystream
    ks = []
    for k in range(len(message)):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        ks.append(S[(S[i] + S[j]) % 256])
    # ciphertext
    c = []
    for k in range(len(message)):
        c.append(ord(message[k]) ^ ks[k])
    return ks,c

def de_rc4(ks,c):
    m_dec=[]
    for k in range(len(c)):
        m_dec.append(chr(c[k] ^ ks[k]))
    return m_dec
def get_str(m_dec):
    str=''
    for i in range(len(m_dec)):
        if(i!=len(m_dec)):
            str=str+"{} ".format(format(int(hex(m_dec[i]), 16), 'x'))
        else:
            str=str+"{}".format(format(int(hex(m_dec[i]), 16), 'x'))
    return str

