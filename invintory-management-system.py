# Abdul Aziz
# BCSF19A026
# Add/drop CS-Afternoon
# Web Assignment 01
# Task 01
# class implementation of product
class Product:
    def __init__(self, p_id = 1, name = "Default", price = 0.0, description = "Default", quantity = 0):
        try:
            self.__ProductID = int(p_id)
            self.__Name = name
            self.__Price = float(price)
            self.__Description = description
            self.__Quantity = int(quantity)
        except Exception as e:
            print("Error creating product: ",str(e))

    @property
    def ProductID(self):
        return self.__ProductID
    @ProductID.setter
    def ProductID(self, id):
        if not (id is not None and isinstance(id, int) and id > 0):
            raise ValueError("ProductID must be a positive integer")
        self.__ProductID = id
        
               
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, name):
        self.__Name = name


    @property
    def Price(self):
        return self.__Price
    @Price.setter
    def Price(self, price):
        if not (price is not None and isinstance(price, (int, float)) and price >= 0):
            raise ValueError("Price must be a positive number")
        self.__Price = price
            
            
    @property
    def Description(self):
        return self.__Description
    @Description.setter
    def Description(self, description):
        self.__Description = description
    
    @property
    def Quantity(self):
        return self.__Quantity
    @Quantity.setter
    def Quantity(self, quantity):
        if not(quantity is not None and isinstance(quantity, int) and quantity >= 0):
            raise ValueError("Quantity must be a non-negative integer")
        self.__Quantity = quantity
        

    def display(self):
        print(self.ProductID, "#", self.Name,"#",self.Price,"#", self.Description,"#", self.Quantity)
        
#Creating Store Class      
class Store:
    def __init__(self, s_id = 1, name = "Default Store"):
        try:
            self.__StoreName = name #Store Name
            self.__StoreID = int(s_id) #Store ID must be unique int
            self.__inventory = [] # list of product 
        except Exception as e:
            print("Error Creating Store: ", str(e))
    @property
    def StoreID(self):
        return self.__StoreID
    @property
    def StoreName(self):
        return self.__StoreName
    
    @StoreID.setter
    def StoreID(self, id):
        if id is not None and isinstance(id, int) and id > 0:
            self.__StoreID = id
        else:
            raise ValueError("StoreID must be a positive integer")
            
    @StoreName.setter
    def StoreName(self, name):
        self.__StoreName = name
    
    def AddProduct(self, product): # product given will be added to the inventory list
        try:
            if not isinstance(product, Product):
                raise TypeError("Product must be an instance of Product class")
            self.__inventory.append(product)
            product.display()
            print("Added Successfully")
        except Exception as e:
            print("Product Cannot be Added: ", e)

    def DeleteProduct(self, name):
        try:
            if not isinstance(name, str):
                raise TypeError("Name must be a string")
            index = -1
            for i, product in enumerate(self.__inventory):
                if product.Name == name:
                    index = i
                    break
            if index == -1:
                raise ValueError("Product not found in inventory")
        except Exception as e:
            print("Error: ", e)
        else:
            self.__inventory[index].display()
            self.__inventory.pop(index) # remove from inventory
            print("Deleted Successfully")
    
    def UpdateProduct(self, name):
        try:
            if not isinstance(name, str):
                raise TypeError("Name must be a string")
            index = -1
            for i, product in enumerate(self.__inventory):
                if product.Name == name:
                    index = i
                    break
            if index == -1:
                raise ValueError("Product not found in inventory")
        except Exception as e:
            print("Error: ", e)
        else:
            try:
                old_product =self.__inventory[index]
                print("\nOld Name: ",old_product.Name)
                choice = input ("1) Change Name\n2) Skip\nYour Choice: " )
                while not (choice == "1" or choice == "2"):
                    choice = input ("1) Change Name\n2) Skip\nYour choice: " )
                if ( choice == "1"):
                        old_product.Name = input("Enter new name: ")
                        print("Name updated")
                print("\nOld Price: ", old_product.Price)
                choice = input ("1) Update Price\n2) Skip\nYour Choice: ")
                while not (choice == "1" or choice == "2"):
                    choice = input ("1) Update\n2) Skip\nYour choice: " )
                if ( choice == "1"):
                        old_product.Price = float(input("Enter new price (positive int,float): "))
                        print("Price updated")
                print("\nOld Description: ",old_product.Description)
                choice = input ("1) Change Description\n2) Skip\nYour Choice: ")
                while not (choice == "1" or choice == "2"):
                    choice = input ("1) Update\n2) Skip\nYour choice: " )
                if ( choice == "1"):
                        old_product.Description = input("Enter new Description: ")
                        print("Description updated")
                print("\nOld Quantity: ", old_product.Quantity)
                choice = input ("1) Update Quantity\n2) Skip\nYour Choice: ")
                while not (choice == "1" or choice == "2"):
                    choice = input ("1) Update\n2) Skip\nYour choice: " )
                if ( choice == "1"):
                        old_product.Quantity = int(input("Enter Quantity (positive int): "))
                        print("Quantity Updated")
            except Exception as e:
                print("Error: ", str(e))
            print("Product updated Successfully\n")

    def SearchProduct(self, name):
        try:
            if not isinstance(name, str):
                raise TypeError("Name must be a string")
            for product in self.__inventory:
                if product.Name == name:
                    print("Product Founded")
                    product.display()
                    return product
            raise ValueError("Product not found in inventory")
        except Exception as e:
            print("Error: ", e)

    def DisplayAllProduct(self):
        for product in self.__inventory:
            product.display()
    def update(self):
        while True:
            print("\n\n1) ADD PRODUCT\n2) DELETE PRODUCT\n3) UPDATE PRODUCT\n4) SEARCH PRODUCT\n5) DISPLAY ALL PRODUCTS\n6) Exit\n")
            n = input("Please select option from (1-6): ")
            while n < "1" or n > "6":
                n = input("Please select option from (1-6): ")
            if  not (n == "6" or n == "5"):
                try:
                    name = input("Name of Product: ")
                except Exception as e:
                    print("Error: ", str(e))
            if n == "1":
                try:
                    for product in self.__inventory:
                        if name == product.Name:
                            raise Exception("Product already exists")
                    print("Enter "+ name +" Detail to added")
                    price = float(input ("Price: "))
                    description = input("Description: ")
                    quantity = int(input ("Quantity: "))
                    if not self.__inventory:
                        self.AddProduct(Product(1, name, price, description, quantity))
                    else:
                        id = self.__inventory[-1].ProductID + 1
                        self.AddProduct(Product(id, name, price, description, quantity))
                except Exception as e:
                    print ("Error: ", e)                   

            elif n == "2":
                self.DeleteProduct(name)
            elif n == "3":
                self.UpdateProduct(name)
            elif n == "4":
                self.SearchProduct(name)
            elif n == "5":
                self.DisplayAllProduct()
            else:
                with open ("inventory_" + str(self.StoreID) + ".txt", "w") as f:
                    f.write(str(len(self.__inventory))+"\n")
                    for product in self.__inventory:
                        f.write(str(product.ProductID) + "#" + product.Name +"#" + str(product.Price)+"#" + product.Description +"#" +str(product.Quantity)+"\n")
                return 
