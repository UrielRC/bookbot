#se cuentan las palabras

def count_words(book):
    divided = book.split()
    num_words = 0
    for word in divided:
        num_words +=1
    return num_words

#se cuentan los caracteres
def count_characters (book):
    lower = book.lower()
    char_dict = dict()

    for letter in lower:
        if letter in char_dict:
            char_dict[letter] +=1
        else:
            char_dict[letter] = 1
    
    return char_dict



# se cuentan en listas y dicts los num y se ordenan

def key_def(item):
    return item["num"]

def sort_book (list_done):
    ordered_list = []
    for letter in list_done:
        temp_dict = dict()
        #print(f"{letter} es la letra y {list_done[letter]} es el numero")
        if letter.isalpha() == True:
            temp_dict["char"] = letter
            temp_dict["num"] = list_done[letter]
            ordered_list.append(temp_dict)
    ordered_list.sort(reverse=True, key=key_def)
    
    return ordered_list
 