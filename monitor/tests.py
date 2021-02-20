from django.test import TestCase
import json

data = '{"cpu_count": 4, "cpu_percent": 0.0, "mem_total": 8201011200, "mem_percent": 6.7, "disk_total": 42135011328, "disk_percent": 7.3}'

print(data)
print(json.loads(data)['cpu_count'])
# Create your tests here.
