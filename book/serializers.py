from rest_framework import serializers
from .models import Book,Author
# from rest_framework.serializers import HyperlinkedIdentityField
class Authorserializer(serializers.ModelSerializer):
    # author=serializers.CharField()
    class Meta:
            model=Author
            fields=["author"]

class BookSerializer(serializers.HyperlinkedModelSerializer):

    author=Authorserializer()

    url = serializers.HyperlinkedIdentityField( 
        view_name='details', 
        lookup_field='pk'
    ) 

    class Meta:
        model=Book
        fields=["id","url","bookname","author","pages","content"]

    def create(self, validated_data):
            author = validated_data.pop('author')
            author, created = Author.objects.get_or_create(author=author['author'])
            author.save()
            book = Book.objects.create(author=author,**validated_data)
            return book
    

    def update(self, instance, validated_data):
        author = validated_data.pop('author')
        
        author = instance.author

        instance.bookname = validated_data.get('bookname', instance.bookname)
        instance.pages = validated_data.get('pages', instance.pages)
        instance.content = validated_data.get('content', instance.content)

        instance.save()
        return instance

    # def update(self, instance, validated_data):
    #             author = validated_data.pop('author')               
    #             author = instance.author
    #             for k, v in author.items():
    #                 setattr(author, k, v)
    #             author.save()
    #             instance.bookname = validated_data.get('bookname', instance.bookname)
    #             instance.pages= validated_data.get('pages', instance.pages)
    #             instance.content = validated_data['content',instance.content]
    #             instance.save()
    #             return instance


    