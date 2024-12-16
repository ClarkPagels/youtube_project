import matplotlib.pyplot as plt
import pandas as pd
import pickle
from collections import Counter

def bar_chart(file):
    # Read the text file
    with open(file, "r") as f:
        text = f.read()

    # Tokenize the text (using a custom tokenizer or basic split for simplicity)
    words = text.split()  # Replace with tokenizer logic if needed

    # Count word frequencies
    word_counts = Counter(words)

    # Get the top 10 most common words
    top_words = word_counts.most_common(10)

    # Convert to a DataFrame for easier plotting
    df = pd.DataFrame(top_words, columns=["Word", "Frequency"])

    # Plot the bar chart
    plt.figure(figsize=(16, 8))
    df.plot(x="Word", y="Frequency", kind="bar", legend=False, color="skyblue")
    plt.title("Top 10 Words by Frequency")
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save the chart to a file
    chart_file = 'youtube_project/Downloads/charts.pkl'
    with open(chart_file, 'wb') as f:
        pickle.dump(df, f)

    # Display the plot
    plt.show()

# Example usage:
# bar_chart("path_to_your_file.txt")