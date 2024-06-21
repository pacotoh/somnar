import pandas as pd
import statsmodels.tsa.api as tsa
from sklearn.metrics import root_mean_squared_error


def split_train_test(df: pd.DataFrame, field: str) -> list[pd.DataFrame]:
    # TODO: Split by year or semester -> 5 months or 11 months to predict 1
    pass


# FIXME: FIX fit creation and root_mean_squared_error error
def holt_winters_grid(df: pd.DataFrame, field: str) -> list:
    holt_grid = []
    opt = ['add', 'mul']

    for i in range(2, 13):
        for t in opt:
            for s in opt:
                fit = tsa.ExponentialSmoothing(df[field], seasonal_periods=i, trend=t, seasonal=s).fit()
                fc = fit.forecast(len(df[field]))
                rmse = root_mean_squared_error(df[field], fc)
                holt_grid.append([[i, t, s], fit.bic, fit.aic, rmse])

    return holt_grid


if __name__ == '__main__':
    df_sleep = pd.read_csv('../../data/sleep.csv')
    holt_winters_grid(df_sleep, 'deep_sleep_time')
