d = """YQBUFOMMXJOZ
OD NFY OTZRFI OTZ RFOAXJOZ, AFD NOWOZ DOTZOY YQBOZ CFDOXFM FID
YQBUFOMMXJOZ AOLTZTOYB NEYAO. ATO REBBOY LQYREITOYBO ATO FELWFCO:
"WOJO KEY WYQDDREBBOY. WOJO ZTXJB TR AYOTOXU QAOY TR YOXJBOZ NTZUOI,
DQZAOYZ DEXJO ATO UEOYKODBO GOYCTZAEZW AOD NOWOD. FAATOYO ATO CIEROZ
FR NOWYFZA KE OTZOR NEZAOYDXJQOZOZ DBYFEDD EZA UEOYKO TJZ DQNOTB NTO
RQOWITXJ."
YQBUFOMMXJOZ DERRTOYBO OTZOZ UEXJOZ, OTZO NEYDB EZA OTZO LIFDXJO NOTZ
TZ OTZOR UQYC FEL. FEL AOR NOW KEY WYQDDREBBOY COWOWZOBO AOR RFOAXJOZ
TZ AOY ROJYOYO JF WYQDDOZ LIFOXJO AOD NFIAOD, AEYXJ AOZ OD WTZW, KELFOIITW
OTZ NQIL, QCNQJI ATO NFJYDXJOTZITXJUOTB AFLEOY ZFJOKE ZEII NFY. AFD BTOY
ERUYOTDBO YQBUFOMMXJOZ TR DBOBD WIOTXJOZ FCDBFZA. AFCOT LYFWBO AOY
NQIL DTO ZFXJ TJYOR ZTOI EZA OYREZBOYBO DTO ZQXJ NOTBOYO CIEROZ KE
MLIEOXUOZ, ER AOZ DBYFEDD KE OYNOTBOYZ.
OY DOICDB FCOY OZBLOYZBO DTXJ.
FID YQBUFOMMXJOZ DMFOBOY ATO DBOTWEZW AOD WOYFAOZ FZDBTOWD KER JFED
AOY WYQDDREBBOY WOZQRROZ JFBBO, COROYUBO DTO OTZOZ CODOZ ZOCOZ AOY
JFEDBüY, AODDOZ UOJYNOYB DOJY UIOTZ NFY, NOTI OY UFER ZQXJ CQYDBOZ JFBBO.
TR JFED BYFL DTO ATO WYQDDREBBOY TR COBB FZ. DTO LYFWBO: "WYQDDREBBOY,
NFYER JFDB AE DQ WYQDDO FEWOZ?" "TXJ JFCO LYEOJOY TRROY GOYDEXJB COT
ROTZOR ZFXJCFYZ FCKEDXJYOTCOZ!" "WYQDDREBBOY, NFYER JFDB AE DQ WYQDDO
QJYOZ\?" "TXJ JFCO ROTZ JFZAH TRROY FEL IFEBIQD WODBOIIB EZA NTII UOTZOZ FZYEL
GOYMFDDOZ!" "WYQDDREBBOY, NFYER JFDB AE DQ OTZ WYQDDOD RFEI?" "TXJ JFCO
TRROY GOYDEXJB, ROTZOZ CEYWOY WFZK TZ AOZ REZA KE DXJTOCOZ!"
AFYFEL LYFDD AOY NQIL AFD YQBUFOMMXJOZ.
OTZ PFOWOY UFR, DFJ, AFDD ATO FCDQIEBO JFOELTWUOTB GQZ WYQDDREOBBOYZ
TR JFED ZEII NFY. AFZZ ZFJR OY DOTZ RODDOY EZA DECBYFJTOYBO ATO QRF EZA
YQBUFOMMXJOZ GQR NQIL. ZER NQIL NEYAO OTZO WYQDDO ROZWO GQZ DBOTZOZ
JTZKEWOLüWB. OY LTOI TZ OTZOZ KHITZAOYLQOYRTWOZ CYEZZOZ."""

o = {}
for letter in d:
 if letter in o:
  o[letter]+=1
 else:
  o[letter]=1

print (o)
print ("sort")
print ({v: k for k, v in reversed(o.items())})

# ceasar
def enigma_rad(alphabet, letter, secret_index):
 ret_val = ""
 rad_size = len(alphabet)
 p = alphabet.index(letter)
 if p+secret_index > rad_size:
   ret_val = alphabet[p+secret_index-rad_size]
 else:
   if p+secret_index < 0:
     ret_val = alphabet[p+secret_index+rad_size]
   else:
     ret_val = alphabet[p+secret_index]

 return ret_val

# geheim text
def enigma_rad2(letter, secret_dict):
 ret_val = letter
 for zeihen in secret_dict:
     if zeihen['geheim'] == letter:
       return zeihen['klar']
 return ret_val

# alphabet
secret_dict = [
{'klar':'p', 'geheim':'M'},
{'klar':'l', 'geheim':'I'},
{'klar':'m', 'geheim':'R'},
{'klar':'a', 'geheim':'F'},
{'klar':'r', 'geheim':'Y'},
{'klar':'d', 'geheim':'A'},
{'klar':'u', 'geheim':'E'},
{'klar':'f', 'geheim':'L'},
{'klar':'i', 'geheim':'T'},
{'klar':'w', 'geheim':'N'},
{'klar':'b', 'geheim':'C'},
{'klar':'y', 'geheim':'H'},
{'klar':'q', 'geheim':'S'},
{'klar':'k', 'geheim':'U'},
{'klar':'x', 'geheim':'V'},
{'klar':'g', 'geheim':'W'},
{'klar':'c', 'geheim':'X'},
{'klar':'n', 'geheim':'Z'},
{'klar':'t', 'geheim':'B'},
{'klar':'s', 'geheim':'D'},
{'klar':'v', 'geheim':'G'},
{'klar':'h', 'geheim':'J'},
{'klar':'z', 'geheim':'K'},
{'klar':'e', 'geheim':'O'},
{'klar':'j', 'geheim':'P'},
{'klar':'o', 'geheim':'Q'}]


# This is a sample Python script.
if __name__ == '__main__':
  for l in d:
    print(enigma_rad2(l, secret_dict), end='')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
