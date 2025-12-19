#!/usr/bin/env python3
"""
Digital Detox Weaver: Production Launch Script
Quick deployment for production-ready dashboard
"""

import subprocess
import sys
import os
from pathlib import Path

def main():
    """Launch the Digital Detox Weaver dashboard in production mode"""
    
    print("🧵 Digital Detox Weaver - Production Launch")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not Path("app.py").exists():
        print("❌ Error: app.py not found. Please run from project root.")
        sys.exit(1)
    
    # Check if data exists
    if not Path("outputs").exists():
        print("⚠️  No AI analysis found. Run 'python kiro_main.py' first for full experience.")
    
    print("🚀 Launching production dashboard...")
    print("📊 Loading 4 data sources...")
    print("🎨 Modern dark theme enabled")
    print("🌐 Opening at http://localhost:8501")
    print("\n💡 Tip: Press Ctrl+C to stop the server")
    print("-" * 50)
    
    try:
        # Launch Streamlit with production settings
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "app.py",
            "--server.port", "8501",
            "--server.headless", "false",
            "--browser.gatherUsageStats", "false",
            "--theme.base", "dark",
            "--theme.primaryColor", "#00D4AA"
        ])
    except KeyboardInterrupt:
        print("\n\n🛑 Dashboard stopped. Thank you for using Digital Detox Weaver!")
    except Exception as e:
        print(f"\n❌ Error launching dashboard: {e}")
        print("💡 Try: pip install streamlit plotly pandas")

if __name__ == "__main__":
    main()