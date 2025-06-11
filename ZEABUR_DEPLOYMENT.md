# TRAVIA v2.0 - Zeabur Deployment Guide

This guide will help you deploy your TRAVIA travel planner application to Zeabur.com.

## Prerequisites

1. **Zeabur Account**: Sign up at [zeabur.com](https://zeabur.com)
2. **GitHub Repository**: Your code should be in a GitHub repository
3. **Supabase Database**: Your PostgreSQL database is already set up

## Deployment Steps

### 1. Prepare Your Repository

Make sure your repository contains all the necessary files:

```
├── app.py                 # Production entry point
├── main.py               # FastAPI application
├── config.py             # Configuration settings
├── requirements.txt      # Python dependencies
├── Dockerfile           # Container configuration
├── zeabur.json          # Zeabur deployment config
├── .dockerignore        # Docker ignore file
├── services/            # Service modules
│   └── recommendation_service.py
└── models/              # Data models
```

### 2. Configure Environment Variables

In your Zeabur dashboard, set the following environment variables:

**Required Variables:**
```
DATABASE_URL = postgresql://postgres.cqcsgwlskhuylgbqegnz:traviaSupabase@aws-0-eu-central-1.pooler.supabase.com:5432/postgres
ENVIRONMENT = production
PORT = 8000
HOST = 0.0.0.0
```

**Optional Variables:**
```
LOG_LEVEL = info
DB_MIN_SIZE = 5
DB_MAX_SIZE = 20
ALLOWED_ORIGINS = *
```

### 3. Deploy to Zeabur

1. **Connect Repository**:
   - Go to your Zeabur dashboard
   - Click "New Project"
   - Connect your GitHub repository

2. **Configure Service**:
   - Zeabur will automatically detect your Dockerfile
   - The `zeabur.json` file will provide additional configuration
   - Set your environment variables in the dashboard

3. **Deploy**:
   - Click "Deploy"
   - Zeabur will build your Docker container and deploy it
   - You'll get a public URL for your API

### 4. Verify Deployment

After deployment, test your API:

1. **Health Check**: `GET https://your-app.zeabur.app/health`
2. **API Documentation**: `https://your-app.zeabur.app/docs`
3. **Root Endpoint**: `https://your-app.zeabur.app/`

## Configuration Details

### Environment Variables Explained

| Variable | Description | Default |
|----------|-------------|---------|
| `DATABASE_URL` | Your Supabase PostgreSQL connection string | Required |
| `ENVIRONMENT` | Deployment environment (production/development) | production |
| `PORT` | Port number for the application | 8000 |
| `HOST` | Host address to bind to | 0.0.0.0 |
| `LOG_LEVEL` | Logging level (debug/info/warning/error) | info |
| `DB_MIN_SIZE` | Minimum database pool size | 5 |
| `DB_MAX_SIZE` | Maximum database pool size | 20 |
| `ALLOWED_ORIGINS` | CORS allowed origins (comma-separated or *) | * |

### Resource Configuration

The `zeabur.json` file configures:
- **Memory**: 1 GB
- **CPU**: 0.5 cores
- **Health Check**: `/health` endpoint
- **Port**: 8000

## Troubleshooting

### Common Issues

1. **Database Connection Errors**:
   - Verify your `DATABASE_URL` is correct
   - Check Supabase database is accessible
   - Ensure connection pool settings are appropriate

2. **Build Failures**:
   - Check Dockerfile syntax
   - Verify all dependencies in requirements.txt
   - Review build logs in Zeabur dashboard

3. **Runtime Errors**:
   - Check application logs in Zeabur dashboard
   - Verify environment variables are set correctly
   - Test endpoints manually

### Log Monitoring

Access logs through the Zeabur dashboard:
1. Go to your project
2. Click on your service
3. View "Logs" tab for real-time monitoring

## API Endpoints

Your deployed API will have these main endpoints:

- `GET /` - Root endpoint
- `GET /health` - Health check
- `GET /docs` - API documentation
- `POST /users` - Create user
- `GET /locations` - Get available locations
- `POST /users/{user_id}/itinerary` - Generate travel itinerary
- `POST /users/{user_id}/feedback` - Submit user feedback

## Security Considerations

1. **Environment Variables**: Never commit sensitive data to your repository
2. **CORS**: Configure `ALLOWED_ORIGINS` appropriately for production
3. **Database**: Use connection pooling for better performance
4. **Logging**: Set appropriate log levels for production

## Next Steps

After successful deployment:

1. **Test all endpoints** using the interactive docs at `/docs`
2. **Monitor performance** through Zeabur dashboard
3. **Set up monitoring** and alerts if needed
4. **Configure custom domain** if required
5. **Integrate with your Flutter mobile app**

## Support

For issues with:
- **Zeabur Platform**: Contact Zeabur support
- **Application Code**: Check application logs and debug locally first
- **Database**: Verify Supabase connection and queries

Your TRAVIA travel planner is now ready for production use on Zeabur! 🚀 