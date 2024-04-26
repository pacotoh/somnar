import great_expectations as gx
import pandas as pd


def create_checkpoint(context: gx.DataContext, validator: pd.DataFrame, name: str) -> None:
    checkpoint = context.add_or_update_checkpoint(
        name=name,
        validator=validator,
    )

    checkpoint_result = checkpoint.run()
    context.view_validation_result(checkpoint_result)


def gx_sleep(context: gx.DataContext) -> None:
    val_sleep = context.sources.pandas_default.read_csv('../../data/sleep.csv')
    val_sleep.expect_table_columns_to_match_set(['date',
                                                 'deepSleepTime',
                                                 'shallowSleepTime',
                                                 'wakeTime',
                                                 'start',
                                                 'stop'])

    [val_sleep.expect_column_values_to_not_be_null(col) for col in ['date',
                                                                    'deepSleepTime',
                                                                    'shallowSleepTime',
                                                                    'wakeTime',
                                                                    'start',
                                                                    'stop']]

    val_sleep.expect_column_values_to_be_between(column='deepSleepTime', min_value=0, max_value=200)
    val_sleep.expect_column_values_to_be_between(column='shallowSleepTime', min_value=0, max_value=650)
    val_sleep.expect_column_values_to_be_between(column='wakeTime', min_value=0, max_value=100)
    val_sleep.expect_column_values_to_match_strftime_format(column='date', strftime_format='%Y-%m-%d')
    val_sleep.expect_column_values_to_match_strftime_format(column='start', strftime_format='%Y-%m-%d %H:%M:%S+0000')
    val_sleep.expect_column_values_to_match_strftime_format(column='stop', strftime_format='%Y-%m-%d %H:%M:%S+0000')

    val_sleep.save_expectation_suite(discard_failed_expectations=False)

    create_checkpoint(context, val_sleep, 'sleep')


def gx_activity(context: gx.DataContext) -> None:
    val_act = context.sources.pandas_default.read_csv('../../data/activity.csv')
    [val_act.expect_column_values_to_not_be_null(col) for col in ['date',
                                                                  'steps',
                                                                  'distance',
                                                                  'runDistance',
                                                                  'calories']]

    val_act.expect_column_values_to_match_strftime_format(column='date', strftime_format='%Y-%m-%d')
    val_act.expect_column_values_to_be_between(column='steps', min_value=0, max_value=20000, mostly=0.95)
    val_act.expect_column_values_to_be_between(column='distance', min_value=0, max_value=15000, mostly=0.95)
    val_act.expect_column_values_to_be_between(column='runDistance', min_value=0, max_value=12000)
    val_act.expect_column_values_to_be_between(column='calories', min_value=0, max_value=1500, mostly=0.95)

    val_act.save_expectation_suite(discard_failed_expectations=False)

    create_checkpoint(context, val_act, 'activity')


def gx_activity_minute(context: gx.DataContext) -> None:
    pass


def gx_activity_stage(context: gx.DataContext) -> None:
    pass


def gx_heartrate_auto(context: gx.DataContext) -> None:
    pass


def gx_sport(context: gx.DataContext) -> None:
    pass


if __name__ == '__main__':
    csv_context = gx.get_context()
    gx_sleep(csv_context)
    gx_activity(csv_context)
