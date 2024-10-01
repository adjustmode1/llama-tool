import argparse
from utils import load_config

def main():
  parser = argparse.ArgumentParser(description='Generate dataset for finetune LLMs instruction')
  parser.add_argument('--config', action='store_const', default='configs/data.yml', help='Config file')

  args = parser.parse_args()

  config = load_config.load_config(args.config)
  print(config)


if __name__ == '__main__':
    main()