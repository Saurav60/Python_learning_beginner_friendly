import csv
class Item:
    pay_rate = 0.9 #pay rate after 20% discount
    all = []
    def __init__(self,name: str,price: float,quantity=0):
        #run validations to the recieved arguments
        assert price >= 0, f'price {price} is not greater than and equal to zero'
        assert quantity >= 0

        #assign to self object
        self.__name = name
        self.__price = price  
        self.quantity = quantity

        #Actions to execute
        Item.all.append(self)

    @property
    def price(self):
        return self.__price
    
    
    def apply_discount(self):
        self.__price = self.__price * self.pay_rate 


    def apply_increment(self,increment_value):
        self.__price= self.__price + self.__price * increment_value

    @property
    # property decorator 
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception('The name is too long!')
        else:
            self.__name = value


    def calcualte_total_price(self):
        return self.__price * self.quantity
    

    @classmethod # take cls as param and modifies class state as these methods operates on class level data.
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            ) 

    @staticmethod # they do not take self and cls param and do not modifies class state.
    def is_integer(num):
        # we will count out the floats that are point zero
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}',{self.__price},{self.quantity})"
    

    #encapsulation
    def __connect(self, smtp_server):
        pass 
    def __prepare_body(self):
        return f'''
        hello someone
        we have {self.name} {self.quantity} times.
        regards, gashwa'''
    def __send(self):
        pass 
    def send_email(self):
        self.__connect('')
        self.__prepare_body()
        self.__send()