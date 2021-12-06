from numba import cuda
import numpy as np
import math

'''
CommFunc.py:This is a public function module.
'''

@cuda.jit
def gpu_multiply(a, b, c, result, n, m):
    idx = cuda.threadIdx.x + cuda.blockDim.x * cuda.blockIdx.x
    idy = cuda.threadIdx.y + cuda.blockDim.y * cuda.blockIdx.y
    if idx < n and idy < m:
        result[idx][idy] = a[idx][idy] * b[idx][idy] * c[idx][idy]

#The MNPMultiply function implements matrix operations with GPU.
def MNPMultiply(A=0,B=0,C=0):
    n,m=np.shape(A)
    x = np.ascontiguousarray(A)
    y = np.ascontiguousarray(B)
    z = np.ascontiguousarray(C)
    x_device = cuda.to_device(x)
    y_device = cuda.to_device(y)
    z_device = cuda.to_device(z)
    gpu_result = cuda.device_array((n,m))
    threads_per_block = (16, 16)
    blocks_per_grid_x = int(math.ceil(x.shape[0] / threads_per_block[0]))
    blocks_per_grid_y = int(math.ceil(y.shape[1] / threads_per_block[1]))
    blocksPerGrid = (blocks_per_grid_x, blocks_per_grid_y)
    gpu_multiply[blocksPerGrid, threads_per_block](x_device, y_device, z_device, gpu_result, n, m)
    cuda.synchronize()
    return np.array(gpu_result.copy_to_host().tolist())