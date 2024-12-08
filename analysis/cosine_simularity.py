import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

class cosine_simularity(file1, file2):
    text1 = ""
    text = ""
    X_list = []
    Y_List = []
    def __init__(self,file1, file2):
        self.file1 = file1
        self.file2 = file2
    def cosine_simularity(self): 
        with open(self.file1, 'r') as file:
            text = file.read()
        with open(self.file2, 'r') as file:
            text1 = self.file2.read()
        X_list = word_tokenize(text)  
        Y_list = word_tokenize(text1) 

        sw = stopwords.words('english')  
        l1 =[];l2 =[] 
        # remove stop words from the string 
        X_set = {w for w in X_list if not w in sw}  
        Y_set = {w for w in Y_list if not w in sw} 
  
        # form a set containing keywords of both strings  
        rvector = X_set.union(Y_set)  
        for w in rvector: 
            if w in X_set: l1.append(1) # create a vector 
            else: l1.append(0) 
        if w in Y_set: l2.append(1) 
        else: l2.append(0) 
        c = 0
  
# cosine formula  
        for i in range(len(rvector)): 
            c+= l1[i]*l2[i] 
        cosine = c / float((sum(l1)*sum(l2))**0.5) 
        print("similarity: ", cosine) 
        
    




