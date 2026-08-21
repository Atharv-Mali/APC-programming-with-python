sentence=input("enter sentence:")
freq={}
for word in sentence.split():
    freq[word]=freq.get(word,0)+1
print(freq)
