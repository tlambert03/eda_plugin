from unittest import mock
import pytest

from pymm_eventserver.data_structures import MMSettings

from eda_plugin.utility.event_bus import EventBus
from test_mm_mocks import mock_datastore, datastore_save_path


@pytest.fixture
def event_bus(qtbot):
    widget = EventBus(mock.MagicMock())
    yield widget


@pytest.fixture
def java_settings_event(mock_datastore):
    mockup = mock.MagicMock()
    mockup.get_settings.return_value = None
    mockup.get_datastore.return_value = mock_datastore
    yield mockup


@pytest.fixture
def java_settings_event_w_save_loc(datastore_save_path):
    mockup = mock.MagicMock()
    mockup.get_settings.return_value = None
    mockup.get_datastore.return_value = datastore_save_path
    yield mockup


def test_java_settings_event(java_settings_event):
    assert java_settings_event.get_settings() is None
    assert isinstance(java_settings_event.get_datastore(), mock.MagicMock)


def test_event_bus(event_bus):
    assert event_bus.acquisition_started_event
    assert event_bus.initialized
