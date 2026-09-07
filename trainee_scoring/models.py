from django.db import models

from .rubric import Rubric as r


class Attendance(models.Model):
    on_time = models.BooleanField(verbose_name="Arrived on time", choices=r.ON_TIME)
    dress = models.BooleanField(verbose_name="Appropriately dressed", choices=r.DRESS)
    duration = models.BooleanField(
        verbose_name="Present for full duration", choices=r.DURATION
    )

    class Meta:
        pass


class Engagement(models.Model):
    answers = models.IntegerField(verbose_name="Answers questions", choices=r.ANSWERS)
    focus = models.IntegerField(
        verbose_name="Participated in discussion", choices=r.FOCUS
    )
    roleplay = models.IntegerField(
        verbose_name="Engaged in roleplay", choices=r.ROLEPLAY
    )
    peers = models.IntegerField(
        verbose_name="Peer interactions", choices=r.PEER_INTERACTIONS
    )
    staff = models.IntegerField(
        verbose_name="Staff interactions", choices=r.STAFF_INTERACTIONS
    )

    class Meta:
        pass


class Feedback(models.Model):
    accepts = models.IntegerField(verbose_name="Accepts feedback", choices=r.ACCEPTS)
    implements = models.IntegerField(
        verbose_name="Implements feedback", choices=r.IMPLEMENTS
    )

    class Meta:
        pass


class Rubric(models.Model):
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    engagement = models.ForeignKey(Engagement, on_delete=models.CASCADE)
    feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE)

    class Meta:
        pass
