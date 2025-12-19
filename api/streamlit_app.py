"""
Streamlit app wrapper for Vercel deployment
"""
import os
import sys
from pathlib import Path

# Add parent directory to Python path
parent_dir = Path(__file__).parent.parent
sys.path.insert(0, str(parent_dir))

def handler(request):
    """Vercel handler for Streamlit app"""
    
    # Set Streamlit configuration
    os.environ.update({
        'STREAMLIT_SERVER_HEADLESS': 'true',
        'STREAMLIT_SERVER_PORT': '8080',
        'STREAMLIT_SERVER_ADDRESS': '0.0.0.0',
        'STREAMLIT_BROWSER_GATHER_USAGE_STATS': 'false'
    })
    
    try:
        # Import and run the main app
        import streamlit as st
        from data_generators import get_all_data
        
        # Simple data display without heavy dependencies
        st.set_page_config(
            page_title="Digital Detox Weaver",
            page_icon="🧵",
            layout="wide"
        )
        
        st.title("🧵 Digital Detox Weaver")
        st.markdown("**Production-Ready Health Analytics Platform**")
        
        # Load and display basic data
        try:
            data = get_all_data()
            
            st.header("📊 Data Overview")
            for name, df in data.items():
                with st.expander(f"{name.replace('_', ' ').title()} ({len(df)} records)"):
                    st.dataframe(df.head())
            
            st.success("✅ Full dashboard available locally - run `streamlit run app.py`")
            
        except Exception as e:
            st.error(f"Data loading error: {e}")
            st.info("📱 This is a simplified version. Run locally for full features.")
        
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'text/html'},
            'body': 'Streamlit app running'
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'application/json'},
            'body': f'{{"error": "{str(e)}"}}'
        }