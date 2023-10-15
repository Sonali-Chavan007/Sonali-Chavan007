import string
def count_words_in_program(file_path):
    with open(file_path, 'r') as file:
        program_text = file.read()
    
    words = program_text.split()
    word_count = len(words)
    
    return word_count

if __name__ == "__main__":
    file_path = "scrap_txt.txt"  # Replace with the path to your Python program
    word_count = count_words_in_program(file_path)
    print(f"Word count in the program: {word_count}")

 
