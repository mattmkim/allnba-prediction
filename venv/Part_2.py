# code assumes that dates are stored in this format : YYYY-MM-DD

import sqlite3 as sql
import calender

con = sql.connect("company.db")
c = con.cursor()

# performs left join on two tables, assuming that users matches user_id, orders table according to the date a
# user was created
c.execute("""SELECT users.users, users.created_at, exercises.exercise_completion_date
             FROM users
             LEFT JOIN exercises
             ON users.users = exercises.user_id
             ORDER BY users.created_at, exercises.exercise_completion_date""")

# if users have multiple entries, want to delete rows so that only row remaining
# for that user has the earliest
c.execute("""DELETE FROM users
             WHERE rowid NOT IN(
                SELECT min(rowid)
                FROM users
                GROUP BY users.users)""")

# now table includes every user that has signed up in order by the month
# and the earliest date they have completed an exercise. Users that have
# signed up but have not completed any exercises yet will have NULL
# in the exercise_completed_date column

# for each month, want to count all the users who have completed an exercise
# in that same month and divide by the total amount of users who have signed up
# in that month

months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]

total_results = []
for count, month in enumerate(months):
    c.execute("""SELECT 
                    (SELECT COUNT(*) 
                     FROM users 
                     WHERE strftime("%m", users.created_at)=months[count]) as TotalUsers
                    (SELECT COUNT(*) 
                     FROM users
                     WHERE strftime("%m", exercises.exercise_completion_date)=months[count]) 
                     AND strftime("%m", users.created_at)=months[count]) as ExerciseUsers""")
    result = c.fetchone()
    number_of_rows = result[0]
    total_results.append(number_of_rows)

# totalresults list contains 12 tuples, with first value in each representing
# the total amount of users that signed up that month, and second value representing
# the total amount of users that have completed anb exercise in their first month


# can use this function to print out the percentage of users that have completed an exercise in the first month of
# signing up. function will take in a number corresponding to a month
def percent_of_users(month):
    x, y = totalresults[month - 1]
    print("The 2018 " + calender.month_name[month] + " cohort has " + str(x / y) + "% of users completing an "
                                                                                   "exercise in the first month")





