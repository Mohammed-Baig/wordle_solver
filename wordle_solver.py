import re

def filter_by_known_positions_regex(word_list, correct_letters):
    # Build regex pattern
    pattern = "^" + "".join([letter if letter.isalpha() else "." for letter in correct_letters]) + "$"

    # Debug: Print the generated regex pattern
    print(f"Generated regex pattern: {pattern}")

    # Filter the words
    filtered_list = [word for word in word_list if re.match(pattern, word)]
    return filtered_list

def filter_by_known_positions_and_yellow_tiles(word_list, correct_letters, wrong_spots, yellow_tiles):
    filtered_list = []
    
    for word in word_list:
        # Check if the word contains all the yellow tiles (l, o, g) somewhere in it
        if not all(tile in word for tile in yellow_tiles):
            continue
        
        # Check that yellow tiles are not in their wrong positions
        valid = True
        for i, letter in enumerate(wrong_spots):
            if letter != ' ' and word[i] == letter:
                valid = False
                break
        
        if not valid:
            continue
        
        # If all checks pass, add the word to the filtered list
        filtered_list.append(word)
    
    return filtered_list


# opening the file in read mode
my_file = open("words.txt", "r")

# reading the file
data = my_file.read()

# replacing end splitting the text
# when newline ('\n') is seen.
data_into_list = data.split("\n")
print(data_into_list)
#print(data_into_list[0])
my_file.close()

correct_letters = input("Enter your word with ONLY the green tiles in the exact same spots, leave grey and yellow tiles as empty spaces here:")
wrong_spots = input("Enter your word with ONLY the yellow tiles in the exact same spots, leave grey and green tiles as empty spaces here:")
incorrect_letters = input("Enter ALL the letters that are greyed out(incorrect) with no spaces in between: ")

print(list(correct_letters))
print(list(wrong_spots))
print(list(incorrect_letters))

pattern = f"[{incorrect_letters}]"
filtered_words = [word for word in data_into_list if not re.search(pattern, word)]
print(filtered_words)

filtered_words_2 = filter_by_known_positions_regex(filtered_words, list(correct_letters))
print(filtered_words_2)

filtered_words_3 = filter_by_known_positions_and_yellow_tiles(filtered_words_2, correct_letters, wrong_spots, yellow_tiles)
print(filtered_words_3)
