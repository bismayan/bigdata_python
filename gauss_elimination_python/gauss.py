import numpy as np


def upper_triangle(A,B):
	dim=A.shape[0]
	tot_mat=np.hstack((A,B.reshape(dim,1)))
	for i in range(dim):
		if tot_mat[i,i]==0:
			el=np.where(np.diag(tot_mat[i:dim,i:dim])!=0)[0][0]+i
			if el is None:
				raise ValueError," System might not have a solution"
			else:
				tot_mat[[i,el]]=tot_mat[[el,i]]
		for j in range(i+1,dim):
			tot_mat[j]=tot_mat[j]-(tot_mat[j,i]/tot_mat[i,i])*tot_mat[i]
	return tot_mat[0:dim,0:dim],tot_mat[:,-1]


def lower_triangle(A,B):
	dim=A.shape[0]
	tot_mat=np.hstack((A,B.reshape(dim,1)))
	for i in range(dim-1,-1,-1):
		if tot_mat[i,i]==0:
			el=np.where(np.diag(tot_mat[i:0,i:0])!=0)[0][0]
			if el is None:
				raise ValueError," System might not have a solution"
			else:
				tot_mat[[i,el]]=tot_mat[[el,i]]
		for j in range(i-1,-1,-1):
			tot_mat[j]=tot_mat[j]-(tot_mat[j,i]/tot_mat[i,i])*tot_mat[i]
	return tot_mat[0:dim,0:dim],tot_mat[:,-1]

def solve_diag(A,B):
	return (B/np.diag(A))

def solve_upper(A,B):
	dim=A.shape[0]
	soln=np.array([None]*dim, dtype=float)
	for i in range(0,dim):
		soln[dim-i-1]=(B[dim-i-1]-np.dot(A[dim-i-1][dim-i:dim],soln[dim-i:dim]))/A[dim-i-1,dim-i-1]
	return soln

if __name__=="__main__":
	a=np.array([[1,-1,-1,1],[2,0,2,0],[0,1,2,0],[3,-3,-2,4]],dtype=float)
	b=np.array([0,8,8,7],dtype=float)
	up_a,up_b=upper_triangle(a,b)
	print "Soln=",solve_upper(up_a,up_b)
	diag_a,diag_b=lower_triangle(up_a,up_b)
	print solve_diag(diag_a,diag_b)
	#print np.linalg.pinv(a)
