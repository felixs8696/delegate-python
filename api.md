# Delegate

Methods:

- <code title="get /">client.<a href="./src/delegate/_client.py">retrieve</a>() -> object</code>

# Objectives

Types:

```python
from delegate.types import Objective, ObjectiveListResponse
```

Methods:

- <code title="post /objectives">client.objectives.<a href="./src/delegate/resources/objectives.py">create</a>(\*\*<a href="src/delegate/types/objective_create_params.py">params</a>) -> <a href="./src/delegate/types/objective.py">Objective</a></code>
- <code title="get /objectives/{objective_id}">client.objectives.<a href="./src/delegate/resources/objectives.py">retrieve</a>(objective_id) -> <a href="./src/delegate/types/objective.py">Objective</a></code>
- <code title="get /objectives">client.objectives.<a href="./src/delegate/resources/objectives.py">list</a>(\*\*<a href="src/delegate/types/objective_list_params.py">params</a>) -> <a href="./src/delegate/types/objective_list_response.py">ObjectiveListResponse</a></code>
- <code title="delete /objectives/{objective_id}">client.objectives.<a href="./src/delegate/resources/objectives.py">delete</a>(objective_id) -> <a href="./src/delegate/types/objective.py">Objective</a></code>
- <code title="post /objectives/{objective_id}:cancel">client.objectives.<a href="./src/delegate/resources/objectives.py">cancel</a>(objective_id, \*\*<a href="src/delegate/types/objective_cancel_params.py">params</a>) -> <a href="./src/delegate/types/objective.py">Objective</a></code>
- <code title="get /objectives/{objective_id}:stream">client.objectives.<a href="./src/delegate/resources/objectives.py">stream_events</a>(objective_id) -> object</code>

# Spans

Types:

```python
from delegate.types import Span, SpanListResponse
```

Methods:

- <code title="post /spans">client.spans.<a href="./src/delegate/resources/spans.py">create</a>(\*\*<a href="src/delegate/types/span_create_params.py">params</a>) -> <a href="./src/delegate/types/span.py">Span</a></code>
- <code title="get /spans/{span_id}">client.spans.<a href="./src/delegate/resources/spans.py">retrieve</a>(span_id) -> <a href="./src/delegate/types/span.py">Span</a></code>
- <code title="patch /spans/{span_id}">client.spans.<a href="./src/delegate/resources/spans.py">update</a>(span_id, \*\*<a href="src/delegate/types/span_update_params.py">params</a>) -> <a href="./src/delegate/types/span.py">Span</a></code>
- <code title="get /spans">client.spans.<a href="./src/delegate/resources/spans.py">list</a>(\*\*<a href="src/delegate/types/span_list_params.py">params</a>) -> <a href="./src/delegate/types/span_list_response.py">SpanListResponse</a></code>

# States

Types:

```python
from delegate.types import State, StateListResponse
```

Methods:

- <code title="post /states">client.states.<a href="./src/delegate/resources/states.py">create</a>(\*\*<a href="src/delegate/types/state_create_params.py">params</a>) -> <a href="./src/delegate/types/state.py">State</a></code>
- <code title="get /states/{state_id}">client.states.<a href="./src/delegate/resources/states.py">retrieve</a>(state_id) -> <a href="./src/delegate/types/state.py">State</a></code>
- <code title="put /states/{state_id}">client.states.<a href="./src/delegate/resources/states.py">update</a>(state_id, \*\*<a href="src/delegate/types/state_update_params.py">params</a>) -> <a href="./src/delegate/types/state.py">State</a></code>
- <code title="get /states">client.states.<a href="./src/delegate/resources/states.py">list</a>(\*\*<a href="src/delegate/types/state_list_params.py">params</a>) -> <a href="./src/delegate/types/state_list_response.py">StateListResponse</a></code>
- <code title="delete /states/{state_id}">client.states.<a href="./src/delegate/resources/states.py">delete</a>(state_id) -> <a href="./src/delegate/types/state.py">State</a></code>

