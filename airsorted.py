from datetime import date
import htmlCalendar

__author__ = 'josebermudez'


bookings = [
    {
        "start": "2015-06-01",
        "end": "2015-06-15"
    },
    {
        "start": "2015-06-19",
        "end": "2015-06-27"
    }
]

year = [
    {
        "start": "2015-06-01",
        "end": "2015-06-15"
    },
    {
        "start": "2015-06-13",
        "end": "2015-06-27"
    },
    {
        "start": "2015-02-01",
        "end": "2015-02-15"
    },
    {
        "start": "2015-02-18",
        "end": "2015-02-27"
    },
    {
        "start": "2015-12-01",
        "end": "2015-12-15"
    },
    {
        "start": "2015-12-18",
        "end": "2015-12-27"
    }
]


def __read_bookings(bookings):
    """
    Read a booking list
    :param bookings: list
    :return: list with all days between start and end
    """
    booked = set()
    double = set()

    for item in bookings:
        year, month, day = __get_y_m_d(item['start'])
        date1 = date(year, month, day).toordinal()

        year, month, day = __get_y_m_d(item['end'])
        date2 = date(year, month, day).toordinal()

        for d in range(date1, date2+1):
            if d not in booked:
                booked.add(d)
            else:
                double.add(d)

    return booked, double


def __get_y_m_d(string_date):
    """
    Return Year, Month and Day from a string YYYY-MM-DD
    :param string_date: string
    :return: year, month, day
    """
    return int(string_date[:4]), int(string_date[5:7]), int(string_date[8:])


def __get_first_last(year, month):
    """
    Return first day and last day in a month (cardinal)
    :param year: year
    :param month: month
    :return: first, last
    """
    first = date(year, month, 1).toordinal()
    if month == 12:
        last = date(year, 12, 31).toordinal()
    else:
        last = date(year, month+1, 1).toordinal()-1

    return first, last


def __get_free_days_month(bookings, year, month):
    """
    Get a list with days free and whit double booked from a month.
    :param bookings: list of bookings
    :return: list of free days and double booked days
    """
    free = []
    double = []

    booked_list, double_list = __read_bookings(bookings=bookings)

    first_day, last_day = __get_first_last(year=year, month=month)

    for item in range(first_day, last_day+1):
        if item not in booked_list:
            free.append(str(date.fromordinal(item)))
        if item in double_list:
            double.append(str(date.fromordinal(item)))

    return free, double


def __create_html_calendar_month(bookings, year, month):
    """
    Get a HTML calendar with free days in green and double booked in red.
    :param bookings: bokkings
    :param year: year
    :param month: month
    :return: HTML calendar
    """
    free, double = __get_free_days_month(bookings=bookings, year=year, month=month)

    myCal = htmlCalendar.MonthlyCalendar(year, month)

    for item in free:
        year, month, day = __get_y_m_d(item)
        myCal.viewEvent(day, day, "#00b33c", "Free")

    for item in double:
        year, month, day = __get_y_m_d(item)
        myCal.viewEvent(day, day, "#ff4d4d", "Double")

    return myCal


def to_print(bookings):
    """
    Print a list of free days or double booked.
    :param bookings: bookings
    """
    year, month, day = __get_y_m_d(bookings[0]['start'])
    booked, double = __get_free_days_month(bookings=bookings, year=year, month=month)
    if double:
        print 'Double booked:'
        for item in double:
            print '  ', item
    elif booked:
        print 'Available:'
        for item in booked:
            print '  ', item


def to_file_month(bookings):
    """
    Create a HTML file with a month info
    :param bookings: bookings
    """
    year, month, day = __get_y_m_d(bookings[0]['start'])
    myCal = __create_html_calendar_month(bookings=bookings, year=year, month=month)

    file = open('out_month.html', 'w')
    file.write(myCal.create())
    file.close()


def to_file_year(bookings):
    """
    Create a HTML file with a year info
    :param bookings: bookings
    """
    file = open('out_year.html', 'w')

    year, month, day = __get_y_m_d(bookings[0]['start'])

    for x in range(1, 12+1):
        myCal = __create_html_calendar_month(bookings=bookings, year=year, month=x)
        file.write(myCal.create() + '<br>')

    file.close()


# CALLS
to_print(bookings)

to_file_month(bookings)

to_file_year(year)
