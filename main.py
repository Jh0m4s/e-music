#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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
#
import webapp2
import jinja2
import os

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

songs = {
    'through the fire and flames' : ["https://www.youtube.com/watch?v=0jgrCKhxE1s", 0,3,4,5],
    'mad world' : ["https://www.youtube.com/watch?v=4N3N1MlvVc4", 5,2,1,0],

}

results = [5,3,2,4]

total = 0
count = 0
ans = ""
key = ""
lowest_diff = 25
#laregest_emo = 0
for song in songs:
    print song
    for score in songs[song][1:]:
        print score
        print results[count]
        total += abs(int(score) - int(results[count]))
        count += 1
    print total
    if(total < lowest_diff):
        lowest_diff = total
        #ans = songs[0]
        key = song
        #print ans
        print song
        print('-----> ' + str(lowest_diff))
    total = 0
    count = 0



class MainHandler(webapp2.RequestHandler):
    def get(self):

        template = jinja_environment.get_template('templates/main.html')
        self.response.write(template.render())

    def post(self):
        r_template = jinja_environment.get_template('templates/results.html')
        self.response.write(r_template.render())



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
