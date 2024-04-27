import great_expectations as gx

context: gx.DataContext = gx.get_context()


def create_checkpoint(validator, name: str) -> None:
    checkpoint = context.add_or_update_checkpoint(
        name=name,
        validator=validator,
    )

    checkpoint_result = checkpoint.run()
    context.view_validation_result(checkpoint_result)


def gx_sleep() -> None:
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
    create_checkpoint(val_sleep, 'sleep')


def gx_activity() -> None:
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
    create_checkpoint(val_act, 'activity')


def gx_activity_minute() -> None:
    val_am = context.sources.pandas_default.read_csv('../../data/activity_minute.csv')
    [val_am.expect_column_values_to_not_be_null(col) for col in ['date',
                                                                 'time',
                                                                 'steps']]

    val_am.expect_column_values_to_match_strftime_format(column='date', strftime_format='%Y-%m-%d')
    val_am.expect_column_values_to_match_strftime_format(column='time', strftime_format='%H:%M')
    val_am.expect_column_values_to_be_between(column='steps', min_value=0, max_value=300, mostly=0.95)

    val_am.save_expectation_suite(discard_failed_expectations=False)
    create_checkpoint(val_am, 'activity_minute')


def gx_activity_stage() -> None:
    val_as = context.sources.pandas_default.read_csv('../../data/activity_stage.csv')

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
    val_as.expect_column_values_to_be_between(column='calories', min_value=0, max_value=800, mostly=0.95)
    val_as.expect_column_values_to_be_between(column='steps', min_value=0, max_value=12000, mostly=0.95)

    val_as.save_expectation_suite(discard_failed_expectations=False)
    create_checkpoint(val_as, 'activity_stage')


def gx_heartrate_auto() -> None:
    val_ha = context.sources.pandas_default.read_csv('../../data/heartrate_auto.csv')

    [val_ha.expect_column_values_to_not_be_null(col) for col in ['date',
                                                                 'time',
                                                                 'heartRate']]

    val_ha.expect_column_values_to_match_strftime_format(column='date', strftime_format='%Y-%m-%d')
    val_ha.expect_column_values_to_match_strftime_format(column='time', strftime_format='%H:%M')
    val_ha.expect_column_values_to_be_between(column='heartRate', min_value=0, max_value=180, mostly=0.95)

    val_ha.save_expectation_suite(discard_failed_expectations=False)
    create_checkpoint(val_ha, 'heartrate_auto')


def gx_sport() -> None:
    pass


if __name__ == '__main__':
    gx_sleep()
    gx_activity()
    gx_activity_minute()
    gx_activity_stage()
    gx_heartrate_auto()
