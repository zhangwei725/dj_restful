from rest_framework.views import APIView
from common.result import ResultsResponse
from main.main_serializers import FilmSerializer, CateLogSerializer
from main.models import Film, CateLog


# 不分离
# 浏览器 --->index/---->请求视图函数--->从数据库取数据---->将数据结合模板渲染--->返回给客服端


# 分离的流程
# 浏览器 ---->静态文件(.html) ----> ajax请求接口---->从数据库获取数据--->转化json数据---直接响应
# ---->浏览器--->>dom操作--->展示数据
# html    加载数据的东西
class FilmView(APIView):
    def get(self, request):
        try:
            films = Film.objects.all()
            # 转化json
            serializer = FilmSerializer(films, many=True)
            return ResultsResponse.success_to_response(data=serializer.data)
        except Exception as e:
            print(e)
            return ResultsResponse.error_to_response()


class CateView(APIView):
    def get(self, request):
        cate_list = CateLog.objects.all()
        ser = CateLogSerializer(cate_list, many=True)
        return ResultsResponse.success_to_response(data=ser.data)
