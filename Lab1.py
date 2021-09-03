from bs4 import BeautifulSoup                                                   #Import statements get stopwords, token separators
import urllib.request
import nltk
from nltk.corpus import stopwords
sr = stopwords.words('english')
response = urllib.request.urlopen('https://en.wikipedia.org/wiki/SpaceX')       #Get Spacex info from its Wikipedia page
html = response.read()                                                          #Get text from page
soup = BeautifulSoup(html, "html5lib")                                          
text = soup.get_text(strip=True)
tokens = [t for t in text.split()]                                              #Separate and tokenize text
clean_tokens = tokens[:]
for token in tokens:
    if token in stopwords.words('english'):
        clean_tokens.remove(token)                                              #Remove stopword tokens
freq = nltk.FreqDist(clean_tokens)
for key,val in freq.items():
    if val > 4:                                                                 #print tokens with >5 frequency
        print(str(key) + ':' + str(val))
freq.plot(10, cumulative=False)                                                 #plot frequency