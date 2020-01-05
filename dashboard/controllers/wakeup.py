import logging
import subprocess
import sys

logger = logging.getLogger("dashboard")

def wake_pc(mac_address):
    subprocess.call(["wakeonlan", mac_address])
    logger.info(f"Sent wake on lan request to '{mac_address}'")