#!/usr/bin/env python3

import sys

from collections import defaultdict


part1 = False

pattern = [0, 1, 0, -1]
for line in sys.stdin:
	line = line.strip()
	if not line:
		continue
	inputs = tuple(map(int, line))
	if part1:
		data = list(inputs)
		next = [0] * len(data)
		for phase in range(100):
			for x in range(len(data)):
				next[x] = 0
				for i, d in enumerate(data):
					p = pattern[((i+1)//(x+1)) % len(pattern)]
					next[x] += d * p
				next[x] = abs(next[x]) % 10
			data, next = next, data
		print(line[:20], ''.join(str(v) for v in data[:8]))
	else:
		data = []
		skip = int(line[:7])
		for i in range(10000):
			data.extend(inputs)
		assert skip > len(data) / 2
		data = data[skip:]
		next = [0] * len(data)
		for phase in range(100):
			if len(data) > 100000:
				print('phase', phase)
			next[-1] = data[-1]
			for i in range(2, len(data)+1):
				next[-i] = (data[-i] + next[-i+1])%10
			data, next = next, data
		#data = [d % 10 for d in data]
		print(line[:20], ''.join(str(v) for v in data[:8]))
