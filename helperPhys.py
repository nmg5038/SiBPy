import os
import sys
import numpy as np

if __name__ == "__main__":
    datContent = [i.strip().split() for i in open(
        "/Users/nmg5038/SiB4/trunk/input/params/sib_phys.dat").readlines()]

    text_file = open("physHelper.txt", "w")
    text_file.write('ecologicalParameters=[]\n')
    text_file.write('stressParameters=[]\n')
    text_file.write('photosynthesisParameters=[]\n')
    text_file.write('radiativeParameters=[]\n')

    print datContent[39]
    for i in np.arange(1, 25):
        text_file.write(
            'ecologicalParameters.append([' + ', '.join(datContent[39 + i][2:]) + '])\n')

    print datContent[67]
    for i in np.arange(1, 25):
        text_file.write(
            'stressParameters.append([' + ', '.join(datContent[67 + i][2:]) + '])\n')
#
    print datContent[95 - 2]
    for i in np.arange(1, 25):
        text_file.write(
            'photosynthesisParameters.append([' + ', '.join(datContent[95 + i][2:]) + '])\n')
#
# 	print datContent[237-2]
    for i in np.arange(1, 25):
        text_file.write(
            'radiativeParameters.append([' + ', '.join(datContent[123 + i][2:]) + '])\n')
#
    text_file.write(
        'ecologicalParameters=ecologicalParameters[self.pftNumber-1]\n')
    text_file.write('stressParameters=stressParameters[self.pftNumber-1]\n')
    text_file.write(
        'photosynthesisParameters=photosynthesisParameters[self.pftNumber-1]\n')
    text_file.write(
        'radiativeParameters=radiativeParameters[self.pftNumber-1]\n')

    text_file.close()
