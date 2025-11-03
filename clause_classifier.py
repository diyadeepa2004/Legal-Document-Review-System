from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

def train_clause_classifier(data, labels):
    vec = CountVectorizer()
    X = vec.fit_transform(data)
    model = MultinomialNB()
    model.fit(X, labels)
    pickle.dump((vec, model), open("models/risk_model.pkl", "wb"))
    print("Model trained and saved.")

def predict_clause_risk(text):
    vec, model = pickle.load(open("models/risk_model.pkl", "rb"))
    X = vec.transform([text])
    pred = model.predict(X)
    return "High Risk" if pred[0] == 1 else "Low Risk"
