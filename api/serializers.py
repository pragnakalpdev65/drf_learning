from rest_framework import serializers
from .models import Book, Task, Author, Product

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published_date', 'isbn', 'description', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'desc', 'completed', 'created_at', 'updated_at', 'priority', 'due_date']
        read_only_fields = ['id', 'created_at', 'updated_at']

        priority = serializers.ChoiceField(choices=[
             ('high', 'High'),
             ('medium', 'Medium'),
             ('low', 'Low'),
         ])

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields=['name','bio','email']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        field=['name', 'description', 'price', 'stock', 'is_available', 'created_at','updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

