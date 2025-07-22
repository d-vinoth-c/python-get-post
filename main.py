import json

def main(request):
    path = request.path
    method = request.method

    if path == '/hello' and method == 'GET':
        return ('Hello from Python (no Flask)!', 200, {'Content-Type': 'text/plain'})

    elif path == '/echo' and method == 'POST':
        try:
            data = request.get_json(force=True)
            response = {'received': data}
            return (json.dumps(response), 200, {'Content-Type': 'application/json'})
        except Exception as e:
            return (json.dumps({'error': str(e)}), 400, {'Content-Type': 'application/json'})

    else:
        return ('Not Found', 404, {'Content-Type': 'text/plain'})
