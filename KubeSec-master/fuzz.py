from scanner import isValidUserName, isValidPasswordName, isValidKey, checkIfValidKeyValue, checkIfValidSecret
import random

# bad strings
with open("blns.json", "r", encoding='utf-8-sig') as f:
    data = f.read()
    data = data.replace("\n", "")
    blns = data.split(",")

def fuzzValues():
    for i in range (7):
       invalidstr = random.choice(blns)
       print(invalidstr)
       print(isValidUserName(invalidstr))
       print(isValidPasswordName(invalidstr))
       print(isValidKey(invalidstr))
       print(checkIfValidKeyValue(invalidstr))
       print(checkIfValidSecret(invalidstr))

def simpleFuzzer():
    fuzzValues()


if __name__=='__main__':
    simpleFuzzer()
