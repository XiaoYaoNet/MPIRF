from numba import cuda
import numpy as np
import math
# from time import time

@cuda.jit
def gpu_multiply(a, b, c, result, n, m):
    idx = cuda.threadIdx.x + cuda.blockDim.x * cuda.blockIdx.x
    idy = cuda.threadIdx.y + cuda.blockDim.y * cuda.blockIdx.y
    if idx < n and idy < m:
        result[idx][idy] = a[idx][idy] * b[idx][idy] * c[idx][idy]

def MNPMultiply(A=0,B=0,C=0):
    n,m=np.shape(A)
    x = np.ascontiguousarray(A)
    y = np.ascontiguousarray(B)
    z = np.ascontiguousarray(C)
    # n = 121
    # m = 121
    # x = np.ones((n,m)).astype(np.float64)
    # y =  x
    # z =  2*x


    # 拷贝数据到设备端
    x_device = cuda.to_device(x)
    y_device = cuda.to_device(y)
    z_device = cuda.to_device(z)

    gpu_result = cuda.device_array((n,m))

    threads_per_block = (128, 128)
    blocks_per_grid_x = int(math.ceil(x.shape[0] / threads_per_block[0]))
    blocks_per_grid_y = int(math.ceil(y.shape[1] / threads_per_block[1]))
    blocksPerGrid = (blocks_per_grid_x, blocks_per_grid_y)
    # start = time()
    gpu_multiply[blocksPerGrid, threads_per_block](x_device, y_device, z_device, gpu_result, n, m)
    cuda.synchronize()
    #print(gpu_result)
    # print("gpu vector add time " + str(time() - start))

    return gpu_result.copy_to_host()

# MNPMultiply()