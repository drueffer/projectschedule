import arrow
from datetime import timedelta


class Calendar(object):

    @staticmethod
    def get_lines(t0, dt):
        out = []
        if dt < timedelta(days=14):
            t1 = timedelta(seconds=0)
            while t1 < dt:
                out.append(t1)
                t1 += timedelta(days=1)
        elif dt < timedelta(days=28):
            t1 = timedelta(seconds=0)
            while t1 < dt:
                out.append(t1)
                t1 += timedelta(days=7)
        elif dt < timedelta(days=64):
            t1 = timedelta(seconds=0)
            while t1 < dt:
                out.append(t1)
                t1 += timedelta(days=14)
        return [i/dt for i in out]
