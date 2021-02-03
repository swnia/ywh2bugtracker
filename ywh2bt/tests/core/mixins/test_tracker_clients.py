from typing import (
    List,
    Optional,
)
from unittest import TestCase

from ywh2bt.core.api.models.report import (
    Log,
    Report,
)
from ywh2bt.core.api.tracker import (
    TrackerClient,
    TrackerComments,
    TrackerIssue,
)
from ywh2bt.core.configuration.tracker import TrackerConfiguration
from ywh2bt.core.exceptions import CoreException
from ywh2bt.core.mixins.tracker_clients import (
    TrackerClientClassesRegistry,
    TrackerClientsMixin,
)


class MyConfiguration(TrackerConfiguration):
    pass


class MyTrackerClient(TrackerClient[MyConfiguration]):

    @property
    def tracker_type(self) -> str:
        return 'My configuration'

    def get_tracker_issue(self, issue_id: str) -> Optional[TrackerIssue]:
        raise NotImplementedError()

    def send_report(self, report: Report) -> TrackerIssue:
        raise NotImplementedError()

    def send_logs(self, tracker_issue: TrackerIssue, logs: List[Log]) -> TrackerComments:
        raise NotImplementedError()

    def test(self) -> None:
        raise NotImplementedError()


class TestTrackerClients(TestCase):

    def tearDown(self) -> None:
        TrackerClientClassesRegistry.unregister_tracker_client_class(
            configuration_class=MyConfiguration,
        )

    def test_get_tracker_client(self) -> None:
        TrackerConfiguration.register_subtype(
            subtype_name='my',
            subtype_class=MyConfiguration,
        )
        TrackerClientClassesRegistry.register_tracker_client_class(
            configuration_class=MyConfiguration,
            client_class=MyTrackerClient,
        )
        mixin = TrackerClientsMixin()
        mixin.get_tracker_client(
            configuration=MyConfiguration(),
        )

    def test_get_tracker_client_not_registered(self) -> None:
        TrackerConfiguration.register_subtype(
            subtype_name='my',
            subtype_class=MyConfiguration,
        )
        mixin = TrackerClientsMixin()
        with self.assertRaises(CoreException):
            mixin.get_tracker_client(
                configuration=MyConfiguration(),
            )
