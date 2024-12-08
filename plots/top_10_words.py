import matplotlib as mpl 
import tokenizer

def barChart(file):
    content = open(file, "r") 
    text = content.read() 
    my_list.plot = (df[text].value_counts())

    my_list.head(10).plot(kind='bar',stacked=False, figsize=(16,8))
    
    with open('youtube_project\Downloads\charts', 'wb') as f:
        pickle.dump(my_list, f)

    my_list.show() 
