import pandas as pd
import re

SLEEP_PATH = '../data/sleep.csv'
SPORT_PATH = '../data/sport.csv'
HR_PATH = '../data/heartrate_auto.csv'
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


def clean_csv_data() -> None:
    clean_sleep_naps()
    drop_sleep_unused_fields()

    modify_sleep_header()
    modify_sport_header()
    modify_activity_header()
    modify_heartrate_header()


if __name__ == '__main__':
    clean_csv_data()
