

from abc import ABC, abstractmethod


class Customer:
    def __init__(self, customer_id: str, name: str, email: str) -> None:
        self.customer_id = customer_id
        self.name = name
        self.email = email


class CustomerDataAdapter(ABC):
    @abstractmethod    
    def get_customers(self) -> list[Customer]:
        pass

class CsvAdapter(CustomerDataAdapter):
    def __init__(self, csv_file: str):
        pass

    def get_customers(self) -> list[Customer]:
        return [Customer('', '', '')]

class JsonAdapter(CustomerDataAdapter):
    def __init__(self, json_file: str):
        pass
    
    def get_customers(self) -> list[Customer]:
        return [Customer('', '', '')]
    

class CustomerImporter:
    def __init__(self, adapter: CustomerDataAdapter):
        self.adapter = adapter

    def import_customers(self):
        return self.adapter.get_customers()

def main():
    importer = CustomerImporter(CsvAdapter(''))
    data = importer.import_customers()

main()
    
    