# Imports
import wikipedia
import nltk
from nltk import pos_tag, word_tokenize

store = list()
sentence = raw_input("Q. ")
#text = word_tokenize(sentence)
#tagged = nltk.pos_tag(text)
tagged = pos_tag(sentence.split())

print "After POS Tagging :",tagged

propernouns = [word for word,pos in tagged if pos == 'NN' or pos == 'NNP']
print "Proper Nouns :",propernouns


#print wikipedia.summary("Wikipedia")
#print "---------------------------------\nEnter Search Term on Wikipedia :"
#search_term = raw_input();
store = wikipedia.search(propernouns)
print store
"""for i in store:
    print i,
print "---------------------------------"
ny = wikipedia.page("Linus Torvalds")
print"****************************Wikipedia Page of Linus Torvalds :",ny 
print "---------------------------------"
print "***************************Page Title :",ny.title
print "---------------------------------"
print "***************************URL of the Page  :",ny.url
print "---------------------------------"
print "****************************Contents of the Page :",ny.content
"""

#Who is Taylor Swift?

