"""
Policy Advisor Agent – SOURCE 2 (AI-Generated Insights)

Policy design specialist for evidence-based interventions and recommendations.
Temperature: 0.7 (creative, solution-oriented)
"""

import logging
from typing import Iterator

logger = logging.getLogger(__name__)


class PolicyAdvisorAgent:
    """
    Designs evidence-based policy recommendations.
    Produces output: 06_policy_recommendations.md
    """

    def __init__(self, llm_router):
        self.llm_router = llm_router
        self.temperature = 0.7
        self.agent_name = "PolicyAdvisorAgent"

    def generate_policy_recommendations(self, system_prompt: str, prompt: str) -> Iterator[str]:
        """
        Step 7: Generate 3-phase policy pathway and recommendations.
        """
        logger.info(f"[{self.agent_name}] Generating policy recommendations...")
        
        for chunk in self.llm_router.generate(
            prompt=prompt,
            system=system_prompt,
            temperature=self.temperature,
            streaming=True
        ):
            yield chunk