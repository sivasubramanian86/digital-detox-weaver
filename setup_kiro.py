#!/usr/bin/env python3
"""
Digital Detox Weaver: Setup Script
Creates .env.local from template and verifies installation
"""

import os
import shutil
from pathlib import Path

def setup_environment():
    """Setup environment configuration"""
    print("Setting up Digital Detox Weaver environment...")
    
    # Copy .env.example to .env.local if it doesn't exist
    env_example = Path(".env.example")
    env_local = Path(".env.local")
    
    if env_example.exists() and not env_local.exists():
        shutil.copy(env_example, env_local)
        print(f"Created {env_local} from template")
        print("Please edit .env.local and add your Claude API key")
        print("   Get your key from: https://console.anthropic.com")
    elif env_local.exists():
        print(f"{env_local} already exists")
    else:
        print(f"{env_example} not found")
        return False
    
    return True

def verify_structure():
    """Verify directory structure"""
    print("\nVerifying directory structure...")
    
    required_dirs = [
        ".kiro/config",
        ".kiro/agents", 
        ".kiro/prompts",
        ".kiro/logs",
        "outputs",
        "cache",
        "archives"
    ]
    
    for dir_path in required_dirs:
        path = Path(dir_path)
        if path.exists():
            print(f"OK {dir_path}")
        else:
            path.mkdir(parents=True, exist_ok=True)
            print(f"Created {dir_path}")
    
    return True

def verify_files():
    """Verify required files exist"""
    print("\nVerifying required files...")
    
    required_files = [
        ".env.example",
        "requirements-kiro.txt",
        ".kiro/config/llm_config.py",
        ".kiro/config/agent_config.py", 
        ".kiro/config/workflow_config.yaml",
        ".kiro/agents/llm_router.py",
        ".kiro/prompts/analysis_prompts.py",
        "kiro_main.py"
    ]
    
    all_exist = True
    for file_path in required_files:
        path = Path(file_path)
        if path.exists():
            size = path.stat().st_size
            print(f"OK {file_path} ({size} bytes)")
        else:
            print(f"MISSING {file_path}")
            all_exist = False
    
    return all_exist

def main():
    """Main setup function"""
    print("=" * 60)
    print("DIGITAL DETOX WEAVER: SETUP")
    print("=" * 60)
    
    success = True
    success &= setup_environment()
    success &= verify_structure() 
    success &= verify_files()
    
    print("\n" + "=" * 60)
    if success:
        print("Setup complete! Next steps:")
        print("1. Edit .env.local and add your Claude API key")
        print("2. Install dependencies: pip install -r requirements-kiro.txt")
        print("3. Run orchestrator: python kiro_main.py")
        print("4. Run dashboard: streamlit run app.py")
    else:
        print("Setup incomplete. Please check missing files.")
    print("=" * 60)

if __name__ == "__main__":
    main()