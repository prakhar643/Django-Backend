from django.contrib.auth.models import User
from django.http import HttpResponse
from django.test import RequestFactory, TestCase

from blog.middleware import CurrentUserMiddleware, RequestIDMiddleware, get_current_user


def simple_view(request):
    return HttpResponse('ok')


class MiddlewareTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_current_user_middleware_sets_thread_local_user(self):
        request = self.factory.get('/')
        user = User.objects.create_user(username='tester', password='password')
        request.user = user

        middleware = CurrentUserMiddleware(simple_view)
        response = middleware(request)

        self.assertEqual(response.status_code, 200)
        self.assertIs(get_current_user(), user)

    def test_request_id_middleware_adds_header_and_request_attr(self):
        request = self.factory.get('/')

        middleware = RequestIDMiddleware(simple_view)
        response = middleware(request)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(hasattr(request, 'request_id'))
        self.assertTrue(response.has_header('X-Request-ID'))
        self.assertEqual(response['X-Request-ID'], request.request_id)

    def test_request_id_middleware_adds_header_on_real_url(self):
        response = self.client.get('/ping/')

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.has_header('X-Request-ID'))
