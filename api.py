class Shortener():
    """
    The shortner API provides three functions, create, retrive and update shortened URL token.
    """
    def __init__(self, shortener, store, validator) -> None:
        self.__shortener = shortener
        self.__store =  store
        self.__validator = validator
        self.__default_protocol = 'http://'
    
    def create(self, url, user = '') -> str:
        shortened_str = ''
        
        #use the validator to validate the original URL
        if self.__validator(url):
            #add default protocol
            if '://' not in url:
                url = f'{self.__default_protocol}{url}'

            #for each user we will create a differnt short URL token
            input_url = f'{url}{user}'

            #create using the shortener function
            shortened_str = self.__shortener(input_url)

            i = 0
            #try store the pair, if got collision, re-create by adding a trailing number
            while not self.__store.add(shortened_str, url, user):
                #3 is an arbitrary number here to prevent collision, if SHA256 bits are evenly distributed, the chance of collision is very low
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
        #basic check to ensure no infinite redirection
        if url.endswith(shortened_str):
            raise ValueError('Short URL and Original URL cannot be the same.')
        if self.__validator(url):
            #add default protocol
            if '://' not in url:
                url = f'{self.__default_protocol}{url}'
            return self.__store.update(shortened_str, url, user)
        else:
            raise ValueError("URL is invalid.") 