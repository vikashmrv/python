def rW(Sentence): 
	words = Sentence.split(" ") 
	newWords = [word[::-1] for word in words] 
	newSentence = " ".join(newWords) 
	return newSentence 

V= input()
print(rW(V)) 
