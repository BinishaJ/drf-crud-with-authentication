from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.authentication import SessionAuthentication
from rest_framework import permissions, authentication

# from rest_framework. 
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([SessionAuthentication])
def apiOverview(request):
    url = 'http://127.0.0.1:8000/api/'
    try:
        if request.user.is_staff:
            api_urls = {
                'Book List': url + 'book-list',
                'Book Create': url + 'book-create',
                'Book Read': url + 'book-read/<int:pk>',
                'Book Update': url + 'book-update/<int:pk>',
                'Book Delete': url + 'book-delete/<int:pk>',
                'Author List': url + 'author-list',
                'Author Create': url + 'author-create',
                'Author Read': url + 'author-read/<int:pk>',
                'Author Update': url + 'author-update/<int:pk>',
                'Author Delete': url + 'author-delete/<int:pk>'
            }
        else:
            api_urls = {
                'Book List': url + 'book-list',
                'Author List': url + 'author-list'
            }
        return Response(api_urls, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)


# books

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def bookList(request):
    try:
        books = Book.objects.all()
        serializer = BookSerializer(books,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def bookRead(request,pk):
    try:
        book = Book.objects.get(id=pk)
        serializer = BookSerializer(book,many=False)
        return Response(serializer.data,status=status.HTTP_200_OK)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAdminUser])
def bookCreate(request):
    serializer = BookSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def bookUpdate(request,pk):
    book = Book.objects.get(id=pk)
    serializer = BookSerializer(instance=book, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def bookDelete(request,pk):
    try:
        book = Book.objects.get(id=pk)
        book.delete()

        return Response("Item Deleted",status=status.HTTP_204_NO_CONTENT)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)


# authors

# @api_view(['GET'])
# @permission_classes([IsAdminUser])
# def authorList(request):
#     try:
#         authors = Author.objects.all()
#         serializer = AuthorSerializer(authors,many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     except Author.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     except:
#         return Response(status=status.HTTP_400_BAD_REQUEST)

class authorList(APIView):
    permission_classes = [permissions.IsAdminUser]
    def get(self, request, format=None):
        try:
            authors = Author.objects.all()
            serializer = AuthorSerializer(authors,many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Author.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def authorRead(request,pk):
    try:
        author = Author.objects.get(id=pk)
        serializer = AuthorSerializer(author,many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Author.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)


class authorCreate(APIView):
    permission_classes = [permissions.IsAdminUser]
    authentication_classes = [authentication.SessionAuthentication]
    def post(self, request, format=None):
        try:
            serializer = AuthorSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response('Error occured', status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
def authorUpdate(request,pk):
    author = Author.objects.get(id=pk)
    serializer = AuthorSerializer(instance=author, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def authorDelete(request,pk):
    try:
        author = Author.objects.get(id=pk)
        author.delete()

        return Response("Item Deleted",status=status.HTTP_204_NO_CONTENT)
    except Author.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)