import webapp2
import jinja2
import os

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))


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

song1 = Song('Can\'t Stop the Feeling', 'https//www.youtube.com/embed/gWjmyVQwgRw', [5,1,1,3])
song2 = Song('Opening the Gates', 'https://www.youtube.com/embed/Q1B9xShJ2kE', [2,3,5,1])
song3 = Song('Mad World', 'https://www.youtube.com/embed/hW93CV6m-JU', [1,5,1,1])
song4 = Song('Marble Machine', 'https://www.youtube.com/embed/IvUU8joBb1Q', [4,2,4,2])
song5 = Song('Call Me', 'https://www.youtube.com/embed/OugHoTRceyE', [1,5,2,2])

songs = [song1, song2, song3, song4, song5]







class MainHandler(webapp2.RequestHandler):
    def get(self):

        template = jinja_environment.get_template('templates/main.html')
        self.response.write(template.render())

    def post(self):
        r_template = jinja_environment.get_template('templates/results.html')
        happy = self.request.get('happinessMood')
        sad = self.request.get('sadnessMood')
        focus = self.request.get('focusMood')
        pace = self.request.get('paceMood')
        result = [int(happy), int(sad), int(focus), int(pace)] 
        song_name=""
        song_link=""
        lower_score = 20

        for song in songs:
            song.findscore(result)
            if song.score < lower_score:
                lower_score = song.score
                song_name = song.name
                song_link = song.link
        pass_params = {
            'song_name' : song_name,
            'song_link' : song_link
            }


        self.response.write(r_template.render(pass_params))



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
