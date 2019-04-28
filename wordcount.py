# put your code here.

def wordcount(file):

	test_file = open(file)

	word_count = {}

	for word in test_file:
		word_count.get(word, 0) + 1

	test_file.close()

	return word_count

print(wordcount('test.txt'))

