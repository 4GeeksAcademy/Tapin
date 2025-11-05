import plotly.graph_objects as go
import plotly.express as px
import numpy as np

# Data from the provided JSON
strategies = [
    {
        "name": "Volunteer-First",
        "metrics": {
            "ProfitabilityTimeline": 3,
            "CompetitiveIntensity": 1,
            "CACEfficiency": 3,
            "NetworkEffectsStrength": 8,
            "MarketSize": 9
        },
        "color": "#DB4545"  # Using theme red
    },
    {
        "name": "B2B-First",
        "metrics": {
            "ProfitabilityTimeline": 8,
            "CompetitiveIntensity": 7,
            "CACEfficiency": 8,
            "NetworkEffectsStrength": 7,
            "MarketSize": 6
        },
        "color": "#2E8B57"  # Using theme green
    },
    {
        "name": "Local Services",
        "metrics": {
            "ProfitabilityTimeline": 4,
            "CompetitiveIntensity": 2,
            "CACEfficiency": 4,
            "NetworkEffectsStrength": 7,
            "MarketSize": 8
        },
        "color": "#1FB8CD"  # Using theme cyan
    }
]

# Dimension names (abbreviated to 15 chars max)
dimensions = [
    "Profit Timeline",
    "Competitive Int",
    "CAC Efficiency",
    "Network Effects", 
    "Market Size"
]

# Create radar chart
fig = go.Figure()

# Add each strategy as a trace
for strategy in strategies:
    values = [
        strategy["metrics"]["ProfitabilityTimeline"],
        strategy["metrics"]["CompetitiveIntensity"], 
        strategy["metrics"]["CACEfficiency"],
        strategy["metrics"]["NetworkEffectsStrength"],
        strategy["metrics"]["MarketSize"]
    ]
    
    # Close the radar chart by adding first value at end
    values_closed = values + [values[0]]
    dimensions_closed = dimensions + [dimensions[0]]
    
    # Make B2B-First more prominent
    line_width = 4 if "B2B" in strategy["name"] else 2
    
    fig.add_trace(go.Scatterpolar(
        r=values_closed,
        theta=dimensions_closed,
        fill='toself',
        name=strategy["name"],
        line=dict(color=strategy["color"], width=line_width),
        fillcolor=strategy["color"],
        opacity=0.3 if "B2B" not in strategy["name"] else 0.5
    ))

# Update layout
fig.update_layout(
    title="Tapin Strategic Positioning Analysis",
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 10],
            tickvals=[2, 4, 6, 8, 10],
            showticklabels=True
        )
    ),
    legend=dict(
        orientation='h',
        yanchor='bottom',
        y=1.05,
        xanchor='center',
        x=0.5
    )
)

# Save the chart
fig.write_image("tapin_positioning.png")
fig.write_image("tapin_positioning.svg", format="svg")

fig.show()