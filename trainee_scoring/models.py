from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator

from .rubric import Rubric as r
from core.models import Profile


class Trainee(models.Model):
    name = models.CharField(max_length=255)
    day_one = models.DateField()
    day_two = models.DateField()

    def __str__(self):
        return self.name


class ReportCard(models.Model):
    DAYS = {1: 1, 2: 2}
    ON_TIME = {1: 1, 2: 2, 3: 3}
    DRESS = {1: 1, 2: 2}
    DURATION = {
        1: 1,
        2: 2,
        3: 3,
    }

    # ENGAGEMENT
    ANSWERS = {
        1: 1,
        2: 2,
        3: 3,
        4: 4,
    }
    FOCUS = {
        1: 1,
        2: 2,
        3: 3,
    }
    ROLEPLAY = {
        1: 1,
        2: 2,
        3: 3,
    }
    PEER_INTERACTIONS = {}
    STAFF_INTERACTIONS = {}

    # FEEDBACK
    ACCEPTS = {
        1: 1,
        2: 2,
        3: 3,
    }
    IMPLEMENTS = {
        1: 1,
        2: 2,
        3: 3,
    }

    trainee = models.OneToOneField(Trainee, on_delete=models.CASCADE)
    day = models.DateField()
    on_time = models.IntegerField(
        verbose_name="Did the trainee arrive on time (excused tardiness or absence excluded)?",
        choices=ON_TIME,
        validators=[
            MaxValueValidator(r.max_value("ON_TIME")),
        ],
        default=1,
    )
    dress = models.IntegerField(
        verbose_name="Was the trainee appropriately dressed?",
        choices=DRESS,
        validators=[
            MaxValueValidator(r.max_value("DRESS")),
        ],
        default=1,
    )
    duration = models.IntegerField(
        verbose_name="Was the trainee present for the full duration of the training?",
        choices=DURATION,
        validators=[
            MaxValueValidator(r.max_value("DURATION")),
        ],
        default=1,
    )
    answers = models.IntegerField(
        verbose_name="Did the trainee respond to questions/SDs?",
        choices=ANSWERS,
        validators=[
            MaxValueValidator(r.max_value("ANSWERS")),
        ],
        default=1,
    )
    focus = models.IntegerField(
        verbose_name="Was the trainee focused on and engaged with the training?",
        choices=FOCUS,
        validators=[
            MaxValueValidator(r.max_value("FOCUS")),
        ],
        default=1,
    )
    roleplay = models.IntegerField(
        verbose_name="Did the trainee engage in roleplay?",
        choices=ROLEPLAY,
        validators=[
            MaxValueValidator(r.max_value("ROLEPLAY")),
        ],
        default=1,
    )
    """
    peer_interactions = models.IntegerField(
        verbose_name="Did the trainee interact appropriately with their peers?",
        choices=r.PEER_INTERACTIONS,
        validators=[
            MaxValueValidator(r.max_value("PEER_INTERACTIONS")),
        ],
        default=1,
    )
    staff_interactions = models.IntegerField(
        verbose_name="Did the trainee interact appropriately with staff?",
        choices=r.STAFF_INTERACTIONS,
        validators=[
            MaxValueValidator(r.max_value("STAFF_INTERACTIONS")),
        ],
        default=1,
    )
    """
    accepts = models.IntegerField(
        verbose_name="Did the trainee accept feedback from staff?",
        choices=ACCEPTS,
        validators=[
            MaxValueValidator(r.max_value("ACCEPTS")),
        ],
        default=1,
    )
    implements = models.IntegerField(
        verbose_name="Did the trainee implement feedback from staff?",
        choices=IMPLEMENTS,
        validators=[
            MaxValueValidator(r.max_value("IMPLEMENTS")),
        ],
        default=1,
    )
