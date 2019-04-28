# put your code here.

def wordcount(file):

	test_file = open(file)

	file = []
	word_count = {}

	for line in test_file:
		line = line.rstrip()
		file += line.split()
	test_file.close()
	for word in file:
		word_count[word] = word_count.get(word, 0) + 1

	# return word_count

	return (word_count)

print(wordcount('test.txt'))

