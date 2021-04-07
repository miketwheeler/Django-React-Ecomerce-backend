from django.urls import path
from base.views import product_views as views

# url patterns for products 
urlpatterns = [
	# paths for shop browsing
	path('', views.getProducts, name="products"),

	# CRUD paths for products
	path('create/', views.createProduct, name="product-create"),
	path('upload/', views.uploadImage, name="image-upload"),

	path('<str/:pk/reviews', views.createProductReview, name="create-review"),
	
	path('<str:pk>/', views.getProduct, name="product"),
	path('update/<str:pk>/', views.updateProduct, name="product-update"),
	path('delete/<str:pk>/', views.deleteProduct, name="product-delete"),
]