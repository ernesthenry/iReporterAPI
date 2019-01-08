import unittest
import json
from api.routes import app, my_red_flags

class BaseTest(unittest.TestCase):
	def setUp(self):
		self.client = app.test_client()


		self.sample_record_data = {
			"createdBy": "hassan",
			"type": "red-flag",
			"location": "Jinja",
			"status": "Under investigation ",
			"Images": "fed.png",
			"Videos": "gfgg.mp4",
			"comment": "This is good"
		}

class RedFlagTest(BaseTest):
	def test_create_red_flag(self):
		response = self.client.post(
			"/api/v1/red-flags",
			data = json.dumps(self.sample_record_data),
			content_type = "application/json"
			)
		self.assertEqual(response.status_code, 200)