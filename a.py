import pandas as pd
import numpy as np
import time


now = time.time()

df = pd.read_parquet("/data/4/9177/files/10070/ieee_cis_fraud_detection.parquet")

then = time.time()


print((then-now)*1000)



