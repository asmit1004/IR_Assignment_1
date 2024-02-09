import string
import nltk


for i in range(1,1000):
    f=open("file"+str(i)+".txt",'r')
    d=f.read()
    d_lower=d.lower()


    token = nltk.word_tokenize(d_lower) 


    # Define a set of stopwords
    stopwords = set([
        "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves",
        "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their",
        "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was",
        "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and",
        "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between",
        "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off",
        "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any",
        "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so",
        "than", "too", "very", "can", "will", "just", "don't", "should", "now"
    ])


    words = [word for word in token if word not in stopwords]

    punc = [words for words in words if words not in string.punctuation]

    space = [words for words in punc if words.lstrip()!='']

    f=open("copy"+str(i)+".txt", 'w')
    for j in space:
        f.write(j+'\n')

    print("All Preprocessing done and written to:", "copy"+str(i)+".txt")