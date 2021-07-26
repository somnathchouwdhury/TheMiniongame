vowels=['A','E','I','O','U']

def minion_game(string):
    k=0
    s=0
    for letters in range(len(string)):
        if(string[letters] in vowels):
            k+=len(string)-letters
        else:
            s+=len(string)-letters
            
    if(k>s):
        print("Kevin",k)
    elif(k<s):
        print("Stuart",s)
    else:
        print("Draw")
        

if __name__ == '__main__':
    s = input()
    minion_game(s)
