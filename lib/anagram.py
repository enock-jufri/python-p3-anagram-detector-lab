# your code goes here!
class Anagram:
    def __init__(self,word):
        self.word=word
    
    def match(self,list):
        self.list=list
        return [i for i in list if sorted(i)==sorted(self.word)]

listen = Anagram("listen")
print(listen.match(['enlists', 'google', 'inlets', 'banana']))


