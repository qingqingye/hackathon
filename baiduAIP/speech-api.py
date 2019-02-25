from aip import AipSpeech
import pyaudio
import wave



CHUNK=1024
FORMAT=pyaudio.paInt16
CHANNELS=2
RATE=256000
RECORD_SECONDS=2
WAVE_OUTPUT_FILENAME="out.wav"
p=pyaudio.PyAudio()

stream=p.open(format=FORMAT,
	channels=CHANNELS,
 	rate=RATE,
 	input=True,
 	frames_per_buffer=CHUNK)

print("sing for me")

frames=[]
for i in range (0,int(RATE/CHUNK*RECORD_SECONDS)):
	data=stream.read(CHUNK)
	frames.append(data)
print("I know your love now")

stream.stop_stream()
stream.close()
p.terminate()

wf=wave.open(WAVE_OUTPUT_FILENAME,'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()




# class GenAudio(object):
#     def __init__(self):
#         self.num_samples = 2000    #pyaudio内置缓冲大小
#         self.sampling_rate = 8000  #取样频率
#         self.level = 1500          #声音保存的阈值
#         self.count_num = 20        #count_num个取样之内出现COUNT_NUM个大于LEVEL的取样则记录声音
#         self.save_length = 8       #声音记录的最小长度：save_length * num_samples 个取样
#         self.time_count = 8        #录音时间，单位s
#         self.voice_string = []

    
#     #保存文件
#     def save_wav(self, filename):
#         wf = wave.open(filename, 'wb') 
#         wf.setnchannels(1) 
#         wf.setsampwidth(2) 
#         wf.setframerate(self.sampling_rate) 
#         wf.writeframes(np.array(self.voice_string).tostring())
#         wf.close()







""" 你的 APPID AK SK """
APP_ID = '11567018'
API_KEY = 'v8P6XA1I4A2EGnPRQmpt9D99'
SECRET_KEY = 'llbHhdFrRe2TFugk2RbNyCdx6yjLMjAq'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 识别本地文件
print(client.asr(get_file_content('out.wav'), 'pcm', 16000, {
    'dev_pid': 1536,
}))
