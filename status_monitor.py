import requests
import time
from helper import Helper
class Status_Monitor:
    def __init__(self):
        self.round_trip = 0
    '''
        @GET ex /api/customers
        @param url - accept url as string
        @return round_trip as millisecond
    '''
    def get(self, url):
        start = time.time()
        api_response = requests.get(url)
        '''
            Any status codesssss type does not matter here
            because we just want to measure the fully response
            transfer from the server.
        
        '''
        if api_response.status_code:
            self.round_trip = time.time() - start
        return Helper.getMilliSecond(self.round_trip)
    
    '''
        @Todo 
            @Delete ex /api/customers
            - delete all customer
    '''

    '''
        @Todo
            @POST ex /api/customers
            - create new customer
    
    '''
    
    '''
        @Todo
            @PUT ex api/customer
            - update all customer
    
    '''
