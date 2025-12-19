#!/usr/bin/env python3
"""
Simple dashboard runner that handles encoding issues
"""

import subprocess
import sys
import os

def run_dashboard():
    """Run the Streamlit dashboard with proper encoding"""
    try:
        # Set environment variables for proper encoding
        env = os.environ.copy()
        env['PYTHONIOENCODING'] = 'utf-8'
        
        # Run streamlit
        cmd = [sys.executable, '-m', 'streamlit', 'run', 'app.py', '--server.port=8501']
        
        print("Starting Digital Detox Weaver Dashboard...")
        print("Dashboard will be available at: http://localhost:8501")
        print("Press Ctrl+C to stop the server")
        
        subprocess.run(cmd, env=env)
        
    except KeyboardInterrupt:
        print("\nDashboard stopped.")
    except Exception as e:
        print(f"Error starting dashboard: {e}")
        print("Try running manually: python -m streamlit run app.py")

if __name__ == "__main__":
    run_dashboard()