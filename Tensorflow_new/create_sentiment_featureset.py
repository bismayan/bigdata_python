import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import numpy as np
import random, cPickle
from collections import Counter
import io

lemmatizer=WordNetLemmatizer()
hm_lines=100000000

def create_lexicon(pos,neg):
    lexicon=[]
    for fi in [pos,neg]:
        with io.open(fi,'r',encoding='utf-8') as f:
            contents=f.readlines()
            for l in contents[:hm_lines]:
                all_words=word_tokenize(l)
                lexicon+=list(all_words)
    lexicon=[lemmatizer.lemmatize(i) for i in lexicon]
    w_counts=Counter(lexicon)
    l2=[]
    for w in w_counts:
        if 1000 > w_counts[w] > 50:
            l2.append(w)
    print "Length of Lexicon:",len(l2)

    return l2

def sample_handling(sample,lexicon, classification):
    # classification is [1 0] or [0 1] depending on whether it is pos or neg
    featureset=[]

    with io.open(sample,'r',encoding='utf-8') as f:
        contents=f.readlines()
        for l in contents[:hm_lines]:
            current_words=word_tokenize(l.lower())
            current_words=[lemmatizer.lemmatize(i) for i in current_words]
            features=np.zeros(len(lexicon))
            for word in current_words:
                if word.lower() in lexicon:
                    index_value=lexicon.index(word.lower())
                    features[index_value]+=1
            features=list(features)
            featureset.append([features,classification])

    return featureset

def create_feature_sets_and_labels(pos,neg,test_size=0.1):
    ## We should probably create it for only the training set
    lexicon=create_lexicon(pos,neg)
    features=[]
    features+=sample_handling('data_pos_neg/pos.txt', lexicon,[1,0])
    features += sample_handling('data_pos_neg/neg.txt', lexicon, [0, 1])
    random.shuffle(features)

    features=np.array(features)
    testing_size=int(test_size*len(features))
    train_x= list(features[:,0][:-testing_size])
    train_y = list(features[:, 1][:-testing_size])
    test_x = list(features[:, 0][-testing_size:])
    test_y = list(features[:, 1][-testing_size:])

    return(train_x,train_y,test_x,test_y)

if __name__=="__main__":
    train_x, train_y, test_x, test_y=create_feature_sets_and_labels('data_pos_neg/pos.txt','data_pos_neg/pos.txt')
    print "Done creating Vectorizers, Dumping to pickle"
    with open('sentiment_set.pickle','wb') as f:
        cPickle.dump([train_x, train_y, test_x, test_y],f)









