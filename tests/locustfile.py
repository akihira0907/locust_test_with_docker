from locust import HttpLocust, TaskSequence, seq_task, between
from locust.clients import HttpSession


def index(l):
    l.client.get("/")


class UserBehavior(TaskSequence):
    @seq_task(1)
    def index(self):
        index(self)


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(5, 9)
