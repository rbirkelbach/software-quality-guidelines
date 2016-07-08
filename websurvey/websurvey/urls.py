"""websurvey URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from websurvey.views import interactive_survey, survey_template, result, resultmarkdown, resultjson, resultcsv
#from django.contrib import admin

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', interactive_survey,name='interactive_survey'),
    url(r'^template.md$', survey_template, name='survey_template'),
    url(r'^result/(?P<result_id>[\w\d]+)/?$', result, name='result'),
    url(r'^result/(?P<result_id>[\w\d]+).md$', resultmarkdown, name='resultmarkdown'),
    url(r'^result/(?P<result_id>[\w\d]+).json$', resultjson, name='resultjson'),
    url(r'^result/(?P<result_id>[\w\d]+).csv$', resultcsv, name='resultcsv'),
]
