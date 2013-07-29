# Objected-Oriented Programming

# Warmup

class Account(object):

    interest = 0.02
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Yes!")
a = Account("Billy")


class CheckingAccount(Account):
    def __init__(self, account_holder):
        Account.__init__(self, account_holder)
    def deposit(self, amount):
            Account.deposit(self, amount)
            print("Have a nice day!")        

c = CheckingAccount("Eric")
a.deposit(30)
c.deposit(30)

# 1.) Consider the following basic definition of a Person class:

class Person(object):
	def __init__(self, name,repeated = "I squirreled it away before it could catch on fire."):
		self.name = name
		self.repeated = repeated

	def say(self,stuff):
		self.repeated = stuff
		return stuff

	def ask(self,stuff):
		return self.say("Would you please " + stuff)

	def greet(self):
		return self.say("Hello, my name is " + self.name) 

	def repeat(self):
		return self.repeated

class DoubleTalker(Person):
    def __init__(self, name):
        Person.__init__(self, name)
    def say(self, stuff):
        return Person.say(self, stuff + " " + stuff)

class Account(object):
    """A bank account that allows deposits and withdrawals."""

    interest = 0.02

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
        self.transactions = []

    def deposit(self, amount):
        """Increase the account balance by amount and return the new balance."""
        self.balance = self.balance + amount
        self.transactions.append(('deposit',amount))
        return self.balance

    def withdraw(self, amount):
        """Decrease the account balance by amount and return the new balance."""
        self.transactions.append(('withdraw',amount))
        if amount > self.balance:
            return 'Insufficient funds'
        self.balance = self.balance - amount
        return self.balance



class CheckingAccount(Account):
    """A bank account that charges for withdrawals."""

    withdraw_fee = 1
    interest = 0.01

    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_fee)

    def deposit_check(self,check):
    	if self.holder != check.holder or check.deposited:
    		print("The police have been notified.")
    		return 
    	else:
    		CheckingAccount.deposit(self,check.amount)
    		check.deposited = True

class Check(object):
	def __init__(self,holder,amount):
		self.holder = holder
		self.amount = amount
		self.deposited = False


check = Check("Steven",42)
steven_account = CheckingAccount("Steven")

eric_account = CheckingAccount("Eric")
eric_account.deposit_check(check)
print(check.deposited)

steven_account.deposit_check(check)
print(check.deposited)

steven_account.deposit_check(check)


