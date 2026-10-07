
import re
import string
import emoji
import contractions
import nltk
from nltk.corpus import stopwords

try:
    stopwords.words("english")
except LookupError:
    nltk.download("stopwords")

# Keep negation words because they carry sentiment
keep_words = {"not", "no", "nor", "do", "does", "did"}
stop_words2 = set(stopwords.words("english")) - keep_words

# create clean_text function
def clean_text(text):                                                 # we are creating a function called 'clean_text' and 'text' is the input

    text= emoji.demojize(str(text))                                   # convert emojis to descriptive text
    
    text= str(text).lower()                                           # str- coverts input into string, lower()- coverts uppercase letters to lowercase

    text= contractions.fix(text)                                      # automatically expand contractions 
    
    text= re.sub(r"<.*?>", " ", text)                                 # re.sub()- regular expression, finds patter and replace it with something else
                                                                      # <.*?>: is designed to find HTML tags
    
    text= re.sub(r"http\S+|www\S+"," " , text)                        # this removes web addresses
    
    for i in string.punctuation:                                      # removing punctuations and replacing with a space
        text= text.replace(i, ' ')

    text= re.sub(r"\s+", " ", text).strip()                           # removes extra spaces

    words1= text.split()                                              # split text into words

    words2= [word for word in words1 if word not in stop_words2]      # removing stop words

    text= " ".join(words2)                                            # join words again to a single string
    
    return text                                                       # return the cleaned text
