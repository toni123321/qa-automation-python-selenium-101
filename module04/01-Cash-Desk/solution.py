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

