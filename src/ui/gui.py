from taipy.gui import Gui
import pandas as pd


def get_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    df["date"] = pd.to_datetime(df["date"])
    return df


page = """
# somnAR: Time Series Health Monitor

## 😪 Sleep
<|{dataset}|chart|mode=lines|x=date|y[1]=deep_sleep_time|y[2]=shallow_sleep_time|y[3]=wake_time|>
<|{dataset}|table|>

"""

if __name__ == '__main__':
    path_to_csv = '../../data/sleep.csv'
    dataset = get_data(path_to_csv)

    Gui(page).run(debug=True, watermark='')
