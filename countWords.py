introString = input("enter you introduction")
characterCount = 0
wordCount = 1
for i in introString:
    characterCount = characterCount+1
    if(i ==' '):
        wordCount = wordCount+1
        characterCount = characterCount-1

print(wordCount,characterCount)