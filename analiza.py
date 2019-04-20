import textblob

neutral = 0 # from -0.15 to 0.15
positive = 0 # 0.15 +
negative = 0 # -0.15 +

with open('engleski.txt', 'r') as file:
    for line in file.readlines():
        line = textblob.TextBlob(line)
        sent = line.sentiment.polarity
        if sent > 0.15:
            positive += 1
        elif sent < (-0.15):
            negative += 1
        else:
            neutral += 1

total = positive + negative + neutral

with open('engleski.txt', 'a') as file:
    file.write(f"""
    Total comments: {total}
    Positive comments: {positive} ({positive/total}%)
    Negative comments: {negative} ({negative/total}%)
    Neutral comments: {neutral} ({neutral/total}%)
    """)
