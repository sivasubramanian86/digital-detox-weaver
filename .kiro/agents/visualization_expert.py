"""
Visualization Expert Agent – SOURCE 2 (AI-Generated Insights)

Chart design specialist for modern, accessible data visualization.
Temperature: 0.6 (creative, design-focused)
"""

import logging
from typing import Iterator

logger = logging.getLogger(__name__)


class VisualizationExpertAgent:
    """
    Designs visualizations for SOURCE 1 data.
    Produces output: 04_visualization_design.md
    """

    def __init__(self, llm_router):
        self.llm_router = llm_router
        self.temperature = 0.6
        self.agent_name = "VisualizationExpertAgent"

    def generate_visualization_specs(self, system_prompt: str, prompt: str) -> Iterator[str]:
        """
        Step 4: Design visualization specifications for 8 dashboard tabs.
        """
        logger.info(f"[{self.agent_name}] Designing visualizations...")
        
        for chunk in self.llm_router.generate(
            prompt=prompt,
            system=system_prompt,
            temperature=self.temperature,
            streaming=True
        ):
            yield chunk