import matplotlib.pyplot as plt
import re
import pickle 
def zipf(text):

    #Convert text to lower case
    text = text.lower()

    #Remove the unwanted characters
    textList = re.split(', | |\. ', text)

    textDict = {}
    wordFrequency={}

#Find the frequency of words
    for txt in textList:
        if txt in textDict.keys():
            textDict[txt]+=1
        else:
            textDict[txt]=1

#Sort the word frequencies in descending order
    wordFrequency = dict(
            sorted(
                textDict.items(),
                key=lambda x: x[1],
                reverse=True)
            )

#Define two lists, rank and frequency
    rank = []
    frequency = []
    init = 0

#Assign ranks based on frequencies of words
    for freq in wordFrequency.values():
        init+=1
        rank.append(init)
        frequency.append(freq)

    #Plot the rank and frequency
    plt.plot(rank,frequency)

    # Labelling the x axis
    plt.xlabel('Rank(r)')
    # Labelling the y axis
    plt.ylabel('Frequency(f)')

    # Providing a title to the graph
    plt.title("Zipf's law")
    #save graph
    with open('youtube_project\Downloads\charts', 'wb') as f:
        pickle.dump(plt, f)
    
    plt.show()
    
