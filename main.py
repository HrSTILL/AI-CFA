import csv

def analyze_sentiment(text):
    text = text.lower()

    positive_words = [
        "great",
        "excellent",
        "amazing",
        "good",
        "fast"
    ]

    negative_words = [
        "bad",
        "terrible",
        "awful",
        "slow",
        "poor"
    ]

    for word in negative_words:
        if word in text:
            return "Negative"
    for word in positive_words:
        if word in text:
            return "Positive"
    return "Neutral"


def count_sentiments(reviews):
    stats = {
        "Positive": 0,
        "Negative": 0,
        "Neutral": 0
    }

    for review in reviews:
        result = analyze_sentiment(review)
        stats[result] += 1

    return stats


reviews = []

with open("reviews.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        reviews.append(row["Review"])

stats = count_sentiments(reviews)

with open("results.csv", "w", newline="") as file:
    fieldnames = ["Review", "Sentiment"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    for review in reviews:
        result = analyze_sentiment(review)

        writer.writerow({
            "Review": review,
            "Sentiment": result
        })

with open("summary.txt", "w") as file:
    file.write(f"Positive: {stats['Positive']}\n")
    file.write(f"Negative: {stats['Negative']}\n")
    file.write(f"Neutral: {stats['Neutral']}\n")

print("Analysis completed.")
print("Results saved to results.csv")
print("Statistics saved to summary.txt")
