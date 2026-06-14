from django.db import models


# Create your models here.
class Behavior(models.Model):
    name = models.CharField(max_length=255)
    opdef = models.TextField(verbose_name="Operational Definition")
    data_type = models.CharField(max_length=10)
    examples = models.ManyToManyField(
        "Event", related_name="example_events", blank=True, verbose_name="Examples"
    )

    class Meta:
        pass


class Event(models.Model):
    behavior = models.ForeignKey(Behavior, on_delete=models.CASCADE)
    event = models.TextField()
    meetsdef = models.BooleanField(verbose_name="Meets Operational Definition?")
    example = models.BooleanField(verbose_name="Is an Example Event?", default=False)

    class Meta:
        pass
