import great_expectations as gx
from great_expectations.checkpoint.types.checkpoint_result import CheckpointResult

context: gx.DataContext = gx.get_context()


def create_checkpoint(validator, name: str):
    checkpoint = context.add_or_update_checkpoint(
        name=name,
        validator=validator,
    )

    return checkpoint.run()


def gx_sleep() -> CheckpointResult:
    val_sleep = context.sources.pandas_default.read_csv('../../data/sleep.csv')
    val_sleep.expect_table_columns_to_match_set(['date',
                                                 'deep_sleep_time',
                                                 'shallow_sleep_time',
                                                 'wake_time',
                                                 'start',
                                                 'stop'])

    [val_sleep.expect_column_values_to_not_be_null(col) for col in ['date',
                                                                    'deep_sleep_time',
                                                                    'shallow_sleep_time',
                                                                    'wake_time',
                                                                    'start',
                                                                    'stop']]

    val_sleep.expect_column_values_to_be_between(column='deep_sleep_time', min_value=0, max_value=200)
    val_sleep.expect_column_values_to_be_between(column='shallow_sleep_time', min_value=0, max_value=650)
    val_sleep.expect_column_values_to_be_between(column='wake_time', min_value=0, max_value=100)
    val_sleep.expect_column_values_to_match_strftime_format(column='date', strftime_format='%Y-%m-%d')
    val_sleep.expect_column_values_to_match_strftime_format(column='start', strftime_format='%Y-%m-%d %H:%M:%S+0000')
    val_sleep.expect_column_values_to_match_strftime_format(column='stop', strftime_format='%Y-%m-%d %H:%M:%S+0000')

    val_sleep.save_expectation_suite(discard_failed_expectations=False)
    return create_checkpoint(val_sleep, 'sleep')


def gx_activity() -> CheckpointResult:
    val_act = context.sources.pandas_default.read_csv('../../data/activity.csv')
    val_act.expect_table_columns_to_match_set(['date',
                                               'steps',
                                               'distance',
                                               'run_distance',
                                               'calories'])

    [val_act.expect_column_values_to_not_be_null(col) for col in ['date',
                                                                  'steps',
                                                                  'distance',
                                                                  'run_distance',
                                                                  'calories']]

    val_act.expect_column_values_to_match_strftime_format(column='date', strftime_format='%Y-%m-%d')
    val_act.expect_column_values_to_be_between(column='steps', min_value=0)
    val_act.expect_column_values_to_be_between(column='distance', min_value=0)
    val_act.expect_column_values_to_be_between(column='run_distance', min_value=0)
    val_act.expect_column_values_to_be_between(column='calories', min_value=0)

    val_act.save_expectation_suite(discard_failed_expectations=False)
    return create_checkpoint(val_act, 'activity')


def gx_activity_minute() -> CheckpointResult:
    val_am = context.sources.pandas_default.read_csv('../../data/activity_minute.csv')
    val_am.expect_table_columns_to_match_set(['date',
                                              'time',
                                              'steps'])

    [val_am.expect_column_values_to_not_be_null(col) for col in ['date',
                                                                 'time',
                                                                 'steps']]

    val_am.expect_column_values_to_match_strftime_format(column='date', strftime_format='%Y-%m-%d')
    val_am.expect_column_values_to_match_strftime_format(column='time', strftime_format='%H:%M')
    val_am.expect_column_values_to_be_between(column='steps', min_value=0)

    val_am.save_expectation_suite(discard_failed_expectations=False)
    return create_checkpoint(val_am, 'activity_minute')


def gx_activity_stage() -> CheckpointResult:
    val_as = context.sources.pandas_default.read_csv('../../data/activity_stage.csv')
    val_as.expect_table_columns_to_match_set(['date',
                                              'start',
                                              'stop',
                                              'distance',
                                              'calories',
                                              'steps'])

    [val_as.expect_column_values_to_not_be_null(col) for col in ['date',
                                                                 'start',
                                                                 'stop',
                                                                 'distance',
                                                                 'calories',
                                                                 'steps']]

    val_as.expect_column_values_to_match_strftime_format(column='date', strftime_format='%Y-%m-%d')
    val_as.expect_column_values_to_match_strftime_format(column='start', strftime_format='%H:%M')
    val_as.expect_column_values_to_match_strftime_format(column='stop', strftime_format='%H:%M')
    val_as.expect_column_values_to_be_between(column='distance', min_value=0, max_value=8000, mostly=0.95)
    val_as.expect_column_values_to_be_between(column='calories', min_value=0)
    val_as.expect_column_values_to_be_between(column='steps', min_value=0)

    val_as.save_expectation_suite(discard_failed_expectations=False)
    return create_checkpoint(val_as, 'activity_stage')


