def analyze_sentiment(text):
    text = text.lower()

    if "bad" in text:
        return "Negative"
    elif "great" in text:
        return "Positive"
    else:
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


with open("reviews.txt", "r") as f:
    reviews = f.readlines()

stats = count_sentiments(reviews)

with open("results.txt", "w") as file:
    for review in reviews:
        review = review.strip()
        result = analyze_sentiment(review)
        file.write(review + " -> " + result + "\n")

    file.write("\n")
    file.write(f"Positive: {stats['Positive']}\n")
    file.write(f"Negative: {stats['Negative']}\n")
    file.write(f"Neutral: {stats['Neutral']}\n")