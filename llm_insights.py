def generate_insight(profile):

    prompt = f"""
    Customer Risk: {profile['Churn_Risk']}
    Revenue: {profile['Predicted_Revenue']}
    Segment: {profile['Segment']}

    Give:
    1 Executive Summary
    2 Business Risk
    3 Recommended Action
    """

    return prompt