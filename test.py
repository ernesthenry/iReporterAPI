import unittest
import json
from api.routes import app 


class BaseTest(unittest.TestCase):
	def setUp(self):
		self.client = app.test_client()


		self.sample_record_data = {
            "createdBy": "ernest",
            "type": "red-flag",
            "location": "kampala",
            "status": "draft",
            "Images": "gfg.png",
            "Videos": "hg.m4",
            "comment": "This is a red-flag record"
			}

class RedFlagTest(BaseTest):
	def test_create_red_flag(self):
		response = self.client.post(
			"/api/v1/red-flags",
			data = json.dumps(self.sample_record_data),
			content_type = "application/json")
		self.assertIn("ernest", str(response.data))
		self.assertEqual(response.status_code, 200)

	def test_get_redflag(self):
		self.client.post(
			"/api/v1/red-flags",
			data = json.dumps(self.sample_record_data),
			content_type = "application/json")
		response = self.client.get(
			"/api/v1/red-flags",
			content_type = "application/json"
			)
		#data = json.loads(response.data.decode())
		#print(response.data)
		#self.assertEqual(response.data['data']['createdBy'], "ernest")
		self.assertEqual(response.status_code, 200)



