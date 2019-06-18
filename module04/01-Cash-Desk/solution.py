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
	

#class CashDeck
class CashDeck:
	pass
