from __future__ import absolute_import
from enum import Enum


class ReportStatus(unicode, Enum):
    CANCELLED = u"CANCELLED"
    DONE = u"DONE"
    FATAL = u"FATAL"
    IN_PROGRESS = u"IN_PROGRESS"
    IN_QUEUE = u"IN_QUEUE"
