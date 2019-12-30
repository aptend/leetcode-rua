import json
import requests
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

import sys


sns.set()

# cookie = None  # {"LEETCODE_SESSION": "xxxxxxx"}

url = 'https://leetcode.com/api/problems/algorithms/'
r = requests.get(url, cookies=cookie).json()

skimmed = {int(stat['stat']['frontend_question_id']): stat['status'] == 'ac'
           for stat in r['stat_status_pairs']}

max_id = 0
for key in sorted(skimmed.keys(), reverse=True):
    if key > 5000:
        del skimmed[key]
    else:
        max_id = key
        break

row_cnt, remaining = divmod(max_id, 100)
row_cnt += 1
size = row_cnt * 100

vector = [False] * size
for key in skimmed:
    vector[key] = skimmed[key]

data = np.reshape(vector, (row_cnt, 100))
mask = np.zeros_like(data)
mask[0, 0] = True
mask[row_cnt-1, remaining:] = True


with sns.axes_style("white"):
    f, ax = plt.subplots(figsize=(16, 9), dpi=100)
    sns.heatmap(
        data, mask=mask, ax=ax,
        center=0.6,
        linewidths=2,
        yticklabels=list(range(0, size, 100)),
        square=True,
        cbar=False,
    )

plt.show()
