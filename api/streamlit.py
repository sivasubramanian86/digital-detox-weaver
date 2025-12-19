"""
Vercel serverless function for Digital Detox Weaver Streamlit app
"""

import os
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))

def handler(request, response):
    """Vercel serverless handler for Streamlit app"""
    
    # Set environment variables for Streamlit
    os.environ['STREAMLIT_SERVER_HEADLESS'] = 'true'
    os.environ['STREAMLIT_SERVER_PORT'] = '8501'
    os.environ['STREAMLIT_SERVER_ADDRESS'] = '0.0.0.0'
    
    # Import and run the Streamlit app
    try:
        import streamlit.web.cli as stcli
        import app
        
        # Run the main app function
        app.main()
        
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'text/html',
            },
            'body': 'Digital Detox Weaver Dashboard Running'
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
            },
            'body': f'{{"error": "Deployment error: {str(e)}"}}'
        }

# For Vercel compatibility
def main(request, response):
    return handler(request, response)