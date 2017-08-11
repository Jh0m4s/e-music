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
    for i in range(5):
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

song1 = Song('Can\'t Stop the Feeling', 'https://www.youtube.com/embed/gWjmyVQwgRw?&autoplay=1', [1,5,1,1,3])
song2 = Song('Opening the Gates', 'https://www.youtube.com/embed/Q1B9xShJ2kE?&autoplay=1', [1,2,3,5,1])
song3 = Song('Mad World', 'https://www.youtube.com/embed/hW93CV6m-JU?&autoplay=1', [1,1,5,1,1])
song4 = Song('Marble Machine', 'https://www.youtube.com/embed/IvUU8joBb1Q?&autoplay=1', [1,4,2,4,2])
song5 = Song('Call Me', 'https://www.youtube.com/embed/OugHoTRceyE?&autoplay=1', [1,1,4,1,2])
song6 = Song('September', 'https://www.youtube.com/embed/gZorFBddby0?&autoplay=1', [1,4,1,1,4])
song7 = Song('Alone Time', 'https://www.youtube.com/embed/cw8KbFHPcYU?&autoplay=1', [1,1,2,1,3])
song8 = Song('Breaking Inside', 'https://www.youtube.com/embed/LEx-HYsmOQ8?&autoplay=1', [2,1,4,1,1])
song9 = Song('Geronimo', 'https://www.youtube.com/embed/E-SeaCZE2TM?&autoplay=1', [1,3,2,1,4])
song10 = Song('Walk On Water', 'https://www.youtube.com/embed/hpDKd40Y71w?&autoplay=1', [1,1,3,2,1])
song11 = Song('Gold', 'https://www.youtube.com/embed/TC2YeGEoN1w?&autoplay=1', [1,3,2,1,2])
song12 = Song('Dapperblook', 'https://www.youtube.com/embed/yeJx04_47Lc?&autoplay=1', [1,4,1,4,4])
song13 = Song('Through the Fire and Flames', 'https://www.youtube.com/embed/Wbrrma9Cutk?&autoplay=1', [1,1,1,1,5])
song14 = Song('Monster', 'https://www.youtube.com/embed/u9NStVkSCuk?&autoplay=1', [5,1,2,1,3])
song15 = Song('Break','https://www.youtube.com/embed/SJJSQD12v04?&autoplay=1', [3,1,2,1,4])
song16 = Song('Enemies', 'https://www.youtube.com/embed/3z9Kmla_ceA?&autoplay=1', [5,1,1,1,4])
song17 = Song('Believer', 'https://www.youtube.com/embed/9MJAg0VDgO0?&autoplay=1', [3,1,2,1,3])
song18 = Song('Fire', 'https://www.youtube.com/embed/uQHGYgpg3Pg?&autoplay=1', [4,1,2,1,4])
song19 = Song('Victorious', 'https://www.youtube.com/embed/agG-yNlFwCY?&autoplay=1', [2,2,1,1,4])
song20 = Song('One Me Two Hearts', 'https://www.youtube.com/embed/DnQ-Nk8qHSk?&autoplay=1', [1,2,2,1,4])
song21 = Song('Trash Candy', 'https://www.youtube.com/embed/dHmhJcMUTj8?&autoplay=1', [2,2,1,1,3])
song22 = Song('Thnks fr Th Mmrs', 'https://www.youtube.com/embed/3jx7SF65wbs?&autoplay=1', [1,4,2,1,5])
song23 = Song('Ignorance', 'https://www.youtube.com/embed/6GKjW-TCnu0?&autoplay=1', [4,1,3,1,4])
song24 = Song('All I Want', 'https://www.youtube.com/embed/L2RBYHTqHfA?&autoplay=1', [2,1,3,1,5])
song25 = Song('Roar', 'https://www.youtube.com/embed/n2f501YWxso?&autoplay=1', [2,2,2,1,3])
song26 = Song('Immigrants (We Get The Job Done)', 'https://www.youtube.com/embed/6_35a7sn6ds?&autoplay=1', [4,2,3,1,4])
song27 = Song('Diamond Eyes', 'https://www.youtube.com/embed/Mj_hApbc5qg?&autoplay=1', [4,2,2,1,4])
song28 = Song('Hero', 'https://www.youtube.com/embed/RRkIQ1Djlbs?&autoplay=1', [2,1,2,1,4])
song29 = Song('I\'m Alive', 'https://www.youtube.com/embed/Z7r4jtEaRG0?&autoplay=1', [4,1,1,1,5])
song30 = Song('Last One Standing', 'https://www.youtube.com/embed/uurkmfkKodg?&autoplay=1', [3,1,1,1,4])
song31 = Song('Speak With Your Heart', 'https://www.youtube.com/embed/laHlg3OQO8E?&autoplay=1', [1,4,2,1,4])
song32 = Song('Sir Duke', 'https://www.youtube.com/embed/6sIjSNTS7Fs?&autoplay=1', [1,5,1,1,2])
song33 = Song('I Wish You Well', 'https://www.youtube.com/embed/5Wq3Fzj1FhE?&autoplay=1', [1,2,3,1,2])
song34 = Song('CAN\'T HOLD US', 'https://www.youtube.com/embed/Nhvm8r75aMo?&autoplay=1', [1,3,1,1,4])
song35 = Song('Don\'t You Worry \'Bout A Thing', 'https://www.youtube.com/embed/I038NxV1Mtg?&autoplay=1', [1,4,1,1,3])
song36 = Song('I\'m Still Standing', 'https://www.youtube.com/embed/nYCOA2jQ-XA?&autoplay=1', [1,4,3,1,4])
song37 = Song('My Way', 'https://www.youtube.com/embed/bShYtQVINBY?&autoplay=1', [1,2,2,1,2])
song38 = Song('Shake It Off', 'https://www.youtube.com/embed/DrFZ6fXyia0?&autoplay=1', [1,4,2,1,4])
song39 = Song('Centuries', 'https://www.youtube.com/embed/dZEnQogAd8U?&autoplay=1', [3,1,3,1,4])
song40 = Song('Perfect Circle', 'https://www.youtube.com/embed/lX8QVBl-ZG0?&autoplay=1', [1,1,2,5,2])
song41 = Song('Middle Ground', 'https://www.youtube.com/embed/qYCznM6Hlys?&autoplay=1', [1,2,3,1,3])
song42 = Song('See You Again', 'https://www.youtube.com/embed/LWfFm-fsXIc?&autoplay=1', [1,2,4,2,3])
song43 = Song('Stay With Me', 'https://www.youtube.com/embed/iGxvQGgkpMc?&autoplay=1', [1,1,4,2,1])
# song44 = Song()
# song45 = Song()
# song46 = Song()
# song47 = Song()
# song48 = Song()

songs = [song1, song2, song3, song4, song5, song6, song7, song8, song9, song10, song11, song12, song13, song14, song15, song16, song17, song18, song19, song20, song21, song22, song23, song24, song25, song26, song27, song28, song29, song30, song31, song32, song33, song34, song35, song36, song37, song38, song39, song40, song41, song42, song43]







class MainHandler(webapp2.RequestHandler):
    def get(self):

        template = jinja_environment.get_template('templates/main.html')
        self.response.write(template.render())

    def post(self):
        r_template = jinja_environment.get_template('templates/results.html')
        angry = int(self.request.get('angryMood'))
        happy = int(self.request.get('happinessMood'))
        sad = int(self.request.get('sadnessMood'))
        focus = int(self.request.get('focusMood'))
        pace = int(self.request.get('paceMood'))
        result = [angry, happy, sad, focus, pace]
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
