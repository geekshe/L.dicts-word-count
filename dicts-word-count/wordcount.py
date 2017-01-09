import sys

# put your code here.


def count_words(file_name):

    the_file = open(file_name)
    word_count = {}
    for line in the_file:
        line = line.rstrip()
        word_list = line.split(" ")
        for word in word_list:
            word = word.rstrip(",").rstrip(".").rstrip("!").rstrip("?")
            word = word.lower()
            word_count[word] = word_count.get(word, 0) + 1
    for key, value in word_count.iteritems():
        print key, value
    # word_count_list = word_count.items()
    # for item in word_count_list:
    #     print item
    # return word_count

# count_words("test.txt")
count_words(sys.argv[1])
