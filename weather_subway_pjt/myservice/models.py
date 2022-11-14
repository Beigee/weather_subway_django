from django.db import models
class MyPlace(models.Model):
    mp_idx = models.BigAutoField(primary_key=True)
    id = models.CharField(max_length=30)
    station_name = models.CharField(max_length=30)
    t_name = models.CharField(max_length=100)
    cate = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'my_place'
