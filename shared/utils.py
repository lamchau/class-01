#!/usr/bin/env python
import os
import logging

def create_logger(logger_name, log_level=logging.DEBUG):
	console = logging.StreamHandler()
	console.setFormatter(get_formatter())
	if os.path.isfile(logger_name):
		filename = os.path.basename(logger_name)
		filename = os.path.splitext(filename)[0]
		if len(filename):
			logger_name = filename
	log = logging.getLogger(logger_name)
	# DEBUG, INFO, WARNING, ERROR, CRITICAL
	log.setLevel(log_level)
	log.addHandler(console)
	return log

def get_formatter():
	return logging.Formatter('%(asctime)s [%(levelname)-4s] %(funcName)s - %(message)s')

def array2str(array, index, array_name="array", mark=False, spacing=None):
	if spacing is None:
		spacing = 0
	format_array_name = "%%%ds" % spacing
	array_name = format_array_name % array_name
	format_map = {}
	format_map.setdefault("array_name", array_name)
	format_map.setdefault("mark", " *" if mark else "")
	format_map.setdefault("index", index)
	format_map.setdefault("value", str(array[index]))
	return "%(array_name)s[%(index)d] = %(value)s%(mark)s" % format_map

def read_integer_file(path):
	integers = []
	if not os.path.isfile(path):
		raise IOError("Invalid file: %s" % path)
	with open(path, "r") as f:
		for line in f.readlines():
			try:
				value = int(line.strip())
				integers.append(value)
			except exceptions.ValueError:
				pass
	return integers

def read_graph_file(path):
	graph = {}
	if not os.path.isfile(path):
		raise IOError("Invalid file: %s" % path)
	with open(path, "r") as f:
		for line in f.readlines():
			try:
				print value.split(" ")
			except exceptions.ValueError:
				pass
	return graph