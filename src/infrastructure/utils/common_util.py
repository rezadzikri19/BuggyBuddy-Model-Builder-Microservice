import re
import json
import numpy as np
import pandas as pd

from typing import Union

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

from sklearn.metrics import precision_score, recall_score, roc_auc_score

nltk.download('stopwords')
nltk.download('punkt')

def remove_special_chars(text: str):
  text = text.lower()
  text = re.sub(r'\n|\t|\r|\0', ' ', text)
  text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)
  text = re.sub(r'\s{2,}', ' ', text)
  text = re.sub(r'\s$', '', text)
  text = re.sub(r'\s[b-z]\s', ' ', text)
  text = re.sub(r'\s[b-z]\s', ' ', text)
  text = re.sub(r'\s{2,}', ' ', text)
  return text


def remove_stops(text: str):
  stop_words = set(stopwords.words('english'))
  words = word_tokenize(text)
  filtered_words = [word for word in words if word not in stop_words]
  return ' '.join(filtered_words)


def custom_cosine_similarity(text_1: np.ndarray, text_2: np.ndarray):
  dot_product = np.dot(text_1, text_2)
  norm_text_1 = np.linalg.norm(text_1)
  norm_text_2 = np.linalg.norm(text_2)
  similarity = dot_product / (norm_text_1 * norm_text_2)
  return similarity


def evaluate_embedding_model(similarity_scores: Union[np.ndarray, pd.Series], labels: Union[np.ndarray, pd.Series], threshold: float):
  embd_binary_similarity = (similarity_scores > threshold).astype(int)
  precision = precision_score(labels, embd_binary_similarity)
  recall = recall_score(labels, embd_binary_similarity)
  auc = roc_auc_score(labels, embd_binary_similarity)
  return [precision, recall, auc]


def save_json(data, path: str):
  with open(path, 'w') as json_file:
    json.dump(data, json_file)