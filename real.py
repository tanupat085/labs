from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.uix.button import  Button
from kivy.core.window import Window
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.lang import Builder
from random import randint
#from kivy.core.audio import SoundLoader


import random
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
Builder.load_file(dir_path + '/real.kv')

Pause_1 = False


class Checkup(Widget):
    ccu1 = NumericProperty(0)
    ccu2 = NumericProperty(0)
    def checkup_item(self,item1,item2):
        if self.collide_widget(item1) :
            self.ccu1 = 1
            

        if self.collide_widget(item2) :
            self.ccu2 = 1
            
class empu(Widget):
    pass
class empd(Widget):
    pass

class Checkdown(Widget):
    ccd1 = NumericProperty(0)
    ccd2 = NumericProperty(0)

    def checkdown_item(self,item1,item2):
        if self.collide_widget(item1) :
        
            self.ccd1 = 1
            self.ccd2 = 0
        if self.collide_widget(item2) :
            self.ccd1 = 0
            self.ccd2 = 1

class Level(Widget) :
    pass

class Background_Bonus(Widget):
    pass


class Pushup(Widget):
    upup = bool
    checked1 = NumericProperty(0)
    checked2 = NumericProperty(0)



    image2 = ObjectProperty(None)

    def change(self,chg):
        if chg == True :
            self.image2.source = "realup.png"
        if chg == False :
            self.image2.source = "realdown.png"





    def send_item1(self,item1):
        
        if self.collide_widget(item1) and self.upup == True and self.checked1 == 0 :
            
            vx, vy = item1.velocity
            bounced = Vector( 0  , 4 )
            item1.velocity = bounced.x, bounced.y
            self.checked1 = 1
            
            
        if self.collide_widget(item1)  and self.upup == False and self.checked1 == 0 :
            
            vx, vy = item1.velocity
            bounced = Vector( 0  , -4 )
            item1.velocity = bounced.x, bounced.y
            self.checked1 = 1

    def send_item2(self,item2) :
        
        if self.collide_widget(item2) and self.upup == True and self.checked2 == 0 :
            
            vx, vy = item2.velocity
            bounced = Vector( 0  , 4 )
            item2.velocity = bounced.x, bounced.y
            self.checked2 = 1
           
        if self.collide_widget(item2)  and self.upup == False and self.checked2 == 0:
            
            vx, vy = item2.velocity
            bounced = Vector( 0  , -4 )
            item2.velocity = bounced.x, bounced.y
            self.checked2 = 1
             
            
        

class Gamemain(Widget):
    
    item1 = ObjectProperty(None)
    item2 = ObjectProperty(None)


    time1 = NumericProperty(0)
    time2 = NumericProperty(0)
    time3 = NumericProperty(0)

    image = ObjectProperty(None)
    scoretext = ObjectProperty(Label)
    score = NumericProperty(0)
    scoretextmiss = ObjectProperty(Label)
    scoremiss = NumericProperty(0)
    push = ObjectProperty(None)
    checkup = ObjectProperty(None)
    checkdown = ObjectProperty(None)
   # sound1 = SoundLoader.load("musmus.wav")
   # sound2 = SoundLoader.load("music.wav")

    clickbutt = ObjectProperty(None)
    chg = bool

    pausebutt = ObjectProperty(None)
    resumebutt = ObjectProperty(None)



    def reitem1(self):
        self.item1.center_x = self.center_x * 1.35
        self.item1.center_y = self.center_y
        self.time1 = -100
        self.serve1()
    def reitem2(self):
        self.item2.center_x = self.center_x * 1.35
        self.item2.center_y = self.center_y
        self.time2 = -100
        self.serve2()

    
    def serve1(self,vel = (-4,0)):
        
        self.item1.velocity = vel
        self.time1 = -100
        self.item1.setpic()
       
        
    def serve2(self,vel = (-4,0)):
        
        self.item2.velocity = vel    
        self.time2 = 0
        self.item2.setpic()

    def checkpointupcanre1(self):
        
        if self.item1.itemtype == 0 :
            
            self.score += 10
           # self.sound1.play()

        if self.item1.itemtype == 1:
            
            self.score -= 15
            self.scoremiss += 1
           # self.sound1.play()

    def checkpointupcanre2(self) :

        if self.item2.itemtype == 0 :
            
            self.score += 10
         #   self.sound1.play()

        if self.item2.itemtype == 1:
            
            self.score -= 15
            self.scoremiss += 1
         #   self.sound1.play()
        
        
        
        
    def checkpointdowncantre1(self):
        if self.item1.itemtype == 0 :
            self.score -= 15
            self.scoremiss += 1

        if self.item1.itemtype == 1:
            self.score += 10
        
        
        
        
    def checkpointdowncantre2(self):
        if self.item2.itemtype  == 0 :
            self.score -= 15
            self.scoremiss += 1


        if self.item2.itemtype == 1 :
            self.score += 10
        
        
        
        






    def update(self,dt):
        
        self.scoretext.text = self.scoretext.text
        self.clickbutt.tell = self.clickbutt.tell
        self.scoretextmiss.text = self.scoretextmiss.text
        self.score = self.score


        self.push.change(self.chg)
        self.time3 += 1
        #if self.time3 == 10 :
           # self.sound2.play()
        
        if self.pausebutt.pause == True :
            print('pause')
            #self.item1.velocity = (0,0)
            #self.item2.velocity = (0,0)            
            global Pause_1
            Pause_1 = True  

        if self.scoremiss == 10 :
            
            Pause_1 = True
            print(Pause_1)
        
        
        if self.score <= 0 :
            self.score = 0
        



        if self.checkup.ccu1 == 1 :           #item1 checked
            self.checkpointupcanre1()
            self.item1.randomi()
            self.item1.image.source = self.item1.image.source
            self.item1.itemtype = self.item1.itemtype
            self.reitem1()
            self.checkup.ccu1 = 0
            self.push.checked1 = 0
            

        if self.checkdown.ccd1 == 1 :
            self.checkpointdowncantre1()
            self.item1.randomi()
            self.item1.image.source = self.item1.image.source
            self.item1.itemtype = self.item1.itemtype
            self.reitem1()
            self.checkdown.ccd1 = 0
            self.push.checked1 = 0
            

        if self.checkup.ccu2 == 1 :
            self.checkpointupcanre2()
            self.item2.randomi()
            self.item2.image.source = self.item2.image.source
            self.item2.itemtype = self.item2.itemtype            #item2 checked
           
            self.reitem2()
            self.checkup.ccu2 = 0
            self.push.checked2 = 0
            

        if self.checkdown.ccd2 == 1 :
            self.checkpointdowncantre2()
            self.item2.randomi()
            self.item2.image.source = self.item2.image.source
            self.item2.itemtype = self.item2.itemtype
            self.reitem2()
            self.checkdown.ccd2 = 0
            self.push.checked2 = 0
            
        

        if self.clickbutt.move_up == True :
            self.chg = True
            self.push.upup = True

            

        if self.clickbutt.move_up == False :
            self.chg = False
            self.push.upup = False
            
        


        self.push.send_item1(self.item1)
        self.push.send_item2(self.item2)
        self.checkup.checkup_item(self.item1 ,self.item2)
        self.checkdown.checkdown_item(self.item1 , self.item2)


        self.time1 += 1 
        self.time2 += 1
        if self.time1 >= 1:
            
            self.serve1()
            
            
            
        if self.time2 >= 100:
            
            self.serve2()
            
            

        self.item1.move()
        self.item2.move()



