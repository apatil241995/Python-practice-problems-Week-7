def replace_word(sent):
  word = input("Enter the word to be replaced: ")
  replace_with = ("Enter thr word to replace with: ")
  sent.replace(word,replace_with)
  return sent

def replace_alphabet(sent):
  alphabet = input("Enter the alphabet to be replaced: ")
  replace_with = input("Enter the alphabet to replace with: ")
  sent.replace(alphabet,replace_with)
  return sent


if __name__=="__main__":
  sentence = input("write the sentence: ")
  replace_word(sentence)
  replace_alphabet(sentence)