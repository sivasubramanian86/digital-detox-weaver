"""
Digital Detox Weaver: Configuration
SOURCE 3 (Project Code) - Dashboard and application configuration
"""

import os
from pathlib import Path
from typing import Dict, Any

# Project paths
PROJECT_ROOT = Path(__file__).parent
KIRO_DIR = PROJECT_ROOT / ".kiro"
OUTPUTS_DIR = PROJECT_ROOT / "outputs"
CACHE_DIR = PROJECT_ROOT / "cache"
ARCHIVES_DIR = PROJECT_ROOT / "archives"

# Ensure directories exist
for dir_path in [OUTPUTS_DIR, CACHE_DIR, ARCHIVES_DIR]:
    dir_path.mkdir(exist_ok=True)

# Dashboard configuration
DASHBOARD_CONFIG = {
    "title": "🧵 Digital Detox Weaver",
    "subtitle": "Screen Time & Health Analytics Platform",
    "description": "Weaving together epidemiological data, AI analysis, and policy insights",
    "theme": {
        "primary_color": "#33aabc",
        "background_color": "#ffffff",
        "secondary_background_color": "#f0f2f6",
        "text_color": "#262730"
    }
}

# Data source configuration
DATA_SOURCES = {
    "source_1": {
        "name": "Epidemiological Data Generator",
        "location": "data_generators.py",
        "description": "494+ records across 8 datasets",
        "status": "operational"
    },
    "source_2": {
        "name": "AI-Generated Insights", 
        "location": ".kiro/agents/",
        "description": "25,000+ words from 4 specialized agents",
        "status": "operational"
    },
    "source_3": {
        "name": "Dashboard & Visualization",
        "location": "app.py, visualizations.py",
        "description": "8-tab interactive interface",
        "status": "operational"
    },
    "source_4": {
        "name": "Orchestration Framework",
        "location": ".kiro/",
        "description": "Multi-LLM routing and workflows",
        "status": "operational"
    }
}

# Chart configuration
CHART_CONFIG = {
    "template": "plotly_white",
    "color_palette": ["#33aabc", "#ff6b6b", "#4ecdc4", "#45b7d1", "#96ceb4", "#feca57"],
    "height_default": 400,
    "height_large": 500,
    "accessibility": {
        "contrast_ratio": 4.5,
        "font_size_min": 12
    }
}

# Tab configuration
TAB_CONFIG = [
    {"id": "global", "name": "🌍 Global", "description": "Global trends and KPIs"},
    {"id": "age", "name": "👥 Age", "description": "Age vulnerability analysis"},
    {"id": "platforms", "name": "📱 Platforms", "description": "Platform comparison"},
    {"id": "mechanisms", "name": "🔬 Mechanisms", "description": "Causal pathways"},
    {"id": "diseases", "name": "🏥 Diseases", "description": "Disease timelines"},
    {"id": "inequality", "name": "💰 Inequality", "description": "SES disparities"},
    {"id": "detox", "name": "✨ Detox", "description": "Recovery trajectories"},
    {"id": "policy", "name": "📋 Policy", "description": "Recommendations"}
]

def get_config(key: str) -> Any:
    """Get configuration value by key"""
    config_map = {
        "dashboard": DASHBOARD_CONFIG,
        "data_sources": DATA_SOURCES,
        "charts": CHART_CONFIG,
        "tabs": TAB_CONFIG
    }
    return config_map.get(key, {})