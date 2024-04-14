from TTP.Item import Item
import random 

def calculateRatioItem(Element: Item) -> float:
        ElementProfit = Element.get_profit()
        ElementWeight = Element.get_weight()
        ratio = ((ElementProfit)/(ElementWeight))
        return ratio

def knapsack(Objects, maxWeigth):
    #ratioDict = addItemsToDict(Objects)
    items = []
    knapsackCurrentWeigth = 0
    # Función que ordena una lista de objetos de tipo Items
    orderedItems = sorted(Objects, key=calculateRatioItem, reverse=True)    

    for i in range(len(orderedItems)):
        if (knapsackCurrentWeigth + orderedItems[i].get_weight() <= maxWeigth):
            items.append(orderedItems[i])  
            knapsackCurrentWeigth += orderedItems[i].get_weight()

        if(knapsackCurrentWeigth == maxWeigth): break


    for i in range(len(items)):
        print(items[i].get_weight(), items[i].get_profit(), calculateRatioItem(items[i]))     
    return items



# ---------------------------------------------------------------- Main ----------------------------------------------------------------


# random example: (Item: profit = x, weigth = y) (n = items amount)
n = int(input())

# creating n Items
Items = []
for i in range (n):
    # Ranges of the Item parameters
    W = random.randint(1, 10)
    P = random.randint(1, 230)
    Items.append(Item(W,P))

for i in range(n):
    print(Items[i].get_weight(), Items[i].get_profit())
print("----------------------------------")
maxWeigth = 10

# Principal call to function knapsack() with House Objects list and Max Weight
Knapsack = knapsack(Items, maxWeigth)
print("Final knapsack:", Knapsack)





