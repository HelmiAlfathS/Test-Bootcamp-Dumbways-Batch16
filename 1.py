def matching(wordlist, word):
    for i in wordlist:
        if i in word:
            print(i+' =>',True)
        else:
            print(i+' =>',False)
            
dataKey = ['dumb','ways','the','best']
myword = 'dumbways'
matching(dataKey, myword)