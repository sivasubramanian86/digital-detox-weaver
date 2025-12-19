"""
Digital Detox Weaver - Full Streamlit Cloud App
Production-ready dashboard for epidemiological data analysis
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from data_generators import get_all_data

# Page config
st.set_page_config(
    page_title="Digital Detox Weaver",
    page_icon="🧵",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
.main { padding-top: 1rem; }
.stMetric { background: #1e1e1e; padding: 1rem; border-radius: 0.5rem; }
.stTabs [data-baseweb="tab-list"] { gap: 2px; }
.stTabs [data-baseweb="tab"] { background: #262730; color: #fafafa; }
</style>
""", unsafe_allow_html=True)

# Title
st.title("🧵 Digital Detox Weaver")
st.markdown("**Production-Ready Health Analytics Platform**")

# Load data with error handling
@st.cache_data
def load_data():
    try:
        return get_all_data()
    except Exception as e:
        st.error(f"Data generation failed: {e}")
        # Return mock data for demo
        return {
            'global_epidemiology': pd.DataFrame({
                'country': ['USA', 'UK', 'Germany', 'Japan'],
                'prevalence_rate': [15.2, 12.8, 14.1, 11.5],
                'population': [331000000, 67000000, 83000000, 125000000]
            }),
            'age_stratified': pd.DataFrame({
                'age_group': ['13-17', '18-24', '25-34', '35-44', '45+'],
                'prevalence_rate': [22.1, 18.5, 15.2, 12.8, 8.9]
            }),
            'platform_specific': pd.DataFrame({
                'platform': ['TikTok', 'Instagram', 'YouTube', 'Twitter'],
                'daily_usage_hours': [2.5, 1.8, 3.2, 1.2],
                'harm_score': [7.2, 6.8, 5.1, 5.9],
                'user_base_millions': [1000, 2000, 2500, 450]
            }),
            'disease_timeline': pd.DataFrame({
                'months_since_onset': list(range(0, 25, 3)),
                'severity_score': [2.1, 3.2, 4.5, 5.8, 6.2, 5.9, 5.1, 4.2, 3.8],
                'condition': ['Digital Addiction'] * 9
            }),
            'ses_inequality': pd.DataFrame({
                'ses_category': ['Low', 'Middle', 'High'],
                'prevalence_rate': [18.5, 14.2, 9.8]
            }),
            'detox_recovery': pd.DataFrame({
                'weeks_in_program': list(range(0, 13)),
                'improvement_score': [0, 1.2, 2.8, 4.1, 5.5, 6.8, 7.9, 8.5, 8.9, 9.2, 9.4, 9.6, 9.7]
            })
        }

# Check API key from environment variables or secrets
import os
try:
    # Try environment variable first (for Cloud Run)
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        # Fallback to Streamlit secrets (for Streamlit Cloud)
        api_key = st.secrets.get("GEMINI_API_KEY", None)
except:
    # If secrets.toml doesn't exist, use environment variable
    api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.warning("🔑 GEMINI_API_KEY not found - using demo mode")
    st.info("**For Cloud Run**: Set environment variable GEMINI_API_KEY")
    st.info("**For Streamlit Cloud**: Add GEMINI_API_KEY in secrets")
    # Don't stop - continue with demo data

try:
    data = load_data()
    
    # Sidebar
    with st.sidebar:
        st.header("📊 Navigation")
        tab_selection = st.radio("Select View:", [
            "🌍 Global Overview",
            "👥 Age Analysis", 
            "📱 Platforms",
            "🔬 Mechanisms",
            "🏥 Disease Timeline",
            "💰 Inequality",
            "✨ Detox Effects",
            "📋 Reports"
        ])
    
    # Main content
    if "Global Overview" in tab_selection:
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Records", f"{sum(len(df) for df in data.values()):,}")
        with col2:
            st.metric("Countries", data['global_epidemiology']['country'].nunique())
        with col3:
            st.metric("Avg Screen Time", f"{data['global_epidemiology']['avg_screen_time_hours'].mean():.1f}h")
        with col4:
            st.metric("Data Sources", len(data))
        
        # World map
        fig = px.choropleth(
            data['global_epidemiology'].groupby('country')['avg_screen_time_hours'].mean().reset_index(),
            locations='country',
            locationmode='country names',
            color='avg_screen_time_hours',
            title="Global Average Screen Time (Hours/Day)",
            color_continuous_scale='Reds'
        )
        st.plotly_chart(fig, use_container_width=True)
        
    elif "Age Analysis" in tab_selection:
        fig = px.line(
            data['age_stratification'],
            x='age_group',
            y='health_impact_score',
            title="Health Impact by Age Group",
            markers=True
        )
        st.plotly_chart(fig, use_container_width=True)
        
    elif "Platforms" in tab_selection:
        fig = px.scatter(
            data['platform_comparison'],
            x='engagement_score',
            y='harm_score',
            size='user_base_millions',
            color='platform',
            title="Platform Engagement vs Harm Score"
        )
        st.plotly_chart(fig, use_container_width=True)
        
    elif "Disease Timeline" in tab_selection:
        fig = px.line(
            data['disease_timeline'],
            x='year',
            y='prevalence_rate',
            color='disease',
            title="Disease Prevalence Timeline (2010-2025)"
        )
        st.plotly_chart(fig, use_container_width=True)
        
    elif "Inequality" in tab_selection:
        fig = px.bar(
            data['ses_inequality'].groupby('income_level')['health_impact_multiplier'].mean().reset_index(),
            x='income_level',
            y='health_impact_multiplier',
            title="Health Impact by Socioeconomic Status"
        )
        st.plotly_chart(fig, use_container_width=True)
        
    elif "Detox Effects" in tab_selection:
        fig = px.line(
            data['detox_timeline'],
            x='week',
            y='sleep_quality_improvement',
            title="Sleep Quality Recovery Over Time",
            markers=True
        )
        st.plotly_chart(fig, use_container_width=True)
        
    elif "Reports" in tab_selection:
        st.header("📋 Generated Reports")
        
        reports = {
            "Research Framework": "01_initialization.md",
            "Statistical Analysis": "03_analysis.md", 
            "Visualization Design": "04_visualization_design.md",
            "Health Insights": "05_health_insights.md",
            "Policy Recommendations": "06_policy_recommendations.md",
            "Final Report": "FINAL_REPORT.md"
        }
        
        for name, file in reports.items():
            with st.expander(f"📄 {name}"):
                try:
                    with open(f"outputs/{file}", 'r', encoding='utf-8') as f:
                        st.markdown(f.read())
                except:
                    st.info(f"Report not generated yet. Run `python kiro_main.py` to generate.")
    
    # Data explorer at bottom
    with st.expander("🔍 Raw Data Explorer"):
        dataset = st.selectbox("Select Dataset", list(data.keys()))
        st.dataframe(data[dataset], use_container_width=True)
    
except Exception as e:
    st.error(f"Error: {e}")
    st.info("💡 Make sure to add your GEMINI_API_KEY in Streamlit Cloud secrets.")