# these are mock APIs

def get_campaign_data():
    return {
        "campaign": "Winter Sale",
        "ctr": 1.2,
        "cpc": 2.3,
        "roas": 1.1,
        "impressions": 15000,
        "conversions": 120
    }

def update_budget(campaign, percent):
    return f"Budget for {campaign} increased by {percent}%"