# Events

Types:

```python
from delegate.types import Event, EventListResponse
```

Methods:

- <code title="post /events">client.events.<a href="./src/delegate/resources/events.py">create</a>(\*\*<a href="src/delegate/types/event_create_params.py">params</a>) -> <a href="./src/delegate/types/event.py">Event</a></code>
- <code title="get /events/{event_id}">client.events.<a href="./src/delegate/resources/events.py">retrieve</a>(event_id) -> <a href="./src/delegate/types/event.py">Event</a></code>
- <code title="get /events">client.events.<a href="./src/delegate/resources/events.py">list</a>(\*\*<a href="src/delegate/types/event_list_params.py">params</a>) -> <a href="./src/delegate/types/event_list_response.py">EventListResponse</a></code>

# Users

Types:

```python
from delegate.types import User, UserListResponse
```

Methods:

- <code title="get /users/{user_id}">client.users.<a href="./src/delegate/resources/users.py">retrieve</a>(user_id) -> <a href="./src/delegate/types/user.py">User</a></code>
- <code title="put /users/{user_id}">client.users.<a href="./src/delegate/resources/users.py">update</a>(user_id, \*\*<a href="src/delegate/types/user_update_params.py">params</a>) -> <a href="./src/delegate/types/user.py">User</a></code>
- <code title="get /users">client.users.<a href="./src/delegate/resources/users.py">list</a>(\*\*<a href="src/delegate/types/user_list_params.py">params</a>) -> <a href="./src/delegate/types/user_list_response.py">UserListResponse</a></code>
- <code title="delete /users/{user_id}">client.users.<a href="./src/delegate/resources/users.py">delete</a>(user_id) -> <a href="./src/delegate/types/user.py">User</a></code>
- <code title="get /users/username/{username}">client.users.<a href="./src/delegate/resources/users.py">retrieve_by_username</a>(username) -> <a href="./src/delegate/types/user.py">User</a></code>
- <code title="get /users/me">client.users.<a href="./src/delegate/resources/users.py">retrieve_current</a>() -> <a href="./src/delegate/types/user.py">User</a></code>

# Channels

Types:

```python
from delegate.types import Channel, ChannelMembership, ChannelListResponse
```

Methods:

- <code title="post /channels">client.channels.<a href="./src/delegate/resources/channels/channels.py">create</a>(\*\*<a href="src/delegate/types/channel_create_params.py">params</a>) -> <a href="./src/delegate/types/channel.py">Channel</a></code>
- <code title="get /channels/{channel_id}">client.channels.<a href="./src/delegate/resources/channels/channels.py">retrieve</a>(channel_id) -> <a href="./src/delegate/types/channel.py">Channel</a></code>
- <code title="put /channels/{channel_id}">client.channels.<a href="./src/delegate/resources/channels/channels.py">update</a>(channel_id, \*\*<a href="src/delegate/types/channel_update_params.py">params</a>) -> <a href="./src/delegate/types/channel.py">Channel</a></code>
- <code title="get /channels">client.channels.<a href="./src/delegate/resources/channels/channels.py">list</a>(\*\*<a href="src/delegate/types/channel_list_params.py">params</a>) -> <a href="./src/delegate/types/channel_list_response.py">ChannelListResponse</a></code>
- <code title="delete /channels/{channel_id}">client.channels.<a href="./src/delegate/resources/channels/channels.py">delete</a>(channel_id) -> <a href="./src/delegate/types/channel.py">Channel</a></code>
- <code title="post /channels/{channel_id}:join">client.channels.<a href="./src/delegate/resources/channels/channels.py">join</a>(channel_id, \*\*<a href="src/delegate/types/channel_join_params.py">params</a>) -> <a href="./src/delegate/types/channel_membership.py">ChannelMembership</a></code>
- <code title="post /channels/{channel_id}:leave">client.channels.<a href="./src/delegate/resources/channels/channels.py">leave</a>(channel_id, \*\*<a href="src/delegate/types/channel_leave_params.py">params</a>) -> <a href="./src/delegate/types/channel_membership.py">ChannelMembership</a></code>

