"""
Simple in-memory conversation store.

Later:
    Local Dict  ---> Redis
"""

from collections import defaultdict


class ConversationMemory:

    def __init__(self):
        self.memory = defaultdict(list)

    def add_message(self, session_id, role, content):
        """
        Store conversation message.
        """

        self.memory[session_id].append(
            {
                "role": role,
                "content": content
            }
        )

    def get_history(self, session_id):
        """
        Return conversation history.
        """

        return self.memory.get(session_id, [])

    def clear(self, session_id):
        """
        Clear session.
        """

        self.memory.pop(session_id, None)


memory = ConversationMemory()