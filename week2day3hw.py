
#Exercise 1


my_cart = {}

def addtoCart ():
    item = input ("What do you want to add?")
    quantity = input ("How many items do you want? (Please input a number)")
    my_cart[item] = quantity

    def showCart():
            print (my_cart)


    def removeFromCart():
        Item = input("Which item do you want to remove from your cart?")
        if item in my_cart:

            del my_cart[item]
            print(f"Successfully removed {item} from your cart")
        else: 
            print("You don't have that item in your cart")

        def num():
            while True:
                answer = input("What do you want to do(show/add/delete/quit)")
                if answer.lower() == "quit":
                    showCart()
                    break
                elif answer.lower() == "add":
                    addtoCart()
                
                elif answer.lower() == "show":
                    showCart()
                
                elif answer.lower() == "delete":
                    removeFromCart()
                else:
                    print("Invalid reponse")

                
    
    def run():
        while True:
            answer = input("what do you want to do? (show/add/delete/quit)")
            if answer.lower() == "quit":
                showCart()
                break
            elif answer.lower() == "add":
                addtoCart()

            elif answer.lower() == "show":
                showCart()
            elif answer.lower() == " delete":
                removeFromCart()
            else:
                print("Invalid reponse")

    run()



#Exerise 2

#Function to calculate square footage of a house

def AreaofRectangle(width, height):
    Area = width * height
    print ("Area of a Rectangle is: %.2f%")
    

#function to calculate circle circumfrance
def circumference(r):
    return (2 * PI * r)