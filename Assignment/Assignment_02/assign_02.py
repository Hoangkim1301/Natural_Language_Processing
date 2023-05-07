import pandas as pd
import numpy as np
import re

def readFile(file_name):
    with open(file_name,'r') as file:
        sentences = []
        for line in file:
            text_lable = re.split('(pos|neg)', line)
            #print(text_lable[0])
            #print(text_lable[1])
            sentences.append([text_lable[0],text_lable[1]])

    df = pd.DataFrame(sentences, columns=['Text', 'Label'])
    df['Text'] = df['Text'].replace('\t','')
    return(df)

def convert_lable(df):
    # define a lambda function to map values to 0 or 1
    binary_map = lambda x: 0 if x == 'neg' else 1 if x == 'pos' else None
    # apply the lambda function to the 'reviews' column of the dataframe
    df['Label'] = df['Label'].apply(binary_map)
    # print the resulting binary dataframe
    print(df)
    
    
    
#This is the first document.
#This document is the second document.
#And this is the third one.
#Is this the first document?    

def create_count_and_probability(file_name):
    # here comes your code
    words = []
    with open(file_name,'r') as file:
        # iterate over each line of the file
        for line in file:
            # split the line into words using whitespace as a delimiter
            line_words = line.split()
            # add each word to the list if it doesn't already exist in the list
            for word in line_words:
                word = word.replace('?','').replace('.','').lower()
                if word not in words:
                    words.append(word)  
    # print the list of words
    print(words)
    #for line in file:
        
    
    
    
    
    
    #return(csv_file)
    
    
def countVectorize(line,vector):   
    
    
    
    
    
    
    return()
                 
            
if __name__ == "__main__":
    df = readFile('/Users/tommy/Documents/Informatik_Uni_Marburg/Natural_Language_Processing/Assignment/Assignment_02/polarity.txt')        
    #print(df['Label'])
    #convert_lable(df)
    
    
    create_count_and_probability('/Users/tommy/Documents/Informatik_Uni_Marburg/Natural_Language_Processing/Assignment/Assignment_02/corpus.txt')
    my_string = "this is the first document"

    # count the occurrences of the word "the" in the string
    count = my_string.count("the")

    # print the count
    print(count)