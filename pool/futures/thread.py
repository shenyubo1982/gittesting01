# thread.py
class ThreadPoolExecutor:
    def __init__(self, max_workers):
        self.max_workers = max_workers

    def submit(self):
        print('ThreadPool submit')


