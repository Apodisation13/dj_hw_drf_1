# from django.views.decorators.csrf import csrf_exempt
# from car_test.views import car_view
# from car_test.views import CarApiView
# from car_test.views import CarApiViewSet

from measurements.views import ProjectViewSet, MeasurementViewSet
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
# router.register('car', CarApiViewSet)
router.register('project', ProjectViewSet)
router.register('measurment', MeasurementViewSet)


# TODO: настройте роутер и подключите `ProjectViewSet` и `MeasurementViewSet`

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('cars/', csrf_exempt(car_view), name='car')
    # path('cars/', CarApiView.as_view(), name='car')
    path('', include(router.urls))
]