# สิ่งที่ต้องเพิ่ม
# def set moving ว่าเป็นบนหรือล่าง
# แยกif collide_widget กับ set velocity(vel)     
# ปรับปรุงcode การเคลื่อนที่ขึ้นลงของ item 
# ปรับปรุงcode senditem ทั้งหมด
# ปรับปรุงcode checkup_item บางส่วน
# **ลองพยายามย่อcodeและทำให้ output ออกมาเป็นเหมือนเดิมดู
# **ฝึกการใช้ bool แทนตัวเลข
        
    
        

         




class Itemgame(Widget):
    image = ObjectProperty(None)
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    picturelist = ["news","can","waterbottle","plasticbag","phone","brokenbottle"]
    randompicture = random.SystemRandom()
    picture = randompicture.choice(picturelist)

    itemtype = NumericProperty(0)

    def move(self):
        self.pos = Vector(self.velocity_x ,self.velocity_y) + self.pos 

    def randomi(self):
        self.picture = self.randompicture.choice(self.picturelist)
        self.setpic()
        


    def setpic(self):
        print(self.picture)
        print("setbefore %d"%self.itemtype)
        
        if self.picture == "news":
            self.image.source = "item/newsgood.png"
            self.itemtype = 0
        if self.picture == "can":
            self.image.source = "item/cangood.png"
            self.itemtype = 0
        if self.picture == "waterbottle" :
            self.image.source = "item/waterbottlegood.png"
            self.itemtype = 0
        if self.picture == "plasticbag" :
            self.image.source = "item/plasticbagbad.png"
            self.itemtype = 1
        if self.picture == "phone" :
            self.image.source = "item/phonebad.png"
            self.itemtype = 1
        if self.picture == "brokenbottle" :
            self.image.source = "item/bottlebad.png"
            self.itemtype = 1

        print("setlast %d \n"%self.itemtype)

    
        
class Pausebutt(Button):
    pause = False

    def on_press(self):
        self.pause = not self.pause
        
class Resumebutt(Button):
    resume = True
    def on_press(self):
        self.resume = not self.resume

class Clickbutt(Button):
    move_up = True
    tell = True



    def on_press(self):
        print('dfasdf')
        self.move_up = not self.move_up 
        self.tell = not self.tell
        

 # self.a = not self.a
        # print(self.a)

            



class Trashgame(App):
    def build(self):
        game = Gamemain()
        Clock.schedule_interval(game.update, 1 / 60 ) #คำสั่งupdate
        return game

if __name__ == '__main__':
    Trashgame().run()