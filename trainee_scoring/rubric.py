from dataclasses import dataclass


@dataclass
class Rubric:
    DAYS = {1: "Day One", 2: "Day Two"}
    # ATTENDANCE
    ON_TIME = {1: "No show", 2: "Arrives >15m late", 3: "Arrives on time"}
    DRESS = {1: "Dressed inappropriately", 2: "Dressed appropriately"}
    DURATION = {
        1: "Misses more than 15 minutes or takes excessive breaks",
        2: "Misses up to 15 minutes or takes occasional breaks",
        3: "Present and participates for entire session",
    }

    # ENGAGEMENT
    ANSWERS = {
        1: "Unable to answer/Refuses to attempt",
        2: "Attempts to answer when prompted",
        3: "Attempts to answer independently",
        4: "Has to be banned from answering to give others chances",
    }
    FOCUS = {
        1: "Regularly distracted, on personal devices, in loud environment, camera off, etc. AND unresponsive",
        2: "Regularly distracted, on personal devices, in loud environment, camera off, etc. BUT responsive",
        3: "Not distracted, in quiet environment, camera on, responsive, etc.",
    }
    """ROLEPLAY = {
        1: "Does not engage in roleplay, prompted or independently",
        2: "Engages in roleplay when prompted",
        3: "Engages in roleplay independently",
    }
    # PEER_INTERACTIONS = {}
    # STAFF_INTERACTIONS = {}

    # FEEDBACK
    ACCEPTS = {
        1: "Does not accept feedback or responds combatively/defensively",
        2: "Reluctant to accept feedback but does",
        3: "Willingly accepts feedback from staff",
    }
    IMPLEMENTS = {
        1: "Does not implement feedback",
        2: "Delays implementation of feedback",
        3: "Immediately implements feedback from staff",
    }"""

    @classmethod
    def keystring(cls, attr):
        a = getattr(cls, attr)
        return " ".join([f"{k}" for k in a.keys()])

    @classmethod
    def max_value(cls, attr):

        return max(getattr(cls, attr).keys())
