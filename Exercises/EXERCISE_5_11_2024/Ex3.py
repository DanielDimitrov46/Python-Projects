text = str(input("Input text: "))
di={}
for i in text:
    if i in di:
        di[i]+=1
    else:
        di[i]=1
# di = {char: text.count(char) for char in set(text)}
print(f"Letters and their count in {text} : {di}")