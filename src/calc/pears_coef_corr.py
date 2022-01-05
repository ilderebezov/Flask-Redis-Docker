from scipy.stats import pearsonr


def pearson_corr_coef(x, y):
    p_c_c, p_value = pearsonr(x, y)
    return p_c_c, p_value
