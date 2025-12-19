#!/bin/bash
# Fix Cloud Run deployment with API key

echo "🔧 Updating Cloud Run service with GEMINI_API_KEY..."

# Update the existing service with environment variable
gcloud run services update digital-detox-weaver \
  --region us-central1 \
  --set-env-vars GEMINI_API_KEY=YOUR_ACTUAL_GEMINI_API_KEY_HERE

echo "✅ Service updated! Check: https://digital-detox-weaver-638140367111.us-central1.run.app/"