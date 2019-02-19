class BankAccount:

	def _init_(self, balance = 0, interest_rate = 0.02):
		self.balance = balance
		self.interest_rate = interest_rate
	
	def deposit(self, deposit):
		if deposit < 0:
			return False
		else:
			self.balance += deposit
			return self.balance
		
	def withdraw(self, withdraw):
		if withdraw < 0 or withdraw > self.balance:
			return False
		else:
			self.balance -= withdraw
			return self.balance

	def accumulate_interest(self):
		self.balance += self.balance * self.interest_rate
		return self.balance


class ChildrensAccount(BankAccount):
	def _init_(self, balance = 0):
		interest_rate = 0
		super()._init_(balance, interest_rate)

	def accumulate_interest(self):
		self.balance += 10


class OverdraftAccount(BankAccount):
	def _init_(self, balance = 0, overdraft_penalty = 40):
		super()._init_(balance)
		self.overdraft_penalty = overdraft_penalty

	def withdraw(self, withdraw):
		if withdraw < 0:
			return False
		elif withdraw > self.balance:
			self.balance -= self.overdraft_penalty
			return self.balance
		else:
			self.balance -= withdraw
			return self.balance

	def accumulate_interest(self):
		if self.balance > 0:
			self.balance += self.balance * self.bankaccount_interest_rate
			return self.balance
		else:
			return self.balance






basic_account = BankAccount()
basic_account.deposit(600)
print("Basic account has ${}".format(basic_account.balance))
basic_account.withdraw(17)
print("Basic account has ${}".format(basic_account.balance))
basic_account.accumulate_interest()
print("Basic account has ${}".format(basic_account.balance))
print()

childs_account = ChildrensAccount()
childs_account.deposit(34)
print("Child's account has ${}".format(childs_account.balance))
childs_account.withdraw(17)
print("Child's account has ${}".format(childs_account.balance))
childs_account.accumulate_interest()
print("Child's account has ${}".format(childs_account.balance))
print()

overdraft_account = OverdraftAccount()
overdraft_account.deposit(12)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.withdraw(17)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.accumulate_interest()
print("Overdraft account has ${}".format(overdraft_account.balance))



# Basic account has $600
# Basic account has $583
# Basic account has $594.66

# Child's account has $34
# Child's account has $17
# Child's account has $27

# Overdraft account has $12
# Overdraft account has $-28
# Overdraft account has $-28