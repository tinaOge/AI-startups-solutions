# app/query_interface/suggest_viz.py
def suggest_visualization(query):
    keywords_to_charts = {
        "trend": ["Line Chart", "Area Chart"],
        "compare": ["Bar Chart", "Stacked Bar Chart"],
        "growth": ["Line Chart", "Scatter Plot"],
        "breakdown": ["Pie Chart", "Treemap"],
        "relationship": ["Scatter Plot", "Bubble Chart"],
        "goal": ["Gauge Chart", "Bullet Chart"],
        "outliers": ["Box Plot", "Histogram"],
    }

    suggestions = []
    for keyword, charts in keywords_to_charts.items():
        if keyword in query.lower():
            suggestions.extend(charts)

    return list(set(suggestions)) or ["Line Chart"]  # Default suggestion


# Example query
query = "Show the revenue and profit margin trends for Tech Innovators."
print(suggest_visualization(query))