## url shortener core
This is the core api support the simple URL shortener.
It provides three functions:
- Create a short URL given a URL and optioanlly a user name
- Update an existing short URL (user can only update his own URL)
- Retrieve the full URL given the shortened string

## design
The core api have three injectable functions to do the real work:
- URL validation
- URL shortening
- URL backend store
It includes a basic implementation of the validator and shortening algorithm.
The backend store is not impelmented. The consumer application should implements its own backend store and inject to the core api.

## test
The code is tested with python 3.8+.
To setup the project, assumed python is installed.
Clone the project and create python venv:
```
git clone https://github.com/Springf/url-shortener-core.git
cd url-shortener-core
python -m venv venv
```
Activate the venv:
Windows `venv\Scripts\activate.bat`
Linux `source venv/bin/activate`
Install the package: `pip install -r requirements.txt`
Run unit tests: `pytest tests`

