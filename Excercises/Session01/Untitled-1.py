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
   


if __name__ == "__main__":
    extract_words_tokens("this is a example string")
   
