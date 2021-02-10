from datetime import datetime

# ceasar
def enigma_rad(alphabet, letter, secret_index):
 ret_val = ""
 rad_size = len(alphabet)
 p = alphabet.index(letter)
 if p+secret_index >= rad_size:
   ret_val = alphabet[p+secret_index-rad_size]
 else:
   if p+secret_index < 0:
     ret_val = alphabet[p+secret_index+rad_size]
   else:
     ret_val = alphabet[p+secret_index]

 return ret_val


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
    print(enigma_rad(abc, d1[i], 19), end="")
    if i < d2len:
       # E
        print(enigma_rad(abc, d2[i], 22), end="")
    if i < d3len:
       # U
        print(enigma_rad(abc, d3[i], 6), end="")

print("")
print("end in microseconds:", datetime.now().microsecond-dstart.microsecond)
