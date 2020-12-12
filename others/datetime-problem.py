from dateutil.relativedelta import relativedelta
import datetime as dt


def get_min_fraction(i):
    return (int(i) * .5) / 30


def get_diff(diff):
    if diff.hours != None:
        return float(diff.hours) + get_min_fraction(diff.minutes)
    return get_min_fraction(diff.minutes)


def get_range(i):
    return i.strip().split('-')


def get_format(i):
    return '%H:%M' if ':' in i else '%H'


def get_time(i, format):
    return dt.datetime.strptime(i.strip(), format.strip())


def get_start_end(i):
    start, end = get_range(i)

    start_hour = int(start.split(':')[0])
    end_hour = int(end.split(':')[0])

    if start_hour > end_hour:
        end_hour += 12
        end_min = ':' + end.split(':')[1] if len(end.split(':')) == 2 else ''
        end = f'{end_hour}{end_min}'

    start_time, end_time = get_time(start, get_format(start)), get_time(end, get_format(end))
    diff = relativedelta(start_time, end_time)

    return get_diff(diff)


def solution(times):
    total = 0

    for i in times:
        total += get_start_end(i)
    return abs(total)


times = ['2-3', '5-6', '6-9', '3-9', '9-2', ' 9-10', '12-1', '12-1', ' 2-9', '3-4', '9-11', '11-12', ' 7:30-8:30',
         '5-8', '9-1', '11-1', '3-6', '4-8', '12:30-2:30', ' 5-9', '10-11', '8-12', '8-9', ' 10-10:30', ' 11:30 - 2',
         '10-10:30', ' 11-12', ' 1:30-3', ' 4-5:30', '9:30-11']

# calculate the total number of hours from the a list of start_time-end_time range
print(solution(times))
