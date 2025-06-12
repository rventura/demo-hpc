import numpy as np
from mpi4py import MPI

# Number of points per process
N = 10**8


# Main computation

for chunk in [10**n for n in range(2,9)]:
    print(f"chunk={chunk} ", end='', flush=True)
    t0 = MPI.Wtime()
    n_inside = 0
    for nc in (N//chunk) * [chunk] + [N%chunk]:
        # Dividing the computation in chunks
        points = np.random.uniform(-1, 1, (nc,2))
        inside = (np.sum(points**2, axis=1) <= 1)
        n_inside += np.sum(inside)
    t = MPI.Wtime() - t0
    print(f"t={t}")
