import pandas as pd

data = []

with open("../datasets/raw/SMSSpamCollection", "r", encoding="latin-1") as file:
    for line in file:
        parts = line.strip().split("\t")
        if len(parts) == 2:
            label, text = parts
            label = 1 if label == "spam" else 0
            data.append([label, text])

df = pd.DataFrame(data, columns=["label", "text"])

df.to_csv("../datasets/processed/sms_spam.csv", index=False)

print("CSV created successfully!")
print(df.head())