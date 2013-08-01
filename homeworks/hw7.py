"""61A Homework 6
Name:
Login:
TA:
Section:
"""

# Q1.
class VendingMachine(object):
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('crab', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.restock(2)
    'Current crab stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your crab and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your crab.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    """
    "*** YOUR CODE HERE ***"
    def __init__(self,material,price ):
        self.material = material #sell things such,'cab'
        self.money = 0
        self.price = price  #the cab's price
        self.mount = 0

    def restock(self,mount):
        self.mount += mount
        return 'Current '+self.material+' stock: ' + str(self.mount)

    def vend(self,hm = 1):
        need_money = hm * self.price
        if hm > self.mount:
            return 'Machine is out of stock.'
        elif self.money < need_money  :
            return 'You must deposit $' + str(need_money - self.money)+ ' more.'
        elif self.money - need_money > 0:
            change = self.money - need_money
            self.mount -= hm
            self.money = 0
            return 'Here is your ' + self.material + ' and $'+ str(change) + ' change.'
        else:
            self.money = 0
            self.mount -= hm
            return 'Here is your crab.' 
    def deposit(self,money):
        if self.mount <= 0:
            return  'Machine is out of stock. Here is your $' +str(money) +  '.'
        self.money += money
        return "Current balance: $" + str(self.money)

# Q2.

class MissManners(object):
    """A container class that only forward messages that say please.

    >>> v = VendingMachine('teaspoon', 10)
    >>> v.restock(2)
    'Current teaspoon stock: 2'
    >>> m = MissManners(v)
    >>> m.ask('vend')
    'You must learn to say please.'
    >>> m.ask('please vend')
    'You must deposit $10 more.'
    >>> m.ask('please deposit', 20)
    'Current balance: $20'
    >>> m.ask('now will you vend?')
    'You must learn to say please.'
    >>> m.ask('please give up a teaspoon')
    'Thanks for asking, but I know not how to give up a teaspoon'
    >>> m.ask('please vend')
    'Here is your teaspoon and $10 change.'
    """
    "*** YOUR CODE HERE ***"
    def __init__(self,instance):
        self.instance =  instance
    def ask(self,*args):
        if  not 'please' in args[0].split(' '):
            return 'You must learn to say please.'
        else:
            method = args[0].split(' ')[1]
            if len(args) >= 2:
                par = args[1]
            if method == 'vend':
                return self.instance.vend()
            elif method == 'deposit':
                return self.instance.deposit(par)
            else:
                return 'Thanks for asking, but I know not how to give up a ' + self.instance.material
# Q3.

class Amount(object):
    """An amount of nickels and pennies.
    >>> a = Amount(3, 7)
    >>> a.nickels
    3
    >>> a.pennies
    7
    >>> a.value
    22
    >>> a.nickels = 5
    >>> a.value
    32
    """
    "*** YOUR CODE HERE ***"
    nickels_value = 5
    pennies_value = 1
    def __init__(self,nickels,pennies):
        self.nickels = nickels
        self.pennies = pennies
################ 
    @property        
    def value(self):
        return Amount.nickels_value * self.nickels  + self.pennies *  Amount.pennies_value


class MinimalAmount(Amount):
    """An amount of nickels and pennies that is initialized with no more than
    four pennies, by converting excess pennies to nickels.

    >>> a = MinimalAmount(3, 7)
    >>> a.nickels
    4
    >>> a.pennies
    2
    >>> a.value
    22
    """
    "*** YOUR CODE HERE ***"
    def __init__(self,nickels,pennies):
        self.nickels = nickels
        self.pennies = pennies
        # #############
        value = self.value
        ##################
        # self.nickels = int(value /  Amount.nickels_value)
        ################### 
        # ==
        self.nickels = int(value /  self.nickels_value)
        self.pennies = int((value  % self.nickels_value) / self.pennies_value)

# Q4.
class Container(object):
    """A container for a single item.

    >>> c = Container(12)
    >>> c
    Container(12)
    >>> len(c)
    1
    >>> c[0]
    12
    """
    def __init__(self, item):
        self._item = item

    def __repr__(self):
        return 'Container({0})'.format(repr(self._item))

    def __len__(self):
        return 1

    def __getitem__(self, index):
        assert index == 0, 'A container holds only one item'
        return self._item

class Rlist(object):
    """A recursive list consisting of a first element and the rest.

    >>> s = Rlist(1, Rlist(2, Rlist(3)))
    >>> len(s)
    3
    >>> s[0]
    1
    >>> s[1]
    2
    >>> s[2]
    3
    """
    "*** YOUR CODE HERE ***"
    def __init__(self,first,remain = 'empty'):
        self.first = first
        self.remain = remain

    # def __len__(self):
    #     r = self.remain
    #     l = 1
    #     while r != 'empty':
    #         l ,r= l + 1,r.remain
    #     return l

    def __len__(self):
        if self.remain == 'empty':
            return 1
        else :
            return 1 + len(self.remain)

    def __getitem__(self, index):
        c = 0
        r = self
        while c < index:
            r ,c= r.remain ,c+ 1
        return r.first

class Base(object):
    var = "in base"
    def __init__(self,name):
        self.name = name
b = Base("b")        
print(b.var)
class Inheri(Base):
    def get_var(self):
        return self.var
# >>>>>>>>>???????????????????
i = Inheri("in")    
print(i.get_var())
# >>>>>>>>>???????????????????
