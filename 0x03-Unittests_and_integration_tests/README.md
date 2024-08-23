# 0x03. Unittests and Integration Tests

This project covers the implementation of unit and integration tests in Python, 
using the `unittest` framework. The project includes testing various utilities 
and client code for correctness, with a focus on mocking external calls and 
parameterizing test cases.

## Files

- **utils.py**: Contains utility functions that are tested.
- **client.py**: Contains client-side code that interacts with external APIs.
- **fixtures.py**: Contains fixtures used for integration tests.
- **test_utils.py**: Unit tests for `utils.py`.
- **test_client.py**: Unit and integration tests for `client.py`.

## Requirements

- Python 3.7
- Ubuntu 18.04 LTS
- `unittest` and `unittest.mock` for testing.
- All files are executable and conform to PEP 8 style guidelines.

## Installation

No special installation is required other than ensuring Python 3.7 is installed.

## How to run tests

To run the tests, execute the following command:

```bash
python3 -m unittest discover
