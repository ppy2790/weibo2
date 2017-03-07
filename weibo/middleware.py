# -*- coding: utf-8 -*-
import random
from cookies import cookies

class CookiesMiddleware(object):
    """ 换Cookie """

    def process_request(self, request, spider):
        cookie = random.choice(cookies)
        request.cookies = cookie
