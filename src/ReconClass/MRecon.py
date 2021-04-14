# coding=UTF-8

from ReconClass.BaseClass.ReconBase import *
from Config.ConstantList import *
import numpy as np

class MReconClass(ReconBaseClass):

    def __init__(self, Message, Iterations=20, Lambd=1e-6):
        super().__init__()
        self.__Iterations=Iterations
        self.__Lambd=Lambd
        self._ImageRecon(Message[MEASUREMENT][AUXSIGNAL], Message[MEASUREMENT][MEASIGNAL], Message[MEASUREMENT][MEANUMBER])

    def _ImageRecon(self, A, b, size):
        self._ImagSignal.append(self.__Kaczmarz(A, b, self.__Iterations, self.__Lambd))
        self._ImagSignal.append(self._ImageReshape(self._ImagSignal[0],size))

        return True

    def _ImageReshape(self, c, size):
        x = size[0]
        y = size[1]
        z = 1
        if len(size)>2:
            z=size[2]
        if x == 1 or y == 1 or z == 1:
            c = np.real(np.reshape(c, (x, y)))
            c = c[1:-1, 1:-1]
            c = c / np.max(c)
            return c, None, None
        else:
            c = np.real(np.reshape(c, (x, y, z)))
            Ixy = np.zeros((x, y))
            Ixz = np.zeros((x, y))
            Iyz = np.zeros((x, y))
            for i in range(0, x - 1):
                for j in range(0, x - 1):
                    Ixy[i, j] = max(c[i, j, :])
                    Ixz[i, j] = max(c[i, :, j])
                    Iyz[i, j] = max(c[:, i, j])
            Ixy = Ixy / np.max(Ixy)
            Ixz = Ixz / np.max(Ixz)
            Iyz = Iyz / np.max(Iyz)

            return np.real(Ixy), np.real(np.transpose(Ixz)), np.real(np.transpose(Iyz))

    def __Compute_RowEnergy(self, A):
        M = A.shape[0]
        energy = np.zeros(M, dtype=np.double)

        for m in range(M):
            energy[m] = np.linalg.norm(A[m, :])
        return energy

    # function() Kaczmarz comes from https://github.com/MagneticParticleImaging/MDF/tree/master/python
    def __Kaczmarz(self, A, b, iterations=10, lambd=0, enforceReal=False, enforcePositive=False, shuffle=False):
        M = A.shape[0]
        N = A.shape[1]

        x = np.zeros(N, dtype=b.dtype)
        residual = np.zeros(M, dtype=x.dtype)

        energy = self.__Compute_RowEnergy(A)

        rowIndexCycle = np.arange(0, M)

        if shuffle:
            np.random.shuffle(rowIndexCycle)

        lambdIter = lambd

        for l in range(iterations):
            for m in range(M):
                k = rowIndexCycle[m]
                if energy[k] > 0:
                    beta = (b[k] - A[k, :].dot(x) - np.sqrt(lambdIter) * residual[k]) / (energy[k] ** 2 + lambd)

                    x[:] += beta * A[k, :].conjugate()

                    residual[k] += np.sqrt(lambdIter) * beta

            if enforceReal and np.iscomplexobj(x):
                x.imag = 0
            if enforcePositive:
                x = x * (x.real > 0)

        return x
