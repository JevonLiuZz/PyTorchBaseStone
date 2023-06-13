import numpy as np

arrayProto = np.array([[1, 2], [3, 4], [5, 6]])
arrayProtoLine1 = arrayProto[:, -1].T
print(arrayProtoLine1)
# print(arrayProto.T)
print(arrayProto.transpose())
print("\n***\n", arrayProto)


arrayCol = np.array([[7, 8, 9], [11, 10, 12]])
arrayColT = arrayCol.T
print("\n***\n")
# npCat = np.insert(arrayProto, 1, arrayColT, axis=0)
npCat = np.insert(arrayProto, 1, arrayCol, axis=1)
print(npCat)
