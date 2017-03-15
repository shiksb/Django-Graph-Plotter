from datetime import datetime, timedelta
from django import core
import pytz



from .models import Data, Pi


class ChartData(object):

    @classmethod
    def get_avg_by_day(cls, pi):
        dataObjects = Data.objects.all()


        # data = {'dates': [], 'values': []}
        #
        # for datum in dataObjects:
        #     data['dates'].append(int((datum.date_time.timestamp() + 14400) *1000))
        #     data['values'].append(datum.vol)

        data = []

        for datum in dataObjects:
            data.append([int((datum.date_time.timestamp() - 14400) * 1000),
                         datum.vol])

        return data