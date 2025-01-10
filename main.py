def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    # counts number of words
    number_of_words = count_words(file_contents)
    
    #lists how many of each character in the text
    total_count = character_count(file_contents)
    #print(f"The total character count is {total_count}")

    print("--- Begin report of books/frankenstein.txt ---")
    print("")
    print(f"{number_of_words} words found in the document.")

    def sort_on(dict):
        return dict["count"]
    
    char_list = []
    char_counts = character_count(file_contents)
    for char, count in char_counts.items():
        if char.isalpha():
            char_dict = {
                "char": char,
                "count": count
            }
            char_list.append(char_dict)
            
    char_list.sort(reverse=True, key=sort_on)
    
    # Need to loop through the sorted list to print each item
    for item in char_list:
        print(f"The '{item['char']}' character was found {item['count']} times.")
    print("")
    print("--- End report ---")



    #print(char_counts)

def count_words(text):
    words = text.split()
    return len(words)

def character_count(text):
    running_count = {}
    for char in text.lower():
        if char not in running_count:
            running_count[char] = 1
        else:
            running_count[char] += 1
    return running_count


main()  



    
