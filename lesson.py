"""
CRITICAL
ERROR
WARNING
INFO
DEBUG
"""
import logging
import logtest


logging.basicConfig(level=logging.INFO)


logger = logging.getLogger(__name__)
logger.info('from main')


