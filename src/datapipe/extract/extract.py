import asyncio
import os
from rnet import Impersonate, Client, Proxy, BlockingClient
from logger import logger
import logging
from tenacity import (
    before_log,
    retry,
    stop_after_attempt,
    wait_exponential,
    )


class Extractor:
    def __init__(self):
#        
#    self.proxy = os.getenv()        
#
        self.session = Client()
        self.session.update(
            impersonate=Impersonate.Firefox136
        )

        self.blocking = BlockingClient()
        self.blocking.update(
            impersonate=Impersonate.Firefox135,
            proxies=[
                #Proxy.http(self.proxy),                
            ]
        )
        logger.info("Sessions Created.")

    @retry(
        stop=stop_after_attempt(5),
        wait=wait_exponential(multiplier=1, min=3, max=10),
        before=before_log(logger=logger, log_level=logging.INFO)
    )
    def fetch_html_sync(self, url):
        logger.info(f"requresting{url}")
        resp = self.blocking.get(url)
        if resp.status != 200:
            raise Exception(resp.status)
        return resp.text()

    async def fetch_json_async(self, url):
        logger.info(f"async requesting {url}")
        resp = await self.session.get(url)
        return await resp.json()

    async def fetch_all_json(self, urls):
        tasks = [self.fetch_json_async(url) for url in urls]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        return results
