def get_result(S,k):
    qoutient=len(S)/k
    words=[S[k*i:k*(i+1)] for i in xrange(qoutient)]
    for word in words:
        word_set=''
        for i in word:
            if i not in word_set:
                word_set=word_set+i
        print word_set
    return

if __name__=="__main__":
    get_result(raw_input(),input())