## Members

Types:

```python
from delegate.types.channels import MemberListResponse
```

Methods:

- <code title="put /channels/{channel_id}/members/{user_id}">client.channels.members.<a href="./src/delegate/resources/channels/members.py">update</a>(user_id, \*, channel_id, \*\*<a href="src/delegate/types/channels/member_update_params.py">params</a>) -> <a href="./src/delegate/types/channel_membership.py">ChannelMembership</a></code>
- <code title="get /channels/{channel_id}/members">client.channels.members.<a href="./src/delegate/resources/channels/members.py">list</a>(channel_id, \*\*<a href="src/delegate/types/channels/member_list_params.py">params</a>) -> <a href="./src/delegate/types/channels/member_list_response.py">MemberListResponse</a></code>

# Messages

Types:

```python
from delegate.types import Message, TextContent, MessageListResponse
```

Methods:

- <code title="post /messages">client.messages.<a href="./src/delegate/resources/messages.py">create</a>(\*\*<a href="src/delegate/types/message_create_params.py">params</a>) -> <a href="./src/delegate/types/message.py">Message</a></code>
- <code title="get /messages/{message_id}">client.messages.<a href="./src/delegate/resources/messages.py">retrieve</a>(message_id) -> <a href="./src/delegate/types/message.py">Message</a></code>
- <code title="put /messages/{message_id}">client.messages.<a href="./src/delegate/resources/messages.py">update</a>(message_id, \*\*<a href="src/delegate/types/message_update_params.py">params</a>) -> <a href="./src/delegate/types/message.py">Message</a></code>
- <code title="get /messages">client.messages.<a href="./src/delegate/resources/messages.py">list</a>(\*\*<a href="src/delegate/types/message_list_params.py">params</a>) -> <a href="./src/delegate/types/message_list_response.py">MessageListResponse</a></code>
- <code title="delete /messages/{message_id}">client.messages.<a href="./src/delegate/resources/messages.py">delete</a>(message_id) -> <a href="./src/delegate/types/message.py">Message</a></code>

# Notifications

Types:

```python
from delegate.types import (
    NotificationCreateResponse,
    NotificationRetrieveResponse,
    NotificationUpdateResponse,
    NotificationListResponse,
    NotificationDeleteResponse,
)
```

Methods:

- <code title="post /notifications">client.notifications.<a href="./src/delegate/resources/notifications.py">create</a>(\*\*<a href="src/delegate/types/notification_create_params.py">params</a>) -> <a href="./src/delegate/types/notification_create_response.py">NotificationCreateResponse</a></code>
- <code title="get /notifications/{notification_id}">client.notifications.<a href="./src/delegate/resources/notifications.py">retrieve</a>(notification_id) -> <a href="./src/delegate/types/notification_retrieve_response.py">NotificationRetrieveResponse</a></code>
- <code title="put /notifications/{notification_id}">client.notifications.<a href="./src/delegate/resources/notifications.py">update</a>(notification_id, \*\*<a href="src/delegate/types/notification_update_params.py">params</a>) -> <a href="./src/delegate/types/notification_update_response.py">NotificationUpdateResponse</a></code>
- <code title="get /notifications">client.notifications.<a href="./src/delegate/resources/notifications.py">list</a>(\*\*<a href="src/delegate/types/notification_list_params.py">params</a>) -> <a href="./src/delegate/types/notification_list_response.py">NotificationListResponse</a></code>
- <code title="delete /notifications/{notification_id}">client.notifications.<a href="./src/delegate/resources/notifications.py">delete</a>(notification_id) -> <a href="./src/delegate/types/notification_delete_response.py">NotificationDeleteResponse</a></code>
