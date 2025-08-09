# Delegate

Methods:

- <code title="get /">client.<a href="./src/delegate/_client.py">retrieve</a>() -> object</code>

# Objectives

Types:

```python
from delegate.types import Objective, ObjectiveListResponse
```

Methods:

- <code title="post /objectives">client.objectives.<a href="./src/delegate/resources/objectives/objectives.py">create</a>(\*\*<a href="src/delegate/types/objective_create_params.py">params</a>) -> <a href="./src/delegate/types/objective.py">Objective</a></code>
- <code title="get /objectives/{objective_id}">client.objectives.<a href="./src/delegate/resources/objectives/objectives.py">retrieve</a>(objective_id) -> <a href="./src/delegate/types/objective.py">Objective</a></code>
- <code title="get /objectives">client.objectives.<a href="./src/delegate/resources/objectives/objectives.py">list</a>() -> <a href="./src/delegate/types/objective_list_response.py">ObjectiveListResponse</a></code>
- <code title="delete /objectives/{objective_id}">client.objectives.<a href="./src/delegate/resources/objectives/objectives.py">delete</a>(objective_id) -> <a href="./src/delegate/types/objective.py">Objective</a></code>
- <code title="post /objectives/{objective_id}:cancel">client.objectives.<a href="./src/delegate/resources/objectives/objectives.py">cancel</a>(objective_id, \*\*<a href="src/delegate/types/objective_cancel_params.py">params</a>) -> <a href="./src/delegate/types/objective.py">Objective</a></code>
- <code title="get /objectives/{objective_id}:stream">client.objectives.<a href="./src/delegate/resources/objectives/objectives.py">stream_events</a>(objective_id) -> object</code>

## Name

Methods:

- <code title="get /objectives/name/{objective_name}">client.objectives.name.<a href="./src/delegate/resources/objectives/name.py">retrieve</a>(objective_name) -> <a href="./src/delegate/types/objective.py">Objective</a></code>
- <code title="delete /objectives/name/{objective_name}">client.objectives.name.<a href="./src/delegate/resources/objectives/name.py">delete</a>(objective_name) -> <a href="./src/delegate/types/objective.py">Objective</a></code>
- <code title="get /objectives/name/{objective_name}:stream">client.objectives.name.<a href="./src/delegate/resources/objectives/name.py">stream_events</a>(objective_name) -> object</code>

# Activities

Types:

```python
from delegate.types import (
    DataContentEntity,
    FileAttachment,
    ObjectiveActivity,
    TextContentEntity,
    TextFormat,
    ToolRequestContentEntity,
    ToolResponseContentEntity,
    ActivityListResponse,
)
```

Methods:

- <code title="post /activities">client.activities.<a href="./src/delegate/resources/activities.py">create</a>(\*\*<a href="src/delegate/types/activity_create_params.py">params</a>) -> <a href="./src/delegate/types/objective_activity.py">ObjectiveActivity</a></code>
- <code title="get /activities/{activity_id}">client.activities.<a href="./src/delegate/resources/activities.py">retrieve</a>(activity_id) -> <a href="./src/delegate/types/objective_activity.py">ObjectiveActivity</a></code>
- <code title="get /activities">client.activities.<a href="./src/delegate/resources/activities.py">list</a>(\*\*<a href="src/delegate/types/activity_list_params.py">params</a>) -> <a href="./src/delegate/types/activity_list_response.py">ActivityListResponse</a></code>

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

# Contexts

Types:

```python
from delegate.types import Context, ContextCreateResponse, ContextListResponse, ContextChatResponse
```

Methods:

- <code title="post /contexts">client.contexts.<a href="./src/delegate/resources/contexts.py">create</a>() -> <a href="./src/delegate/types/context_create_response.py">ContextCreateResponse</a></code>
- <code title="get /contexts/{context_id}">client.contexts.<a href="./src/delegate/resources/contexts.py">retrieve</a>(context_id) -> <a href="./src/delegate/types/context.py">Context</a></code>
- <code title="patch /contexts/{context_id}">client.contexts.<a href="./src/delegate/resources/contexts.py">update</a>(context_id, \*\*<a href="src/delegate/types/context_update_params.py">params</a>) -> <a href="./src/delegate/types/context.py">Context</a></code>
- <code title="get /contexts">client.contexts.<a href="./src/delegate/resources/contexts.py">list</a>() -> <a href="./src/delegate/types/context_list_response.py">ContextListResponse</a></code>
- <code title="delete /contexts/{context_id}">client.contexts.<a href="./src/delegate/resources/contexts.py">delete</a>(context_id) -> object</code>
- <code title="post /contexts/{context_id}:chat">client.contexts.<a href="./src/delegate/resources/contexts.py">chat</a>(context_id, \*\*<a href="src/delegate/types/context_chat_params.py">params</a>) -> <a href="./src/delegate/types/context_chat_response.py">ContextChatResponse</a></code>

