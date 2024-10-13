fruits={'apple':3,
        'orange':10,
        'banana':12,
        'cherry':35,
        }
orderCount={fruitName:stockCount-0 for fruitName,stockCount in fruits.items() if stockCount<20}
print(orderCount)

print("********************")
orderCount={fruitName:20-stockCount for fruitName,stockCount in fruits.items() if stockCount<20}
print(orderCount)

print("********************")
#convert Dictionary to List
orderCount={[fruitName,stockCount] for fruitName,stockCount in fruits.items() if stockCount<20}
print(orderCount)