import numpy as np
from sklearn import metrics

vy = [0, 0, 0, 0, 0, 1, 1, 1, 1]
vh = [0.1, 0.2, 0.3, 0.4, 0.5, 0.3, 0.6, 0.7, 0.5]

auc = 0
nm = 0
for i in range(len(vy)):
  for j in range(len(vy)):
    if vy[i] == 1 and vy[j] == 0:
      nm += 1
      if vh[i] > vh[j]:
        auc += 1.0
      elif vh[i] == vh[j]:
        auc += 0.5
auc /= nm
print(auc)
# 0.85

y = np.array(vy)
h = np.array(vh)
fpr, tpr, thresholds = metrics.roc_curve(y, h, pos_label=1)
print(metrics.auc(fpr, tpr))
# 0.85
