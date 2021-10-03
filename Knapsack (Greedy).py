# Python Program to implement Knapsack Problem using Greedy Method

class Item:

    def __init__(self, wt, val, ind):
        self.wt = wt
        self.val = val
        self.ind = ind
        self.cost = val // wt

    def __lt__(self, other):
        return self.cost < other.cost


class KnapSack:

    @staticmethod
    def getMaxValue(wt, val, capacity):
        i_val = []
        for i in range(len(wt)):
            i_val.append(Item(wt[i], val[i], i))

        i_val.sort(reverse=True)

        totalValue = 0
        for i in i_val:
            cur_Wt = int(i.wt)
            cur_Val = int(i.val)
            if capacity - cur_Wt >= 0:
                capacity -= cur_Wt
                totalValue += cur_Val
            else:
                fraction = capacity / cur_Wt
                totalValue += cur_Val * fraction
                capacity = int(capacity - (cur_Wt * fraction))
                break
        return totalValue


if __name__ == "__main__":
    wt = [10, 40, 20, 30]
    val = [60, 40, 100, 120]
    capacity = 50

    maxValue = KnapSack.getMaxValue(wt, val, capacity)
    print("Maximum value in Knapsack =", maxValue)

