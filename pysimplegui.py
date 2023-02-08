import sys
import PySimpleGUI as sg
import os.path
from moviepy.editor import *
import cv2
import time

# First the window layout in 2 columns

INITIAL_HEIGHT = 240
transforms = [
    [
        sg.Text("Select a video:"),
        sg.In(size=(25, 1), enable_events=True, key="-VIDEO-SELECTED-"),
        sg.FilesBrowse(file_types=[("Video Files", "*.mp4")]),
        sg.Button("Load/Reload Video")
    ],
    [   sg.Text("Start:"),
        sg.Slider(range = (0, 10), resolution=1, tick_interval=10, enable_events = True, orientation= 'horizontal',size=(50,30), key='start_slider'),
    ],
    [   sg.Text("Ending:"),
        sg.Slider(range = (0, 10), resolution=1, tick_interval=10, enable_events = True, orientation= 'horizontal',size=(50,30), key='end_slider'),
    ],
]

# For now will only show the name of the file that was chosen
image_viewer_column = [
    [sg.Text(size=(40, 1), key="-TOUT-")],    
    [sg.Image(key="-IMAGE-")],
    [sg.Slider(range = (0, 10), resolution=1, tick_interval=10, enable_events = True, orientation= 'horizontal',size=(50,30), key='trackbar')],
    [sg.Button("Play"),
    #sg.Button("Pause"), 
    sg.Button("Stop"),
    sg.In(size=(25, 1), enable_events=True, visible=False, key="Save GIF"),
    sg.FileSaveAs(button_text = "Save GIF", initial_folder='./', file_types = (('GIF', '*.gif'),)),
    ]
]

# ----- Full layout -----
layout = [
    
    [
        sg.Column(transforms),
        sg.VSeperator(),
        sg.Column(image_viewer_column),
    ]
]


def image_2_bytes(image):    
    return cv2.imencode('.png', image[...,::-1])[1].tobytes()
def clip_image(clip,time):
    image=clip.get_frame(time)
    return cv2.imencode('.png', image[...,::-1])[1].tobytes()


window = sg.Window("Video to GIF", layout, return_keyboard_events=True, )


class Gif:
    def __init__(self, file):
        self.fullclip = VideoFileClip(file)
        self.original_shape=self.fullclip.get_frame(0).shape        
        
        self.init_clip()

        self.is_video_loaded=True
        self.transforms=[]
        self.transform_index=0
        self.current_time=0

    def init_clip(self):
        self.clip=self.fullclip.copy()
        if self.original_shape[0]>INITIAL_HEIGHT:
            self.clip=self.clip.resize(height=INITIAL_HEIGHT)
        self.image = self.clip.get_frame(0)        
        self.current_shape=self.image.shape
        self.dur = self.clip.duration
        self.fps=self.clip.fps
        self.play_range=(0,self.dur)
        

            
    def save_gif(self,filename):
        if filename:
            print('saving:', filename)
            self.clip.write_gif(filename)
            try:
                from pygifsicle import optimize
                optimize(filename)
            except:
                raise Warning('Error in pyfigsicle, not optimizing gif.')

    
    def cut(self,start, end, inside=True):
        if inside:
            transform = ('cut inside',start, end)
        else: 
            transform = ('cut outside',start, end)
        self.apply_transform(transform)        
        self.add_transform(transform)

    
    def add_transform(self,transform):
        self.transforms=self.transforms[0:self.transform_index]
        self.transforms.append(transform)
        self.transform_index+=1
        print('TRANSFOR INDEX' ,gif.transform_index, gif.transforms)
       
    def apply_transform(self,t):       
        if t[0] == 'scale change':
            self.clip=self.fullclip.resize(height=t[1])

    def apply_transform_list(self):        
        #clip=fullclip.copy()
        self.init_clip()
        if len(self.transforms)<=0:            
            return
        # the only scaling applied is the last one
        scale_change_indexes=[loc for loc, t in enumerate(self.transforms) if t[0] == 'scale change']
        if len(scale_change_indexes)>0:
            last_scale_index = max(scale_change_indexes)
            self.apply_transform(self.transforms[last_scale_index])
        else:
            self.init_clip()
        
        trans = [t for t in self.transforms[0:self.transform_index] if t[0] != 'scale change'] 
        print(trans)
        for t in trans:
            print(t)
            self.apply_transform(t)
    
    
    def display(self):
        return clip_image(self.clip,self.current_time)        

