from math import *


def ODR_not(Pm0, E, r1, r2, r3, var1, var2, var3):
    """ optimum decision rule for not jointly statistically independent """
    TH = (1 / (2 * sqrt(E))) * log((1-Pm0)/Pm0)
    l = [r/(variance ^ 2)
         for r, variance in zip([r1, r2, r3], [var1, var2, var3])]
    if l > TH:
        mhat = 1
    elif l < TH:
        mhat = 0
    return mhat


if __name__ == "__main__":
