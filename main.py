#!/usr/bin/env
# -*- coding:utf-8 -*-

if __name__ == "__main__":
	try:
		print("Hello World")
	except KeyboardInterrupt:
		print("KeyboardInterrupt")
	except Exception as e:
		print(e)
