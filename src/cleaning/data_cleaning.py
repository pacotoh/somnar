import pandas as pd
import re
import numpy as np

SLEEP_PATH = '../data/sleep.csv'
SPORT_PATH = '../data/sport.csv'
HR_PATH = '../data/heartrate_auto.csv'
HR_DAILY_PATH = '../data/heartrate_daily.csv'
HR_DT_PATH = '../data/heartrate_datetime.csv'
ACTIVITY_PATH = '../data/activity.csv'


def clean_sleep_naps() -> None:
    with open(SLEEP_PATH, 'r') as sleep:
        text = sleep.read()
        cl_text = re.sub(pattern='\".*', repl='', string=text)
    with open(SLEEP_PATH, 'w') as sleep:
        sleep.write(cl_text)


def drop_sleep_unused_fields() -> None:
    sleep_df = pd.read_csv(SLEEP_PATH)
    sleep_df.drop(['naps', 'REMTime'], axis=1).to_csv(SLEEP_PATH, index=False)


def modify_sleep_header() -> None:
    sleep_df = pd.read_csv(SLEEP_PATH)
    sleep_df.rename(columns={
        'deepSleepTime': 'deep_sleep_time',
        'shallowSleepTime': 'shallow_sleep_time',
        'wakeTime': 'wake_time'
    }, inplace=True)

    sleep_df.to_csv(SLEEP_PATH, index=False)


def modify_sport_header() -> None:
    sport_df = pd.read_csv(SPORT_PATH)
    sport_df.rename(columns={
        'startTime': 'start_time',
        'sportTime(s)': 'sport_time',
        'maxPace(/meter)': 'max_pace',
        'minPace(/meter)': 'min_pace',
        'distance(m)': 'distance',
        'avgPace(/meter)': 'avg_pace',
        'calories(kcal)': 'calories'
    }, inplace=True)

    sport_df.to_csv(SPORT_PATH, index=False)


def modify_heartrate_header() -> None:
    hr_df = pd.read_csv(HR_PATH)
    hr_df.rename(columns={
        'heartRate': 'heart_rate'
    }, inplace=True)

    hr_df.to_csv(HR_PATH, index=False)


def modify_activity_header() -> None:
    act_df = pd.read_csv(ACTIVITY_PATH)
    act_df.rename(columns={
        'runDistance': 'run_distance'
    }, inplace=True)

    act_df.to_csv(ACTIVITY_PATH, index=False)


def generate_heartrate_by_day() -> None:
    hr_df = pd.read_csv(HR_PATH)
    mean_by_date: pd.DataFrame = hr_df.groupby('date')['heart_rate'].mean()
    mean_by_date.to_csv(HR_DAILY_PATH)


def generate_heartrate_in_datetime() -> None:
    hr_df = pd.read_csv(HR_PATH)
    hr_df['datetime'] = pd.to_datetime(hr_df['date']) + pd.to_timedelta(hr_df['time'] + ':00')
    hr_df[['datetime', 'heart_rate']].to_csv(HR_DT_PATH, index=False)


def clean_zero_values(df: pd.DataFrame, cols: list, window: int = 7) -> pd.DataFrame:
    for col in cols:
        rollmean = df[col].rolling(window=window).mean()
        df[col] = df[col].replace(0, np.nan)
        df[col] = df[col].fillna(rollmean)

    return df


def clean_csv_data() -> None:
    # Sleep cleaning
    clean_sleep_naps()
    drop_sleep_unused_fields()

    # Headers cleaning
    modify_sleep_header()
    modify_sport_header()
    modify_activity_header()
    modify_heartrate_header()

    # HR csv generation
    generate_heartrate_by_day()
    generate_heartrate_in_datetime()

    # Zero values cleaning
    df_sleep = pd.read_csv(SLEEP_PATH)
    (clean_zero_values(df_sleep, ['deep_sleep_time', 'shallow_sleep_time'])
     .to_csv(SLEEP_PATH, index=False))


if __name__ == '__main__':
    clean_csv_data()
