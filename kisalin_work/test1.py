from gtts import gTTS
__author__ = 'info-lab'

tts = gTTS(
    text='안녕하세요 마지막날입니다. 수업을 하고 있네요.....',
    lang='ko', slow=False
)
tts.text.replace('.....','')
tts.save('ex_ko.mp3')

# if '녹음' in '녹음':


tts1 = gTTS(
    text='Hello',
    lang='en', slow=False
)
tts1.save('ex_en.mp3')