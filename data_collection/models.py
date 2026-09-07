from os import name

from django.db import models
from django.conf import settings
from django.utils.text import slugify


class Behavior(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=255)
    opdef = models.TextField(verbose_name="Operational Definition")
    onset = models.TextField(null=True, blank=True)
    offset = models.TextField(null=True, blank=True)
    examples = models.ForeignKey(
        "Event",
        related_name="examples",
        blank=True,
        verbose_name="Example Events",
        on_delete=models.CASCADE,
    )

    class Meta:
        pass

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Behavior, self).save(*args, **kwargs)


class Event(models.Model):
    behavior = models.ForeignKey(Behavior, on_delete=models.CASCADE)
    event = models.TextField()
    explanation = models.TextField()
    meetsdef = models.BooleanField(
        verbose_name="Meets Operational Definition?", default=False
    )
    example = models.BooleanField(verbose_name="Is an Example Event?", default=False)

    class Meta:
        pass

    def __str__(self):
        return f"{self.behavior}: {self.event}"


class EventSet(models.Model):
    set_id = models.IntegerField()
    events = models.ForeignKey(Event, on_delete=models.CASCADE)
    ordered = models.BooleanField(verbose_name="Is Ordered?", default=False)
    index = models.IntegerField()

    class Meta:
        pass

    def __str__(self):
        return f"Event Set {self.set_id}"


class Program(models.Model):
    FREQUENCY = "FRQ"
    DURATION = "DUR"
    RATE = "RTE"
    LATENCY = "LTC"
    INTERRESPONSE_TIME = "IRT"
    PARTIAL_INTERVAL = "PIV"
    WHOLE_INTERVAL = "WIV"
    MOMENTARY_TIME_SAMPLING = "MOM"
    DATA_COLLECTION_CHOICES = {
        FREQUENCY: "Frequency",
        DURATION: "Duration",
        RATE: "Rate",
        LATENCY: "Latency",
        INTERRESPONSE_TIME: "Inter-response Time",
        PARTIAL_INTERVAL: "Partial Interval",
        WHOLE_INTERVAL: "Whole Interval",
        MOMENTARY_TIME_SAMPLING: "Momentary Time Sampling",
    }
    behavior = models.ForeignKey(
        EventSet, related_name="program_behavior", on_delete=models.CASCADE
    )
    type = models.CharField(
        max_length=3,
        verbose_name="Data Collection Method",
        choices=DATA_COLLECTION_CHOICES,
    )
    events = models.ForeignKey(
        EventSet, related_name="program_events", on_delete=models.CASCADE
    )

    class Meta:
        pass

    def __str__(self):
        return f"{self.behavior} - {self.type}"


class Results(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    results = models.JSONField()

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.program}"
