from SLLQueue import SLLQueue
from datetime import datetime

class Item:
    def __init__(self, itemName, price, quantity):
        self.itemName = itemName
        self.price = price
        self.quantity = quantity

class Order:
    def __init__(self, receiptNum, itemList):
        self.receiptNum = receiptNum
        self.itemList = itemList
        self.dateTime = datetime.now()

class FastFood:
    N = 50
    border = "=" * N
    border1 = "-"

    def __init__(self, queue):
        self.queue = queue

    def addOrder(self):
        itemList = []

        print("Orders (enter -1 to stop):\n" + self.border1 * self.N)
        while (True):
            itemName = input("Item name: ").upper()
            if itemName == "-1":
                break
            
            price = float(input("Price: "))
            while(price <= 0):
                price = float(input("Price: "))
                
            quantity = float(input("Quantity: ")) 
            while(quantity <= 0):
                quantity = float(input("Quantity: ")) 

            item = Item(itemName, price, quantity)
            itemList.append(item)
        print(self.border1 * self.N)

        receiptNum = int(input("Receipt Number: "))

        order = Order(receiptNum, itemList)

        self.queue.enqueue(order)

    def displayOrder(self):
        if self.queue.isEmpty():
            print("No orders")
            return

        curr_order = self.queue.front().getValue()

        print("Here's your order:\n" + self.border1 * self.N)

        print(curr_order.dateTime.strftime("%c"))
        print("Receipt Number: " + str(curr_order.receiptNum))
        
        print("{0:10}\t{1:10}\t{2:10}".format("Item", "Price", "Quantity"))
        print(self.border1 * 10 + " \t" + self.border1 * 10 + " \t" + self.border1 * 10)
        for item in curr_order.itemList:
            print("{0:10}\t{1:10}\t{2:10}".format(item.itemName, item.price, item.quantity))
        
        print(self.border1 * self.N)

    def removeOrder(self):
        if self.queue.isEmpty():
            print("No orders left!")
            return
        
        self.queue.dequeue()
        print("Order removed successfully.")

    def on(self):
        while(True):
            print(self.border + "\nGood day! This is FastFoodCorp. How can I assist you today?")
            print("\t1 - Add order\n\t2 - Display order\n\t3 - Remove current order\n\t4 - Exit\n")

            choice = int(input("Choice: "))

            print(self.border)
            if choice == 1:
                # PROBLEM: 1 wrong item order ruins 1 whole order
                # Possible solution: Put the whole input block to another function
                try:
                    self.addOrder()
                except ValueError:
                    print("Invalid input!")
            elif choice == 2:
                self.displayOrder()
            elif choice == 3:
                self.removeOrder()
            elif choice == 4:
                break
            else:
                print("Invalid input!")
        print(self.border)   

def main():
    queue = SLLQueue()
    fastFood = FastFood(queue)

    fastFood.on()        

if __name__ == "__main__":
    main()



