# Lab 07: Alexa reviews
# Your name
# Your email

import string   # for input file parsing

# load input file as list of words (all lower-case, punctuation and spaces removed)
with open('lab_07_alexa_reviews.txt', 'r', encoding = 'utf8') as f: 
    words = f.read().lower().translate(str.maketrans('', '', string.punctuation)).split()
    
### INSERT YOUR CODE BELOW THIS LINE ###
a = int(input("Please Enter Phrase Length: "))
phrase = []
count = {}
for i in range(len(words)-2):
	phrase = words[i]
	for j in range(a - 1):
		phrase += ' ' + words[i+j+1]
		count[phrase] = count.get(phrase, 0) + 1
count_list = []
for k,v in count.items():
	count_list.append([v,k])
count_list = sorted(count_list, reverse = True)

for i in range(10):
	print(count_list[i])
