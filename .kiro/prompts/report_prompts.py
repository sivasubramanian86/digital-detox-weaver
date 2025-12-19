"""
Report Prompts – Digital Detox Weaver

Specialized prompts for comprehensive final report generation.
Focuses on publication-ready synthesis for policymakers and researchers.
"""


class ReportPrompts:
    """Prompts for comprehensive final report generation."""

    @staticmethod
    def final_report_prompt(analysis_str: str, health_insights_str: str, policy_str: str) -> str:
        """
        Prompt for Step 8: Generate 3000+ word final comprehensive report.
        """
        return f"""
        You are writing a comprehensive public health report for a major health organization.
        
        Synthesis of prior analysis:
        
        ANALYSIS:
        {analysis_str}
        
        HEALTH INSIGHTS:
        {health_insights_str}
        
        POLICY RECOMMENDATIONS:
        {policy_str}
        
        Write a **3000+ word publication-ready report** with these sections:
        
        ## Executive Summary (250 words)
        - Key findings with numbers
        - Main policy recommendations
        - Urgency and call to action
        
        ## 1. Introduction
        - Screen time prevalence and trends globally
        - Known health impacts from literature
        - Why this problem matters now
        - Report objectives and scope
        
        ## 2. Methods
        - Data sources and integration approach
        - Analysis methodology
        - Study populations and timeframe
        - Limitations and assumptions
        
        ## 3. Global Epidemiology Results
        - Screen time trends 2010-2024
        - Disease burden trends by type
        - Geographic variation
        - Inflection points and critical thresholds
        
        ## 4. Vulnerable Populations
        - Age stratification (why adolescents at highest risk)
        - Socioeconomic inequality (SES disparities)
        - Platform-specific vulnerabilities
        - Intersectional considerations
        
        ## 5. Mechanistic Pathways
        - Circadian disruption pathway
        - Sleep → metabolic dysfunction → obesity/diabetes
        - Dopamine system downregulation
        - Social comparison and mental health
        
        ## 6. Recovery & Reversibility
        - Evidence that harms are reversible
        - Detox timelines and recovery trajectories
        - Factors predicting successful recovery
        - Implications for prevention and treatment
        
        ## 7. Policy Recommendations
        - 3-phase implementation pathway
        - Evidence-based interventions ranked by effectiveness
        - Cost-benefit analysis
        - Equity considerations and disparities-focused approaches
        
        ## 8. Discussion
        - What do findings mean for different stakeholders?
        - Consistency with published literature
        - Implications for researchers, policymakers, families
        - Knowledge gaps and future research priorities
        
        ## 9. Conclusion
        - Summary of key messages
        - Urgency for action
        - Call to decision-makers
        
        ## References
        - Include 30+ citations
        - Mix academic papers, government reports, data sources
        
        Write with:
        - Academic rigor and evidence-based reasoning
        - Clear, compelling language for policy audience
        - Specific numbers and statistics
        - Actionable recommendations
        """

report_prompts = ReportPrompts()