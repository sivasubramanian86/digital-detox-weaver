"""
Data Analyst Agent – SOURCE 2 (AI-Generated Insights)

Statistical analysis specialist for Digital Detox Weaver.
Temperature: 0.3 (precise, analytical)
"""

import logging
from typing import Iterator

logger = logging.getLogger(__name__)


class DataAnalystAgent:
    """
    Analyzes SOURCE 1 epidemiological data with statistical rigor.
    Produces outputs: 01_initialization.md, 03_analysis.md
    """

    def __init__(self, llm_router):
        """
        Args:
            llm_router: LLM routing instance (handles Claude, Gemini, etc.)
        """
        self.llm_router = llm_router
        self.temperature = 0.3
        self.agent_name = "DataAnalystAgent"

    def generate_initialization(self, system_prompt: str, prompt: str) -> Iterator[str]:
        """
        Step 1: Generate research framework and initialization.
        Yields streaming text chunks.
        """
        logger.info(f"[{self.agent_name}] Generating initialization...")
        
        for chunk in self.llm_router.generate(
            prompt=prompt,
            system=system_prompt,
            temperature=self.temperature,
            streaming=True
        ):
            yield chunk

    def generate_analysis(self, system_prompt: str, prompt: str, data_summary: str) -> Iterator[str]:
        """
        Step 3: Analyze SOURCE 1 data statistically.
        """
        logger.info(f"[{self.agent_name}] Analyzing SOURCE 1 data...")
        
        full_prompt = f"{prompt}\n\nData Summary:\n{data_summary}"
        
        for chunk in self.llm_router.generate(
            prompt=full_prompt,
            system=system_prompt,
            temperature=self.temperature,
            streaming=True
        ):
            yield chunk