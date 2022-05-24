from __future__ import absolute_import
import datetime


def load_date_bound(interval_days = 30):
    def make_end_date(s, e, i):
        end_date = s + datetime.timedelta(days=i)
        if end_date > e:
            return e
        return end_date

    def parse_if_needed(dt):
        if isinstance(dt, datetime.datetime):
            return dt
        return datetime.datetime.fromisoformat(dt)

    date_range = {}

    def decorator(function):
        def wrapper(*args, **kwargs):
            date_range.update({
                u'dataStartTime': parse_if_needed(kwargs[u'dataStartTime']),
                u'dataEndTime': parse_if_needed(kwargs.get(u'dataEndTime', datetime.datetime.utcnow()))
            })
            kwargs.update({
                u'dataEndTime': make_end_date(date_range[u'dataStartTime'], date_range[u'dataEndTime'], interval_days)
            })
            while kwargs[u'dataStartTime'] < kwargs[u'dataEndTime']:
                yield function(*args, **kwargs)
                kwargs.update({
                    u'dataStartTime': parse_if_needed(kwargs[u'dataEndTime']),
                    u'dataEndTime': make_end_date(parse_if_needed(kwargs[u'dataEndTime']), date_range[u'dataEndTime'],
                                                 interval_days)
                })

        wrapper.__doc__ = function.__doc__
        return wrapper

    return decorator
