# -*- coding:utf-8 -*-
import pyrec
import wav2pcm
from aip import AipSpeech

def audio2text():
	APP_ID = '11567018'
	API_KEY = 'v8P6XA1I4A2EGnPRQmpt9D99'
	SECRET_KEY = 'llbHhdFrRe2TFugk2RbNyCdx6yjLMjAq'

	client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

	pyrec.rec("1.wav")
	pcm = wav2pcm.wav_to_pcm("1.wav")


	with open('1.pcm', 'rb') as fp:
	    file_context = fp.read()
	data = client.asr(file_context, 'pcm', 16000, {'dev_pid': 1536})
	if (data[u'err_msg'] == u'success.'):
		
		with open('test.txt','w+') as f:
			
			for i in data[u'result']:
				print i
				f.write(i.encode("utf-8"))
		return True
	else:
		return False

audio2text()