def toBeTheList(word):
    wordList = list()
    for i in word:
        wordList.append(i)
    wordList.sort()
    return wordList

def isAnagram(s1,s2):
    result = True
    if toBeTheList(s1) != toBeTheList(s2):
        result = False
    return result

if __name__ == '__main__':
    s1 = ["listen", "car", "anagram", "a", "ttttttta"]
    s2 = ["slient", "rat", "nagaram", "an", "tatttttt"]
    for i in range(5):
        print(isAnagram(s1[i], s2[i]))
