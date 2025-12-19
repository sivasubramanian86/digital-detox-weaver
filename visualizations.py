"""
Digital Detox Weaver: Visualization Templates
SOURCE 3 (Project Code) - Plotly chart templates and utilities
"""

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd


def create_global_trends_chart(data: pd.DataFrame) -> go.Figure:
    """Create global screen time trends chart"""
    fig = px.line(
        data, 
        x='year', 
        y='avg_screen_time_hours',
        color='country',
        title='Global Screen Time Trends (2010-2024)',
        template='plotly_white'
    )
    fig.update_layout(
        height=400,
        hovermode='x unified'
    )
    return fig


def create_age_vulnerability_chart(data: pd.DataFrame) -> go.Figure:
    """Create age vulnerability curves"""
    fig = px.line(
        data,
        x='screen_time_hours',
        y='health_impact_score',
        color='age_group',
        title='Health Impact by Age Group',
        template='plotly_white'
    )
    fig.update_layout(height=400)
    return fig


def create_platform_bubble_chart(data: pd.DataFrame) -> go.Figure:
    """Create platform engagement vs harm bubble chart"""
    fig = px.scatter(
        data,
        x='engagement_score',
        y='harm_score',
        size='user_base_millions',
        color='addiction_potential',
        hover_name='platform',
        title='Platform Engagement vs Health Harm',
        template='plotly_white'
    )
    fig.update_layout(height=500)
    return fig


def create_mechanisms_heatmap(data: pd.DataFrame) -> go.Figure:
    """Create mechanism-outcome pathway heatmap"""
    pivot_data = data.pivot_table(
        values='pathway_strength',
        index='mechanism',
        columns='outcome',
        fill_value=0
    )
    
    fig = px.imshow(
        pivot_data,
        title='Mechanism-Outcome Pathway Strengths',
        color_continuous_scale='Reds',
        aspect='auto'
    )
    fig.update_layout(height=500)
    return fig


def create_detox_recovery_chart(data: pd.DataFrame) -> go.Figure:
    """Create detox recovery trajectories"""
    fig = go.Figure()
    
    outcomes = ['sleep_quality_improvement', 'mood_improvement', 'attention_improvement']
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
    
    for outcome, color in zip(outcomes, colors):
        fig.add_trace(go.Scatter(
            x=data['week'],
            y=data[outcome],
            mode='lines+markers',
            name=outcome.replace('_', ' ').title(),
            line=dict(color=color)
        ))
    
    fig.update_layout(
        title='13-Week Digital Detox Recovery Trajectories',
        xaxis_title='Weeks',
        yaxis_title='Improvement Score',
        template='plotly_white',
        height=500
    )
    return fig


def create_ses_inequality_chart(data: pd.DataFrame) -> go.Figure:
    """Create SES inequality visualization"""
    summary = data.groupby('income_level')['health_impact_multiplier'].mean().reset_index()
    
    fig = px.bar(
        summary,
        x='income_level',
        y='health_impact_multiplier',
        title='Health Impact Multiplier by Income Level',
        color='health_impact_multiplier',
        color_continuous_scale='Reds',
        template='plotly_white'
    )
    fig.update_layout(height=400)
    return fig