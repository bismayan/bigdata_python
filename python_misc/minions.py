def get_words(S):
    cons_sum=0
    vow_sum=0
    for i in xrange(len(S)):
        if S[i] in ['A','E','I','O','U']:
            vow_sum+=len(S)-i
        else:
            cons_sum += len(S) -i
    if vow_sum > cons_sum:
        print "Kevin {}".format(vow_sum)
    elif vow_sum==cons_sum:
        print "Draw"
    else:
        print "Stuart {}".format(cons_sum)
    return

if __name__=="__main__":
    get_words(raw_input())