import numpy as np
from mpi4py import MPI

# Number of points per process
N = 10**8

# Setup OpenMPI
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank==0:
    # Master process
    t0 = MPI.Wtime()
    base = int(t0)
else:
    # Slave process
    base = None

# Ensure different seeds per process
seed = rank + comm.bcast(base, root=0)
np.random.seed(seed)

print(f"I'm instance {rank} in {size} and my seed is {seed}.")

# Main computation
chunk = 10**6
n_inside = 0
for nc in (N//chunk) * [chunk] + [N%chunk]:
    # Dividing the computation in chunks
    points = np.random.uniform(-1, 1, (nc,2))
    inside = (np.sum(points**2, axis=1) <= 1)
    n_inside += np.sum(inside)

# Collect results by summing all n_inside
total_inside = comm.reduce(n_inside, op=MPI.SUM, root=0)

if rank==0:
    # Master process
    t = MPI.Wtime() - t0
    result = 4 * total_inside / (N*size)
    error = np.abs(result - np.pi)
    print(f"My approximation of π is {result} (error is {error}).\nIt took {t} seconds.")
