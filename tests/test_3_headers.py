import re

from api.httpbin_api import http_bin_api
from http import HTTPStatus

def test_list_html():
    resp = http_bin_api.list_html()


    assert resp.status_code == HTTPStatus.OK
    assert resp.headers['Content-Type'] == 'text/html; charset=utf-8'
def test_robots():
    resp = http_bin_api.robots()


    assert resp.status_code == HTTPStatus.OK
    assert resp.headers['Content-Type'] == 'text/plain'
    assert re.fullmatch(r'.*User-agent: \*.*Disallow: /deny.*', resp.text, flags=re.DOTALL)


