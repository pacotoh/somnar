import pandas as pd
import re
import sys


def clean_naps(file_path: str) -> None:
    with open(file_path, 'r') as sleep:
        text = sleep.read()
        cl_text = re.sub(pattern='\".*', repl='', string=text)
    with open(file_path, 'w') as sleep:
        sleep.write(cl_text)


def drop_sleep_unused_fields(df: pd.DataFrame, path: str) -> None:
    return df.drop(['naps', 'REMTime'], axis=1).to_csv(path, index=False)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        sleep_path = sys.argv[1]
        clean_naps(file_path=sleep_path)
        df_sleep = pd.read_csv(sleep_path)
        drop_sleep_unused_fields(df_sleep, sleep_path)
    else:
        print("ERROR: No arguments provided")
