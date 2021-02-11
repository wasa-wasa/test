d = "RRLYLEEVHFIWMVVPEPQWRJYHMRIMIHOHLWRIIRVIMVEVVVXJXVH VLKYIIIIGRVREEIISIEMEPPXPGMYDVHQIEIIRRLMSIRHWIYIIWA VMEXIEYHOHRWFDLPFSIEMEIISIRVSYVLHWIMISEMEPFYXQVYVV"
o = {}
for letter in d:
 if letter in o:
  o[letter]+=1
 else:
  o[letter]=1

print("letters gistogram")
print (o)
print ("sorted letters by count")
letters_count = []
for i in reversed(o.items()):
   letters_count.append(str(i[0])+"\t"+ str(i[1]))


for ii in sorted(letters_count):
   print(ii)




