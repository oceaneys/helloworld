#!/usr/bin/env
# -*- coding:utf-8 -*-

import argparse
from time import sleep
import logging

logger = logging.getLogger(__name__)

def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", type=str, default="single")
    return parser.parse_args()

def setup_logging():
    logging.basicConfig(filename='output.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    logger.setLevel(logging.INFO)

if __name__ == "__main__":
    try:
        args = arg_parser()
        setup_logging()
        if args.type == "single":
             print("Hello World")
             logger.info("output type: single")
        elif args.type == "loop":
            logger.info("output type: loop")
            while True:
                sleep(1)
                print("Hello World")
        else:
            print("Invalid type")
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        logger.info("KeyboardInterrupt")
    except Exception as e:
        print(e)
