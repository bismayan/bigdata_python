#seperateCodes.py
from mpi4py import MPI
rank = MPI.COMM_WORLD.Get_rank()
try:
	if rank==1:
		assert MPI.COMM_WORLD.Get_size()==3
except:
	print "Code Must be run with 3 processes"
	MPI.COMM_WORLD.Abort()
	raise
a = 6.0
b = 3.0
if rank == 0:
        print a + b
if rank == 1:
        print a * b
if rank == 2:
        print max(a,b)
