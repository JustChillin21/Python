--CREATE OR REPLACE VIEW bbase.work_hours AS 
 UPDATE bbase.timesheet SET work_hours=( 
    DATE_PART('hours',(COALESCE(age(timesheet.wrap_time, timesheet.start_time) + age(timesheet.start_time, COALESCE(timesheet.travel_start, COALESCE(timesheet.start_time, timesheet.ndb_time))) + age(COALESCE(timesheet.travel_wrap, timesheet.wrap_time), timesheet.wrap_time)
    -- WITH MEAL PERIOD
- age(timesheet.meal1_end, timesheet.meal1_start), age(timesheet.wrap_time, timesheet.start_time) + age(timesheet.start_time, COALESCE(timesheet.travel_start, COALESCE(timesheet.start_time, timesheet.ndb_time))) + age(COALESCE(timesheet.travel_wrap, timesheet.wrap_time), timesheet.wrap_time))))*60
    +DATE_PART('minutes',(COALESCE(age(timesheet.wrap_time, timesheet.start_time) + age(timesheet.start_time, COALESCE(timesheet.travel_start, COALESCE(timesheet.start_time, timesheet.ndb_time))) + age(COALESCE(timesheet.travel_wrap, timesheet.wrap_time), timesheet.wrap_time) 
--WITHOUT MEAL PERIOD
- age(timesheet.meal1_end, timesheet.meal1_start), age(timesheet.wrap_time, timesheet.start_time) + age(timesheet.start_time, COALESCE(timesheet.travel_start, COALESCE(timesheet.start_time, timesheet.ndb_time))) + age(COALESCE(timesheet.travel_wrap, timesheet.wrap_time), timesheet.wrap_time))))
 --  FROM bbase.timesheet;
 )/60
;
SELECT bbase.timesheet.work_hours FROM bbase.timesheet;