import unittest
from unittest.mock import patch

import blog

class TestBlog(unittest.TestCase):
    """ Returns predefined JSON response
    """
    @patch('blog.Blog')
    def test_blog_post(self, MockBlog):
        blog = MockBlog()

        blog.posts.return_value = [
            {
                'userId': 1,
                'id': 1,
                'title': 'Hello World'
            }
        ]

        response = blog.posts()
        self.assertIsNotNone(response)
        self.assertIsInstance(response[0], dict)

        # assert MockBlog is blog.Blog
        assert MockBlog.called
        blog.posts.assert_called_with()  # called with no arguments
        blog.posts.assert_called_once_with()

        blog.reset_mock()
        blog.posts.assert_not_called()


if __name__ == '__main__':
    unittest.main()