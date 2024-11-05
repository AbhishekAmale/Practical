class item:
    def __init__(self,w,p):
        self.w=w
        self.p=p
        
def Knap(capacity,arr):
    arr.sort(key=lambda  x:x.p/x.w ,reverse=True)
    
    profit=0
    for item in arr:
        if item.w <= capacity:
            profit += item.p
            capacity -= item.w
            print(profit)
        else:
            profit += item.p * capacity/item.w
            break
    return profit

n=int(input("enter no of item :"))
capacity=int(input("enter capacity :"))
arr=[item(int(input("Weight : ")),int(input("profit :"))) for _ in range(n)]
print("Max Profit : ",Knap(capacity,arr))































# class Item:
# 	def __init__(self, weight,profit):
# 		self.profit = profit
# 		self.weight = weight

# def fractionalKnapsack(W, arr):
# 	arr.sort(key=lambda x: (x.profit/x.weight), reverse=True) 
# 	finalvalue = 0.0

# 	for item in arr:
# 		if item.weight <= W:
# 			W -= item.weight
# 			finalvalue += item.profit
# 		else:
# 			finalvalue += item.profit * W / item.weight
# 			break

# 	return finalvalue

# n = int(input("Enter number of items :"))
# arr = [Item(int(input("Enter weight :")),int(input("Enter profit :")))for _ in range(n)]
# W=int(input("Enter Capacity :"))
# max_val = fractionalKnapsack(W, arr)
# print(max_val)