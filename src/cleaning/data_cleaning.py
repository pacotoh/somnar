import pandas as pd


def clean_naps() -> None:
    pass


def drop_sleep_unused_fields(df: pd.DataFrame, path: str) -> None:
    return df.drop(['naps', 'REMTime'], axis=1).to_csv(path)


if __name__ == '__main__':
    drop_sleep_unused_fields(df=pd.read_csv('../../data/sleep.csv'),
                             path='../../data/sleep.csv')
