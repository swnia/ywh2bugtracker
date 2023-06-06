"""Models and functions used in data typing."""
from typing import Any, Union, cast

from PySide6.QtCore import Signal, SignalInstance


def as_signal_instance(
    signal: Union[Signal, Any],
) -> SignalInstance:
    """
    Cast a Signal object to a SignalInstance.

    PySide6 magic / static typing / mypy.

    Args:
        signal: a signal object

    Returns:
        The signal instance
    """
    return cast(SignalInstance, signal)
