from taipy.gui import Gui
import pandas as pd

SLEEP_PATH = '../../data/sleep.csv'
SPORT_PATH = '../../data/sport.csv'
HR_PATH = '../../data/heartrate_auto.csv'
ACTIVITY_PATH = '../../data/activity.csv'


def get_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    df["date"] = pd.to_datetime(df["date"])
    return df


def toggle_table():
    pass


page = """
# somnAR: Time Series Health Monitor

## 🛌 Sleep
<|{sleep_df}|chart|mode=lines|x=date|y[1]=deep_sleep_time|y[2]=shallow_sleep_time|y[3]=wake_time|>
<|{sleep_df}|table|>

## 🏃 Activity
### Steps
<|{activity_df}|chart|mode=lines|x=date|y[1]=steps|>
### Distance
<|{activity_df}|chart|mode=lines|x=date|y[1]=distance|color[1]=teal|y[2]=run_distance|color[2]=coral|>
### Calories
<|{activity_df}|chart|mode=lines|x=date|y[1]=calories|color[1]=#ffed86|>
<|{activity_df}|table|>

"""

if __name__ == '__main__':
    sleep_df = get_data(SLEEP_PATH)
    activity_df = get_data(ACTIVITY_PATH)

    Gui(page).run(debug=True, watermark='', title='somnAR')
