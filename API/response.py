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
    request.send_header('Access-Control-Allow-Origin', '*')
    request.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
    request.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type')
    request.end_headers()
    request.wfile.write(json.dumps(data).encode('utf-8'))
