from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim

doc_a = "Hardware support for isolated execution (such as Intel SGX) enables development of applications that keep their code and data confidential even while running in a hostile or compromised host. However, automatically verifying that such applications satisfy confidentiality remains challenging. We present a methodology for designing such applications in a way that enables certifying their confidentiality. Our methodology consists of forcing the application to communicate with the external world through a narrow interface, compiling it with runtime checks that aid verification, and linking it with a small runtime that implements the narrow interface. The runtime includes services such as secure communication channels and memory management. We formalize this restriction on the application as Information Release Confinement (IRC), and we show that it allows us to decompose the task of proving confidentiality into (a) one-time, human-assisted functional verification of the runtime to ensure that it does not leak secrets, (b) automatic verification of the application’s machine code to ensure that it satisfies IRC and does not directly read or corrupt the runtime’s internal state. We present \confidential: a verifier for IRC that is modular, automatic, and keeps our compiler out of the trusted computing base. Our evaluation suggests that the methodology scales to real-world applications."
doc_b = "My mother spends a lot of time driving my brother around to baseball practice."
doc_c = "Some health experts suggest that driving may cause increased tension and blood pressure."
doc_d = "I often feel pressure to perform well at school, but my mother never seems to drive my brother to do better."
doc_e = "Health professionals say that brocolli is good for your health."
doc_set = [doc_a, doc_b, doc_c, doc_d, doc_e]

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
print corpus

lda_model = gensim.models.ldamodel.LdaModel(corpus, num_topics=2, id2word=dictionary, passes=30)

print(lda_model.print_topics(num_topics=2, num_words=3))