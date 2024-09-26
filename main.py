#!/usr/bin/env
# -*- coding:utf-8 -*-

import argparse
from time import sleep

def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", type=str, default="single")
    return parser.parse_args()


if __name__ == "__main__":
    try:
        args = arg_parser()
        if args.type == "single":
             print("Hello World")
        elif args.type == "loop":
            while True:
                sleep(1)
                print("Hello World")
        else:
            print("Invalid type")
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
    except Exception as e:
        print(e)
