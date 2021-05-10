import api
from store.store import Store
import pytest

def mock_shortener(url, retry=0):
    if len(url) < 10:
        return f'{url}{retry}'
    else:
        return f'{url[0:9]}{retry}'

class MockStore(Store):
    def __init__(self) -> None:
        super().__init__()
        self.__dict = dict()

    def add(self, short_url:str, url:str, user:str = None) -> bool:
        if short_url not in self.__dict:
            self.__dict[short_url]=user
            return True
        else:
            #to simulate hash collision
            return False
    def get(self, short_url:str) -> str:
        if not short_url:
            return ''
        else:
            return f'{short_url}_long'
    def update(self, short_url:str, url:str, user:str) -> bool:
        if short_url in self.__dict and self.__dict[short_url] == user:
            return True
        return False

def mock_validator(url):
    return not not url

def test_api_create():
    s = api.Shortener(mock_shortener, MockStore(), mock_validator)
    
    #happy path
    url = 'http://google.com'
    assert s.create(url) == f'{url[0:9]}0'

    #empty string should throw error
    with pytest.raises(ValueError):
        assert s.create('')
    
    #protocol should be auto added
    url = 'www.google.com'
    assert s.create(url) == f'http://{url}'[0:9] + '0'

    #retrieve happy path
    short_url = 'http://short.com'
    assert s.retrieve(short_url) == f'{short_url}_long'

    #if not found raise error
    with pytest.raises(ValueError):
        assert s.retrieve('')

    #simulate collision
    url = 'http://www.google.com'
    assert s.create(url) == f'{url}'[0:9] + '1'
    assert s.create(url) == f'{url}'[0:9] + '2'
    assert s.create(url) == f'{url}'[0:9] + '3'
    with pytest.raises(ValueError):
        assert s.create(url)

def test_api_retrieve():
    s = api.Shortener(mock_shortener, MockStore(), mock_validator)

    short = 'short'
    assert s.retrieve(short) == f'{short}_long'

    with pytest.raises(ValueError):
        assert s.retrieve('')

def test_api_update():
    s = api.Shortener(mock_shortener, MockStore(), mock_validator)
    
    url = 'google.com'
    assert s.create(url, 'user') == f'http://{url}'[0:9] + '0'

    assert s.update(f'http://{url}'[0:9] + '0', url, '') == False
    assert s.update(f'http://{url}'[0:9] + '0', url, 'user')

    with pytest.raises(ValueError):
        assert s.update(f'http://{url}'[0:9] + '0', '', 'user')
