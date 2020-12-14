from classes import Phone

"""
INFORMATION:
from outside the module,
you will use the methods sort and filter and as an argument the type of sorting. If you don't have an argument it will be asked later
you have the method print_list which shows all of the info (we won't use it until the next sprint)
you have the method print_name which displays the name, id and price of every phone in the current list  -> we will use it in the display or browse intent
you have reinit that sets the current list to its original one
you hace recommend phone that displays the highest rated phone in the list

"""




class ManagePhones:
    p = Phone()
    list_phones = [None]*p.get_number_of_phones()

    for i in range(p.get_number_of_phones()):
        del p
        p = Phone()
        p = p.get_phone(i)
        list_phones[i]= p
    
    current_list = list_phones[:]

    def __init__(self):
        pass
    
    def print_list(self):
        for i in range(len(ManagePhones.current_list)):
            print(f"""
                ++++++++++++++++
                id: {ManagePhones.current_list[i].id}
                name:{ManagePhones.current_list[i].name}
                brand:{ManagePhones.current_list[i].brand}
                os:{ManagePhones.current_list[i].os}
                price:{ManagePhones.current_list[i].price}
                size:{ManagePhones.current_list[i].size} gb
                color:{ManagePhones.current_list[i].color}
                rating: {ManagePhones.current_list[i].recommend_score}/10
                ++++++++++++++++
                """)
    
    def print_name(self):
        for i in range(len(ManagePhones.current_list)):
            print(f"""
                ++++++++++++++++
                id: {ManagePhones.current_list[i].id}
                name:{ManagePhones.current_list[i].name}
                price: {ManagePhones.current_list[i].price}
                ++++++++++++++++
                """)

    def reinit(self):
        ManagePhones.current_list = ManagePhones.list_phones[:]
    
    def filter(self,specific = None):
        if specific == None:
            specific = input("How would you like to filter the phones? \n")
            specific = specific.lower()
        if specific == 'os':
            self.filter_by_OS()
        elif specific == 'price':
            self.filter_by_price()
        elif specific == 'brand':
            self.filter_by_brand()
        elif specific == 'size':
            self.filter_by_size()
        else:
            print("I'm sorry we cannot do this operation at this moment")

    def filter_by_OS(self):
        sorted_list_iOS = []
        sorted_list_Android = []
        os = input("Enter desired os: ").lower()
        print("OS: ", os)
        if os == "ios":
            for Phone in ManagePhones.list_phones:
                if os in Phone.os:
                    sorted_list_iOS.append(Phone)
            ManagePhones.current_list = sorted_list_iOS[:]
            print("Here are your filtered phones:")
            self.print_name()
        elif os == "android":
            for Phone in ManagePhones.list_phones:
                if os in Phone.os:
                    sorted_list_Android.append(Phone)
            ManagePhones.current_list = sorted_list_Android[:]
            print("Here are your filtered phones:")
            self.print_name()
        else:
            print("Phones with such OS are unavailable")

    def filter_by_price(self):
        sorted_list_by_price = []
        a = int(input("Enter lower price range: "))
        b = int(input("Enter upper price range: "))

        for Phone in (y for y in ManagePhones.list_phones if a <= y.price <= b):
            sorted_list_by_price.append(Phone)
        ManagePhones.current_list = sorted_list_by_price[:]
        print("Here are your filtered phones:")
        self.print_name()


    def filter_by_brand(self):
        filtered_list_brand = []
        brand = input("Enter desired brand: ").lower()
        print("Brand: ", brand)
        for Phone in ManagePhones.list_phones:
            if brand in Phone.brand:
                filtered_list_brand.append(Phone)
        if len(filtered_list_brand) == 0:
            print("This brand is not available in this store")
            return None 
        ManagePhones.current_list = filtered_list_brand[:]
        print("Here are your filtered phones:")
        self.print_name()
    
    def filter_by_size(self):
        filtered_list_size = []
        s = int(input("Enter lower size range: "))
        d = int(input("Enter upper size range: "))

        for Phone in (y for y in ManagePhones.list_phones if s <= y.size <= d):
            filtered_list_size.append(Phone)
        if len(filtered_list_size) == 0:
            print("Sorry. We do not have phones with this specifiction...")
            return None
        ManagePhones.current_list = filtered_list_size[:]
        print("Here are your filtered phones:")
        self.print_name()


    def sort(self, specific = None):
        if specific == None:
            specific = input("How would you like to sort the phones? \n")
            specific = specific.lower()
        if specific == 'price':
            self.sort_price()
        elif specific == 'name':
            self.sort_by_name()
        elif specific == 'brand':
            self.sort_by_brand()
        else:
            print("I'm sorry we cannot do this operation at this moment")

        
    def sort_price(self):
        temp = ManagePhones.current_list[:]
        for i in range(1,len(temp)):
            item_to_insert = temp[i]
            j = i-1
            while j >=0 and temp[j].price> item_to_insert.price:
                temp[j+1] = temp[j]
                j -=1
            temp[j+1]=item_to_insert
        ManagePhones.current_list = temp[:]
        self.print_name()

    def sort_by_name(self):
        sortn = input("Enter whether to sort by name a-z or z-a: ")
        sorted_list_by_name = sorted(ManagePhones.current_list, key=lambda Phone: Phone.name.lower())
        
        if sortn == "a-z":
            ManagePhones.current_list = sorted_list_by_name[:]
            
        elif sortn == "z-a":
            sorted_list_by_name.reverse()
            ManagePhones.current_list = sorted_list_by_name[:]
        else:
            print(f"Sorting {sortn} unavailable")
            return None
        
        self.print_name()

    def sort_by_brand(self):
        sortn = input("Enter whether to sort by name a-z or z-a: ")
        sorted_list_by_name = sorted(ManagePhones.current_list, key=lambda Phone: Phone.brand.lower())
        
        if sortn == "a-z":
            ManagePhones.current_list = sorted_list_by_name[:]
            
        elif sortn == "z-a":
            sorted_list_by_name.reverse()
            ManagePhones.current_list = sorted_list_by_name[:]
        else:
            print(f"Sorting {sortn} unavailable")
            return None
        
        self.print_name()





    def recommend_phone(self):
        id = 0
        max = ManagePhones.current_list[id].recommend_score
        for i in range(1,len(ManagePhones.current_list)):
            if max < ManagePhones.current_list[i].recommend_score:
                id = i
                max = ManagePhones.current_list[id].recommend_score
        print("Here is our recommendation:")
        print(f"""
                ++++++++++++++++
                id: {ManagePhones.current_list[id].id}
                name:{ManagePhones.current_list[id].name}
                brand:{ManagePhones.current_list[id].brand}
                os:{ManagePhones.current_list[id].os}
                price:{ManagePhones.current_list[id].price}
                size:{ManagePhones.current_list[id].size} gb
                color:{ManagePhones.current_list[id].color}
                rating: {ManagePhones.current_list[id].recommend_score}/10
                ++++++++++++++++
                """)



    def check_phone_info(self, id):
        stock = "not in stock"
        if self.check_if_stock(id):
            stock = "In stock"
        
        for phone in ManagePhones.list_phones:
            # print(type(phone))
            if phone.id == id:
                print(f"""
                ++++++++++++++++
                id: {phone.id}
                name:{phone.name}
                brand:{phone.brand}
                os:{phone.os}
                price:{phone.price}
                size:{phone.size} gb
                color:{phone.color}
                rating: {phone.recommend_score}/10
                stock: {stock}
                ++++++++++++++++
                """)
                return True
        print("This phone is not available")
        return False

    def check_if_stock(self, id):
        for phone in ManagePhones.list_phones:
            # print(type(phone))
            if phone.id == id:
                if phone.stock > 0:
                    return True
                else:
                    return False
        return False

    def remove_stock(self,id):
        for phone in ManagePhones.list_phones:
            # print(type(phone))
            if phone.id == id:
                phone.stock -=1
        ManagePhones.current_list = ManagePhones.list_phones[:]

    def update_list(self):
        ls = []
        for phone in ManagePhones.list_phones:
            d = {"id": phone.id, "name": phone.name, "brand": phone.brand, "os": phone.os, "price": phone.price, "size": phone.size, "color": phone.color, "recommend" : phone.recommend_score, "stock":phone.stock}
            ls.append(d)
        # print(ls[0]['name'])
        ph = Phone()
        ph.update_db(ls)


    
    def reserve_phone(self, id = None):
        if id == None or id > len(ManagePhones.list_phones):
            id = int(input("Which Phone do you want to check "))

        if not (self.check_if_stock(id)):
            print("I'm sorry this phone is not in stock. Please try again at a later date!")
            return None
        print("Here are the details of the phone you requested...")
        self.check_phone_info(id)
        reserve = input("Do you want to reserve this phone? ")
        while reserve != True:
            if reserve == 'yes' or reserve == 'y' or reserve == '1':
                reserve = True
            elif reserve == 'no' or reserve == 'n' or reserve == '0':
                return None
            else:
                print("I didn't understand that please write yes if you wish to reserve a phone and no if you don't")
        
        print("You're in luck, The phone is currently in stock!! However we don't have a delivery system so you will have to come pick your device up and pay in one of our branches")
        last_check = False
        while last_check == False:
            branch = input("Which branch do you want to pick up your device from? We currently have branches in Cairo, Alexandria and Sharm el Sheikh \n")
            branch = branch.lower()
            while not (branch in "cairo alexandria sharm el sheikh"):
                branch = input("This branch is not available. Please try again. If you have decided not to reserve a phone write 'exit' \n")
                branch = branch.lower()
                if branch == 'exit':
                    return None
            
            name = input("Who would be picking up the order? Make sure you write their name right; they will be asked for identification. \n")
            phone_number = input("Please enter you phone number so that we could contact you \n")

            reserve = input("Are you sure about this information? ")
            if reserve == 'yes' or reserve == 'y' or reserve == '1':
                reserve = True
                last_check = True
            
        self.remove_stock(id)
        order_num = id*1000 + ManagePhones.list_phones[id-1].stock +1
        print(f"Phone is reserved!! Your order number is {order_num} Please come to the branch as asked to pick up and pay for it. If you don't come in the next 48 hours The phone will no longer be reserved!")
        ph = Phone()
        ph.order_phone(f"order number: {order_num}: \t Phone id: {id}\t info: {name}\t {phone_number} \t branch: {branch}\n")
        self.update_list()

    


        
        

            



#reserve phone: check phone info -> choose to reserve -> choose branch -> stock -1 in list -> update current list -> add to text number with name and branch -> change db.json with information



'''
TESTING
'''
    
# mp = ManagePhones()
# mp.sort("brand")
# mp.update_list()
# mp.reserve_phone()
# # mp.print_name()
# mp.filter('size')
# mp.recommend_phone()


# mp.reinit()
# mp.print_name()   

