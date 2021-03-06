# Copyright (C) 2009 Daniel Carvalho <idnael@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __pyjamas__ import JS

from pyjamas.gmaps.Utils import dictToJs, createListenerMethods


def InfoWindow(content):
    infoWindow = JS("""new $wnd.google.maps.InfoWindow(@{{content}})""")

    createListenerMethods(infoWindow)

    return infoWindow


def InfoWindowOptions(**params):
    return dictToJs(params)
