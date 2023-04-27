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
    dictionary = {"word":"lemma"}
    with open(file_name, 'r') as file:
        for line in file:
            word = line.split()
            dictionary.update({word[0]:word[1]})  # strip the newline character from each line
    print(dictionary)        
    
    #split the any_string
    tonken = any_string.split()
    print(dictionary[tonken[0]])
    
    """
    dictionary_of_lemmatized_words = {" ":" "}
    for x in tonken:
        dictionary_of_lemmatized_words.update({x,dictionary[x]})

    """
    #print(dictionary[any_string])    
    
    
    
            
    """"   
    if word[0] == any_string:
                print(word[1])
                dictionary_of_lemmatized_words = {word[1],word[0]}
                """

    
    #return(print(dictionary_of_lemmatized_words))


if __name__ == "__main__":
   #extract_words_tokens("this is a example string")
   lemmatize("10 and","/Users/tommy/Documents/Informatik_Uni_Marburg/Natural_Language_Processing/Excercises/Session01/lemmatization-en.txt")
