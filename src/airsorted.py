from datetime import date

import htmlCalendar

__author__ = 'josebermudez'


class AirSorted(object):

    def __read_bookings(self, bookings):
        """
        Read a booking list
        :param bookings: list
        :return: list with all days between start and end
        """
        booked = set()
        double = set()

        for item in bookings:
            year, month, day = self.__get_y_m_d(item['start'])
            date1 = date(year, month, day).toordinal()

            year, month, day = self.__get_y_m_d(item['end'])
            date2 = date(year, month, day).toordinal()

            for d in range(date1, date2+1):
                if d not in booked:
                    booked.add(d)
                else:
                    double.add(d)

        return booked, double

    def __get_y_m_d(self, string_date):
        """
        Return Year, Month and Day from a string YYYY-MM-DD
        :param string_date: string
        :return: year, month, day
        """
        return int(string_date[:4]), int(string_date[5:7]), int(string_date[8:])

    def __get_first_last(self, year, month):
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

    def __get_free_days_month(self, bookings, year, month):
        """
        Get a list with days free and whit double booked from a month.
        :param bookings: list of bookings
        :return: list of free days and double booked days
        """
        free = []
        double = []

        booked_list, double_list = self.__read_bookings(bookings=bookings)

        first_day, last_day = self.__get_first_last(year=year, month=month)

        for item in range(first_day, last_day+1):
            if item not in booked_list:
                free.append(str(date.fromordinal(item)))
            if item in double_list:
                double.append(str(date.fromordinal(item)))

        return free, double

    def __create_html_calendar_month(self, bookings, year, month):
        """
        Get a HTML calendar with free days in green and double booked in red.
        :param bookings: bokkings
        :param year: year
        :param month: month
        :return: HTML calendar
        """
        free, double = self.__get_free_days_month(bookings=bookings, year=year, month=month)

        myCal = htmlCalendar.MonthlyCalendar(year, month)

        for item in free:
            year, month, day = self.__get_y_m_d(item)
            myCal.viewEvent(day, day, "#00b33c", "Free")

        for item in double:
            year, month, day = self.__get_y_m_d(item)
            myCal.viewEvent(day, day, "#ff4d4d", "Double")

        return myCal

    def to_print(self, bookings):
        """
        Print a list of free days or double booked.
        :param bookings: bookings
        """
        result = None
        year, month, day = self.__get_y_m_d(bookings[0]['start'])
        booked, double = self.__get_free_days_month(bookings=bookings, year=year, month=month)
        if double:
            result = 'Double booked:\n'
            for item in double:
                result += item + '\n'
        elif booked:
            result = 'Available:\n'
            for item in booked:
                result += item + '\n'
        return result

    def to_file_month(self, bookings, filename):
        """
        Create a HTML file with a month info
        :param bookings: bookings
        """
        year, month, day = self.__get_y_m_d(bookings[0]['start'])
        myCal = self.__create_html_calendar_month(bookings=bookings, year=year, month=month)

        file = open(filename, 'w')
        file.write(myCal.create())
        file.close()

    def to_file_year(self, bookings, filename):
        """
        Create a HTML file with a year info
        :param bookings: bookings
        """
        file = open(filename, 'w')

        year, month, day = self.__get_y_m_d(bookings[0]['start'])

        for x in range(1, 12+1):
            myCal = self.__create_html_calendar_month(bookings=bookings, year=year, month=x)
            file.write(myCal.create() + '<br>')

        file.close()
