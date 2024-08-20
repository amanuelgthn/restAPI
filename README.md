# OOP and Simple REST Api client

## Introduction

You are integrating  your application with CRM using simple REST API client class which inherits from base class.
This task will test practical `Python 3` skills as well as basic Object-Oriented Programming knowledge.

## Task details

1. Please do NOT modify any tests unless specifically told to do so.
2. Make tests pass by implementing the missing features in the production code.
3. There are multiple tests placed in the project that will help you verify your solution. Please use them as a guide when developing the project. Keep in mind that only a subset of the tests is visible to you and that your solution will be tested against many edge cases.

## Problem Statement

### Task 1 - `app/client/base.py`

Implement property (getter) `SimpleAPIClient.logger` which returns protected `_logger`attribute.

### Task 2 - `app/client/crm.py`

Modify class `CRMApiClient` to meet the following requirements:
* The class mentioned above should inherit from `SimpleAPIClient`
* Implement `CRMApiClient` instance initializer method (often called a constructor) which takes two arguments (`api_key` and `root_api_url`). Given arguments should be assigned to instance attributes with the same names. Example usage:
```python
client = CRMApiClient("qwer1234", "https://example.com/api/v3/")
assert client.api_key == "qwer1234"
assert client.root_api_url == "https://example.com/api/v3/"
```
* `CRMApiClient.call` is a facade that should return the result of method `_call` from the parent class. Please set the appropriate keyword arguments for the function call (use kwargs instead of args).

### Task 3 - `app/models/deal.py`

Implement two `Deal` instance methods:
* `is_success()`which return `True` if `_status` attribute is equal to `DealStatus.SUCCESS` enum,
* `is_rejected()` which return `True` if `_status` attribute is equal to `DealStatus.REJECTED` enum.

### Task 4 - `app/services/deals.py`

* Method `CRMDealsService.get_list()` should get data from `deals` endpoint and return as a list of `Deal` objects. You should use endpoint without trailing slash.

## Environment setup
To execute the unit tests, use:
```
pip install -q -e . && python3 setup.py pytest
```
