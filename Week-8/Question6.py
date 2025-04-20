def preprocess(s):
    s = s.lower()
    s = s.split(" ")
    stop = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your",
    "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers",
    "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what",
    "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was",
    "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did",
    "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of",
    "at", "by", "for", "with", "about", "against", "between", "into", "through", "during",
    "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off",
    "over", "under", "again", "further", "then", "once", "here", "there", "when", "where",
    "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some",
    "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t",
    "can", "will", "just", "don", "should", "now"]
    s_out = []
    for w in s:
        if w not in stop:
            s_out.append(w)
    return s_out

def BAND(coll, q):
    length = len(q)
    for key in coll:
        match = 0
        for w in q:
        #print("w: "+w)
            if w in coll[key]:
                match = match + 1
        #print(str(match))
        if match == length:
            print(key)

def BOR(coll, q):
    length = len(q)
    for key in coll:
        match = 0
        for w in q:
        #print("w: "+w)
            if w in coll[key]:
                match = match + 1
        #print(str(match))
        if match > 0:
            print(key)
coll = {
    "doc1" : "Information Retrieval is the science of search engines",
    "doc2" : "This is the age of information technology",
    "doc3" : "Mathematics in the language of science",
    "doc4" : "Efficient retrieval of important data is the feature of any sound search system.",
    "doc5" : "Gerard Salton is the father of Information Retrieval"
    }
for key in coll:
    coll[key] = preprocess(coll[key])
    print(coll[key])
q = "information retrieval".split(" ")
print(q)
BAND(coll, q)
#BOR(coll, q)