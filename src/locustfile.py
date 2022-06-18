from locust import HttpUser, task, between
import random

myStatement = ["I love you", "i love you so much", "i hate you very much", "sky is blue color"]
class AppUser(HttpUser):
    wait_time = between(2,5)
    
    @task
    def index_page(self):
        self.client.get('/')
        
    @task
    def sentiment_page(self):
        myText = random.choice(myStatement)
        self.client.get('/sentiment/'+str(myText))
        