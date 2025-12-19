# 🚀 Secure Deployment Guide

## 🔒 Environment Variables Setup

### Local Development
```bash
# Copy template
cp .env.example .env.local

# Edit .env.local with your API keys
GEMINI_API_KEY=your-actual-gemini-key
CLAUDE_API_KEY=your-actual-claude-key
```

### Production Deployment

#### Vercel
```bash
# Set environment variables in Vercel dashboard
vercel env add GEMINI_API_KEY
vercel env add CLAUDE_API_KEY
```

#### Google Cloud Run
```bash
gcloud run services update digital-detox-weaver \
  --set-env-vars GEMINI_API_KEY=your-key,CLAUDE_API_KEY=your-key
```

#### AWS Amplify
```bash
# Set in AWS Amplify Console > Environment Variables
GEMINI_API_KEY=your-key
CLAUDE_API_KEY=your-key
```

## 🛡️ Security Checklist

- [ ] API keys in environment variables only
- [ ] `.env.local` gitignored
- [ ] No hardcoded credentials in code
- [ ] HTTPS enabled in production
- [ ] Rate limiting configured
- [ ] Error messages don't expose internals

## 📋 Quick Deploy Commands

### Vercel (Recommended)
```bash
npm install -g vercel
vercel login
vercel --prod
```

### Docker
```bash
docker build -t digital-detox-weaver .
docker run -p 8501:8501 \
  -e GEMINI_API_KEY=your-key \
  digital-detox-weaver
```

## 🔧 Configuration

All configuration is handled through environment variables. See `.env.example` for the complete list of supported variables.

## 📞 Support

For deployment issues, check the main README.md or create an issue.