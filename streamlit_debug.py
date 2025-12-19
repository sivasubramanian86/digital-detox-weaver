"""
Debug version of Streamlit app - bypasses API key check
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import os

# Page config
st.set_page_config(
    page_title="Digital Detox Weaver - Debug",
    page_icon="🧵",
    layout="wide"
)

st.title("🧵 Digital Detox Weaver - Debug Mode")

# Show environment info
st.subheader("🔍 Environment Debug")
api_key = os.getenv("GEMINI_API_KEY")
st.write(f"API Key present: {'✅ Yes' if api_key else '❌ No'}")
if api_key:
    st.write(f"API Key length: {len(api_key)} characters")
    st.write(f"API Key starts with: {api_key[:10]}...")

# Mock data (no API calls)
st.subheader("📊 Mock Dashboard")

mock_data = {
    'global_epidemiology': pd.DataFrame({
        'country': ['USA', 'UK', 'Germany', 'Japan', 'France'],
        'prevalence_rate': [15.2, 12.8, 14.1, 11.5, 13.7],
        'population': [331000000, 67000000, 83000000, 125000000, 68000000]
    }),
    'age_stratified': pd.DataFrame({
        'age_group': ['13-17', '18-24', '25-34', '35-44', '45+'],
        'prevalence_rate': [22.1, 18.5, 15.2, 12.8, 8.9]
    })
}

# Show metrics
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Countries", len(mock_data['global_epidemiology']))
with col2:
    st.metric("Age Groups", len(mock_data['age_stratified']))
with col3:
    st.metric("Avg Prevalence", f"{mock_data['global_epidemiology']['prevalence_rate'].mean():.1f}%")

# Show charts
st.subheader("🌍 Global Prevalence")
fig1 = px.bar(
    mock_data['global_epidemiology'],
    x='country',
    y='prevalence_rate',
    title="Digital Addiction Prevalence by Country"
)
st.plotly_chart(fig1, use_container_width=True)

st.subheader("👥 Age Analysis")
fig2 = px.line(
    mock_data['age_stratified'],
    x='age_group',
    y='prevalence_rate',
    title="Prevalence by Age Group",
    markers=True
)
st.plotly_chart(fig2, use_container_width=True)

st.success("✅ Debug dashboard working! If you see this, the deployment is successful.")