#!/usr/bin/env python
#########################################################################
#
# Copyright (C) 2012-2015 Paolo Corti, pcorti@gmail.com
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

from django.conf.urls import url, include
from .api import TrainingResource, TagResourceSimple

from geonode.api import api as geonode_api
from geonode.api.urls import api

from trainings import views as trainings


api.api_name = 'api'
api.register(TrainingResource())
api.unregister(geonode_api.TagResource())
api.register(TagResourceSimple())

urlpatterns = [
    url(
        r'^upload', trainings.training_upload,
        name='training_upload'
    ),
    url(
        r'^check$', trainings.training_download_check,
        name='training_download_check'
    ),
    url(
        r'^$', trainings.trainings_browse,
        name='trainings_browse'
    ),
    url(
        r'^(?P<keyword>[^/]*)$', trainings.trainings_browse,
        name='trainings_browse'
    ),
    url(
        r'^(?P<id>\d+)/$', trainings.training_detail,
        name='training_detail'
    ),
    url(
        r'^(?P<id>\d+)/download/$', trainings.training_download,
        name='training_download'
    ),
    url(
        r'^api/', include(api.urls)
    ),
]
