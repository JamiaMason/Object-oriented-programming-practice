
class cart():
    def __init__(self):
        self.my_cart = {}


    def addtoCart(self):
        item = input ("What do you want to add?")
        quantity = input ("How many items do you want? (Please input a number)")
        self.my_cart[item] = quantity

    def showCart(self):
            print (self.my_cart)


    def removeFromCart(self):
        item= ""
        item = input("Which item do you want to remove from your cart?")
        if item in self.my_cart: 

            del self.my_cart[item]
            print(f"Successfully removed {item} from your cart")
        else: 
            print("You don't have that item in your cart")

        def num(self):
            while True:
                answer = input("What do you want to do(show/add/delete/quit)")
                if answer.lower() == "quit":
                    self.showCart()
                    break
                elif answer.lower() == "add":
                    self.addtoCart()
                
                elif answer.lower() == "show":
                    self.showCart()
                
                elif answer.lower() == "delete":
                    self.removeFromCart()
                else:
                    print("Invalid reponse")

                

    def run(self):
        while True:
            answer = input("what do you want to do? (show/add/delete/quit)")
            if answer.lower() == "quit":
                self.showCart()
                break
            elif answer.lower() == "add":
                self.addtoCart()

            elif answer.lower() == "show":
                self.showCart()
            elif answer.lower() == " delete":
                self.removeFromCart()
            else:
                print("Invalid reponse")

run = cart()
run.run()


#Exercise 2

class E2():
    def __init__(self):
        self.S1 = ""

    def getstring(self):
        self.S1 = input("How is your day")

    def printstring(self):
        print(self.S1.upper())

run= E2()
run.getstring()
run.printstring()