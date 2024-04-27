# In-Memory Database

This is a simple implementation of an in-memory database with transaction support in Python. The database allows you to set key-value pairs where keys are strings and values are integers. It supports transactions which allows you to make multiple changes atomically.

## Features

- `get`: Retrieve the value associated with a key.
- `put`: Set the value for a key.
- `begin_transaction`: Begin a new transaction.
- `commit`: Commit the changes made in the current transaction.
- `rollback`: Roll back the changes made in the current transaction.

## Quick Setup and Running

To use this module, no special setup is required apart from having Python installed on your system. Clone or download the repository, navigate to the directory containing `in_memory_db.py`, and run the Python shell or scripts within the same directory.

Example to run a simple test from the command line:
```shell
python -c "from in_memory_db import InMemoryDB; db = InMemoryDB(); db.begin_transaction(); db.put('test', 123); print(db.get('test')); db.commit(); print(db.get('test'))"
```

## In File Library Usage 

If you want to use this in your own python file, first, import the `InMemoryDB` class from the `in_memory_db.py`:
```python
file from in_memory_db import InMemoryDB
```
Create an instance of the InMemoryDB class:
```python
db = InMemoryDB()
```

Set and get values using the put and get methods, respectively:

```python
db.put("test", 1)  # Raises an exception because a transaction is not in progress
db.begin_transaction()
db.put("test", 1)  # Now it works, value is set within the transaction
value = db.get("test")  # Should return `None` because the transaction is not committed yet
db.commit()
value = db.get("test")  # Now it should return `1`
```

Start a transaction using begin_transaction, make changes, and then either commit them with commit or roll them back with rollback:

```python
db.begin_transaction()
db.put("test", 2)
db.rollback()
value = db.get("test")  # Should still return `1`
```

Remember, all changes made in a transaction are not visible until the transaction is committed.

## Modification Suggestions for Official Assignment
For future assignments, it may be beneficial to:

- Specify the expected behavior when methods are called outside of their intended use, such as calling commit without an active transaction.
- Include examples that cover edge cases, such as updating the same key multiple times within a transaction.
- Consider providing a template for exceptions to standardize error messages and simplify the grading process.

## Exceptions
- Trying to put without a transaction in progress will raise an exception.
- Attempting to begin a transaction when one is already in progress will raise an exception.
- Committing or rolling back without an active transaction will also raise an exception.

## Contributions
Contributions are welcome. Please submit a pull request or create an issue for any bugs or feature requests.
  
