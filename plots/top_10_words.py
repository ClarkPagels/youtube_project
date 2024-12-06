import matplotlib as mpl 
import ../tokenizer

def barChart(file):
    content = open(file, "r") 
    text = content.read() 
    my_list.plot = (df[text].value_counts())

    my_list.head(10).plot(kind='bar',stacked=False, figsize=(16,8))
