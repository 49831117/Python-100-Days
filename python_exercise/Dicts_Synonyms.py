Statement
You are given a dictionary consisting of word pairs. Every word is a synonym of the other word in its pair. All the words in the dictionary are different.

After the dictionary there's one more word given. Find a synonym for it.

Example input
3
Hello Hi
Bye Goodbye
List Array
Goodbye

Example output
Bye

Theory
If you don't know how to start solving this assignment, please, review a theory for this lesson:
https://snakify.org/lessons/dictionaries_dicts/


n = int(input())
keyvalue = {}

for i in range(n):
    key, value = input().strip().split()
    keyvalue[key] = value

new_keyvalue = {x:y for y, x in keyvalue.items()}

s = input()

if s in keyvalue:
    print( keyvalue[s] )
else:
    new_keyvalue = {x:y for y, x in keyvalue.items()}
    print( new_keyvalue[s] )



Model Solution

synonyms = {}
for i in range(int(input())):
  w1, w2 = input().split()
  synonyms[w1] = w2
  synonyms[w2] = w1
print(synonyms[input()])