import json


def response(request, data=None, status=200, headers='text/html'):
    if data is None:
        data = {}
    request.send_response(status)
    request.send_header('Content-type', headers)
    request.end_headers()
    request.wfile.write(data)


def json_response(request, data=None, status=200):
    if data is None:
        data = {}
    request.send_response(status)
    request.send_header('Content-type', 'application/json')
    request.end_headers()
    request.wfile.write(json.dumps(data).encode('utf-8'))