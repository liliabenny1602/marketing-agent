import time

class LiveTracer:

    def __init__(self, container):
        self.container = container

    def log(self, message):
        self.container.markdown(message)

    def node_start(self, name):
        self.log(f"▶ **{name} running...**")

    def node_end(self, name):
        self.log(f"✔ **{name} complete**")
        time.sleep(0.2)