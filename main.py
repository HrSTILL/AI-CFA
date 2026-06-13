def analyze_sentiment(text):
    text = text.lower()

    if "bad" in text:
        return "Negative"
    elif "great" in text:
        return "Positive"
    else:
        return "Neutral"


def count_positive(reviews):
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

for review in reviews:
    review = review.strip()
    result = analyze_sentiment(review)
    print(review + " -> " + result)

stats = count_positive(reviews)
print()

print("Positive:", stats["Positive"])
print("Negative:", stats["Negative"])
print("Neutral:", stats["Neutral"])

