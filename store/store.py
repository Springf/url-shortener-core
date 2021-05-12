from abc import ABC

class Store(ABC):
    """
    A backend store that stores the mapping between shortened URL and original URL.
    The consumer application needs to implment the store to suit their needs.
    """

    def add(self, short_url_token:str, url:str, user:str = None) -> bool:
        """
        Add the shortened URL token and original URL pair into store.

        Parameters
        ----------
        short_url_token : str
            The shortened URL token without domain, it should not be None or Empty and should not contain the domain.
        url : str
            The original URL, it should not be None or Empty.
        user: str
            Optional, user's name who created this shortened URL token.

        Returns
        ----------
        bool: 
        If the shortened URL token already exsits in the store, do nothing. Return True if the original URL is the same, otherwise return False.
        If the shortened URL token does not exsit in the store, add the pair and return True.
        """
        raise NotImplementedError()

    def get(self, short_url_token:str) -> str:
        """
        Using the shortened URL token  to retrieve the original URL.

        Parameters
        ----------
        short_url_token : str
            The shortened URL token without domain, it should not be None or Empty and should not contain the domain.

        Returns
        ----------
        str: 
        If the shortened URL token exists in the store, return the original URL. Otherwise return None.
        """
        raise NotImplementedError()

    def update(self, short_url_token:str, url:str, user:str) -> bool:
        """
        Update the shortened URL token and original URL pair in the store.

        Parameters
        ----------
        short_url_token : str
            The shortened URL token without domain, it should not be None or Empty and should not contain the domain.
        url : str
            The original URL, it should not be None or Empty.
        user: str
            Required for update a URL, as the user only can update his/her own shortened URL token. 

        Returns
        ----------
        bool: 
        If the shortened URL token exsits in the store and the user is the creator, update the new URL to the store and return True.
        If the shortened URL token does not exsit in the store or user is not the creator, return False.
        """
        raise NotImplementedError()