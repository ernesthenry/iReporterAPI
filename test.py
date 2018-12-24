import unittest
import json
from api.routes import app, my_red_flags

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
			content_type = "application/json"
			)
		#self.assertIn("createdBy", str(response.data))
		self.assertEqual(response.status_code, 200)

	def test_get_redflag(self):
		self.client.post(
			"/api/v1/red-flags",
			data = json.dumps(self.sample_record_data),
			content_type = "application/json"
			)
		response = self.client.get(
			"/api/v1/red-flags",
			content_type = "application/json"
			)
		#data = json.loads(response.data.decode())
		#print(response.data)
		#self.assertEqual(response.data['data']['createdBy'], "ernest")
		self.assertEqual(response.status_code, 200)

	

	def test_edit_location(self):
		new_location = {"location": "Kampala"}
		response = self.client.patch(
			"/api/v1/red-flags/{}/location"
			.format(my_red_flags[0]._id),
			content_type="application/json",
			data=json.dumps(new_location)
			)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(my_red_flags[0].location, "Kampala")


	def test_edit_comment(self):
		new_comment = {"comment": "Tribalism"}
		response = self.client.patch(
			"/api/v1/red-flags/{}/comment"
			.format(my_red_flags[0]._id),
			content_type="application/json",
			data=json.dumps(new_comment)
			)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(my_red_flags[0].comment, "Tribalism")



	def test_delete_record(self):
		response = self.client.delete(
			"/api/v1/red-flags/{}"
			.format(my_red_flags[0]._id))
		self.assertEqual(response.status_code, 204)
		response = self.client.get("/api/v1/red-flags")
		self.assertEqual(response.status_code, 404)

