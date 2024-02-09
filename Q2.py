import pickle
import nltk
import string

def pre(d):
    d_lower=d.lower()


    token = nltk.word_tokenize(d_lower) 


    # Define a set of stopwords
    stopwords_set = set([
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


    filtered_words = [word for word in token if word not in stopwords_set]

    filtered_punctuation = [words for words in filtered_words if words not in string.punctuation]

    content_without_spaces = [words for words in filtered_punctuation if words.lstrip()!='']

    return content_without_spaces

inverted_index = {}

for i in range(1,1000):
    file_path='copy'+str(i)+'.txt'

    f=open(file_path, 'r')
    for line in f:
        words = line.strip().split()
        for word in words:
            if word not in inverted_index:
                inverted_index[word] = set([i])
            else:
                inverted_index[word].add(i)

# print(inverted_index)
                
fi = open("index.pickle","wb")
pickle.dump(inverted_index,fi)

fread = open("index.pickle","rb")
load=pickle.load(fread)

#print(load)
SET = set()
for i in range(1,1000):
    SET.add(i)

def function_operation(op,sq,result_set):
    if (op=="AND"):
        if sq not in load:
            return result_set & set()
        return result_set & load[sq]
    elif (op=="OR"):
        if sq not in load:
            return result_set
        return result_set | load[sq]
    elif (op=="AND NOT"):
        if sq not in load:
            return result_set - set()
        return result_set - load[sq]
    


print('\n')
n = int(input("enter number of queries: "))

for i in range(n):
    inp1=input("Enter sequence : ")
    inp2=input("Enter queries : ")

    inp3=pre(inp1)
    sp=inp2.split(',')

    result_set=load[inp3[0]]
    # print(result_set)

    for i in range(len(sp)):
        result_set = function_operation(sp[i],inp3[i+1],result_set)
    
    print(result_set)