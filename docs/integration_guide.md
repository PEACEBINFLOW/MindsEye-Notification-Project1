# MindsEye Notification Integration Guide

## Overview
This guide explains how to integrate MindsEye Notification with third-party systems like SuprSend, Slack, or Postgres AI pipelines.

## Prerequisites
- Python 3.10+
- Active SMTP credentials (e.g., Gmail or SendGrid)
- MindsEye Notification repository cloned locally
- `.env` file configured with your email credentials

## Steps

### 1. Clone the Repository
```bash
git clone https://github.com/PeaceThabiwa/PEACEBINFLOW.git
cd PEACEBINFLOW
```

### 2. Set Up Environment
Rename `.env.example` to `.env` and fill in your email credentials.

### 3. Run Notification Service
```bash
python mindseye_email.py
```

### 4. Optional: Integrate with SuprSend
MindsEye can trigger SuprSend events for cross-channel delivery.  
Example pseudocode:
```python
from suprsend import SuprSend

supr_client = SuprSend(api_key="YOUR_API_KEY")
supr_client.send_notification({
    "user": "user@example.com",
    "message": "MindsEye Notification Triggered"
})
```

## Support
For further support or to contribute, contact **peace.thabiwa@sageworks.ai**.
