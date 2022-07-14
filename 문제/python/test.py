import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from prometheus_client import Summary

word_dict={
    "apple":"사과",
    "banana":"바나나",
    "Carrot":"당근",
    "Durian":"두리안"
}

frequency_dict={
    "apple":3,
    "Banana":5,
    "Carrot":np.nan,
    "Durian":2
}

importance_dit={
    "apple":3,
    "Banana":2,
    "Carrot":1,
    "Durian":1
}

word = pd.Series(word_dict)
frequency = pd.Series(frequency_dict)
importance = pd.Series(importance_dit)

summary = pd.DataFrame({
    'word':word,
    'frequency':importance,
    'importance':importance
})

print(summary)