import re
import sys

print(sys.argv)
exit 

#f = open("/usr/share/dict/words")
#https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt
f = open("words.txt")
words = f.read().splitlines()
expression = sys.argv[1]
missing = ''
if len(sys.argv)>2:
	missing = sys.argv[2]
bulls = ''
if len(sys.argv)>3:
	bulls = sys.argv[3]
suggestions = []
expression = expression.lower().replace("?",".")
bulls = bulls.lower()
missing = missing.lower()

print("Expression "+ expression)
print("missing "+ missing)
print("bulls "+bulls)


def char_match(word1, word2):
	return len(set(word1)&set(word2))

for word in words:
	word = word.lower()
	if len(word)==5:
		if len(re.findall(expression, word))==1:
			if missing=='' or char_match(word, missing)==0:
				if bulls=='' or char_match(word, bulls)==len(bulls):
					suggestions.append(word)
print("-------------SUGGESTIONS------\n")
for word in suggestions:
	print(word)


