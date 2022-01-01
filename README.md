# Pytest python example with automated testing

- At every push and/or merge to `main` branch `pytest` is used to run the tests which are written in the `./tests` directory of this repo
- The exact same tests may be ran locally (see "Run tests locally")

## Setup (local)

```
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

Copy api key (this is an *example* , it's not a real api key-you can use any value).
```
cp .env.example .env
```

## Run tests locally

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
