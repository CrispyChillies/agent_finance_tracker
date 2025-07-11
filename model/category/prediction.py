from sentence_transformers import SentenceTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
import numpy as np

texts = []
labels = []

with open("expense_samples.txt", "r", encoding="utf-8") as f:
    for line in f:
        label, text = line.strip().split(" ", 1)
        labels.append(label.replace("__label__", ""))
        texts.append(text)

embedder = SentenceTransformer("all-MiniLM-L6-v2")
X = embedder.encode(list(texts))
y = np.array(labels)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

clf = LogisticRegression(max_iter=1000)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))

joblib.dump(clf, "expense_classifier.joblib")
joblib.dump(embedder, "embedding_model.joblib")
