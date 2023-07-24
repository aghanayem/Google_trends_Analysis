import pandas as pd 
from pytrends.request import TrendReq
import matplotlib.pyplot as plt

trends = TrendReq()
trends.build_payload(kw_list = ["machine learning"])
data = trends.interest_by_region()
data = data.sort_values(by = "machine learning" , ascending= False)
print(data)
