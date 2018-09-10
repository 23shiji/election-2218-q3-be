from typing import Iterable
import async_calc
import model

def exists_ip(ip_addr_checksum):
  return model.check_ip(ip_addr_checksum)

def save_record(ip_addr_checksum: str, data: dict):
  model.create_record(ip_addr_checksum, data)
  async_calc.run()
