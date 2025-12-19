from pydantic_settings import BaseSettings
from pydantic import Field
from typing import Optional
import os

class LLMConfig(BaseSettings):
    """
    Digital Detox Weaver: Multi-LLM Configuration
    
    This module implements SOURCE 4 - Orchestration Framework
    Manages routing between 4 LLM providers with automatic failover
    """
    
    # Provider Configuration
    llm_provider: str = Field(default="claude", description="Primary LLM provider")
    fallback_provider: str = Field(default="gemini", description="Fallback provider")
    
    # Claude Configuration
    claude_api_key: Optional[str] = Field(default=None)
    claude_model: str = Field(default="claude-3-5-sonnet-20241022")
    claude_max_tokens: int = Field(default=4096)
    
    # Gemini Configuration
    gemini_api_key: Optional[str] = Field(default=None)
    gemini_model: str = Field(default="gemini-2.0-flash")
    gemini_max_tokens: int = Field(default=4096)
    
    # AWS/Bedrock Configuration
    aws_access_key_id: Optional[str] = Field(default=None)
    aws_secret_access_key: Optional[str] = Field(default=None)
    aws_region: str = Field(default="us-east-1")
    aws_bedrock_model_id: str = Field(default="anthropic.claude-3-5-sonnet-20241022-v2:0")
    
    # OpenAI Configuration
    openai_api_key: Optional[str] = Field(default=None)
    openai_model: str = Field(default="gpt-4-turbo-preview")
    
    # Common Settings
    temperature: float = Field(default=0.7, ge=0.0, le=1.0)
    top_p: float = Field(default=0.95, ge=0.0, le=1.0)
    timeout: int = Field(default=300)
    retry_attempts: int = Field(default=3)
    
    # Streaming Configuration
    enable_streaming: bool = Field(default=True)
    stream_chunk_size: int = Field(default=100)
    
    # Kiro Configuration
    kiro_environment: str = Field(default="development")
    kiro_log_level: str = Field(default="INFO")
    
    class Config:
        env_file = ".env.local"
        env_file_encoding = "utf-8"
        extra = "allow"

# Initialize config
llm_config = LLMConfig()