class Inventory_Manager:
    def __init__(self):
        self.__Stores = []
    def Create_Store(self):
        name = input("Enter store name: ")
        try:
            for store in self.__Stores:
                if store.StoreName == name:
                    raise Exception ("Duplicate Store Error")
        except Exception as e:
            print("Error: ", e)
        else:
            if not self.__Stores:
                self.__Stores.append(Store(1,name))
            else:
                id = self.__Stores[-1].StoreID
                self.__Stores.append(Store(id+1, name))
            print("Successfully Created")

    def Delete_Store(self):
        name = input("Enter store name: ")
        for store in self.__Stores:
            if store.StoreName == name:
                self.__Stores.remove(store)
                print("Store Successfully deleted")
                return
        print(name," not found")
    def Existing_store(self):
        name = input("Enter store name: ")
        for store in self.__Stores:
            if store.StoreName == name:
                store.update()
                return
        print(name, " not found")
    def Exit(self):
        with open ("storeData.txt", "w") as f:
            f.write(str(len(self.__Stores))+"\n")
            for i, store in enumerate(self.__Stores):
                f.write(str(i+1) + "#" + store.StoreName +"\n")   
   
manager = Inventory_Manager()
while True:
    print("\n\n1) Create Store")
    print("2) Delete Store")
    print("3) Existing store")
    print("4) Exit\n")
    n = input("Please select option from (1-4): ")
    while n < "1" or n > "4":
        n = input("Please select option from (1-4): ")
    if n == "1":
        manager.Create_Store()
    elif n == "2":
        manager.Delete_Store()
    elif n == "3":
        manager.Existing_store()
    else:
        manager.Exit()
        break


