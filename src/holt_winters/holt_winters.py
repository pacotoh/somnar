import pandas as pd
from statsmodels.tsa.api import ExponentialSmoothing
from sklearn.metrics import root_mean_squared_error


def holt_winters_grid(df: pd.DataFrame):
    holt_grid = []
    opt = ['add', 'mul']

    for i in range(2, 13):
        for t in opt:
            for s in opt:
                fit = ExponentialSmoothing(df[0] ,seasonal_periods=i, trend=t, seasonal=s).fit()
                fc = fit.forecast(len(df[0]))
                rmse = root_mean_squared_error(df[0], fc)
                holt_grid.append([[i, t, s], fit.bic, fit.aic, rmse])

    return holt_grid


if __name__ == '__main__':
    pass