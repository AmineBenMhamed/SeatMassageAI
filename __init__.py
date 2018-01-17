# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.
from os.path import dirname

from adapt.intent import IntentBuilder

from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'Amine'

LOGGER = getLogger(__name__)


class SeatMassageSkill(MycroftSkill):
    def __init__(self):
        super(SeatMassageSkill, self).__init__(name="SeatMassageSkill")

    def initialize(self):
        self.load_data_files(dirname(__file__))

        seat_massage_intent = IntentBuilder("SeatMassageIntent"). \
            require("SeatMassageKeyword").build()
        self.register_intent(seat_massage_intent, self.handle_seat_massage_intent)



    def handle_seat_massage_intent(self, message):
        """url = 'http://51.255.38.68/data/58ff3d4bbcc0e1114a8d8c5b'
        r = requests.get(url)
        getData= r.json()
        events = getData['health']['heartRate']
        #format(events)"""
        self.speak(" Seat massage is on ")



    def stop(self):
        pass


def create_skill():
    return SeatMassageSkill()
