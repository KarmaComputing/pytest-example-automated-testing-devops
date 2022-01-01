# Pytest python example with automated testing

- At every push and/or merge to `main` branch `pytest` is used to run the tests which are written in the `./tests` directory of this repo
- The exact same tests may be ran locally (see "Run tests locally")
- Automated testing with a pipline and secrets (using Github actions- but this process is the same for any provider Gitlab, bitbucket etc) see https://github.com/KarmaComputing/pytest-example-automated-testing/actions

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

## Example Output (when tests pass)
```
collected 1 item                                                                                                                  

tests/test_app.py::test_add PASSED                                                                                          [100%]

======================================================== 1 passed in 0.01s ========================================================
(venv) (base) $
```

## Example Output (when a test fails)
```

Run python -m pytest -vv
============================= test session starts ==============================
platform linux -- Python 3.10.1, pytest-6.2.5, py-1.11.0, pluggy-1.0.0 -- /opt/hostedtoolcache/Python/3.10.1/x64/bin/python
cachedir: .pytest_cache
rootdir: /home/runner/work/pytest-example-automated-testing/pytest-example-automated-testing
collecting ... collected 2 items

tests/test_app.py::test_add PASSED                                       [ 50%]
tests/test_app.py::test_get_api_key FAILED                               [100%]

=================================== FAILURES ===================================
_______________________________ test_get_api_key _______________________________

    def test_get_api_key():
>       assert app.get_api_key() is not None

tests/test_app.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

    def get_api_key():
>       assert API_KEY is not None, "An empty API_KEY should never be allowed, did you forget to either add it to your .env file or, set the environment variable?"  # noqa: E501
E       AssertionError: An empty API_KEY should never be allowed, did you forget to either add it to your .env file or, set the environment variable?

app/app.py:13: AssertionError
=========================== short test summary info ============================
FAILED tests/test_app.py::test_get_api_key - AssertionError: An empty API_KEY...
========================= 1 failed, 1 passed in 0.04s ==========================
Error: Process completed with exit code 1.
```