# Users

Types:

```python
from delegate.types import User, UserListResponse
```

Methods:

- <code title="post /users">client.users.<a href="./src/delegate/resources/users.py">create</a>(\*\*<a href="src/delegate/types/user_create_params.py">params</a>) -> <a href="./src/delegate/types/user.py">User</a></code>
- <code title="get /users/{user_id}">client.users.<a href="./src/delegate/resources/users.py">retrieve</a>(user_id) -> <a href="./src/delegate/types/user.py">User</a></code>
- <code title="put /users/{user_id}">client.users.<a href="./src/delegate/resources/users.py">update</a>(user_id, \*\*<a href="src/delegate/types/user_update_params.py">params</a>) -> <a href="./src/delegate/types/user.py">User</a></code>
- <code title="get /users">client.users.<a href="./src/delegate/resources/users.py">list</a>(\*\*<a href="src/delegate/types/user_list_params.py">params</a>) -> <a href="./src/delegate/types/user_list_response.py">UserListResponse</a></code>
- <code title="delete /users/{user_id}">client.users.<a href="./src/delegate/resources/users.py">delete</a>(user_id) -> <a href="./src/delegate/types/user.py">User</a></code>
- <code title="get /users/username/{username}">client.users.<a href="./src/delegate/resources/users.py">retrieve_by_username</a>(username) -> <a href="./src/delegate/types/user.py">User</a></code>

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
- <code title="get /channels/name/{channel_name}">client.channels.<a href="./src/delegate/resources/channels/channels.py">retrieve_by_name</a>(channel_name) -> <a href="./src/delegate/types/channel.py">Channel</a></code>

## Members

Types:

```python
from delegate.types.channels import MemberListResponse
```

Methods:

- <code title="put /channels/{channel_id}/members/{user_id}">client.channels.members.<a href="./src/delegate/resources/channels/members.py">update</a>(user_id, \*, channel_id, \*\*<a href="src/delegate/types/channels/member_update_params.py">params</a>) -> <a href="./src/delegate/types/channel_membership.py">ChannelMembership</a></code>
- <code title="get /channels/{channel_id}/members">client.channels.members.<a href="./src/delegate/resources/channels/members.py">list</a>(channel_id, \*\*<a href="src/delegate/types/channels/member_list_params.py">params</a>) -> <a href="./src/delegate/types/channels/member_list_response.py">MemberListResponse</a></code>

# ChannelMessages

Types:

```python
from delegate.types import ChannelMessage, CreateChannelMessage, ChannelMessageListResponse
```

Methods:

- <code title="post /channel-messages">client.channel_messages.<a href="./src/delegate/resources/channel_messages/channel_messages.py">create</a>(\*\*<a href="src/delegate/types/channel_message_create_params.py">params</a>) -> <a href="./src/delegate/types/channel_message.py">ChannelMessage</a></code>
- <code title="get /channel-messages/{message_id}">client.channel_messages.<a href="./src/delegate/resources/channel_messages/channel_messages.py">retrieve</a>(message_id) -> <a href="./src/delegate/types/channel_message.py">ChannelMessage</a></code>
- <code title="put /channel-messages/{message_id}">client.channel_messages.<a href="./src/delegate/resources/channel_messages/channel_messages.py">update</a>(message_id, \*\*<a href="src/delegate/types/channel_message_update_params.py">params</a>) -> <a href="./src/delegate/types/channel_message.py">ChannelMessage</a></code>
- <code title="get /channel-messages">client.channel_messages.<a href="./src/delegate/resources/channel_messages/channel_messages.py">list</a>(\*\*<a href="src/delegate/types/channel_message_list_params.py">params</a>) -> <a href="./src/delegate/types/channel_message_list_response.py">ChannelMessageListResponse</a></code>
- <code title="delete /channel-messages/{message_id}">client.channel_messages.<a href="./src/delegate/resources/channel_messages/channel_messages.py">delete</a>(message_id) -> <a href="./src/delegate/types/channel_message.py">ChannelMessage</a></code>

## Batch

Types:

```python
from delegate.types.channel_messages import BatchCreateResponse, BatchUpdateResponse
```

Methods:

- <code title="post /channel-messages/batch">client.channel_messages.batch.<a href="./src/delegate/resources/channel_messages/batch.py">create</a>(\*\*<a href="src/delegate/types/channel_messages/batch_create_params.py">params</a>) -> <a href="./src/delegate/types/channel_messages/batch_create_response.py">BatchCreateResponse</a></code>
- <code title="put /channel-messages/batch">client.channel_messages.batch.<a href="./src/delegate/resources/channel_messages/batch.py">update</a>(\*\*<a href="src/delegate/types/channel_messages/batch_update_params.py">params</a>) -> <a href="./src/delegate/types/channel_messages/batch_update_response.py">BatchUpdateResponse</a></code>
