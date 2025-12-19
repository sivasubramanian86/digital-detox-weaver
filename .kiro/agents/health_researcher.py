"""
Health Researcher Agent – SOURCE 2 (AI-Generated Insights)

Public health specialist for mechanistic insights and evidence synthesis.
Temperature: 0.5 (balanced, evidence-based)
"""

import logging
from typing import Iterator

logger = logging.getLogger(__name__)


class HealthResearcherAgent:
    """
    Generates health insights, mechanisms, and comprehensive reports.
    Produces outputs: 05_health_insights.md, FINAL_REPORT.md
    """

    def __init__(self, llm_router):
        self.llm_router = llm_router
        self.temperature = 0.5
        self.agent_name = "HealthResearcherAgent"

    def generate_health_insights(self, system_prompt: str, prompt: str) -> Iterator[str]:
        """
        Step 5: Generate mechanistic pathways and health implications.
        """
        logger.info(f"[{self.agent_name}] Generating health insights...")
        
        for chunk in self.llm_router.generate(
            prompt=prompt,
            system=system_prompt,
            temperature=self.temperature,
            streaming=True
        ):
            yield chunk

    def generate_report(self, system_prompt: str, prompt: str) -> Iterator[str]:
        """
        Step 8: Generate comprehensive 3000+ word final report.
        """
        logger.info(f"[{self.agent_name}] Generating final report...")
        
        for chunk in self.llm_router.generate(
            prompt=prompt,
            system=system_prompt,
            temperature=self.temperature,
            streaming=True
        ):
            yield chunk