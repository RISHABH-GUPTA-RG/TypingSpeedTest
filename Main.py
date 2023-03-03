import time
import random

def Random_sentense():
    with open("sentense.txt",'r') as f:
        filedata=f.readlines()
        DataOfFile=("".join(filedata)).split("\n")
        Sentense=DataOfFile[random.randint(0,len(DataOfFile)-1)]
    return Sentense

def Intro():
    print("".center(100,"-"))
    print("Typing speed test".center(100,"-"))
    print("".center(100,"-"))
    print()
    sentense=Random_sentense()
    print_sentense(sentense,100)
    print()
    input("Press Enter to Start")
    print()
    return sentense

def print_sentense(sentense,width=100):
    '''or you could save time and use this 
    import textwrappr
    textwrap.fill(sentense,100)'''
    BP=width
    if len(sentense)>=width:
        for i in range(width,0,-1):
            if sentense[i]==" ":
                BP=i
                break
    if len(sentense)>0:
        print("".join([j for i,j in enumerate(sentense) if i<=BP]))
        print_sentense([j for i,j in enumerate(sentense) if i>=BP],width)

def typing_error(words,iwords):
    error=0
    for i in range(len(iwords)):
        if i in (0,len(iwords)-1):
            if iwords[i]==words[i]:
                continue
            else:
                error+=1
        else:
            if iwords[i]==words[i]:
                if(iwords[i+1]==words[i+1])&(iwords[i-1]==words[i-1]):
                    continue
                else:
                    error+=1
            else:
                error+=1
    return error

sentense=Intro()
words=sentense.split()

stime=time.time()
input_prompt=input()
etime=time.time()

input_words=input_prompt.split()

time=round(etime-stime,2)
speed=round((len(input_words)/time)*60,2)
error=typing_error(words,input_words)

print("""
You have used {0} seconds of time.
Your typing speed is {1} words/minute
With a total error of {2}.
""".format(time,speed,error))
input()