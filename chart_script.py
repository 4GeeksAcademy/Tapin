import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime, timedelta

# Data for the roadmap phases with proper risk level mapping
roadmap_data = [
    {
        "phase": "Discovery & Validation",
        "start_month": 1,
        "end_month": 2,
        "duration_months": 2,
        "risk_level": "On Track",
        "color": "#2E8B57",  # Sea green for on track
        "key_activities": "15-20 nonprofit interviews | Identify target city | Validate pricing | Build MVP spec",
        "metrics": "3-5 nonprofits commit | $200-300/mo pricing | Feature roadmap confirmed",
        "checkpoint": "GO if 3+ nonprofits ready to pilot"
    },
    {
        "phase": "Pilot Program", 
        "start_month": 3,
        "end_month": 5,
        "duration_months": 3,
        "risk_level": "On Track",
        "color": "#2E8B57",  # Sea green for on track
        "key_activities": "Launch nonprofit MVP | Recruit 200+ volunteers | 10+ nonprofit customers | Optimize matching",
        "metrics": "10+ nonprofits pilot | 200+ volunteers matched | 50%+ follow-through | 3+ case studies",
        "checkpoint": "GO if 50%+ follow-through; 10 nonprofits engaged"
    },
    {
        "phase": "Product Optimization",
        "start_month": 6,
        "end_month": 8,
        "duration_months": 3,
        "risk_level": "Watch",
        "color": "#D2BA4C",  # Moderate yellow for watch
        "key_activities": "Iterate algorithm | 30+ paying nonprofits | Volunteer verification | Impact tracking",
        "metrics": "30+ nonprofits paying | 70%+ follow-through | $50K ARR | 10%+ monthly growth",
        "checkpoint": "GO if 30+ customers; 70% follow-through; $50K ARR"
    },
    {
        "phase": "Geographic Expansion",
        "start_month": 9,
        "end_month": 12,
        "duration_months": 4,
        "risk_level": "Critical",
        "color": "#DB4545",  # Bright red for critical timeline
        "key_activities": "Expand 2-3 cities | Sales playbook | Partner integrations | Series A prep",
        "metrics": "100+ nonprofits total | $150K+ ARR | 3-4 cities active | 80%+ retention",
        "checkpoint": "Path to profitability clear; $150K ARR; national expansion viable"
    }
]

# Create the Gantt chart
fig = go.Figure()

# Track which risk levels we've added to avoid duplicates in legend
added_risk_levels = set()

# Add bars for each phase
for i, phase in enumerate(roadmap_data):
    # Detailed hover text with all key information
    hover_text = f"<b>{phase['phase']}</b> (Months {phase['start_month']}-{phase['end_month']})<br>" + \
                f"<b>Risk Level:</b> {phase['risk_level']}<br><br>" + \
                f"<b>Key Activities:</b><br>• {phase['key_activities'].replace(' | ', '<br>• ')}<br><br>" + \
                f"<b>Target Metrics:</b><br>• {phase['metrics'].replace(' | ', '<br>• ')}<br><br>" + \
                f"<b>Checkpoint:</b><br>{phase['checkpoint']}"
    
    # Only show in legend if this risk level hasn't been added yet
    show_legend = phase['risk_level'] not in added_risk_levels
    if show_legend:
        added_risk_levels.add(phase['risk_level'])
    
    fig.add_trace(go.Bar(
        y=[phase['phase']],
        x=[phase['duration_months']],
        base=[phase['start_month'] - 1],
        orientation='h',
        marker=dict(color=phase['color']),
        name=phase['risk_level'],
        hovertemplate=hover_text + "<extra></extra>",
        width=0.5,
        showlegend=show_legend,
        text=f"M{phase['start_month']}-{phase['end_month']}",
        textposition="inside",
        textfont=dict(color="white", size=11)
    ))

# Add milestone markers and key targets as annotations
annotations = []
annotations.append(dict(
    x=2.5, y=3.3, text="3-5 nonprofits commit",
    showarrow=False, font=dict(size=9), bgcolor="rgba(255,255,255,0.8)"
))
annotations.append(dict(
    x=4.5, y=2.3, text="10+ nonprofits, 50%+ follow-through",
    showarrow=False, font=dict(size=9), bgcolor="rgba(255,255,255,0.8)"
))
annotations.append(dict(
    x=7.5, y=1.3, text="$50K ARR, 70%+ follow-through", 
    showarrow=False, font=dict(size=9), bgcolor="rgba(255,255,255,0.8)"
))
annotations.append(dict(
    x=10.5, y=0.3, text="$150K+ ARR, 100+ nonprofits",
    showarrow=False, font=dict(size=9), bgcolor="rgba(255,255,255,0.8)"
))

# Update layout
fig.update_layout(
    title="Tapin B2B Roadmap: 12-Month Timeline",
    xaxis_title="Timeline (Months)",
    yaxis_title="Phases", 
    barmode='overlay',
    showlegend=True,
    legend=dict(
        orientation='h',
        yanchor='bottom',
        y=1.05,
        xanchor='center',
        x=0.5,
        title="Risk Level"
    ),
    annotations=annotations
)

# Update x-axis to show months 1-12 clearly
fig.update_xaxes(
    range=[0, 13],
    tickmode='linear',
    tick0=1,
    dtick=1,
    tickvals=list(range(1, 13)),
    ticktext=[f"M{i}" for i in range(1, 13)]
)

# Update y-axis to reverse order so Discovery is at top
fig.update_yaxes(autorange="reversed")

# Update traces for consistent styling
fig.update_traces(cliponaxis=False)

# Save the chart
fig.write_image("gantt_roadmap.png")
fig.write_image("gantt_roadmap.svg", format="svg")

fig.show()