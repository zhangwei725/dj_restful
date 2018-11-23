from django.http import JsonResponse
from rest_framework import status

# 不需要使用类的字段 静态字段
# def success_to_response(data, status=200, msg='success'):
#     res = {'status': status, 'msg': msg, 'data': data}
#     return JsonResponse(res)
#
#
# def error_to_response(status=404, msg='error'):
#     res = {'status': status, 'msg': msg}
#     return JsonResponse(res)

# 账号密码错误 1
# 该账号已被注册  2
# http规定状态
# 表示账号密码错误
STATUS_LOGIN_CODE = 1
#  表示用户已存在
STATUS_USER_EXITS_CODE = 2

MSG_SUCCESS_STR = 'ok'


class ResultsResponse:
    @staticmethod
    def success_to_response(data, status=status.HTTP_200_OK, msg=MSG_SUCCESS_STR):
        res = {'status': status, 'msg': msg, 'data': data}
        return JsonResponse(res)

    @staticmethod
    def error_to_response(status=404, msg='error'):
        res = {'status': status, 'msg': msg}
        return JsonResponse(res)
