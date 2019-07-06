class BankAccount:
	def __init__(self, name, balance_value, currency):
		if balance_value < 0:
			raise ValueError()
		if currency == "":
			raise ValueError()

		self.name = name
		self.balance_value = balance_value
		self.currency = currency
		self.account_history = ["Account was created"]

	def deposit(self, amount):
		if amount < 0:
			raise ValueError()

		self.balance_value += amount
		deposit_text = "Deposited %d%s" %(self.balance_value, self.currency)
		self.account_history.append(deposit_text)

	def balance(self):
		balance_text = "Balance check -> %d%s" %(self.balance_value, self.currency)
		self.account_history.append(balance_text)
		return self.balance_value

	def withdraw(self, amount):
		if amount < 0:
			raise ValueError()

		if amount > self.balance_value:
			withdraw_text = "Withdraw for %d%s failed." %(self.balance_value, self.currency)
			self.account_history.append(withdraw_text)
			return False
		else:
			self.balance_value -= amount
			withdraw_text = "%d%s was withdrawn" %(self.balance_value, self.currency)
			self.account_history.append(withdraw_text)
			return True

	def __str__(self):
		return "Bank account for %s with balance of %d%s" %(self.name, self.balance_value, self.currency)

	def __int__(self):
		int_text = "__int__ check -> %d%s" %(self.balance_value, self.currency)
		self.account_history.append(int_text)
		return self.balance_value

	def transfer_to(self, account, amount):
		if amount < 0:
			raise ValueError()

		if(self.currency == account.currency):
			if amount > self.balance_value:
				transfer_text = "Transfer to %s for %d%s failed" %(account.name, self.balance_value, self.currency)
				self.account_history.append(transfer_text)

				transfer_text = "Transfer from %s for %d%s failed" %(self.name, self.balance_value, self.currency)
				self.account_history.append(transfer_text)

				raise ValueError()
			else:
				self.balance_value -= amount
				account.balance_value += amount

				transfer_text = "Transfer to %s for %d%s" %(account.name, self.balance_value, self.currency)
				self.account_history.append(transfer_text)

				transfer_text = "Transfer from %s for %d%s" %(self.name, self.balance_value, self.currency)
				self.account_history.append(transfer_text)

				return True
		else:
			transfer_text = "Transfer to %s for %d%s failed" %(account.name, self.balance_value, self.currency)
			self.account_history.append(transfer_text)

			transfer_text = "Transfer from %s for %d%s failed" %(self.name, self.balance_value, self.currency)
			self.account_history.append(transfer_text)
			raise TypeError()

	def history(self):
		return self.account_history
