def is_matched(expression):
    brack_stack=[]
    rep_dict={'(':')','{':'}','[':']',')':'(','}':'{',']':'['}
    brack_stack.append(rep_dict[expression[0]])
    for i in expression[1:]:
#    	print i,brack_stack
    	if brack_stack==[]:
		brack_stack.insert(0,rep_dict[i])
	elif brack_stack[0]==i:
	        brack_stack.pop(0)
	else:
		brack_stack.insert(0,rep_dict[i])	
    return(len(brack_stack)==0,brack_stack)





with open('brack_input.dat','r') as f:
	with open('brack_out.dat','r') as f1:
		lines_out=f1.readlines()
		lines=f.readlines()
		t=int(lines[0].strip())
		count=0
		for a0 in xrange(t):
		    expression = lines[a0+1].strip()

		    if is_matched(expression)[0] == True:
		       if ('YES'!=lines_out[a0].strip()):
		       		print "Fuck_up:",a0+2,'Yes',lines_out[a0].strip()
		    		print expression,is_matched(expression)[1]
		       else:
				count+=1
		    else:
		       if ('NO'!=lines_out[a0].strip()):
		       		print "Fuck_up:",a0+2,'No',lines_out[a0].strip()
		    		print expression,is_matched(expression)[1]
		       else:
		       		count+=1
		print count
#t = int(raw_input().strip())
#for a0 in xrange(t):
#    expression = raw_input().strip()
#    if is_matched(expression) == True:
#    	print "YES"
#    else:
#    	print "NO"
