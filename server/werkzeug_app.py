from werkzeug.wrappers import Request, Response
import werkzeug

run_simple = werkzeug.run_simple
@Request.application
def application(request):
    print(f'This web server is running at {request.remote_addr}')
    return Response('A WSGI generated this response!')
if __name__ == '__main__':
    
    run_simple(
        hostname = 'localhost',
        port=5555,
        application = application
    )