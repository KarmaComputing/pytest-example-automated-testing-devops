# Pytest pyton example with automated testing


## Setup (local)

```
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

## Run tests

```
. venv/bin/activate
python -m pytest -vv
```

Output:
```
collected 1 item                                                                                                                  

tests/test_app.py::test_add PASSED                                                                                          [100%]

======================================================== 1 passed in 0.01s ========================================================
(venv) (base) $
```
