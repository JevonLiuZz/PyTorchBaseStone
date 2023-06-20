import numpy as np
from scipy.io import loadmat
from prettytable import PrettyTable


matPath = "./FileRead/MatFiles/40_val.mat"
data = loadmat(matPath)
# print(data.keys())

# posShape = data.__getitem__("POS")
leftPos = data["POS"][:, 0]
rightPos = data["POS"][:, 1]
leftAcc = data["ACC"][:, -2]
rightAcc = data["ACC"][:, -1]
leftVel = data["VEL"][:, -2]
rightVel = data["VEL"][:, -1]
# print("Left:\nPosition dimension:", np.shape(leftPos),
#       "\nVelocity dimension:", np.shape(leftVel),
#       "\nAccelerate dimension:", np.shape(leftAcc))

#  manual selection
dimension_diff = max(np.shape(leftPos)[0], np.shape(leftVel)[0], np.shape(leftAcc)[0]) \
                 - min(np.shape(leftPos)[0], np.shape(leftVel)[0], np.shape(leftAcc)[0])
leftPos = leftPos[dimension_diff:]
rightPos = rightPos[dimension_diff:]

#  dimension info
# table = PrettyTable(['Dimension', 'Left', 'Right'])
# table.border, table.align, table.valign = (True, 'l', 'b')
# table.add_row(['Position', np.shape(leftPos), np.shape(rightPos)])
# table.add_row(['Velocity', np.shape(leftPos), np.shape(rightPos)])
# table.add_row(['Accelerate', np.shape(leftPos), np.shape(rightPos)])
# print(table)

PosCat = np.c_[leftPos, rightPos]
VelCat = np.c_[leftVel, rightVel]
AccCat = np.c_[leftAcc, rightAcc]

dataRaw = np.c_[PosCat, VelCat, AccCat]
row = dataRaw[256, :]
print(row)
oneCol = dataRaw[:, 0]
print(oneCol.shape[0])
print("**")
