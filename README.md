# shivani-ssc-sdet-coding-exercise

Coding exercise for  the SS&C SDET role using Python. 
Includes a functional programming solution for removing duplicates and automated tests for the JSONPlaceholder API.

## Remove Duplicates and API Testing - Take Home Challenge

This repository contains a solution to a two-part coding challenge.

---

## Project Structure
```
├── remove_duplicates.py
├── tests/
│   ├── test_remove_duplicates.py
│   └── test_api.py
└── README.md
```


## Part 1: Functional Programming - Remove Duplicates
This part demonstrates how to remove duplicates from a list while preserving the original order of first occurrences using functional programming principles. 
- The `remove_duplicates.py` file contains the function that solves the problem.
- Functional programming concepts such as immutability and built-in functions (`filter`) are used.

### Tests

- Test cases for the function are located in `tests/test_remove_duplicates.py`. The tests covers:
    - Removing duplicates from a list of mixed values.
    - Handling lists with all duplicates. 
    - Handling empty lists
    - Handling lists with mixed data types (e.g., strings and integers)
    - Ensuring the function raises a `TypeError` when the input is not a list.

## Part 2: API Testing - JSONPlaceholder API 

This part demonstrates automated tests for [JSONPlaceholder API](https://jsonplaceholder.typicode.com/).

The following scenarios are covered:

1. **GET Request**: Fetching a user and validating the response structure.
2. **POST Request**: Creating a new post and verifying its creation.
3. **Error Handling**: Testing for a 404 response for a non-existent resource.

All API tests are implemented in `tests/test_api.py`.

### Test Scenarios

- **test_fetch_user_successfully**: Verifies that `/users/1` returns a 200 status code and contains required fields (`id`, `name`, `email`).

- **test_create_new_post**: Sends a  `POST /posts` request and validates that the post is created successfully.

- **test_nonexistent_user**: Verifies that requesting a non-existent user returns a 404 error.

---

## Installation and Running Tests

To run the tests for the remove_duplicates.py and the API testing, follow these steps:

1. **Clone this repository**

```bash
git clone <repository_url>
cd <repository_name>
```

2. **Install dependencies**
```
pip install pytest
```

3. **Run tests**
```
pytest tests/test_remove_duplicates.py
pytest tests/test_api.py
```

## Requirements
- Python 3.x
- pytest
- requests
