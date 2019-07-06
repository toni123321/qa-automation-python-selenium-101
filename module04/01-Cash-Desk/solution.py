#Bill class
class Bill:
	def __init__(self, amount):
		if type(amount) is not int:
			raise TypeError("Error:incorrect type")
		
		if amount < 0:
			raise ValueError("Error:Negative amount")
		else:
			self.amount = amount
			
	def __int__(self):
		return self.amount
		
	def __repr__(self):
		return "A {}$ bill".format(self.amount)
		
	def __str__(self):
		return "A {}$ bill".format(self.amount)
		
	def __hash__(self):
		return self.amount
		
	def __eq__(self, other):
		return self.__hash__() == other.__hash__()
				
#class BatchBill
class BatchBill:
	def __init__(self, bills_list):
		self.bills_list = bills_list
	
	def __repr__(self):
		return self.bills_list
		
	
	def __getitem__(self, index):
		return self.bills_list[index]

	def __len__(self):
		return len(self.bills_list)
	
	def total(self):
		amount = 0
		length = self.__len__()
		
		for i in range(0, length):
			amount+= int(self.bills_list[i])
		
		return amount

#class CashDeck
class CashDesk:
	def __init__(self):
		self.desk = []

	def take_money(self, money):
		try:
			for m in money:
				self.desk.append(m)		
		except:
			self.desk.append(money)

	def total(self):
		amount = 0
		for d in self.desk:
			amount += int(d)

		return amount
		
	
	def inspect(self):
		output = "We have a total of %d$ in the desk\n" % (self.total())
		output += "We have the following count of bills, sorted in ascending order:"
		#output += "%d$ bills - %d\n"
		
		dict_desk = {}
		for d in self.desk:
			dict_desk[int(d)] = 0
		
		for d in self.desk:
			if int(d) in dict_desk:
				dict_desk[int(d)]+=1;
		
		bill_values = sorted(dict_desk.keys())
		
		for bill_value in bill_values:
			output += "\n%d$ bills - %d" % (bill_value, dict_desk[bill_value])
			
		return output