def update_bars(gif, window):
    window.Element("start_slider").Update(range=(0,gif.dur), value=0)#, tick_interval=dur/10)
    window["start_slider"].update(value=0)
    window.Element("end_slider").Update(range=(0,gif.dur), value=0)#, tick_interval=dur/10)
    window["end_slider"].update(value=gif.dur)  
    window.Element("trackbar").Update(range=(0,gif.dur), value=0)#, tick_interval=dur/10)
    window["trackbar"].update(value=0)      
    window["-IMAGE-"].update(gif.display())
    

playing = False
paused=False
play_time = 0.0
play_start_time = 0.0
is_video_loaded=False
square=(0,0,0,0)
#list of tuples
transforms=[]
transform_index=0
# Run the Event Loop
while True:
    # Timeout set only when playing the video.
    if not playing:
        event, values = window.read()
    else:
        if is_video_loaded:
            event, values = window.read(timeout = 1000/gif.fps)

    if event == "Exit" or event == sg.WIN_CLOSED:
        break
        
    # Load video
    if event == "Load/Reload Video" and values["-VIDEO-SELECTED-"].endswith('.mp4'):
        playing=False
        window['Play'].update('Play')
        file = values["-VIDEO-SELECTED-"]       

        try:
            gif=Gif(file)    
            is_video_loaded=gif.is_video_loaded
        except:
            raise Warning("Error loading the file")
            break
        update_bars(gif,window)
    
    # Save Video
    elif event == 'Save GIF' and is_video_loaded:
        filename = values['Save GIF']
        gif.save_gif(filename)
    
    # 시작 시간 지정
    elif event == "start_slider" and is_video_loaded: 
        playing=False
        window['Play'].update('Play')
        gif.current_time=values['start_slider']
        gif.play_range=(gif.current_time,values['end_slider'])
        if gif.current_time >  values["end_slider"]:
            window["end_slider"].update(value=gif.current_time)    
        window["-IMAGE-"].update(gif.display())
        
    # 시작 시간 지정
    elif event == "end_slider" and is_video_loaded: 
        playing=False
        window['Play'].update('Play')
        gif.current_time=values['end_slider']
        gif.play_range=(values['start_slider'],gif.current_time)
        if gif.current_time <  values["start_slider"]:
            window["start_slider"].update(value=gif.current_time) 
        window["-IMAGE-"].update(gif.display())

    elif event == "trackbar" and is_video_loaded: 
        gif.current_time=values['trackbar']
        window["-IMAGE-"].update(gif.display())         
        if playing:
            playing=False   
            window['Play'].update('Play')
        

    elif event == 'Play' and is_video_loaded:
        if playing:
            window['Play'].update('Play')
            playing=False
        else:
            window['Play'].update('Pause')      
            playing=True
            play_time=time.time()
            play_start_time=values['trackbar']
            paused=False
    
    elif event == 'Stop' and is_video_loaded:
        window['Play'].update('Play')
        playing=False
        window["-IMAGE-"].update(gif.display())
        window["trackbar"].update(0)


    #play the video        
    if is_video_loaded and playing:        
        trackbar_time=(time.time()-play_time)+play_start_time
        if trackbar_time < gif.play_range[1]:
            window["trackbar"].update(value=trackbar_time) 
            window["-IMAGE-"].update(gif.display())
            gif.current_time=trackbar_time
        else:
            playing=False
            window['Play'].update('Play')
    
    #window['Pause'].update(disabled=paused)
    #print(transforms)
    
    def getParameter(video, gif, start_time, end_time, process_time, browse, load, create, save, play, stop):
        
        return video, gif, start_time, end_time, process_time, browse, load, create, save, play, stop

if __name__ == '__main__':
    getParameter(file, sg.Image(key="-IMAGE-"),values['start_slider'],values['end_slider'],values['trackbar'],sg.FilesBrowse(file_types=[("Video Files", "*.mp4")]),sg.Button("Load/Reload Video"),sys.argv[8],sg.FileSaveAs(button_text = "Save GIF", initial_folder='./', file_types = (('GIF', '*.gif'),)),sg.Button("Play"), sg.Button("Stop"))

window.close()