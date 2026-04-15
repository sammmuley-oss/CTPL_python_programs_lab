# write a python program to read the contents of a file and count the frequency of each word in the file.
# display the word and its frequency.

import string

file=open("story.txt","w")
file.write("Welcome to CTP lab , CTP lab is the best lab")
file.close() 

file=open("story.txt","r")
text=file.read().lower()
for ch in string.punctuation:
    text=text.replace(ch,"")
words=text.split()
word_count={}
for word in words:
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1
sorted_words=sorted(word_count.items(),key=lambda x:x[1],reverse=True)
for word, count in sorted_words:
    print(f"{word}: {count}")