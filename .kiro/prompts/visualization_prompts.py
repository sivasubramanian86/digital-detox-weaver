"""
Visualization Prompts – Digital Detox Weaver

Specialized prompts for VisualizationExpertAgent (T=0.6)
Focuses on modern, accessible chart design for 8 dashboard tabs.
"""


class VisualizationPrompts:
    """Prompts for visualization design and specification."""

    @staticmethod
    def visualization_design_prompt(analysis_summary: str) -> str:
        """
        Prompt for Step 4: Design visualizations for the dashboard.
        """
        return f"""
        You are a world-class data visualization designer specializing in healthcare dashboards.
        
        Based on this analysis:
        {analysis_summary}
        
        Design visualizations for 8 dashboard tabs:
        
        1. **🌍 Global Overview**
           - KPI metrics cards (screen time, health burden, affected population)
           - Global time-series chart (2010-2024)
           - World map or country comparison heatmap
        
        2. **👥 Age Analysis**
           - Age-vulnerability curves (non-linear relationship)
           - Stacked bar chart (age group vs health outcome)
           - Risk hierarchy visualization
        
        3. **📱 Platforms**
           - Bubble chart (engagement × harm × user base)
           - Ranked bar chart (platforms by harm index)
           - Social media comparison matrix
        
        4. **🔬 Mechanisms**
           - 4-panel layout: circadian disruption, sleep-weight, dopamine, social comparison
           - Each panel: timeline or pathway diagram
        
        5. **🏥 Disease Timelines**
           - Multi-line chart (7 diseases over 15 years)
           - Toggle filters by disease type
           - Trend acceleration visualization
        
        6. **💰 SES Inequality**
           - Side-by-side comparison (high vs low income)
           - Inequality index trends
           - Healthcare access gap visualization
        
        7. **✨ Detox Effects**
           - 12-13 week recovery curves (4 outcomes)
           - Before/after delta metrics
           - Success rate visualization
        
        8. **📋 Policy & Report**
           - Policy effectiveness ranking
           - 3-phase implementation timeline
           - Cost-benefit visualization
        
        For each:
        - Specify chart type and Plotly template
        - Recommend color scheme (WCAG AA contrast ≥4.5:1)
        - Suggest interactive elements (hover, filter, toggle)
        - Describe accessibility features (alt text, keyboard nav)
        
        Prioritize clarity, insight revelation, and modern aesthetic.
        """

visualization_prompts = VisualizationPrompts()