def extract_words_tokens(any_string):
    #split a string and store in a list
    resList = any_string.split(" ")
    num_words = len(resList)
    print(num_words)
    
    #split a word into tonken, store to a list after each loop and add length to num_tonkens
    num_tokens = 0
    tonken = list()
    for x in resList:
        characters = [char for char in x]
        tonken = tonken + characters
        num_tokens += len(characters)
    
    #test print the characters tonken
    print(tonken)
    return(print(any_string, ":", "num_words:", num_words, "and", "num_tokens:", num_tokens, "respectively"))
   

def lemmatize(any_string, file_name):
    #here comes your code
    dictionary = {}
    
    with open(file_name, 'r') as file:
        for line in file:
            word = line.split()
            dictionary.update({word[1]:word[0]})  # strip the newline character from each line 
            dictionary.update({word[0]:word[0]})
    
    resList = any_string.split()
    dictionary_of_lemmatized_words = {}
    for x in resList:
        dictionary_of_lemmatized_words.update({x:dictionary[x]})    
    
    
    print(dictionary["tests"])
    print(dictionary_of_lemmatized_words)
    #return(print(dictionary_of_lemmatized_words))


if __name__ == "__main__":
   # extract_words_tokens("this is a example string")
   # 
   lemmatize("this is a test","D:\\Informatik_Uni_Marburg\\Natural Language Processing\\Excercises\\Session01\\lemmatization-en.txt")
