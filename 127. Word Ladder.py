class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # ## use single-direction BFS  
        # if endWord not in wordList:
        #     return 0
        # queue = collections.deque()
        # queue.append((beginWord,1 ))
        # while queue:
        #     word, count = queue.popleft()
        #     for index in range(len(word)):
        #         for letter in string.ascii_lowercase:
        #             newword = word[:index] + letter + word[index + 1:]
        #             if newword == endWord:
        #                 return count + 1
        #             if newword in wordList:
        #                 queue.append((newword,count+1)) 
        #                 wordList.remove(newword)
        # return 0
     ## bidirection BFS
        worddict = set(wordList)
        if endWord not in wordList:
            return 0
        beginqueue = {beginWord}
        endqueue = {endWord}
        worddict.remove(endWord)
        count = 0  
        while beginqueue and endqueue:
            count += 1 
            queue = set()
            if len(beginqueue) > len(endqueue):
                beginqueue, endqueue = endqueue, beginqueue
            for word in beginqueue:
                newwords= [word[:index] + letter + word[index + 1:] for letter in string.ascii_lowercase for index in xrange(len(beginWord))]
                for new in newwords:
                    if new in endqueue:
                        return count + 1 
                    if new in worddict:
                        queue.add(new) 
                        worddict.remove(new)
            beginqueue = queue
        return 0