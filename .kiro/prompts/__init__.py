"""
Digital Detox Weaver Prompts Module

Contains specialized prompt templates for 4 agents:
- Analysis prompts (statistical, research methodology)
- Visualization prompts (chart design, accessibility)
- Insight prompts (mechanisms, evidence synthesis)
- Report prompts (comprehensive narrative, policy framing)
"""

from .analysis_prompts import AnalysisPrompts
from .visualization_prompts import VisualizationPrompts
from .insight_prompts import InsightPrompts
from .report_prompts import ReportPrompts

__all__ = [
    "AnalysisPrompts",
    "VisualizationPrompts",
    "InsightPrompts",
    "ReportPrompts",
]