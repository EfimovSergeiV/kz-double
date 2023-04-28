"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, re_path
from kzeso.views import *

urlpatterns = [
    # RU
    # path("", index, name='index'),
    # re_path("<slug:path>/", pages_view, name='page_view' ),
    re_path(r'^(.*)$', pages_view, name='pages_view'),
    # path("contacts/", contacts, name='contacts'),
    # path("about/", about, name='about'),
    # path("catalog/", catalog, name='about'),

    # path("catalog/rail-welding-equipment/", ru_rail_welding_equipment, name="ru_rail_welding_equipment"),
    # path("catalog/rail-welding-equipment/<slug:product>/", ru_catalog_product, name='ru_catalog_product'),


    # # # EN
    # path("en/", index, name='index'),
    # path("en/contacts-2/", contacts, name='contacts'),
    # path("en/about/", about, name='about'),
    # path("en/products/", catalog, name='about'),    
    # path("en/products/rail-welding-equipment/", en_rail_welding_equipment, name="en_rail_welding_equipment"),
    # path("en/<slug:product>/", en_catalog_product, name='en_catalog_product'),



    # # Рельсосварка
    # path("catalog/rail-welding-equipment/", rail_welding_equipment, name='rail_welding_equipment'),
    # path("catalog/rail-welding-equipment/k-1000-container-type/", k_1000_container_type, name='k_1000_container_type'),
    # path("catalog/rail-welding-equipment/k-1000/", k_1000, name='k_1000'),
    # path("catalog/rail-welding-equipment/k-1100/", k_1100, name='k_1100'),
    # path("catalog/rail-welding-equipment/k-900-a-1/", k_900_a_1, name='k_900_a_1'),
    # path("catalog/rail-welding-equipment/k920-1/", k920_1, name='k920_1'),
    # path("catalog/rail-welding-equipment/k-922-1/", k_922_1, name='k_922_1'),
    # path("catalog/rail-welding-equipment/k-922-1-kontejnernyj-kompleks-2/", k_922_1_kontejnernyj_kompleks_2, name='k_922_1_kontejnernyj_kompleks_2'),
    # path("catalog/rail-welding-equipment/k-924/", k_924, name='k_924'),
    # path("catalog/rail-welding-equipment/kpm/", kpm, name='kpm'),

    # # EN
    # path("en/", index, name='index'),
    # path("en/contacts-2/", contacts, name='contacts'),
    # path("en/about/", about, name='about'),
    # path("en/products/", catalog, name='about'),    

    # # Рельсосварка
    # path("en/products/rail-welding-equipment/", rail_welding_equipment, name='rail_welding_equipment'),
    # path("en/k-1000-container-type/", k_1000_container_type, name='k_1000_container_type'),
    # path("en/k-1000/", k_1000, name='k_1000'),
    # path("en/k-1100/", k_1100, name='k_1100'),
    # path("en/k-900-a-1/", k_900_a_1, name='k_900_a_1'),
    # path("en/k920-1/", k920_1, name='k920_1'),
    # path("en/k-922-1/", k_922_1, name='k_922_1'),
    # path("en/k-922-1-kontejnernyj-kompleks-2/", k_922_1_kontejnernyj_kompleks_2, name='k_922_1_kontejnernyj_kompleks_2'),
    # path("en/k-924/", k_924, name='k_924'),
    # path("en/kpm/", kpm, name='kpm'),

]
