'''Count consonants and vowels'''

def main():
    filename = input("Enter a File path:")
    readfile = open(filename,'r')
    strFile = readfile.read().lower()
    splitFile = strFile.split()
    print(splitFile)
    vowels={"a","e","i","o","u"}
    vowelcount=0
    consonent=0
    for word in splitFile:
        for c in word:
            if c in vowels and c.isalpha():
                vowelcount+=1
            elif c.isalpha() and c not in vowels:
                consonent+=1
    
    print("Vowels: ", vowelcount)
    print("Consonents: ",consonent)

main()