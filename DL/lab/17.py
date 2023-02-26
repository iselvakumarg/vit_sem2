# Write  a  function  ‘display_words()’  in  python  to  read  lines  from  a  text  file "ebook.txt", and returns a list with words less than 4 characters.

def display_words():

    with open("ebook.txt", "r") as f:
        words = f.read().split()
        return [word for word in words if len(word) < 4]

print(display_words())

