import unittest

from django.contrib.auth.models import User
from django.test import Client

from main.models import UserProfile
from main.tasks import check_flag


class CeleryCaseTest(unittest.TestCase):


    def setUp(self):
        self.userprofile_no_changes= UserProfile.objects.filter(is_notified=False)
        if User.objects.filter(username = 'test1') and User.objects.filter(username = 'test2'):
            self.user1 = User.objects.get(username = 'test1')
            self.user2 = User.objects.get(username = 'test2')
        else:
            self.user1 = User.objects.create(username='test1',
                                         password='test1')
            self.user1.save()
            self.uprofile = UserProfile.objects.create(user=self.user1)
            self.uprofile.save()
            self.user2 = User.objects.create(username='test2',
                                             password='test2')
            self.user2.save()
            self.uprofile2 = UserProfile.objects.create(user=self.user2)
            self.uprofile2.save()


    def test_check_flag_false(self):
        check_flag()
        users = UserProfile.objects.filter(is_notified=False)
        self.assertEqual(users.exists(), False)

    def test_check_flag_instance(self):
        user_profile = UserProfile.objects.first()
        self.assertIsInstance(user_profile, UserProfile)

    def tearDown(self):
        User.objects.filter(pk=self.user1.pk).delete()
        User.objects.filter(pk=self.user2.pk).delete()
        # UserProfile.objects.filter(pk=self.uprofile.pk).delete()
        # UserProfile.objects.filter(pk=self.uprofile2.pk).delete()
