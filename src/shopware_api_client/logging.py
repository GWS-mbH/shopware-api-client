import logging

logger = logging.getLogger("shopware6_api")
logstream = logging.StreamHandler()
logstream.setFormatter(logging.Formatter("%(asctime)s [%(name)s] [%(levelname)s] %(message)s"))
logger.addHandler(logstream)
logger.setLevel(logging.INFO)
