import time
from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    # random time between 1 and 3 seconds
    waitTime = between(1, 3)

    @task
    def index_page(self):
        self.client.get(url='/#home')

    @task
    def index_page(self):
        self.client.get(url='/#about')
