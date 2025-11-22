from dotenv import load_dotenv
import json

CONFIG_PATH = ""
USE_PROXY = False

def load_config(path):
  with open(path) as f:
    config = json.load(f)
  return config

def process_config(config):
  if config.get('load_env'):
    load_dotenv()
  if config.get('use_proxy'):
    USE_PROXY = True

def start():
  config = load_config(CONFIG_PATH)
  process_config(config)
  print('Finished processing the config file!')