#!/bin/bash
# Railway deployment script
echo "🚀 Deploying to Railway..."

# Install Railway CLI
npm install -g @railway/cli

# Login and deploy
railway login
railway link
railway up

echo "✅ Deployed! Check Railway dashboard for URL"