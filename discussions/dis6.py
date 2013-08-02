# Class attribute – these are values that all objects of a class (data type) know and share.
# If any object of the class changes the class attribute, all other objects in the class will
# see the same new value.

# 1.1 Deﬁning a Class
# 1.2 Deﬁning a Method
# 1.3 Using a Class or Its Attributes
class Skittle(object):
	"""A Skittle object has a color to describe it."""
	def __init__(self, color):
		self.color = color

class Bag(object):
	"""A Bag is a collection of skittles. All bags share the number
	of Bags ever made (sold) and each bag keeps track of its skittles
	in a list.
	"""
	number_sold = 0
	def __init__(self):
		self.skittles = ()
		Bag.number_sold += 1

	def tag_line(self):
		"""Print the Skittles tag line."""
		print("Taste the rainbow!")

	def print_bag(self):
		print(tuple(s.color for s in self.skittles))

	def take_skittle(self):
		"""Take the first skittle in the bag (from the front of the
		skittles list).
		"""
		skittle_to_eat = self.skittles[0]
		self.skittles = self.skittles[1:]
		return skittle_to_eat

	def take_color(self, color):
		i = 0
		r = None
		for s in self.skittles:
			if s.color == color:
				r = s
				self.skittles = self.skittles[:i] + self.skittles[i+1:]
				return r
			i += 1
		return r

	def take_all(self):
		while len(self.skittles) != 0:
			print(self.take_skittle().color )			

	def add_skittle(self, s):
		"""Add a skittle to the bag."""
		self.skittles += (s,)		


# 2 Questions

johns_bag = Bag()
johns_bag.print_bag()
johns_bag.add_skittle(Skittle("blue"))

johns_bag.print_bag()
johns_bag.add_skittle(Skittle("red"))
johns_bag.add_skittle(Skittle("green"))
johns_bag.add_skittle(Skittle("red"))
johns_bag.print_bag()

s = johns_bag.take_skittle()
print(s.color)
print(johns_bag.number_sold)
print(Bag.number_sold)

akis_bag = Bag()

akis_bag.print_bag()
johns_bag.print_bag()
print ("Bag number_sold :")
print(Bag.number_sold)
print(akis_bag.number_sold)
print(johns_bag.number_sold)

class Email(object):
	"""Every email object has 3 instance attributes: the message, the
	sender (their name), and the addressee (the destination’s name).
	"""
	def __init__(self, msg, sender, addressee):
		self.msg = msg
		self.sender = sender
		self.addressee = addressee

class Postman(object):
	"""Each Postman has an instance attribute clients, which is a
	dictionary that associates client names with client objects.
	"""
	def __init__(self):
		self.clients = {}

	def register_client(self, client, client_name):
		"""Takes a client object and client_name and adds it to the
		clients instance attribute.
		"""
		self.clients[client_name] = client


	def send(self, email):
		"""Take an email and put it in the inbox of the client it is
		addressed to.
		"""
		name = email.addressee
		if name in self.clients:
			c = self.clients[name]
			c.receive(email)
# 
class Client(object):
	"""Every Client has instance attributes name (which is used
	for addressing emails to the client), mailman (which is
	used to send emails out to other clients), and inbox (a
	tuple of all emails the client has received).
	"""
	def __init__(self, mailman, name):
		self.inbox = ()
		self.mailman = mailman
		self.name = name
		###############
		self.mailman.register_client(self, self.name)

	def compose(self, msg, recipient):
		"""Send an email with the given message msg to the given
		recipient."""
		email = Email(msg,self,recipient)
		self.mailman.send(email)

	def receive(self, email):
		"""Take an email and add it to the inbox of this client.
		"""
		self.inbox += (email,)
# 
current_year = 2012
class Animal(object):
	def __init__(self):
		self.is_alive = True # It’s alive!!!

class Pet(Animal):
	def __init__(self, name, year_of_birth, owner=None):
		Animal.__init__(self) # call the parent’s constructor
		self.name = name
		self.age = current_year - year_of_birth
		self.owner = owner

	def eat(self, thing):
		print(self.name + " ate a " + str(thing) + "!")

	def talk(self):
		print("...")

class Dog(Pet):
	def __init__(self, name, yob, owner, color):
		Pet.__init__(self, name, yob, owner)
		self.color = color

	def talk(self):
		print("Woof!")



class Cat(Pet):
	def __init__(self, name, yob, owner, lives=9):
		Pet.__init__(name,yob,owner)
		self.lives = lives

	def talk(self):
		"""A cat says ’Meow!’ when asked to talk."""
		print ("Meow")

	def lose_life(self):
		"""A cat can only lose a life if they have
		at least one life. When lives reach zero,
		the ’is_alive’ attribute becomes False.
		"""		
		if self.lives > 0:
			self.lives -= 1
				if self.lives == 0:
					self.is_alive = False
		else:
			print("This cat has no more lives to lose :( ")



class NoisyCat(Cat):
		"""A class that behaves just like a Cat, but always
		repeats things twice.
		"""
		def __init__(self, name, yob, owner, lives=9):
			Cat.__init__(name,yob,owner,lives)
		def talk(self):
			"""A NoisyCat will always repeat what he/she said
			twice.
			"""
			Cat.talk()
			Cat.talk()
			