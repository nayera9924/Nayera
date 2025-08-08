import random
GREEN = "\033[92m"   
YELLOW = "\033[93m"  
GRAY = "\033[90m"  
RESET = "\033[0m" 

file=open("words.txt","r")
words=file.read().splitlines()
target=random.choice(words)
tries=6
while tries>0:
    word=input("").lower()
    if len(word)!=5:
        print("word should contain 5 letters only")
    elif word not in words:
            print("not real word")
    elif target==word:
        print("you win")
    else:
        tries-=1
        colored_result = ""

        for i in range(5):
            if word[i]==target[i]:
                colored_result+=GREEN+word[i]+RESET
            elif word[i] in target:
                colored_result+=YELLOW+word[i]+RESET
            else:
                colored_result+=GRAY+word[i]+RESET
        print("             ",colored_result)
           
print("you lost")
print("word is ",target)