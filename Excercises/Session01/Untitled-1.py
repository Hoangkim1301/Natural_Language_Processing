def extract_words_tokens(any_string):
    #split a string and store in a list
    resList = any_string.split(" ")
    num_words = len(resList)
    print('number of word: ',num_words)
    
    #split a word into tonken, store to a list after each loop and add length to num_tonkens
    num_tokens = 0
    tonken = list()
    for x in resList:
        characters = [char for char in x]
        tonken = tonken + characters
        num_tokens += len(characters)
    
    #test print the characters tonken
    print('number of tonken: ',tonken)
    return(print(any_string, ":", "num_words:", num_words, "and", "num_tokens:", num_tokens, "respectively"))
   

def lemmatize(any_string, file_name):
    #here comes your code
    
    #create a dictionary list
    dictionary = {} 
    #read txt file and save each word to dictionary including the word it self, exp: test:test,...
    with open(file_name, 'r') as file:
        for line in file:
            word = line.split() # split each line with space
            dictionary.update({word[1]:word[0]})  # save to dict
            dictionary.update({word[0]:word[0]})
    
    # split the string 
    resList = any_string.split()
    #create a list for lemmatized words
    dictionary_of_lemmatized_words = {}
    for x in resList:
        if not(x in dictionary):
            dictionary_of_lemmatized_words.update({x:x})
        else:
            dictionary_of_lemmatized_words.update({x:dictionary[x]})   
    
    #print(dictionary_of_lemmatized_words)
    return(print(dictionary_of_lemmatized_words))

#study-studi
#studies-studi
#studying-studi
#studied


def stemmer(any_string):
    #here comes your code
    
    #split the string to list of word
    wordsList = any_string.split(" ")
    #give the surfix of words
    surfix = ['y','ies','ying','ied']
    #replace surfix with word
    replace_word = 'i'
    #create a list for steemed string
    stemmed_string_list = list()
    
    #2 loop
    #loop1 for each word in the wordList
    #loop2 for each surfix
    for word in wordsList:
        for x in surfix:
            #if the word's surfix doesn't exist in the list
            if not(word.endswith(x)) and surfix.index(x)==(len(surfix)-1):  #this cond true only when the word does'n and with any surfix in the list
                stemmed_string_list.append(word)
            #if the word's surfix exist, then replace surfix with replace_word and break    
            if word.endswith(x):
                surfix_len = len(x)
                replaced_string = word[:-surfix_len] + replace_word #replace surfix
                stemmed_string_list.append(replaced_string)
                break
                
    stemmed_string = ", ".join(stemmed_string_list)
    return(print(stemmed_string))
    

    

if __name__ == "__main__":
   print('Task 1.1')
   extract_words_tokens("this is a example string")
   print()
   print('Task 1.2')
   lemmatize("this is a testing for Tommy","lemmatization-en.txt")
   print()
   print('Task 1.3')
   stemmer('study studies studying studied Hoangkim')   



