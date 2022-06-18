import os, re, glob

CWD = os.getcwd() #finder current working director, altså stien som scriptet ligger i


for filename in glob.glob(CWD+'/*.txt'):
	with open(filename, 'r', encoding="utf8") as f:
		READ_TEXT = f.read()



#simpelt en til en erstatning, vælg selv hvad der skal erstattes med hvad.
print(re.sub(' E', "", READ_TEXT))

#print(re.findall('[...]?', READ_TEXT))
