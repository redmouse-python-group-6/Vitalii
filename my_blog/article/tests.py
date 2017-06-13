# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from article.models import Article
from comments.models import Comments
from django.contrib.auth.models import User
from datetime import datetime

# Create your tests here.
class ArticleTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(
            username='jacob', email='jacob@…', password='top_secret')
        self.a = Article(title='test', body='test', author=user)

    def test_get_data_create_and_update(self):
        test_str = "Create: %s Update: %s"%(self.a.date_create, self.a.date_update)
        self.assertEqual(self.a.get_data_create_and_update(), test_str)

    def test_get_data_create_and_update_no_now(self):
        test_str = "Create: %s Update: %s"%(datetime.now(), datetime.now())
        self.assertNotEqual(self.a.get_data_create_and_update(), test_str)

class Article2Test(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='jacob', email='jacob@…', password='top_secret')
        self.a = Article(title='test', body='test', author=self.user)
        self.a.save()

    def test_get_comments(self):
        for i in range(0, 10):
            c=Comments(article=self.a, title=str(i), body=str(i), author=self.user)
            c.save()
        self.assertEqual(self.a.get_comments().count(), 0)

    def test_get_comments_one(self):
        for i in range(0, 10):
            c=Comments(article=self.a, title=str(i), body=str(i), author=self.user)
            c.save()
        c = Comments(article=self.a, title=str(i), body=str(i), author=self.user, is_publick=True)
        c.save()
        self.assertEqual(self.a.get_comments().count(), 1)

    def test_get_comments_ten(self):
        for i in range(0, 10):
            c=Comments(article=self.a, title=str(i), body=str(i), author=self.user, is_publick=True)
            c.save()
        self.assertEqual(self.a.get_comments().count(), 10)
