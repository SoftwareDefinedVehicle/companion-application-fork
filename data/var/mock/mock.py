from lib.animator import RepeatMode
from lib.dsl import (
    create_animation_action,
    create_behavior,
    create_event_trigger,
    create_set_action,
    get_datapoint_value,
    mock_datapoint,
)

from lib.trigger import ClockTrigger, EventType

mock_datapoint(
    path="Vehicle.Cabin.Seat.Row1.Pos1.Position",
    initial_value=0,
    behaviors=[
        create_behavior(
            trigger=create_event_trigger(EventType.ACTUATOR_TARGET),
            action=create_animation_action(
                duration=10.0,
                values=["$self", "$event.value"],
            ),
        )
    ],
)