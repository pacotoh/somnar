---------------------------------------------------
-- ACTIVITY
CREATE TABLE IF NOT EXISTS activity (
    date DATE NOT NULL,
    steps INTEGER NOT NULL,
    distance INTEGER NOT NULL,
    run_distance INTEGER NOT NULL,
    calories INTEGER NOT NULL
);


-- ACTIVITY_STAGE
-- Create activity_stage table with diary activity data
CREATE TABLE IF NOT EXISTS activity_stage (
    date DATE NOT NULL,
    start TIME NOT NULL,
    stop TIME NOT NULL,
    distance INTEGER NOT NULL,
    calories INTEGER NOT NULL,
    steps INTEGER NOT NULL
);


---------------------------------------------------
-- ACTIVITY_MINUTE
CREATE TABLE IF NOT EXISTS activity_minute (
    date DATE NOT NULL,
    time TIME NOT NULL,
    steps INTEGER NOT NULL
);


---------------------------------------------------
-- HEARTRATE_AUTO
CREATE TABLE IF NOT EXISTS heartrate_auto (
    date DATE NOT NULL,
    time TIME NOT NULL,
    heart_rate INTEGER NOT NULL
);


---------------------------------------------------
-- SPORT
CREATE TABLE IF NOT EXISTS sport (
    type INTEGER NOT NULL,
    start_time DATE NOT NULL,
    sport_time REAL NOT NULL,
    max_pace NUMERIC(10, 9) NOT NULL,
    min_pace NUMERIC(10, 9) NOT NULL,
    distance REAL NOT NULL,
    avg_pace REAL NOT NULL,
    calories REAL NOT NULL
);


---------------------------------------------------
-- SLEEP
-- NOTE: Need to preprocess the csv file
CREATE TABLE IF NOT EXISTS sleep (
    date DATE NOT NULL,
    deep_sleep_time INTEGER NOT NULL,
    shallow_sleep_time INTEGER NOT NULL,
    wake_time INTEGER NOT NULL,
    start TIMESTAMP NOT NULL,
    stop TIMESTAMP NOT NULL
);


---------------------------------------------------
-- ACTIVITY
COPY activity (date, steps, distance, run_distance, calories)
FROM '/docker-entrypoint-initdb.d/activity.csv'
DELIMITER ','
CSV HEADER;


-- ACTIVITY_STAGE
COPY activity_stage (date, start, stop, distance, calories, steps)
FROM '/docker-entrypoint-initdb.d/activity_stage.csv'
DELIMITER ','
CSV HEADER;


---------------------------------------------------
-- ACTIVITY_MINUTE
COPY activity_minute (date, time, steps)
FROM '/docker-entrypoint-initdb.d/activity_minute.csv'
DELIMITER ','
CSV HEADER;


---------------------------------------------------
-- HEARTRATE_AUTO
COPY heartrate_auto (date, time, heart_rate)
FROM '/docker-entrypoint-initdb.d/heartrate_auto.csv'
DELIMITER ','
CSV HEADER;


---------------------------------------------------
-- SPORT
COPY sport (type, start_time, sport_time, max_pace, min_pace, distance, avg_pace, calories)
FROM '/docker-entrypoint-initdb.d/sport.csv'
DELIMITER ','
CSV HEADER;


---------------------------------------------------
-- SLEEP
COPY sleep (date, deep_sleep_time, shallow_sleep_time, wake_time, start, stop)
FROM '/docker-entrypoint-initdb.d/sleep.csv'
DELIMITER ','
CSV HEADER;