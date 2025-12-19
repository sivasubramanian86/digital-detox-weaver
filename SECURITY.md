# Security Policy

## 🔒 Digital Detox Weaver Security Guidelines

### Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## 🚨 Security Best Practices

### API Key Management
- **NEVER** commit API keys to version control
- Use `.env.local` for local development (ignored by git)
- Use environment variables in production
- Rotate API keys regularly

### Environment Configuration
```bash
# Copy template and add your keys
cp .env.example .env.local

# Edit .env.local with your actual API keys
# This file is automatically ignored by git
```

### Production Deployment
- Set environment variables in your deployment platform
- Use secrets management services (AWS Secrets Manager, etc.)
- Enable HTTPS/TLS for all endpoints
- Implement rate limiting

### Supported API Providers
- **Claude**: Anthropic API (recommended)
- **Gemini**: Google AI API
- **AWS Bedrock**: AWS managed AI services
- **OpenAI**: OpenAI API (planned)

## 🛡️ Security Features

### Built-in Protections
- ✅ Environment variable isolation
- ✅ No hardcoded credentials
- ✅ Automatic failover between providers
- ✅ Request timeout limits
- ✅ Error handling without credential exposure

### Data Privacy
- No user data stored permanently
- Generated reports contain synthetic data only
- API keys never logged or exposed
- Streaming responses don't persist

## 🚨 Reporting a Vulnerability

### How to Report
1. **DO NOT** create public issues for security vulnerabilities
2. Email security concerns to: [your-email@domain.com]
3. Include detailed description and reproduction steps
4. Allow 48 hours for initial response

### What to Expect
- **Acknowledgment**: Within 48 hours
- **Assessment**: Within 1 week
- **Resolution**: Based on severity (1-30 days)
- **Disclosure**: Coordinated disclosure after fix

### Severity Levels
- **Critical**: Immediate attention (24 hours)
- **High**: 1 week resolution
- **Medium**: 2 weeks resolution
- **Low**: Next release cycle

## 🔧 Security Configuration

### Required Environment Variables
```bash
# Primary LLM provider
LLM_PROVIDER=claude  # or gemini, aws, openai

# API Keys (choose your provider)
CLAUDE_API_KEY=your-claude-key-here
GEMINI_API_KEY=your-gemini-key-here
AWS_ACCESS_KEY_ID=your-aws-key-here
AWS_SECRET_ACCESS_KEY=your-aws-secret-here
OPENAI_API_KEY=your-openai-key-here
```

### Security Headers (Production)
```python
# Add to your deployment
SECURITY_HEADERS = {
    'X-Content-Type-Options': 'nosniff',
    'X-Frame-Options': 'DENY',
    'X-XSS-Protection': '1; mode=block',
    'Strict-Transport-Security': 'max-age=31536000; includeSubDomains'
}
```

## 📋 Security Checklist

### Before Deployment
- [ ] All API keys in environment variables
- [ ] `.env.local` not committed to git
- [ ] HTTPS enabled
- [ ] Rate limiting configured
- [ ] Error messages don't expose internals
- [ ] Dependencies updated to latest versions

### Regular Maintenance
- [ ] Rotate API keys quarterly
- [ ] Update dependencies monthly
- [ ] Review access logs
- [ ] Monitor for unusual API usage
- [ ] Backup configuration securely

## 🔍 Security Audit

Last security audit: **January 2025**
Next scheduled audit: **April 2025**

### Audit Scope
- API key management
- Environment configuration
- Dependency vulnerabilities
- Code injection prevention
- Data privacy compliance

## 📞 Contact

For security-related questions:
- **General**: Create an issue (non-sensitive only)
- **Vulnerabilities**: [your-email@domain.com]
- **Documentation**: Update this file via PR

---

**Remember**: Security is everyone's responsibility. When in doubt, ask!