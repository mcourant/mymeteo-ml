import numpy as np
import pandas as pd

import sys
sys.path.insert(0, 'data/')
import api

sys.path.insert(0, 'ml-logic/')
import ml

print(api.getAllData())

ml.handleData("test")