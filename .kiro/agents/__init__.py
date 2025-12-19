"""
Digital Detox Weaver Agents Module

Contains 4 specialized AI agents for multi-source data analysis:
- DataAnalystAgent (SOURCE 2 – Statistical Analysis)
- VisualizationExpertAgent (SOURCE 2 – Chart Design)
- HealthResearcherAgent (SOURCE 2 – Mechanism Insights)
- PolicyAdvisorAgent (SOURCE 2 – Policy Recommendations)
"""

from .data_analyst import DataAnalystAgent
from .visualization_expert import VisualizationExpertAgent
from .health_researcher import HealthResearcherAgent
from .policy_advisor import PolicyAdvisorAgent

__all__ = [
    "DataAnalystAgent",
    "VisualizationExpertAgent",
    "HealthResearcherAgent",
    "PolicyAdvisorAgent",
]