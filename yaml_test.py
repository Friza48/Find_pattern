#!/usr/bin/env python3

import yaml
from yaml.loader import SafeLoader

with open('/home/iris13/code/Find_pattern/test.yaml', 'r') as f:
  data = yaml.load(f, Loader=SafeLoader)

print (data)
