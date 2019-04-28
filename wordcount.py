# put your code here.

def wordcount(file):

	test_file = open(file)

	word_count = {}

	for line in test_file:
		for word in line:
			word_count[word] = word_count.get(word, 0) + 1


	test_file.close()

	# return word_count

	return (word, word_count[word])

print(wordcount('test.txt'))

