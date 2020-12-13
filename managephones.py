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
                size:{ManagePhones.current_list[i].size}
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

    def sort(self, specific = None):
        if specific == None:
            specific = input("How would you like to sort the phones? \n")
            specific = specific.lower()
        if specific == 'price':
            self.sort_price()
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
                size:{ManagePhones.current_list[id].size}
                color:{ManagePhones.current_list[id].color}
                rating: {ManagePhones.current_list[id].recommend_score}/10
                ++++++++++++++++
                """)


'''
TESTING
'''
    
# mp = ManagePhones()
# # mp.print_name()
# mp.filter('os')
# mp.recommend_phone()


# mp.reinit()
# mp.print_name()   

