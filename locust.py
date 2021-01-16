import time
from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    waitTime = between(1, 4)

    @task
    def index_page(self):
        self.client.get(url='/#home')
