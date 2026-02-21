import time
from tools.ads_api import get_campaign_data
from workflows.campaign_graph import build_graph
from eval.metrics import track_latency

def run():

    start = time.time()

    metrics = get_campaign_data()

    graph = build_graph()

    result = graph.invoke({"metrics": metrics})

    latency = track_latency(start)

    print("\n--- RESULTS ---")
    print(result)
    print("\nLatency:", latency, "seconds")

if __name__ == "__main__":
    run()