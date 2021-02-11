from datetime import datetime


# ceasar
def enigma_rad(alphabet, letter, secret_index):
    ret_val = ""
    rad_size = len(alphabet)
    p = alphabet.index(letter)
    if p + secret_index >= rad_size:
        ret_val = alphabet[p + secret_index - rad_size]
    else:
        if p + secret_index < 0:
            ret_val = alphabet[p + secret_index + rad_size]
        else:
            ret_val = alphabet[p + secret_index]

    return ret_val


# {"A": "A", "B": "B", "C": "C", "D": "D", "E": "E", "F": "F", "G": "G", "H": "H", "I": "I", "J": "J", "K": "K", "L": "L", "M": "M", "N": "N", "O": "O", "P": "P", "Q": "Q", "R": "R", "S": "S", "T": "T", "U": "U", "V": "V", "W": "W", "X": "X", "Y": "Y", "Z": "Z"}

#  entschlusselten buchstabe
def vigenere_quadrat(value, geheim):
    vq = {"A": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
          "B": "BCDEFGHIJKLMNOPQRSTUVWXYZA",
          "C": "CDEFGHIJKLMNOPQRSTUVWXYZAB",
          "D": "DEFGHIJKLMNOPQRSTUVWXYZABC",
          "E": "EFGHIJKLMNOPQRSTUVWXYZABCD",
          "F": "FGHIJKLMNOPQRSTUVWXYZABCDE",
          "G": "GHIJKLMNOPQRSTUVWXYZABCDEF",
          "H": "HIJKLMNOPQRSTUVWXYZABCDEFG",
          "I": "IJKLMNOPQRSTUVWXYZABCDEFGH",
          "J": "JKLMNOPQRSTUVWXYZABCDEFGHI",
          "K": "KLMNOPQRSTUVWXYZABCDEFGHIJ",
          "L": "LMNOPQRSTUVWXYZABCDEFGHIJK",
          "M": "MNOPQRSTUVWXYZABCDEFGHIJKL",
          "N": "NOPQRSTUVWXYZABCDEFGHIJKLM",
          "O": "OPQRSTUVWXYZABCDEFGHIJKLMN",
          "P": "PQRSTUVWXYZABCDEFGHIJKLMNO",
          "Q": "QRSTUVWXYZABCDEFGHIJKLMNOP",
          "R": "RSTUVWXYZABCDEFGHIJKLMNOPQ",
          "S": "STUVWXYZABCDEFGHIJKLMNOPQR",
          "T": "TUVWXYZABCDEFGHIJKLMNOPQRS",
          "U": "UVWXYZABCDEFGHIJKLMNOPQRST",
          "V": "VWXYZABCDEFGHIJKLMNOPQRSTU",
          "W": "WXYZABCDEFGHIJKLMNOPQRSTUV",
          "X": "XYZABCDEFGHIJKLMNOPQRSTUVW",
          "Y": "YZABCDEFGHIJKLMNOPQRSTUVWX",
          "Z": "ZABCDEFGHIJKLMNOPQRSTUVWXY"
          }
    abc = vq[geheim.upper()]
    pos = abc.find(value)
    if pos >= 0:
        return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[pos]
    return " "

d1 = "PPTLJUDKULLULHLVMSYAPYHULLDRKULUYLLHZBNAKMBLHOZLBLH LJPTAKIKZVVPHQYNAIDKMPLINLSOKMLUAUKDUYJKIZBLYPTANLU LZTOKTUKUUYHLUYLLZKZZSKUYZBLUHIJUHHSOYKKMPLHOPLLLBL"
d2 = "RRLYLEEVHFIWMVVPEPQWRJYHMRIMIHOHLWRIIRVIMVEVVVXJXVH VLKYIIIIGRVREEIISIEMEPPXPGMYDVHQIEIIRRLMSIRHWIYIIWA VMEXIEYHOHRWFDLPFSIEMEIISIRVSYVLHWIMISEMEPFYXQVYVV"
d3 = "YYUMYGFUFNCNHGBTYYCYYLOMHTCHLCCYCMBHFXYFYUVQCYCGNXC CNYNLLCHBPYJLBHMLHLYGCYYOEWHOCYCCHLHOCNYYTAYNZNLQYU YYWYGHHYCYXFYOIFYHLFGHCAMBAMNMUOXNAWVNMYGCLWYGNLQX"
d2len = len(d2)
d3len = len(d3)

# alphabet uppercase
abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

dstart = datetime.now()
print("start", dstart.microsecond)

for i, val in enumerate(d1):
    if d1[i] == " ":
        continue
    # H
    print(vigenere_quadrat(d1[i], "H"), end="")
    #print(enigma_rad(abc, d1[i], 19), end="")
    if i < d2len:
        # E
        print(vigenere_quadrat(d2[i], "E"), end="")
        #print(enigma_rad(abc, d2[i], 22), end="")
    if i < d3len:
        # U
        print(vigenere_quadrat(d3[i], "U"), end="")
        #print(enigma_rad(abc, d3[i], 6), end="")

print("")
print("end in microseconds:", datetime.now().microsecond - dstart.microsecond)
