from django.db import models
from datetime import datetime

# Create your models here.

class Host(models.Model):
    ''' Host 数据表 '''
    # id = models.IntegerField()
    print("------host-----")
    tag = models.CharField(max_length=32)
    ip = models.CharField(max_length=32)
    cpu = models.DecimalField(max_digits=10,decimal_places=2)
    mem = models.DecimalField(max_digits=10,decimal_places=2)
    disk = models.DecimalField(max_digits=10,decimal_places=2)
    stat = models.IntegerField(default=0)
    cdate = models.DateTimeField(default=datetime.now)

    def toDict(self):
        ob = {
            'id' : self.id,
            'tag' : self.tag,
            'ip' : self.ip,
            'cpu' : self.cpu,
            'mem' : self.mem,
            'disk' : self.disk,
            'stat' : self.stat,
            'cdate' : self.cdate
        }
        return ob
    class Meta:
        db_table = 'host' # 指定表名
