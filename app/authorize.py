# from functools import wraps
#
# from sanic.response import json
#
#
# def check_request_for_authorization_status(request):
#     # TODO: Define your check, for instance cookie, session.
#     flag = True
#     return flag
#
#
# def authorized():
#     def decorator(f):
#         @wraps(f)
#         async def decorated_function(request, *args, **kwargs):
#             # run some method that checks the request
#             # for the client's authorization status
#             is_authorized = check_request_for_authorization_status(request)
#
#             if is_authorized:
#                 # the user is authorized.
#                 # run the handler method and return the response
#                 response = await f(request, *args, **kwargs)
#                 return response
#             else:
#                 # the user is not authorized.
#                 return json({'status': 'not_authorized'}, 403)
#
#         return decorated_function
#
#     return decorator
