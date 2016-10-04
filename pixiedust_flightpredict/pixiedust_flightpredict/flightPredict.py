# -------------------------------------------------------------------------------
# Copyright IBM Corp. 2016
# 
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
# http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# -------------------------------------------------------------------------------
from pixiedust.display.display import *

class PixieDustFlightPredict(Display):
  def runFlightPredict(self):
    flights = self.options.get("flights")
    #todo: start flight predict

  def doRender(self, handlerId):
    self.addProfilingTime = False
    flights = self.options.get("flights")

    if flights is None:
      #self._addHTMLTemplate("flightsScript.html")
      self._addHTMLTemplate("flights.html")

    else:
      self.runFlightPredict()