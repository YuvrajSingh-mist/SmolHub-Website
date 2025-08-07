---
title: "SentimentFlow"
excerpt: "Comprehensive sentiment analysis dataset with 50K labeled social media posts, comments, and reviews across multiple domains and languages.<br/><img src='/images/500x300.png'>"
collection: datasets
---

## Dataset Overview
**SentimentFlow** is a comprehensive multi-domain sentiment analysis dataset containing 50,000 expertly labeled text samples from social media, product reviews, and news comments.

### Dataset Statistics
- **Total Samples**: 50,000
- **Languages**: English, Spanish, French
- **Domains**: Social media, e-commerce, news, forums
- **Labels**: Positive, Negative, Neutral, Mixed
- **Size**: 156MB
- **Format**: JSON, CSV, Parquet

### Label Distribution
- **Positive**: 35% (17,500 samples)
- **Negative**: 30% (15,000 samples)
- **Neutral**: 25% (12,500 samples)
- **Mixed**: 10% (5,000 samples)

### Key Features
- **Multi-domain Coverage**: Diverse text sources and contexts
- **Expert Annotation**: Human-verified labels with inter-annotator agreement >0.85
- **Preprocessing Pipeline**: Cleaned, tokenized, and normalized text
- **Metadata Rich**: Timestamps, source platforms, user demographics

### Applications
- Sentiment analysis model training
- Cross-domain sentiment transfer
- Multilingual sentiment research
- Social media monitoring systems
- Brand reputation analysis

### Data Format
```json
{
  "id": "sample_001",
  "text": "This product exceeded my expectations!",
  "label": "positive",
  "domain": "ecommerce",
  "language": "en",
  "confidence": 0.95,
  "metadata": {
    "timestamp": "2024-01-15",
    "platform": "review_site",
    "rating": 5
  }
}
```
