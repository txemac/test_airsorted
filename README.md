# test airsorted

Test for junior python developer
Company: airsorted

Text: https://github.com/txemac/test_airsorted/blob/master/TechnicalPre-InterviewTask.pdf

# AirSorted Technical Interview Task
## Notes
You are free to use your language of choice, but we would prefer you to use either Python or Ruby. There are no restrictions aside from those specified within the task description.

If you have any questions about the task, please ask b efore you start!

## Task ‐ t ime limit is ONE HOUR

Implement a method which accepts a list of booking start and end dates, along with a specific month, and returns a list of all the days within that month that aren’t already booked. You should also provide a way to test the method.

This task is intended to assess your problem solving ability, coding style, code reusability, and approach to program flow. As such please do not exceed the one hour time limit as it will usually be obvious. If you choose to implement this in Python, we would prefer that you did not use the built­in library calendar module, as it detracts from the problem solving and data structure elements of the task. If you have time to spare then you might consider the bonus question(s) after this one, or spend the time improving your existing solution.

## Input
The input data for bookings might be a list of associative arrays, or possibly a multi­dimensional list, please specify the expected format in your notes. For example, it might be a list of dictionary objects, each one containing a “start” and “end” key:
  [
    {
      “start”: “2015­06­01”,
      “end”: “2015­06­15”
    },
    {
      “start”: “2015­06­18”,
      “end”: “2015­06­27”
    }
  ]

## Output
Return a list of strings, in the format “YYYY­mm­dd” of all the dates within the specified month that are available for booking, e.g.
  [
    “2015­06­16”,
    “2015­06­17”,
    “2015­06­28”,
    “2015­06­29”,
    “2015­06­30”
  ]

## Bonus points!
In order to obtain bonus points within the allowed hour, you may consider some (or all!) of the following bonus point tasks (in order of awesome). Please remember to consider coding style, and design when considering bonus points.
  - 1. Don’t use python library’s built­in calendar module.
  - 2. Raise an exception when a date is double booked ­ the method may cease processing at this point.
  - 3. An extra method (or extend the original) that will either print out, or return a list, of all dates within the input list that are “double booked”.
  - 4. A method to print out the a  $cal style calendar for the specific month.
  - 5. A method to print out a full year $  cal output for the input data specified ­ including all bookings.

Both 3 and 4 may output in HTML format, if necessary.

# Author
Jose Bermudez
info@josebermudez.co.uk
