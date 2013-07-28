# type is type !
# refacor is refactoring !
# one time one thing

class Connector
	attr_accessor :source,:value,:constraints
	# @constraints is all the constraints abut this connector
	# constraint is a relationship between the connector
	def initialize(name)
		@name = name
		@constraints = []
	end
	def inform_all_others(from,action)
		# infor all the constraints relate to this connector
		@constraints.each do |constraint| 
			if action == "new_value" 
				constraint.new_value
			elsif action == "forget_value"
				constraint.forget_value
			end
		end
	end


	def set_value(value)
		val = @value
		if val == nil
			@informant ,@value = @source,value
			inform_all_others(@source,'new_val') #....
		else
			if val != value
				puts "Contradiction detected: " + @value.to_s + " vs " + value.to_s
			end
		end
	end

	def has_val()
		return @value != nil
	end

	def connect(constraint)
		# connect this connector to the relate connector
		@constraints << constraint
	end

	def forget()
		@value = nil
		if @name != nil
			puts @name + "is forgotten"
		end
		inform_all_others(@source,'forget')
	end
end

class TernaryConstraint
	def initialize(a,b,c,ab_operator,ac_operator,cb_operactor)
		@a,@b,@c,@ab_operator,@ca_operator,@cb_operactor = a,b,c,ab_operator,ac_operator,cb_operactor
	end

	def new_value()
		av ,bv,cv = a.has_val,b.has_val,c.has_val
		if av and bv
			c.set_value(ab_operator(a.value,b.value))
		elsif av and cv
			b.set_value(ca_operator(c.value,a.value))
		elsif bv and cv
			a.set_value(cb_operactor(c.value,b.value))
		end
	end

	def forget_value()
		[a,b,c].each do |connector|
			connector.forget
		end
	end
end

def adder(a,b,c)
	return TernaryConstraint.new(a,b,c,add,sub,sub)
end

def add(a,b)
	return a + b
end

def sub(a,b)
	return a - b 
end

def make_add_converter(a,b)
	c = Connector.new("a + b")
	adder(a,b,c)
end

c = Connector.new('connector')
c.set_value(12)
puts c.value
puts "should 12"
c.set_value(13)
puts "should not be able to reset value"
puts c.has_val
puts "should be true"
c.connect(c)
puts c.constraints.inspect

c.forget
puts c.value 
puts "should be nil"
puts c.has_val
puts "should be false"


# t_c = TernaryConstraint.new("new constraint")

puts "!!!!!!!!!test!!!!!!!!!"
a = Connector.new("a")
b = Connector.new("b")
make_add_converter(a,b)
a.set_value(10)
b.set_value(20)