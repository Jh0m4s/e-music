
import webapp2
import jinja2
import os

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

songs = {
    'through the fire and flames' : ["https://www.youtube.com/watch?v=0jgrCKhxE1s", 0,3,4,5],
    'mad world' : ["https://www.youtube.com/watch?v=4N3N1MlvVc4", 5,2,1,0],

}

class Song():
  def __init__(self, name, link, ratings):
    self.name = name
    self.link = link
    self.ratings = ratings
    self.score = None


  def findscore(self, result):
    dif = []
    for i in range(2):
      if abs(result[i] - self.ratings[i] == 0):
        continue
      dif.append(abs(result[i] - self.ratings[i]))
    if len(dif) == 0:
      self.score = -1
    else:
      total = 0
      for i in dif:
        total += i
      self.score = total / len(dif)


result = [1,1]
songs = [
song1 = Song('Can’t Stop the Feeling', 'https://youtu.be/ru0K8uYEZWw', [1,1 ]),
song1 = Song('doesnt matter the name', 'http::ikwjes,dbfzc', [2,4])
song1 = Song('doesnt matter the name', 'http::ikwjes,dbfzc', [2,4])
song1 = Song('doesnt matter the name', 'http::ikwjes,dbfzc', [2,4])
]
for song in songs:
    song.findscore(result)

song1.findscore(result)
print song1.score



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
