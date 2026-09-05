import csv
import uuid
from dataclasses import dataclass
from decimal import Decimal
from pathlib import Path

from .exceptions import AccountNotFoundError, DuplicateAccountError, FileOperationError, InsufficientBalanceError
from .transactions import Transaction, TransactionStore
from .utilities import get_logger
from .validation import validate_amount, validate_text

ACCOUNT_FIELDS = ("account_id", "customer_name", "balance")


@dataclass
class Account:
	account_id: str
	customer_name: str
	balance: Decimal = Decimal("0.00")

	def to_row(self):
		return {"account_id": self.account_id, "customer_name": self.customer_name, "balance": f"{self.balance:.2f}"}


class Bank:
	def __init__(self, accounts_file="accounts.csv", history_file="transactions.csv", log_file="banking.log"):
		self.accounts_file = Path(accounts_file)
		self.store = TransactionStore(history_file)
		self.logger = get_logger(log_file)
		self.accounts = self._load_accounts()

	def _load_accounts(self):
		if not self.accounts_file.exists():
			return []
		try:
			with self.accounts_file.open(newline="", encoding="utf-8") as file:
				return [Account(row["account_id"], row["customer_name"], Decimal(row["balance"])) for row in csv.DictReader(file)]
		except (OSError, KeyError, ValueError) as exc:
			raise FileOperationError(f"Could not load accounts: {exc}") from exc

	def _save_accounts(self):
		try:
			self.accounts_file.parent.mkdir(parents=True, exist_ok=True)
			with self.accounts_file.open("w", newline="", encoding="utf-8") as file:
				writer = csv.DictWriter(file, fieldnames=ACCOUNT_FIELDS)
				writer.writeheader()
				writer.writerows(account.to_row() for account in self.accounts)
		except OSError as exc:
			raise FileOperationError(f"Could not save accounts: {exc}") from exc

	def _find(self, account_id):
		account_id = validate_text(account_id, "Account ID")
		for account in self.accounts:
			if account.account_id == account_id:
				return account
		raise AccountNotFoundError(f"Account not found: {account_id}")

	def create_account(self, customer_name, account_id=None):
		customer_name = validate_text(customer_name, "Customer name")
		account_id = validate_text(account_id or str(uuid.uuid4()), "Account ID")
		if any(account.account_id == account_id for account in self.accounts):
			raise DuplicateAccountError(f"Account already exists: {account_id}")
		account = Account(account_id, customer_name)
		self.accounts.append(account)
		self._save_accounts()
		self.logger.info("Created account %s", account_id)
		return account

	def deposit(self, account_id, amount):
		account = self._find(account_id)
		amount = validate_amount(amount)
		account.balance += amount
		self._save_accounts()
		self.store.record(Transaction("DEPOSIT", "EXTERNAL", account.account_id, amount))
		self.logger.info("Deposited %.2f to %s", amount, account.account_id)
		return account.balance

	def withdraw(self, account_id, amount):
		account = self._find(account_id)
		amount = validate_amount(amount)
		if amount > account.balance:
			raise InsufficientBalanceError(f"Insufficient balance in account: {account.account_id}")
		account.balance -= amount
		self._save_accounts()
		self.store.record(Transaction("WITHDRAW", account.account_id, "EXTERNAL", amount))
		self.logger.info("Withdrew %.2f from %s", amount, account.account_id)
		return account.balance

	def transfer(self, from_account_id, to_account_id, amount):
		source = self._find(from_account_id)
		target = self._find(to_account_id)
		amount = validate_amount(amount)
		if amount > source.balance:
			raise InsufficientBalanceError(f"Insufficient balance in account: {source.account_id}")
		source.balance -= amount
		target.balance += amount
		self._save_accounts()
		self.store.record(Transaction("TRANSFER", source.account_id, target.account_id, amount))
		self.logger.info("Transferred %.2f from %s to %s", amount, source.account_id, target.account_id)

	def check_balance(self, account_id):
		return self._find(account_id).balance

	def transaction_history(self, account_id=None):
		history = self.store.history()
		if account_id is None:
			return history
		return [item for item in history if item["from_account"] == account_id or item["to_account"] == account_id]
