import arrow
from datetime import timedelta


class Calendar(object):

    @staticmethod
    def get_lines(t0, dt):
        if (timedelta(days=7) < dt) and (dt < timedelta(weeks=8)):
            out1 = []
            t1 = t0.replace(day=t0.day+1, hour=0, minute=0, second=0)
            te = t0 + dt
            while t1 < te:
                if t1 > t0:
                    out1.append((t1.format('YYYY-MM-DD'), (t1-t0)/dt))
                t1 += timedelta(days=7)
            out2 = []
            t1 = t0.replace(day=t0.day+1, hour=0, minute=0, second=0)
            te = t0 + dt
            while t1 < te:
                if t1 > t0:
                    out2.append((t1.format('DD'), (t1-t0)/dt))
                t1 += timedelta(days=1)
            return out1, out2
        elif (timedelta(days=2) < dt) and (dt < timedelta(days=7)):
            out1 = []
            t1 = t0.replace(day=t0.day+1, hour=0, minute=0, second=0)
            te = t0 + dt
            while t1 < te:
                if t1 > t0:
                    out1.append((t1.format('YYYY-MM-DD'), (t1-t0)/dt))
                t1 += timedelta(days=1)
            out2 = []
            t1 = t0.replace(hour=12, minute=0, second=0)
            te = t0 + dt
            while t1 < te:
                if t1 > t0:
                    out2.append((t1.format('HH:mm'), (t1-t0)/dt))
                t1 += timedelta(hours=24)
            return out1, out2
        elif (timedelta(hours=8) < dt) and (dt < timedelta(days=2)):
            out1 = []
            t1 = t0.replace(hour=0, minute=0, second=0)
            te = t0 + dt
            while t1 < te:
                if t1 > t0:
                    out1.append((t1.format('YYYY-MM-DD HH:mm'), (t1-t0)/dt))
                t1 += timedelta(hours=12)
            out2 = []
            t1 = t0.replace(hour=t0.hour+1, minute=0, second=0)
            te = t0 + dt
            while t1 < te:
                if t1 > t0:
                    out2.append((t1.format('HH:mm'), (t1-t0)/dt))
                t1 += timedelta(hours=1)
            return out1, out2
        elif (timedelta(hours=1) < dt) and (dt < timedelta(hours=8)):
            out1 = []
            t1 = t0.replace(hour=t0.hour+1, minute=0, second=0)
            te = t0 + dt
            while t1 < te:
                if t1 > t0:
                    out1.append((t1, (t1-t0)/dt))
                t1 += timedelta(hours=1)
            out2 = []
            t1 = t0.replace(minute=(t0.minute//30)*30, second=0)
            te = t0 + dt
            while t1 < te:
                if t1 > t0:
                    out2.append((t1, (t1-t0)/dt))
                t1 += timedelta(minutes=30)
            return out1, out2



