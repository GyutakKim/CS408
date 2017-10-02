from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim

import os

doc_set = []

os.chdir('input')
papers = os.listdir('.')

for paper in papers:
  f = open(paper, 'r')
  doc_set.append(f.read().decode('utf-8').strip())

cnt = 0
for doc in doc_set:
  print(cnt)
  print(doc)
  cnt += 1

tokenizer = RegexpTokenizer(r'\w+')

docs = []

for doc in doc_set:
  raw = doc.lower()
  tokens = tokenizer.tokenize(raw)
  print(tokens)

  en_stop = get_stop_words('en')
  stopped_tokens = [i for i in tokens if not i in en_stop]
  print(stopped_tokens)

  p_stemmer = PorterStemmer()

  texts = [p_stemmer.stem(i) for i in stopped_tokens]

  docs.append(texts)

print(docs)

dictionary = corpora.Dictionary(docs)
corpus = [dictionary.doc2bow(doc) for doc in docs]

lda_model = gensim.models.ldamodel.LdaModel(corpus, num_topics=3, id2word=dictionary, passes=30)

print(lda_model.print_topics(num_topics=3, num_words=3))