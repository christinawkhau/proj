
    
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import debug_toolbar  

from products import views





urlpatterns = [
    path('', include("pages.urls", namespace="pages")),
    path('products/', include("products.urls", namespace="products")),  
    path('store/', views.store, name='store'),
  
    #path('contacts/', include("contacts.urls", namespace="contacts")),
    #path('accounts/', include("accounts.urls", namespace="accounts")),
    path('admin/', admin.site.urls),
] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)                                             

# ✅ Only include debug toolbar in development
if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

# ✅ Serve media files
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header="Shop Admin"
admin.site.site_title="Shop Admin Portal"
admin.site.index_title="Welcome to Shop Center Admin Portal"






