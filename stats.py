def word_count(file_contents):
    num_words = len(file_contents.split())

    return num_words

def character_count(file_contents):
    final = {}

    for char in file_contents.lower():
        if char in final:
            final[char] += 1
        else:
            final[char] = 1


    

    return final

def sort_list(dictionary):
    char_list = []
    for char in dictionary:
        count = dictionary[char]
        char_list.append({"char": char, "count": count})

    def sort_on(dict):
        return dict["count"]
    
    char_list.sort(reverse=True, key=sort_on)

    return char_list
    
 
    