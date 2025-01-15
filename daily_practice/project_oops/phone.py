from item import Item
class Phone(Item):
    def __init__(self,name: str,price: float,quantity=0, broken_phones=0):
        # call to super function to access to all attributes of parent class  
        super().__init__(
            name, price, quantity
        )
        assert broken_phones >= 0, f'Broken Phone {broken_phones} is not greater than and equal to zero'

        #assign to self object
        self.broken_phones = broken_phones