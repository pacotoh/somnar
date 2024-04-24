---------------------------------------------------
-- ACTIVITY
COPY activity (date, steps, distance, run_distance, calories)
FROM '../data/activity.csv'
DELIMITER ','
CSV HEADER;


-- ACTIVITY_STAGE
COPY activity_stage (date, start, stop, distance, calories, steps)
FROM '../data/activity_stage.csv'
DELIMITER ','
CSV HEADER;


---------------------------------------------------
-- ACTIVITY_MINUTE
COPY activity_minute (date, time, steps)
FROM '../data/activity_minute.csv'
DELIMITER ','
CSV HEADER;


---------------------------------------------------
-- HEARTRATE_AUTO
COPY heartrate_auto (date, time, heart_rate)
FROM '../data/heartrate_auto.csv'
DELIMITER ','
CSV HEADER;


---------------------------------------------------
-- SPORT
COPY sport (type, start_time, sport_time, max_pace, min_pace, distance, avg_pace, calories_kcal)
FROM '../data/sport.csv'
DELIMITER ','
CSV HEADER;


---------------------------------------------------
-- SLEEP
COPY sleep (date, deep_sleep_time, shallow_sleep_time, wake_time, start, stop)
FROM '../data/sleep.csv'
DELIMITER ','
CSV HEADER;