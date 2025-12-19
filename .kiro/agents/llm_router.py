import os
import logging
from typing import Iterator, Optional
from anthropic import Anthropic as AnthropicClient
import google.generativeai as genai
# import boto3  # Optional AWS dependency
import json
from dotenv import load_dotenv

load_dotenv(".env.local")
logger = logging.getLogger(__name__)

class LLMRouter:
    """
    Digital Detox Weaver: Multi-Provider LLM Router
    
    This module implements SOURCE 4 - Orchestration Framework
    Routes requests to appropriate LLM provider with automatic failover
    Supports: Claude, Gemini, AWS Bedrock, OpenAI
    """
    
    def __init__(self):
        self.primary_provider = os.getenv("LLM_PROVIDER", "claude")
        self.fallback_provider = os.getenv("FALLBACK_PROVIDER", "gemini")
        
        logger.info(f"Initializing LLM Router: Primary={self.primary_provider}, Fallback={self.fallback_provider}")
        
        # Initialize clients
        if os.getenv("CLAUDE_API_KEY"):
            self.claude_client = AnthropicClient(api_key=os.getenv("CLAUDE_API_KEY"))
            logger.info("✓ Claude client initialized")
        
        if os.getenv("GEMINI_API_KEY"):
            genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
            logger.info("✓ Gemini client initialized")
        
        # AWS Bedrock optional
        self.bedrock_client = None
        if os.getenv("AWS_ACCESS_KEY_ID"):
            try:
                import boto3
                self.bedrock_client = boto3.client(
                    "bedrock-runtime",
                    region_name=os.getenv("AWS_REGION", "us-east-1"),
                    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
                    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
                )
                logger.info("✓ AWS Bedrock client initialized")
            except ImportError:
                logger.info("⚠️ AWS Bedrock not available (boto3 not installed)")
        
        if os.getenv("OPENAI_API_KEY"):
            logger.info("✓ OpenAI API key configured")
    
    def generate(
        self,
        prompt: str,
        system: str = "",
        temperature: float = 0.7,
        max_tokens: int = 4096,
        streaming: bool = True
    ) -> Iterator[str]:
        """
        Generate response from primary provider with fallback
        
        Args:
            prompt: User prompt
            system: System message
            temperature: Temperature setting (0-1)
            max_tokens: Maximum tokens to generate
            streaming: Enable streaming responses
        
        Yields:
            Text chunks from LLM
        """
        
        try:
            if self.primary_provider == "claude":
                yield from self._claude_generate(prompt, system, temperature, max_tokens, streaming)
            elif self.primary_provider == "gemini":
                yield from self._gemini_generate(prompt, system, temperature, max_tokens, streaming)
            elif self.primary_provider == "aws":
                yield from self._aws_generate(prompt, system, temperature, max_tokens, streaming)
            elif self.primary_provider == "openai":
                yield from self._openai_generate(prompt, system, temperature, max_tokens, streaming)
        except Exception as e:
            logger.warning(f"Primary provider ({self.primary_provider}) failed: {e}. Attempting fallback...")
            try:
                if self.fallback_provider == "gemini" or self.primary_provider != "gemini":
                    yield from self._gemini_generate(prompt, system, temperature, max_tokens, streaming)
                elif self.fallback_provider == "aws":
                    yield from self._aws_generate(prompt, system, temperature, max_tokens, streaming)
                else:
                    raise
            except Exception as fallback_error:
                logger.error(f"Fallback provider also failed: {fallback_error}")
                yield f"Error: Both primary and fallback providers failed. {str(e)}"
    
    def _claude_generate(self, prompt: str, system: str, temperature: float, max_tokens: int, streaming: bool) -> Iterator[str]:
        """Generate using Claude"""
        if streaming:
            with self.claude_client.messages.stream(
                model=os.getenv("PRIMARY_MODEL", "claude-3-5-sonnet-20241022"),
                max_tokens=max_tokens,
                temperature=temperature,
                system=system,
                messages=[{"role": "user", "content": prompt}]
            ) as stream:
                for text in stream.text_stream:
                    yield text
        else:
            response = self.claude_client.messages.create(
                model=os.getenv("PRIMARY_MODEL", "claude-3-5-sonnet-20241022"),
                max_tokens=max_tokens,
                temperature=temperature,
                system=system,
                messages=[{"role": "user", "content": prompt}]
            )
            yield response.content.text
    
    def _gemini_generate(self, prompt: str, system: str, temperature: float, max_tokens: int, streaming: bool) -> Iterator[str]:
        """Generate using Gemini"""
        model = genai.GenerativeModel(
            os.getenv("PRIMARY_MODEL", "gemini-2.0-flash-exp"),
            system_instruction=system
        )
        
        if streaming:
            response = model.generate_content(
                prompt,
                stream=True,
                generation_config=genai.types.GenerationConfig(
                    temperature=temperature,
                    max_output_tokens=max_tokens
                )
            )
            for chunk in response:
                if chunk.text:
                    yield chunk.text
        else:
            response = model.generate_content(prompt)
            yield response.text
    
    def _aws_generate(self, prompt: str, system: str, temperature: float, max_tokens: int, streaming: bool) -> Iterator[str]:
        """Generate using AWS Bedrock"""
        if not self.bedrock_client:
            logger.warning("AWS Bedrock not available. Install boto3 to use AWS.")
            yield "AWS Bedrock not configured. Please install boto3 and configure AWS credentials."
            return
            
        import json
        body = json.dumps({
            "anthropic_version": "bedrock-2023-06-01",
            "max_tokens": max_tokens,
            "temperature": temperature,
            "system": system,
            "messages": [{"role": "user", "content": prompt}]
        })
        
        if streaming:
            response = self.bedrock_client.invoke_model_with_response_stream(
                modelId=os.getenv("AWS_BEDROCK_MODEL_ID"),
                body=body
            )
            for event in response.get('body', []):
                chunk = event.get('contentBlockDelta', {}).get('delta', {})
                if 'text' in chunk:
                    yield chunk['text']
        else:
            response = self.bedrock_client.invoke_model(
                modelId=os.getenv("AWS_BEDROCK_MODEL_ID"),
                body=body
            )
            result = json.loads(response['body'].read())
            yield result['content']['text']
    
    def _openai_generate(self, prompt: str, system: str, temperature: float, max_tokens: int, streaming: bool) -> Iterator[str]:
        """Generate using OpenAI (placeholder for integration)"""
        logger.warning("OpenAI provider not yet implemented. Use Claude or Gemini.")
        yield "OpenAI provider not configured. Please use Claude or Gemini."

# Initialize router
llm_router = LLMRouter()