"""
File: redis_client.py
Description: This module defines a Redis client for the chatbot application.
Dependencies:
    - redis.asyncio
"""

import redis.asyncio as redis

redis_client = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)
