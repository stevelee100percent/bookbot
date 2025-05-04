


def number_of_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    # Count all characters that are letters
    lower_text = text.lower()
    letter_counts = {}
    
    for char in lower_text:
        if char.isalpha():  # Check if it's a letter (any Unicode letter)
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1
    
    return letter_counts

def sort_chars(char_count):
    # Create a list to hold our dictionaries
    chars_list = []
    
    # Convert each key-value pair to a dictionary and add to list
    for char, count in char_count.items():
        chars_list.append({"char": char, "num": count})
    
    # Sort the list by count (num) in descending order
    def sort_on(dict):
        return dict["num"]
    
    chars_list.sort(reverse=True, key=sort_on)
    
    return chars_list



    
