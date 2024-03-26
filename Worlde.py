import sys, os


def main(argv):

    Master_word_list = []
    debug = True
    debug = False
    
    yellow_letters = {}
    green_letters = {}
    solution_list = []
    valid = True    
            
    with open("word_list.txt", 'r') as f:
        #read in the list of possible words into a list
        for line in f:
            if len(line) >= 1:#in case there are empty lines...
                Master_word_list.append(line.strip())
        
    #get user input
    
    #need a list of all words NOT in the list.
    grey_letters = input("\nEnter all grey Letters (letters NOT in the word) (No spaces) (i.e \"artcl\") \n  :")
    
    
    yellow_letters_list = input("\nEnter all yellow letters found in the word (correct letters in the wrong position (No spaces) (i.e \"klg\") \n  :")
        #for each letter, list all INCORRECT positon(s) as a list
    for letter in yellow_letters_list:
        #TODO input validation
        
        #this conprehnsion grabs user input and converts it to list of ints
        #each letter entry contains a list of ints i.e [1, 4]           
        yellow_letters[letter] = [int(f) for f in input(f"\nWhat position(s) is the yellow {letter} in? [1-5] (no spaces)\n  :")]
            
   
    green_letters_list = input("\nEnter all green letters found in the word (correct letters in the correct position (No spaces) (i.e \"alm\") \n  :")
    for letter in green_letters_list:
            #TODO input validation
            
            #this conprehnsion grabs user input and converts it to list of ints
            #each letter entry contains a list of ints i.e [1, 4]           
            green_letters[letter] = [int(f) for f in input(f"\nWhat position(s) is the yellow {letter} in? [1-5] (no spaces)\n  :")]
            
          
    #for every word in the master word list:
    for word in Master_word_list:
        valid = True 
    
    
        #if the word contains a grey letter:
        for letter in grey_letters:
            if letter in word:
                valid = False
                if debug: print(f"{word} invalid: Grey letter ({letter}) found in word")
                break
                
        #if the word does not contain a yellow letter OR contains a yellow letter in an invalid locaition:
        for letter in yellow_letters.keys():
            if letter not in word: 
                if debug: print(f"{word} invalid: Yellow letter({letter}) not found in word")
                valid = False
                break
                
            if letter in word:
                for position in yellow_letters[letter]:
                    if word[position - 1] == letter:
                        valid = False
                        if debug: print(f"{word} invalid: Yellow letter ({letter}) found in invalid position ({position})")
                        break
            
        #if the word does not contain a green letter or does not contain one in the correct position
            #continue                    
        for letter in green_letters:
            if letter not in word: 
                valid = False
                if debug: print(f"{word} invalid: Green letter({letter}) not found in word")
                break
            if letter in word:
                for position in green_letters[letter]:
                    if word[position - 1] != letter:
                        valid = False
                        if debug: print(f"{word} invalid: Green letter ({letter}) not found in correct position ({position})")
                        break
        
        if debug: print("Adding word to solutions list")
        if valid: solution_list.append(word)
                
                
    #Output solution list
    print(solution_list)
    input("Press \'Enter\' to Exit ")
if __name__ == "__main__":
    main(sys.argv)
