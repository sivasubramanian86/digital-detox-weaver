"""
Simple test to check what's happening with the app
"""
import os
import sys

print("=== ENVIRONMENT TEST ===")
print(f"Python version: {sys.version}")
print(f"GEMINI_API_KEY present: {'Yes' if os.getenv('GEMINI_API_KEY') else 'No'}")

try:
    import streamlit as st
    print("[OK] Streamlit imported successfully")
except Exception as e:
    print(f"[ERROR] Streamlit import failed: {e}")

try:
    import pandas as pd
    print("[OK] Pandas imported successfully")
except Exception as e:
    print(f"[ERROR] Pandas import failed: {e}")

try:
    import plotly.express as px
    print("[OK] Plotly imported successfully")
except Exception as e:
    print(f"[ERROR] Plotly import failed: {e}")

try:
    from data_generators import get_all_data
    print("[OK] Data generators imported successfully")
    
    # Test data generation
    data = get_all_data()
    print(f"[OK] Data generated successfully: {len(data)} datasets")
    for name, df in data.items():
        print(f"  - {name}: {len(df)} records")
        
except Exception as e:
    print(f"[ERROR] Data generation failed: {e}")
    import traceback
    traceback.print_exc()

print("=== TEST COMPLETE ===")