def gx_heartrate_auto() -> CheckpointResult:
    val_ha = context.sources.pandas_default.read_csv('../../data/heartrate_auto.csv')
    val_ha.expect_table_columns_to_match_set(['date',
                                              'time',
                                              'heart_rate'])

    [val_ha.expect_column_values_to_not_be_null(col) for col in ['date',
                                                                 'time',
                                                                 'heart_rate']]

    val_ha.expect_column_values_to_match_strftime_format(column='date', strftime_format='%Y-%m-%d')
    val_ha.expect_column_values_to_match_strftime_format(column='time', strftime_format='%H:%M')
    val_ha.expect_column_values_to_be_between(column='heart_rate', min_value=0, max_value=180, mostly=0.95)

    val_ha.save_expectation_suite(discard_failed_expectations=False)
    return create_checkpoint(val_ha, 'heartrate_auto')


def gx_heartrate_daily() -> CheckpointResult:
    val_had = context.sources.pandas_default.read_csv('../../data/heartrate_daily.csv')
    val_had.expect_table_columns_to_match_set(['date',
                                              'heart_rate'])

    [val_had.expect_column_values_to_not_be_null(col) for col in ['date',
                                                                  'heart_rate']]

    val_had.expect_column_values_to_match_strftime_format(column='date', strftime_format='%Y-%m-%d')
    val_had.expect_column_values_to_be_between(column='heart_rate', min_value=0, max_value=180, mostly=0.95)

    val_had.save_expectation_suite(discard_failed_expectations=False)
    return create_checkpoint(val_had, 'heartrate_daily')


def gx_heartrate_datetime() -> CheckpointResult:
    val_hadt = context.sources.pandas_default.read_csv('../../data/heartrate_datetime.csv')
    val_hadt.expect_table_columns_to_match_set(['datetime',
                                               'heart_rate'])

    [val_hadt.expect_column_values_to_not_be_null(col) for col in ['datetime',
                                                                   'heart_rate']]

    val_hadt.expect_column_values_to_match_strftime_format(column='datetime', strftime_format='%Y-%m-%d %H:%M:%S')
    val_hadt.expect_column_values_to_be_between(column='heart_rate', min_value=0, max_value=180, mostly=0.95)

    val_hadt.save_expectation_suite(discard_failed_expectations=False)
    return create_checkpoint(val_hadt, 'heartrate_datetime')


def gx_sport() -> CheckpointResult:
    val_sport = context.sources.pandas_default.read_csv('../../data/sport.csv')
    val_sport.expect_table_columns_to_match_set(['type',
                                                 'start_time',
                                                 'sport_time',
                                                 'max_pace',
                                                 'min_pace',
                                                 'distance',
                                                 'avg_pace',
                                                 'calories'])

    [val_sport.expect_column_values_to_not_be_null(col) for col in ['type',
                                                                    'start_time',
                                                                    'sport_time',
                                                                    'max_pace',
                                                                    'min_pace',
                                                                    'distance',
                                                                    'avg_pace',
                                                                    'calories']]

    val_sport.expect_column_distinct_values_to_contain_set(column='type', value_set=[6, 24])
    val_sport.expect_column_values_to_match_strftime_format(column='start_time',
                                                            strftime_format='%Y-%m-%d %H:%M:%S+0000')
    val_sport.expect_column_min_to_be_between(column='sport_time', min_value=0)
    val_sport.expect_column_values_to_be_between(column='max_pace', min_value=0)
    val_sport.expect_column_values_to_be_between(column='min_pace', min_value=0)
    val_sport.expect_column_values_to_be_between(column='distance', min_value=0)
    val_sport.expect_column_values_to_be_between(column='avg_pace', min_value=0)
    val_sport.expect_column_min_to_be_between(column='calories', min_value=0)

    val_sport.save_expectation_suite(discard_failed_expectations=False)
    return create_checkpoint(val_sport, 'sport')


if __name__ == '__main__':
    gx_sleep()
    gx_activity()
    gx_activity_minute()
    gx_activity_stage()

    # HR Expectations
    gx_heartrate_auto()
    gx_heartrate_daily()
    gx_heartrate_datetime()

    # Last Expectations checkpoint generates the interface
    checkpoint_result = gx_sport()
    context.view_validation_result(checkpoint_result)
