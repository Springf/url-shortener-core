class Shortener():
    """
    The shortner API provides three functions, create, retrive and update shortened URLs.
    For short URL creation, it will validate and create, then store it, if a collision is found, re-try for three times before throw error.
    For retrieving original URL, if not found, throw error.
    For update a shortened URL's original URL, only the URL's creator can update it.
    """
    def __init__(self, shortener, store, validator) -> None:
        self.__shortener = shortener
        self.__store =  store
        self.__validator = validator
        self.__default_protocol = 'http://'
    
    def create(self, url, user = '') -> str:
        shortened_str = ''
        
        if self.__validator(url):
            if '://' not in url:
                url = f'{self.__default_protocol}{url}'
            input_url = f'{url}{user}'
            shortened_str = self.__shortener(input_url)
            # 3 is an arbitrary number here to prevent collision
            i = 0
            while not self.__store.add(shortened_str, url, user):
                if i == 3:
                    raise ValueError('Failed to shorten the URL.')
                i += 1
                shortened_str = self.__shortener(input_url, i)
        else:
            raise ValueError("URL is invalid.")    

        return shortened_str

    def retrieve(self, shortened_str) -> str:
        url = ''
        url = self.__store.get(shortened_str)
            
        if not url:
            raise ValueError('Failed to find the URL.')
        return url
    
    def update(self, shortened_str, url, user) -> bool:
        if url.endswith(shortened_str):
            raise ValueError('Short URL and Original URL cannot be the same.')
        if self.__validator(url):
            if '://' not in url:
                url = f'{self.__default_protocol}{url}'
            return self.__store.update(shortened_str, url, user)
        else:
            raise ValueError("URL is invalid.") 