from dataclasses import dataclass
from category import Category

@dataclass
class Transaction:
    id: int
    amount: float
    description: str
    category: Category

    def show(self):
        print(f'{self.description} - {self.amount} - {self.category.name}')