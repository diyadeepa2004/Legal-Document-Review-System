import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords', quiet=True)

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^a-zA-Z0-9., ]', '', text)
    words = text.lower().split()
    stop_words = set(stopwords.words('english'))
    filtered = [w for w in words if w not in stop_words]
    return ' '.join(filtered)
