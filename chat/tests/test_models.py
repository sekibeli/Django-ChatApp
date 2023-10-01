from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Chat, Message
from datetime import date

class ChatModelTest(TestCase):

    def test_chat_creation(self):
        chat = Chat.objects.create()
        self.assertTrue(isinstance(chat, Chat))
        self.assertEqual(chat.created_at, date.today())

class MessageModelTest(TestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(username="user1", password="password")
        self.user2 = User.objects.create_user(username="user2", password="password")
        self.chat = Chat.objects.create()

    def test_message_creation(self):
        message = Message.objects.create(
            text="Hello",
            chat=self.chat,
            author=self.user1,
            receiver=self.user2
        )
        self.assertTrue(isinstance(message, Message))
        self.assertEqual(message.text, "Hello")
        self.assertEqual(message.created_at, date.today())
        self.assertEqual(message.author, self.user1)
        self.assertEqual(message.receiver, self.user2)

    def test_chat_relationship(self):
        Message.objects.create(
            text="Hello",
            chat=self.chat,
            author=self.user1,
            receiver=self.user2
        )
        self.assertEqual(self.chat.chat_message_set.count(), 1)