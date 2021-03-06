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

from collections import defaultdict
import os
from django.conf import settings
from django.core.management.base import NoArgsCommand
from django.db import models
from django.db.models.loading import cache


class Command(NoArgsCommand):
    help = "Prints and remove a list of all files in MEDIA_ROOT that are not referenced in the database."

    def handle_noargs(self, **options):

        if settings.MEDIA_ROOT == '':
            print("MEDIA_ROOT is not set, nothing to do")
            return

        # Get a list of all files under MEDIA_ROOT
        media = []
        for root, dirs, files in os.walk(settings.MEDIA_ROOT):
            for f in files:
                if ('geoserver_icons' not in root) and ('resized' not in root):
                    media.append(os.path.abspath(os.path.join(root, f)))

        # Get list of all fields (value) for each model (key)
        # that is a FileField or subclass of a FileField
        model_dict = defaultdict(list)
        for app in cache.get_apps():
            model_list = cache.get_models(app)
            for model in model_list:
                for field in model._meta.fields:
                    if issubclass(field.__class__, models.FileField):
                        model_dict[model].append(field)

        # Get a list of all files referenced in the database
        referenced = []
        for model in model_dict:
            all = model.objects.all().iterator()
            for object in all:
                for field in model_dict[model]:
                    target_file = getattr(object, field.name)
                    if target_file:
                        referenced.append(os.path.abspath(target_file.path))

        # Print each file in MEDIA_ROOT that is not referenced in the database
        c = 0
        for m in media:
            if m not in referenced:
                print 'Removing image %s' % m
        os.remove(m)
        c = c + 1

        print 'Removed %s images, from a total of %s (referenced %s)' % (c, len(media), len(referenced))
