import pandas as pd
import numpy as np


chat_id = 532569024
 # Ваш chat ID, не меняйте название переменной

def solution(sample, threshold, significance_level):
    import math
    n = len(sample)
    x_bar = sum(sample) / n
    s = math.sqrt(sum((x - x_bar) ** 2 for x in sample) / (n - 1))
    t_statistic = (x_bar - threshold) / (s / math.sqrt(n))
    t_critical = abs(stats.t.ppf(significance_level / 2, n - 1))
    p_value = 2 * (1 - stats.t.cdf(abs(t_statistic), n - 1))
    return t_statistic > t_critical, p_value
