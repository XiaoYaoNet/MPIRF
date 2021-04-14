# coding=UTF-8
import matplotlib.pyplot as plot

class ImagerClass(object):

    def WriteImage(ImageData,direction, filename):
        if ImageData.ndim==1:
            plot.bar(range(256), ImageData)
            plot.savefig(direction + filename)
        else:
            plot.gray()
            plot.imshow(ImageData)
            plot.savefig(direction+filename)

        plot.close()

        return True
