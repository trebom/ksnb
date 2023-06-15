from rest_framework.views import APIView
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.exceptions import NotFound, NotAuthenticated
from .models import Category
from .serializers import CategorySerializer, CategoryDetailSerializer, CategoryPostSerializer, CategoryUpdateSerializer

# def getCates(cates, upper, pk):
#   cates.append(cate)
    # return 
class Categories(APIView):
    
    def get_categories_recursive(self, category):
        categories = [category]
        subcategories = Category.objects.filter(upper_no=category.pk)
        
        for subcategory in subcategories:
            categories.extend(self.get_categories_recursive(subcategory))
        
        return categories

    def get(self, request):
        cates = []
        roots = Category.objects.filter(upper_no=0)
        
        for root in roots:
            cates.extend(self.get_categories_recursive(root))
        
        serializer = CategorySerializer(cates, many=True)
        return Response(serializer.data)

    def post(self, request):
        if request.user.is_authenticated:
            
            serializer = CategoryPostSerializer(data=request.data)
            try:
                if request.data['upper_no'] != 0:
                    Category.objects.filter(pk=request.data['upper_no']).update(sub=1)
            except Category.DoesNotExist:
                pass
            if serializer.is_valid():
                category = serializer.save(creator=request.user)
                serializer = CategoryPostSerializer(category)
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            raise NotAuthenticated



class CategoryDetail(APIView):
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        category = self.get_object(pk)
        serializer = CategoryDetailSerializer(category)
        return Response(serializer.data)

    def delete(self, request, pk):
        category = self.get_object(pk) # 삭제할 자료
        try:
            temp = Category.objects.get(pk=category.upper_no) # 삭제할 자료의 상위번호
        except Category.DoesNotExist:
            temp = False  
        if not request.user.is_authenticated:
            raise NotAuthenticated
        if category.creator != request.user:
            raise PermissionDenied
        category.delete()
        if temp:
            temp2 = Category.objects.filter(upper_no=temp.pk) # 삭제할 자료의 상위번호의 하위자료
            if temp2.count() == 0:
                temp.sub =0
                temp.save()
        return Response(status=HTTP_204_NO_CONTENT)

class CategoryUpdate(APIView):
    
    def put(self, request, pk, cateName):
        print(request)
        item = get_object_or_404(Category, pk=pk)
        serializer = CategoryUpdateSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
