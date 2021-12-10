file = open("Perc_vowel",'r')
STR = file.readline()
vowels = "aeiouAEIOU"
constants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
vow = str([i for i in STR if i in vowels])
cons = str([i for i in STR if i in constants])
total=vow+cons
perc_Vowel = int(len(vow)/len(total)*100)
print(perc_Vowel,"%")