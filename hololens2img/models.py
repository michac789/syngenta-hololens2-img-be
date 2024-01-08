from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class AbstractImageModel(models.Model):
    label = models.CharField(max_length=50)
    order = models.IntegerField(unique=True, validators=[
        MinValueValidator(1), MaxValueValidator(100)
    ])
    image_data_base64 = models.TextField()
    
    class Meta:
        abstract = True


class MS1(AbstractImageModel):
    class Meta:
        verbose_name = 'MS1'
        verbose_name_plural = 'MS1'


class MS2(AbstractImageModel):
    class Meta:
        verbose_name = 'MS2'
        verbose_name_plural = 'MS2'


class MS3(AbstractImageModel):
    class Meta:
        verbose_name = 'MS3'
        verbose_name_plural = 'MS3'


class MS4(AbstractImageModel):
    class Meta:
        verbose_name = 'MS4'
        verbose_name_plural = 'MS4'


class MS5(AbstractImageModel):
    class Meta:
        verbose_name = 'MS5'
        verbose_name_plural = 'MS5'


class MS6(AbstractImageModel):
    class Meta:
        verbose_name = 'MS6'
        verbose_name_plural = 'MS6'


class WH(AbstractImageModel):
    class Meta:
        verbose_name = 'WH'
        verbose_name_plural = 'WH'
