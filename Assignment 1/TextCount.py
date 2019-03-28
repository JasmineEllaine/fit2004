def preprocess(filename):
    """Removes punctuation from a text given a filename.
    Args:
        filename (str): the name of the file containing
        the text to be processed.
    Raises:
        None
    Returns:
        words (list<str>): list of processed words.
    Time complexity:
        O(nm): where n is the number of lines of text in
            the file, and m is the number of characters
            per line
    Space Complexity:
        O(nm): same as above.
    """    
    # List of  characters and words to omit.
    punctuation =  [",", ".", "?", "!", ":", ";", '"', \
                    "\n", "\t", "\r"]
    ignoredWords = ["am", "is", "are", "was", "were", \
                    "has", "have", "had", "been", "will", \
                    "shall", "may", "can", "would", \
                    "should","might", "could", "a", \
                    "an", "the"]
    
    # Reads from file and strips it of \n and \t.
    text = open(filename, "r")
    words = []

    for line in text:
        word = ""
        for char in line:
            # Initialises empty word if space is detected.
            if char == " ":
                # Adds word to words if not in ignoredWords.
                if word not in ignoredWords:
                    words.append(word)
                word = ""
            # Includes character if not a punctuation.
            elif char not in punctuation:
                word += char
        # Adds the last word in the line to words.
        if word not in ignoredWords:
            words.append(word)

    return words

def wordSort(words):
    """Sorts list of words in alphabetical order.
    Args:
        words (list<str>): words to be sorted.
    Raises:
        None
    Returns:
        words (list<str>): sorted words.
    Time complexity:
        O(nm): where n is the number of words in words,
        and m is the length of the longest word.
    Space Complexity:
        O(nm): same as above.
    """
    # Get length of the longest word.
    currMax = 0
    for word in words:
        if len(word) > currMax:
            currMax = len(word)
    
    # i is the index of the character by which the list
    # should be sorted by.
    for i in range(currMax-1, -1, -1):
        words = countSort(words, i, currMax)
    
    return words

def countSort(words, index, maxWordLength):
    """Sorts list of words in alphabetical order.
    Args:
        words (list<str>): words to be sorted.
    Raises:
        None
    Returns:
        words (list<str>): sorted words.
    Time complexity:
        O(n): where n is the number of words in words.
    Space Complexity:
        O(n): same as above.
    """
    # Array of indices corresponding to letter where index 0
    # is an a etc.
    countSortArray = [[] for _ in range(27)]

    for wordIndex, word in enumerate(words):
        # Makes word same length as the maximum word length.
        word = word + chr(96)*(maxWordLength-len(word))
        
        # Updates indices array
        countSortIndex = ord(word[index]) - 96
        countSortArray[countSortIndex].append(wordIndex)
        
    newWords = []
    for indices in countSortArray:
        for index in indices:
            newWords.append(words[index])

    return newWords

def wordCount(words):
    """Counts total number of words in a list and
    calculates frequency of each word.
    Args:
        words (list<str>): words to be tallied.
    Raises:
        None
    Returns:
        words (list<list>): frequency tally.
    Preconditions:
        List of words are sorted so that words that are
        identical should be next to each other.
    Time complexity:
        O(n): where n is the number of lines of text in
            the file.
    Space Complexity:
        O(n): same as above.
    """
    words += [""]
    # Frequency table initialised to only contain the
    # length of list.
    wordFrequency = [len(words)] 

    i = 0
    j = 1
    # Check every consecutive word for a match.
    while j < len(words):
        # Increment j if the next word is a duplicate.
        if words[i] == words[j]:
            j += 1
        else:
            # Update frequency table once word is tallied.
            wordFrequency.append([words[i], j-i])
            i = j
            j += 1

    return wordFrequency
        
def kTopWords(k, wordsFrequency):
    """Returns the top k most frequent words in the list.
    Args:
        k (int): nubmer of most frequent words to be
            returned.
        wordsFrequency (list<list>): frequency table of words.
    Raises:
        Exception: When wordsFrequency is empty.
        Exception: When number of elements in wordsFrequency
            is less than k.        
    Returns:
        topWords (list<list>): top k words and their frequency.
    Time complexity:
        ***
    Space Complexity:
        ***
    """
    # Raises
    if wordsFrequency == []:
        raise Exception("List is empty.")
    elif len(wordsFrequency) < k:
        raise Exception("Number of elements in list is less than k.")
    
    topWords = []

    # Finds word with highest frequency.
    currMax = 0
    for wordList in wordsFrequency:
        if wordList[1] > currMax:
            currMax = wordList[1]

    # Finds words with the same frequency as currMax.
    while len(topWords) < k:
        for wordList in wordsFrequency:
            if wordList[1] == currMax:
                topWords.append(wordList)
                if len(topWords) == k:
                    break
        # Decremements currMac so that the next most
        # frequent word can be determined.
        currMax -= 1
    
    return topWords

words = preprocess("Writing.txt")
# for i in words:
#     print(i)
# print(len(words))

# words = preprocess("Writing.txt")
words = wordSort(words)
# for i in words:
#     print(i)

# newWords = ['alien', 'cat', 'cat', 'dog', 'zebra', 'zebra']
newWords = wordCount(words)
# for i in newWords:
#     print(i)

# topWords = [['aggressive',1],['alien',3],['and', 2],['big',1],['creature',1],['it', 4], ['our', 3], ['zebra', 2]]
topWords = kTopWords(11, newWords[1:])
for i in topWords:
    print(i)