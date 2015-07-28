# Copyright 2015 Google Inc. All Rights Reserved.
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

import datetime
import unittest

import gsf


class AttitudeTest(unittest.TestCase):

  def testEmptyAttitude(self):
    data = (
        0x00, 0x00, 0x00, 0x03, 0x00, 0x00, 0x00, 0x04, 0x00, 0x00, 0x00,
        0x00)
    attitude = gsf.GsfAttitude(''.join(chr(v) for v in data))
    self.assertEqual(attitude['record_type'], gsf.GSF_ATTITUDE)
    self.assertEqual(attitude['sec'], 3)
    self.assertEqual(attitude['nsec'], 4)

  def testAttitudeLengthOneZeroValues(self):
    data = (
        0x00, 0x00, 0x00, 0x05, 0x00, 0x00, 0x00, 0x06, 0x00, 0x01, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00)

    attitude = gsf.GsfAttitude(''.join(chr(v) for v in data))
    self.assertEqual(attitude['record_type'], gsf.GSF_ATTITUDE)
    self.assertEqual(attitude['sec'], 5)
    self.assertEqual(attitude['nsec'], 6)
    self.assertEqual(attitude['times'],
                     [datetime.datetime(1970, 1, 1, 0, 0, 5)])
    self.assertEqual(attitude['pitches'], [0.0])
    self.assertEqual(attitude['rolls'], [0.0])
    self.assertEqual(attitude['heaves'], [0.0])
    self.assertEqual(attitude['headings'], [0.0])

  def testAttitudeLengthOneNonZero(self):
    data = (
        0x00, 0x00, 0x00, 0x09, 0x00, 0x00, 0x00, 0x0A, 0x00, 0x01, 0x00,
        0x00, 0xFF, 0x88, 0xFE, 0xAC, 0xFD, 0xD0, 0x03, 0x0C)

    attitude = gsf.GsfAttitude(''.join(chr(v) for v in data))
    self.assertEqual(attitude['record_type'], gsf.GSF_ATTITUDE)
    self.assertEqual(attitude['sec'], 9)
    self.assertEqual(attitude['nsec'], 10)
    self.assertEqual(attitude['times'],
                     [datetime.datetime(1970, 1, 1, 0, 0, 9)])
    self.assertEqual(attitude['pitches'], [-1.2])
    self.assertEqual(attitude['rolls'], [-3.4])
    self.assertEqual(attitude['heaves'], [-5.6])
    self.assertEqual(attitude['headings'], [7.8])

  def testAttitudeLengthTwo(self):
    data = (
        0x55, 0xB6, 0x65, 0x36, 0x00, 0x00, 0x00, 0x01, 0x00, 0x02, 0x00,
        0x00, 0x00, 0x78, 0xD8, 0xE6, 0xB1, 0xCC, 0x46, 0xB4, 0x04, 0x42,
        0xFE, 0xAC, 0x27, 0x24, 0xB1, 0xC2, 0x8C, 0x3C, 0x00, 0x00)

    attitude = gsf.GsfAttitude(''.join(chr(v) for v in data))
    self.assertEqual(attitude['record_type'], gsf.GSF_ATTITUDE)
    self.assertEqual(attitude['sec'], 1438016822)
    self.assertEqual(attitude['nsec'], 1)
    self.assertEqual(attitude['times'],
                     [datetime.datetime(2015, 7, 27, 17, 7, 2),
                      datetime.datetime(2015, 7, 27, 17, 7, 3, 90000)]),
    self.assertEqual(attitude['pitches'], [1.2, -3.4])
    self.assertEqual(attitude['rolls'], [-100.1, 100.2])
    self.assertEqual(attitude['heaves'], [-200.2, -200.3])
    self.assertEqual(attitude['headings'], [181, 359])


class CommentTest(unittest.TestCase):

  def testEmptyComment(self):
    data = (
        0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x02, 0x00, 0x00, 0x00,
        0x00)
    comment = gsf.GsfComment(''.join(chr(v) for v in data))
    self.assertEqual(comment['record_type'], gsf.GSF_COMMENT)
    self.assertEqual(comment['sec'], 1)
    self.assertEqual(comment['nsec'], 2)
    self.assertEqual(comment['comment'], '')

  def test100aComment(self):
    data = (
        0x00, 0x00, 0x00, 0x08, 0x00, 0x00, 0x00, 0x09, 0x00, 0x00, 0x00,
        0x64, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61,
        0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61,
        0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61,
        0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61,
        0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61,
        0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61,
        0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61,
        0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61,
        0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61,
        0x61, 0x61)
    comment = gsf.GsfComment(''.join(chr(v) for v in data))
    self.assertEqual(comment['record_type'], gsf.GSF_COMMENT)
    self.assertEqual(comment['sec'], 8)
    self.assertEqual(comment['nsec'], 9)
    self.assertEqual(comment['comment'], 'a'*100)


class HistoryTest(unittest.TestCase):

  def testAnything(self):
    data = (
        0x00, 0x00, 0x00, 0x03, 0x00, 0x00, 0x00, 0x04, 0x00,
        0x0A, 0x68, 0x6F, 0x73, 0x74, 0x20, 0x6E, 0x61, 0x6D,
        0x65, 0x00, 0x00, 0x0E, 0x6F, 0x70, 0x65, 0x72, 0x61,
        0x74, 0x6F, 0x72, 0x20, 0x4E, 0x41, 0x4D, 0x45, 0x00,
        0x00, 0x0D, 0x63, 0x6F, 0x6D, 0x6D, 0x61, 0x6E, 0x64,
        0x20, 0x6C, 0x69, 0x6E, 0x65, 0x00, 0x00, 0x07, 0x63,
        0x6F, 0x6D, 0x6D, 0x65, 0x6E, 0x74)

    history = gsf.GsfHistory(''.join(chr(v) for v in data))
    self.assertEqual(history['record_type'], gsf.GSF_HISTORY)
    self.assertEqual(history['sec'], 3)
    self.assertEqual(history['nsec'], 4)
    self.assertEqual(history['name'], 'host name')
    self.assertEqual(history['operator'], 'operator NAME')
    self.assertEqual(history['command'], 'command line')
    self.assertEqual(history['comment'], 'comment')

  def testAllFieldsEmpty(self):
    data = (
        0x00, 0x00, 0x00, 0x05, 0x00, 0x00, 0x00, 0x06, 0x00, 0x01, 0x00,
        0x00, 0x01, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00)

    history = gsf.GsfHistory(''.join(chr(v) for v in data))
    self.assertEqual(history['record_type'], gsf.GSF_HISTORY)
    self.assertEqual(history['sec'], 5)
    self.assertEqual(history['nsec'], 6)
    self.assertEqual(history['name'], '')
    self.assertEqual(history['operator'], '')
    self.assertEqual(history['command'], '')
    self.assertEqual(history['comment'], '')

if __name__ == '__main__':
  unittest.main()
