import time
from tools.ads_api import get_campaign_data
from workflows.campaign_graph import build_graph


def run(metrics=None, tracer=None):

    if metrics is None:
        metrics = get_campaign_data()

    graph = build_graph()

    result = graph.invoke({
        "metrics": metrics,
        "tracer": tracer
    })

    return result