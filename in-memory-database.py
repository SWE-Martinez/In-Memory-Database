class InMemoryDB:
    def __init__(self):
        self.db = {}
        self.transaction = None
        self.in_transaction = False

    def get(self, key):
        if self.in_transaction and key in self.transaction:
            return self.transaction[key]
        return self.db.get(key, None)

    def put(self, key, val):
        if not self.in_transaction:
            raise Exception("No transaction in progress. Please begin a transaction before putting values.")
        self.transaction[key] = val

    def begin_transaction(self):
        if self.in_transaction:
            raise Exception("Transaction already in progress. Commit or rollback the current transaction before starting a new one.")
        self.transaction = {}
        self.in_transaction = True

    def commit(self):
        if not self.in_transaction:
            raise Exception("No transaction in progress. Please begin a transaction before committing.")
        self.db.update(self.transaction)
        self.transaction = None
        self.in_transaction = False

    def rollback(self):
        if not self.in_transaction:
            raise Exception("No transaction in progress. Please begin a transaction before rolling back.")
        self.transaction = None
        self.in_transaction = False
