## URL shortener core
This is the core api that provides a simple URL shortener.
It has three functions:
- Create a short URL token given a URL and optioanlly a user name
- Update an existing short URL token (user can only update his own generated token)
- Retrieve the full URL given the short URL token

## Design
The core api has three injectable functions to do the real work:
- URL validation
- URL shortening
- URL backend store

It includes a basic implementation of the validator using regex and a shortening algorithm using sha256 hashing.

The backend store is not implemented. The consumer application should implement its own backend store and inject to the core api.

## Project Structure
```
+-- shortener
|   hash_shortener.py  #the default shortener using the sha256 hash function
+-- store
|   store.py #the abstract class of backend store, consumer application needs to implement
+-- tests
|   unit test cases files
+-- validator
|   regex_validator.py #the default validator using regex
api.py #the core api that provides the create/update/retrieve function.
```

## Test
The code is tested with python 3.8+.

To setup the project, assuming python is installed.

Clone the project and create python venv:
```
git clone https://github.com/Springf/url-shortener-core.git
cd url-shortener-core
python -m venv venv
```
Activate the venv:

Windows: `venv\Scripts\activate.bat`

Linux: `source venv/bin/activate`

Install the package: `pip install -r requirements.txt`

Run unit tests: `pytest tests`

## Applications
A basic demo of the core API from command line: https://github.com/Springf/url-shortener

A local web app demo: https://github.com/Springf/url-shortener-web

An aws version: https://github.com/Springf/url-shortener-aws
