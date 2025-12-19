"""
Digital Detox Weaver: Analysis Prompts

This module implements SOURCE 2 - AI-Generated Insights
Provides structured prompt templates for 4 specialized agents
Each prompt incorporates data source context and weaving methodology
"""

class AnalysisPrompts:
    """AI prompts for Digital Detox Weaver data analysis workflows"""
    
    @staticmethod
    def data_sources_context() -> str:
        """Context explaining all 4 data sources for every prompt"""
        return """
        DIGITAL DETOX WEAVER: Data Source Integration Context
        ═════════════════════════════════════════════════════
        
        You are analyzing data from 4 integrated sources:
        
        SOURCE 1 - Epidemiological Data Generator:
        • 800+ records across 8 datasets
        • Global epidemiology (168): 12 countries, 2010-2024
        • Age stratification (80): 5 age groups, non-linear dose-response
        • Platform comparison (7): Engagement vs health impact metrics
        • Mechanisms (41): Circadian, sleep-weight, dopamine pathways
        • Disease timeline (105): 7 diseases, 15-year progression
        • SES inequality (60): Income-stratified health disparities
        • Detox timeline (13): 13-week recovery trajectories
        • Policy interventions (8): Evidence-based effectiveness metrics
        
        SOURCE 2 - This Analysis (AI-Generated):
        • Real-time synthesis of Source 1 data through specialized agents
        • Expert interpretation through distinct roles (Analyst, Visualizer, Researcher, Advisor)
        • Integration of epidemiological evidence with mechanistic understanding
        
        SOURCE 3 - Original Project Foundation:
        • Dashboard infrastructure (Streamlit app.py)
        • Visualization templates (Plotly visualizations.py)
        • Configuration system (config.py)
        
        SOURCE 4 - Orchestration Framework:
        • Multi-LLM routing (Claude, Gemini, AWS, OpenAI)
        • Agent specialization (4 roles with distinct expertise)
        • Workflow pipeline (10 sequential + parallel steps)
        • Data lineage tracking
        
        DATA WEAVING PRINCIPLE:
        Each insight should reference which source(s) inform it. The strength comes from 
        integrating all 4 sources into coherent, evidence-based findings.
        """
    
    @staticmethod
    def initialization_prompt() -> str:
        """Research framework initialization"""
        return AnalysisPrompts.data_sources_context() + """
        
        STEP 1: INITIALIZE DIGITAL DETOX WEAVER PROJECT
        ══════════════════════════════════════════════
        
        Design the analytical framework:
        
        1. Research Questions (grounded in Source 1 data characteristics)
           - What are the primary relationships between screen time and health?
           - Which populations show highest vulnerability?
           - What mechanisms explain the associations?
        
        2. Hypotheses (based on epidemiological patterns)
           - Screen time causes health harm through [mechanisms]
           - Adolescents are 5.5x more vulnerable than older adults
           - Recovery from digital detox follows predictable trajectories
        
        3. Statistical Methods (appropriate for Source 1 data types)
           - Trend analysis for temporal data
           - Dose-response curves for exposure-outcome relationships
           - Stratified analysis by age, SES, platform
        
        4. Confounding Variables (from Source 1 datasets)
           - Socioeconomic status (SES dataset)
           - Age and developmental stage (age stratification dataset)
           - Platform-specific factors (platform comparison dataset)
        
        5. Data Quality Checks (validation for Source 1)
           - Temporal coherence (2010-2024 trends make sense)
           - Biological plausibility (dose-response is non-linear as expected)
           - External validity (distributions match published literature)
        
        Format as structured markdown with clear methodology section.
        """
    
    @staticmethod
    def analysis_prompt(data_summary: str) -> str:
        """Comprehensive epidemiological analysis"""
        return AnalysisPrompts.data_sources_context() + f"""
        
        STEP 3: ANALYZE SOURCE 1 EPIDEMIOLOGICAL DATA
        ═════════════════════════════════════════════
        
        Conduct comprehensive epidemiological analysis on this data:
        
        {data_summary}
        
        Analyze:
        1. Screen Time Trends (2010-2024)
           - Growth rate and inflection points
           - Global variation by country
           - Statistical significance (p-values, 95% CI)
        
        2. Disease Burden Attribution
           - Attributable risk by disease type
           - Percentage of disease burden from screen time
           - Confidence intervals on estimates
        
        3. Age Vulnerability Hierarchy
           - Relative vulnerability by age group (with numbers)
           - Why adolescents are 5.5x more vulnerable
           - Developmental pathways
        
        4. Platform Comparison
           - Most harmful platforms (ranked)
           - Engagement vs health impact correlation
           - Algorithm-driven toxicity patterns
        
        5. SES Inequality Amplification
           - Health disparities by income level
           - 2.2x disparity (low vs high income)
           - Equity implications
        
        6. Causal Mechanisms
           - Temporal relationships (does exposure precede outcome?)
           - Dose-response (higher screen time = worse health)
           - Biological plausibility (mechanisms explained)
           - Reversibility (can detox improve health?)
        
        7. Effect Sizes & Confidence Intervals
           - Specific numbers with CI (e.g., "depression risk increases by 3.2x, 95% CI: 2.8-3.6")
           - Statistical significance (p-values)
           - Magnitude of public health importance
        
        For each finding: Specify which data source informs it (e.g., "Source 1: global epidemiology dataset").
        Include specific numbers, p-values, effect sizes, confidence intervals.
        Format as detailed analytical report suitable for publication.
        """
    
    @staticmethod
    def visualization_prompt(analysis: str) -> str:
        """Visualization design specifications"""
        return AnalysisPrompts.data_sources_context() + f"""
        
        STEP 4: DESIGN VISUALIZATIONS (PARALLEL)
        ════════════════════════════════════════
        
        Based on this epidemiological analysis:
        
        {analysis}
        
        Design comprehensive data visualizations:
        
        1. Chart Type Recommendations
           - Global trends: Multi-line chart (countries over time)
           - Age vulnerability: Stacked bar or violin plot (vulnerability by age)
           - Platform comparison: Bubble chart (engagement × harm × user base)
           - Mechanisms: 4-panel subplots (circadian, sleep-weight, dopamine, outcomes)
           - Detox recovery: Multi-curve plot (12-week trajectories)
        
        2. Accessibility Specifications
           - Color contrast: 4.5:1 minimum (WCAG AA)
           - Color palette: Colorblind-friendly (avoid red-green)
           - Labels: Large enough (14pt+ for axis labels)
           - Alternative text: Descriptive for all charts
        
        3. Interactive Elements
           - Dropdown filters (country, age group, platform, disease)
           - Hover tooltips (show exact values and CI)
           - Toggle switches (show/hide datasets)
           - Download buttons (export as CSV)
        
        4. Dashboard Layout (8 tabs)
           - Tab 1: Global Overview (KPI cards + main trends)
           - Tab 2: Age Analysis (vulnerability curves)
           - Tab 3: Platforms (engagement ranking)
           - Tab 4: Mechanisms (4-panel explainer)
           - Tab 5: Disease Timeline (7 disease progression curves)
           - Tab 6: SES Inequality (disparity visualization)
           - Tab 7: Detox Recovery (12-week improvement curves)
           - Tab 8: Policy Recommendations (3-phase pathway)
        
        5. Data Lineage Indicators
           - Show which Source(s) feed each visualization
           - Include data quality badges
           - Timestamp of last update
        
        Provide specific visualization recommendations with implementation rationale.
        Focus on clarity, accessibility, and insight revelation.
        """
    
    @staticmethod
    def health_insights_prompt(analysis: str) -> str:
        """Health mechanism and insights"""
        return AnalysisPrompts.data_sources_context() + f"""
        
        STEP 5: GENERATE HEALTH INSIGHTS (PARALLEL)
        ═══════════════════════════════════════════
        
        Based on this epidemiological analysis:
        
        {analysis}
        
        Synthesize health insights grounded in Source 1 data:
        
        1. Causal Mechanisms Explained
           - Circadian rhythm disruption: How blue light suppresses melatonin
           - Sleep-to-weight cascade: Sleep loss → metabolic dysfunction → obesity
           - Dopamine downregulation: Chronic overstimulation → reduced reward sensitivity
           - Social comparison toxicity: Algorithm-driven negative affect
        
        2. Age Vulnerability Pathways
           - Adolescent vulnerability (13-17): Prefrontal development, sleep needs, social sensitivity
           - Young adult vulnerability (18-24): Early dopamine dysregulation
           - Reduced vulnerability in older adults (50+): Brain maturation, sleep less sensitive
        
        3. Biological Plausibility
           - Evidence from neuroscience literature
           - Mechanistic links from screen time to health outcomes
           - Timing and dose-response curves from Source 1 data
        
        4. Reversibility & Recovery
           - 13-week detox timeline from Source 1
           - Recovery trajectories for each outcome
           - Sleep normalization, mood improvement, cognitive recovery
        
        5. SES-Mediated Inequalities
           - Why low-income populations suffer more (access to screens, less supervision, stress)
           - 2.2x disparity from Source 1 SES dataset
           - Equity implications for policy
        
        6. Platform-Specific Harms
           - TikTok algorithm toxicity patterns
           - Instagram social comparison effects
           - YouTube Shorts addiction mechanics
           - Differences in mechanistic pathways
        
        Connect to peer-reviewed research and mechanistic understanding.
        Include specific citations and evidence from Source 1 data.
        Format as 1500+ word mechanism-focused analysis.
        """
    
    @staticmethod
    def policy_prompt(health_findings: str) -> str:
        """Policy design and recommendations"""
        return AnalysisPrompts.data_sources_context() + f"""
        
        STEP 7: DESIGN POLICY RECOMMENDATIONS
        ══════════════════════════════════════
        
        Based on these health findings:
        
        {health_findings}
        
        Design evidence-based policy recommendations:
        
        1. Intervention Effectiveness Ranking (from Source 1 policy dataset)
           - Rank 8 interventions by effectiveness (%reduction in health harm)
           - Include confidence intervals
           - Consider implementation feasibility
        
        2. Mechanism-Targeted Interventions
           - For circadian disruption: Bedroom screen restrictions, blue light filters
           - For dopamine dysregulation: Usage caps, notification controls
           - For sleep loss: Education, parental controls, school policies
           - For social comparison: Algorithm accountability, content warnings
        
        3. Implementation Feasibility Assessment
           - Which interventions are realistic to implement?
           - What barriers exist? (industry lobbying, cultural norms, enforcement)
           - Who are key stakeholders? (government, schools, families, tech companies)
        
        4. Cost-Benefit Analysis
           - Cost per person for each intervention
           - Health benefits gained per cost unit
           - Cost-effectiveness ratio ($ per healthy year gained)
           - Return on investment
        
        5. Equity Implications
           - How do policies affect low vs high-income populations?
           - Can SES-specific approaches improve equity?
           - Access to interventions across groups
        
        6. 3-Phase Implementation Pathway
           - Phase 1 (Years 1-2): Foundation (education, data systems)
           - Phase 2 (Years 3-4): Implementation (rules, enforcement)
           - Phase 3 (Years 5+): Optimization (learning, scale)
        
        7. Success Metrics & Monitoring
           - Key performance indicators for each intervention
           - Data systems needed (population-level tracking)
           - Timeline for outcomes assessment
        
        Include data from Source 1 policy interventions dataset throughout.
        Provide specific numbers on effectiveness, costs, and timeline.
        """
    
    @staticmethod
    def report_prompt(analysis: str, health_findings: str, policy: str) -> str:
        """Comprehensive final report"""
        return AnalysisPrompts.data_sources_context() + f"""
        
        STEP 8: GENERATE COMPREHENSIVE FINAL REPORT
        ═════════════════════════════════════════════
        
        Synthesize all findings into comprehensive report:
        
        {analysis}
        
        Health Findings:
        {health_findings}
        
        Policy Recommendations:
        {policy}
        
        Create publication-ready report (3000+ words):
        
        1. Executive Summary (250 words)
           - Key findings with numbers
           - Main policy recommendations
           - Urgency and call to action
        
        2. Introduction
           - Screen time prevalence and trends
           - Known health impacts
           - Gaps in current understanding
           - Report objectives
        
        3. Methods
           - Data sources and integration approach
           - Analysis methodology
           - Limitations and assumptions
        
        4. Results: Data Analysis
           - Screen time trends (2010-2024)
           - Health burden attribution
           - Age vulnerabilities
           - Platform comparisons
           - Disease timelines
           - SES inequalities
        
        5. Results: Mechanism Analysis
           - Circadian disruption pathway
           - Sleep-to-weight cascade
           - Dopamine dysregulation
           - Social comparison toxicity
        
        6. Results: Recovery Analysis
           - Detox effectiveness (from 13-week timeline)
           - Recovery trajectories by outcome
           - Factors predicting successful recovery
        
        7. Policy Recommendations
           - 3-phase implementation pathway
           - Intervention effectiveness ranking
           - Cost-benefit analysis
           - Equity considerations
        
        8. Discussion
           - What do findings mean?
           - Consistency with existing literature
           - Implications for different stakeholders
           - Knowledge gaps and future research
        
        9. Conclusion
           - Summary of key messages
           - Urgency for action
           - Call to policy makers, researchers, families
        
        10. References
            - Cite 30+ peer-reviewed sources
            - Include data sources (Source 1 datasets)
        
        Format as publication-ready markdown for journal submission.
        Include specific numbers, statistics, and confidence intervals.
        Make arguments clear, evidence-based, and actionable.
        """

analysis_prompts = AnalysisPrompts()