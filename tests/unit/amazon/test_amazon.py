import unittest
from unittest.mock import Mock, patch

from afiliepy.amazon import amazon

class TestAmazon(unittest.TestCase):
    @patch('urllib.request.OpenerDirector.open')
    def test_replace(self, mock_request):
        mock_response = Mock()
        mock_response.status = 301
        mock_response.headers = {
            'Location': 'https://amazon.com/db/111111?tag=aaaa'
        }
        mock_request.return_value = mock_response
        self.assertEqual(amazon.replace('https://amzn.to/example', 'new_tag'), 'https://amazon.com/db/111111?language=ja_JP&tag=new_tag')
