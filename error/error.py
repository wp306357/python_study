# -*- coding: utf-8 -*-

import logging
logging.basicConfig(level=logging.INFO)

def foo(n):
	logging.info('n = %d' % n)
	return 10 / int(n)


foo(0)