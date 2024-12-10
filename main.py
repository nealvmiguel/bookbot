def main():
    
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    char_dict = count_characters(text)
    
    print(print_report(char_dict, num_words))
    

   
  
# file of the text
def get_book_text(path):  
    with open(path) as file:
        return file.read()

# count words in book
def count_words(text):
    words = text.split()
    return len(words)
    
# count characters    
def count_characters(text):
    dict = {}
    to_lower_string = text.lower()
    
    for char in to_lower_string:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
            
    return dict
        
def sort_on(dict):
    return dict["num"]
        
def print_report(dict, num_words):
    list = []
    for name, count in dict.items():
        if name.isalpha():
            entry = {"name" :name, "num": count}
            list.append(entry)
       
    list.sort(reverse=True, key=sort_on)
    
    report = "--- Begin report of books/frankenstein.txt ---\n"
    report += f"{num_words} words found in the document\n\n"
    
    for char in list:
        report+=(f"The '{char["name"]}' character was found {char["num"]} times\n")
    
    report += "--- End report ---"
    return report
        

try:
    main()
except FileNotFoundError:
    print("File not found. Check the path variable and filename")



