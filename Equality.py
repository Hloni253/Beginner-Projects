'''  A program that isolates specific words in a text and replaces them with other words '''

class Equality:
    def __init__(self, text, word, o_word):
        self.text = text
        self.word = word
        self.o_word = o_word
    
    def action(self):
        text_piece = self.text.split(" ")
        for name in text_piece:
            if name == self.word:
                name_index = text_piece.index(name)
                text_piece[name_index] = self.o_word
        print(text_piece)
    
Text = str(input("The text you want changed: "))
Word = str(input("The word you want changed: "))
O_word = str(input("The word you want to change with: "))

equal = Equality(Text, Word, O_word)
equal.action()


#text = str(input("Input your text: "))
#word = str(input("Input the word you want removed: "))
#o_word = str(input("The word you want to replace with: "))

#text_piece = text.split(" ")
#for name in text_piece:
 #   if name == word:
  #      name_index = text_piece.index(name)
   #     text_piece[name_index] = o_word
#print(text_piece)
        