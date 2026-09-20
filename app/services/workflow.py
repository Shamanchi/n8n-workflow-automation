import feedparser
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from loguru import logger
from app.core.config import settings


class WorkflowManager:
    def __init__(self):
        self.scheduler = AsyncIOScheduler()
    
    async def start(self):
        logger.info('Starting workflow manager...')
        # Add RSS feed jobs
        for feed_url in settings.rss_feeds:
            self.scheduler.add_job(
                self.process_feed,
                'interval',
                minutes=15,
                args=[feed_url]
            )
        self.scheduler.start()
    
    async def process_feed(self, feed_url: str):
        logger.info(f'Processing feed: {feed_url}')
        feed = feedparser.parse(feed_url)
        for entry in feed.entries[:5]:
            logger.info(f'New entry: {entry.title}')
            # Send to Telegram, n8n, etc.
    
    async def stop(self):
        self.scheduler.shutdown()
        logger.info('Workflow manager stopped')