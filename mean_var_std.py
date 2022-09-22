import numpy as np
import islice
import sett


def calculate(list1):
    if len(list1) != 9:
        print("List must contain nine numbers.")
    else:
        l = islice.convert(list1, sett.Array_length)  # converting a list of numbers into list of lists
        l1 = np.array(l)

        # mean
        mean1 = [np.mean(l1, axis=0), np.mean(l1, axis=1), np.mean(l1)]

        # variance
        vari = [np.var(l1, axis=0), np.var(l1, axis=1), np.var(l1)]

        # Std. Deviation
        sd = [np.std(l1, axis=0), np.std(l1, axis=1), np.std(l1)]

        # max
        ma = [np.max(l1, axis=0), np.max(l1, axis=1), np.max(l1)]

        # min
        mi = [np.min(l1, axis=0), np.min(l1, axis=1), np.min(l1)]

        # sum
        su = [np.sum(l1, axis=0), np.sum(l1, axis=1), np.sum(l1)]

        print('{')
        print("Mean : ", mean1)
        print("Variance: ", vari),
        print("Standard Deviation : ", sd),
        print("Max : ", ma)
        print("Min : ", mi)
        print("Sum : ", su)
        print('}')
