import pandas as pd
import re

SLEEP_PATH = '../../data/sleep.csv'
SPORT_PATH = '../../data/sport.csv'


def clean_sleep_naps() -> None:
    with open(SLEEP_PATH, 'r') as sleep:
        text = sleep.read()
        cl_text = re.sub(pattern='\".*', repl='', string=text)
    with open(SLEEP_PATH, 'w') as sleep:
        sleep.write(cl_text)


def drop_sleep_unused_fields() -> None:
    sleep_df = pd.read_csv(SLEEP_PATH)
    sleep_df.drop(['naps', 'REMTime'], axis=1).to_csv(SLEEP_PATH, index=False)


def modify_sport_header() -> None:
    sport_df = pd.read_csv(SPORT_PATH)
    sport_df.rename(columns={
        'sportTime(s)': 'sport_time',
        'maxPace(/meter)': 'max_pace',
        'minPace(/meter)': 'min_pace',
        'avgPace(/meter)': 'avg_pace',
        'calories(kcal)': 'calories'
    }, inplace=True)

    sport_df.to_csv(SPORT_PATH, index=False)


if __name__ == '__main__':
    clean_sleep_naps()
    drop_sleep_unused_fields()
    modify_sport_header()
