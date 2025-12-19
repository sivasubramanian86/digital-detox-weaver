#!/usr/bin/env python3
"""
Digital Detox Weaver: Test Script
Quick test of LLM router and agent configuration
"""

import sys
from pathlib import Path

# Add .kiro to path
sys.path.append(str(Path(__file__).parent / ".kiro"))

def test_imports():
    """Test that all modules can be imported"""
    print("Testing imports...")
    
    try:
        from config.llm_config import llm_config
        print("OK LLM config imported")
        
        from config.agent_config import agent_config
        print("OK Agent config imported")
        
        from prompts.analysis_prompts import analysis_prompts
        print("OK Analysis prompts imported")
        
        from agents.llm_router import llm_router
        print("OK LLM router imported")
        
        return True
    except ImportError as e:
        print(f"FAIL Import failed: {e}")
        return False

def test_configuration():
    """Test configuration values"""
    print("\nTesting configuration...")
    
    try:
        from config.agent_config import agent_config
        
        # Test agent temperatures
        temps = agent_config.AGENT_TEMPERATURES
        print(f"OK Agent temperatures: {temps}")
        
        # Test system prompts exist
        prompts = [
            agent_config.DATA_ANALYST_SYSTEM_PROMPT,
            agent_config.VISUALIZATION_EXPERT_SYSTEM_PROMPT,
            agent_config.HEALTH_RESEARCHER_SYSTEM_PROMPT,
            agent_config.POLICY_ADVISOR_SYSTEM_PROMPT
        ]
        
        for i, prompt in enumerate(prompts, 1):
            if len(prompt) > 100:
                print(f"OK Agent {i} prompt loaded ({len(prompt)} chars)")
            else:
                print(f"FAIL Agent {i} prompt too short")
                return False
        
        return True
    except Exception as e:
        print(f"FAIL Configuration test failed: {e}")
        return False

def test_llm_router():
    """Test LLM router initialization"""
    print("\nTesting LLM router...")
    
    try:
        from agents.llm_router import llm_router
        
        # Test router attributes
        print(f"OK Primary provider: {llm_router.primary_provider}")
        print(f"OK Fallback provider: {llm_router.fallback_provider}")
        
        # Test if Claude client exists (if API key provided)
        if hasattr(llm_router, 'claude_client'):
            print("OK Claude client initialized")
        else:
            print("WARN Claude client not initialized (API key needed)")
        
        return True
    except Exception as e:
        print(f"FAIL LLM router test failed: {e}")
        return False

def test_prompts():
    """Test prompt generation"""
    print("\nTesting prompts...")
    
    try:
        from prompts.analysis_prompts import analysis_prompts
        
        # Test context generation
        context = analysis_prompts.data_sources_context()
        if len(context) > 500:
            print(f"OK Data sources context generated ({len(context)} chars)")
        else:
            print("FAIL Context too short")
            return False
        
        # Test initialization prompt
        init_prompt = analysis_prompts.initialization_prompt()
        if len(init_prompt) > 1000:
            print(f"OK Initialization prompt generated ({len(init_prompt)} chars)")
        else:
            print("FAIL Initialization prompt too short")
            return False
        
        return True
    except Exception as e:
        print(f"FAIL Prompts test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("=" * 50)
    print("DIGITAL DETOX WEAVER: KIRO TEST")
    print("=" * 50)
    
    tests = [
        test_imports,
        test_configuration,
        test_llm_router,
        test_prompts
    ]
    
    results = []
    for test in tests:
        results.append(test())
    
    print("\n" + "=" * 50)
    if all(results):
        print("SUCCESS All tests passed! System ready.")
        print("\nNext steps:")
        print("1. Add Claude API key to .env.local")
        print("2. Run: python kiro_main.py")
    else:
        print("FAIL Some tests failed. Check configuration.")
    print("=" * 50)

if __name__ == "__main__":
    main()