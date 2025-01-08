def form(digits):
    return f"{digits[0]}{digits[1]}°{digits[2]}{digits[3]}'{digits[4]}{digits[5]}.{digits[6]} \"N " \
           f"{digits[7]}°{digits[8]}{digits[9]}'{digits[10]}{digits[11]}.{digits[12]} 'W'"

def shift(liste, a):
    a = a % len(liste);
    return liste[a:] + liste[:a];
    
n = 9153787770964;
liste = [int(i) for i in str(n)];

shift_list = shift(liste, -4);
form = form(shift_list)
#print(form)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def trans(C, d, n):
    return pow(C, d, n)

ciphertext = [2726, 1313, 1992, 884, 2412, 1453, 1230, 2185, 2412, 1992, 1313, 1230, 884, 1992, 281, 1632, 281, 2170, 1453, 1992, 1230, 2185, 2160, 1230, 1992, 745, 1632, 1992, 612, 745, 1632, 1627, 2160, 1313, 1992, 2412, 2185, 2160, 2923, 1313]

n = 3233
p = 61  
q = 53  
phi = (p - 1) * (q - 1)
e = 17  
d = inverse(e, phi)

l = [trans(C, d, n) for C in ciphertext]
message = ''.join(chr(num) for num in l)

#print("d =", d)
#print("Decrypted C:", l)
#print("Decrypted message:", message)
