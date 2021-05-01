from mixer.backend.django import mixer
import pytest

from django.test import TestCase

@pytest.mark.django_db
class TestModel:

	def test_post_sell_code(self):
		p = mixer.blend('post.Post', post_type='sell')
		assert p.code == "sell-1"

	def test_post_lost_code(self):
		p = mixer.blend('post.Post', post_type='lost')
		assert p.code == 'lost-1'

	def test_post_found_code(self):
		p = mixer.blend('post.Post', post_type='found')
		assert p.code == 'found-1'

	def test_post_sell_str(self):
		p = mixer.blend('post.Post', post_type='sell')
		assert str(p) == "sell-1"

	def test_post_lost_str(self):
		p = mixer.blend('post.Post', post_type='lost')
		assert str(p) == 'lost-1'

	def test_post_found_str(self):
		p = mixer.blend('post.Post', post_type='found')
		assert str(p) == 'found-1'

	def test_category_str(self):
		c = mixer.blend('post.Category', title='Test1')
		assert str(c) == 'Test1'

	def test_contact_message_str(self):
		c = mixer.blend('post.ContactMessage', name='Test1')
		assert str(c) == '1-Test1'
