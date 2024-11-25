def readBook(link):
    book_content = "could not read"
    with open (link) as f:
        book_content = f.read()
    return book_content

def countWords(text):
    word_count = len(text.split())
    return word_count

def countChar(textRaw):
    text = textRaw.lower()
    charDict = dict()
    for char in text:
        if char.isalpha():
            if char in charDict:
                charDict[char] += 1
            else: 
                charDict[char] = 1
    return dict(sorted(charDict.items()))

def main(): 
    link = "books/frankenstein.txt"
    bookText = readBook(link)
    word_count = countWords(bookText)
    letter_count = countChar(bookText)
    print(f"{link} has been read! It has {word_count} words")
    for key in letter_count.keys(): 
        print(f"The letter '{key}' was found {letter_count[key]} times")

        
main()

