from django.test import TestCase
from videos.apps import VideosConfig

class TestVideos(TestCase):

    def test_video_model(self):
        """ Checks whether the app name matches that in the config class name """
        self.assertEqual(VideosConfig.name, "videos")
