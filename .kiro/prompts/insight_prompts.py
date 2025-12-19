"""
Insight Prompts – Digital Detox Weaver

Specialized prompts for HealthResearcherAgent (T=0.5)
Focuses on mechanistic pathways and evidence synthesis.
"""


class InsightPrompts:
    """Prompts for health insights and mechanism analysis."""

    @staticmethod
    def health_insights_prompt(analysis_summary: str) -> str:
        """
        Prompt for Step 5: Generate mechanistic health insights.
        """
        return f"""
        You are a leading public health researcher specializing in digital health epidemiology.
        
        Based on this analysis:
        {analysis_summary}
        
        Generate comprehensive health insights addressing:
        
        1. **Causal Mechanisms (the 'why')**
           - Circadian rhythm disruption: blue light → melatonin suppression → sleep loss
           - Sleep-to-metabolic cascade: poor sleep → insulin resistance → obesity → diabetes
           - Dopamine dysregulation: chronic overstimulation → reward system downregulation
           - Social comparison toxicity: algorithm-driven negative affect → depression/anxiety
        
        2. **Age Vulnerability Pathways**
           - Why adolescents (13-17) are 5.5× more vulnerable
           - Prefrontal cortex development windows
           - Sleep need variations across ages
           - Social sensitivity during puberty
        
        3. **Biological Plausibility**
           - Cite 5+ peer-reviewed mechanisms
           - Link screen time exposure to each health outcome
           - Explain temporal relationships
           - Quantify dose-response curves
        
        4. **Reversibility & Recovery**
           - Recovery timelines from SOURCE 1 detox data
           - Sleep normalization trajectory
           - Dopamine system recovery
           - Mood/anxiety improvement curves
        
        5. **SES-Mediated Pathways**
           - Why low-income populations suffer more harm
           - Less parental supervision, more screen reliance
           - Stress amplification effects
           - Healthcare access gaps
        
        6. **Platform-Specific Mechanisms**
           - TikTok: algorithm-driven rapid-fire content, dopamine loop
           - Instagram: social comparison, appearance anxiety
           - YouTube: binge-watching mechanics, sleep displacement
           - Twitter: outrage algorithm, cortisol elevation
        
        Write in academic style with citations. Length: 2000+ words.
        Emphasize evidence-based reasoning and biological plausibility.
        """

insight_prompts = InsightPrompts()