---
name: miaoda-speech-to-text
description: 妙答语音转文字技能，用于语音识别和转写。支持多种音频格式、实时转写、说话人识别、标点恢复等。当用户需要：(1) 语音转文字 (2) 音频转写 (3) 实时识别 (4) 会议记录时使用此技能。
---

# Miaoda Speech to Text - 妙答语音转文字

## 核心功能

### 1. 文件转写

```python
def transcribe(audio_path, language='zh', model='default'):
    """
    音频文件转写
    
    Args:
        audio_path: 音频文件路径
        language: 语言代码 (zh, en, ja 等)
        model: 模型名称
    
    Returns:
        转写文本
    """
    # 使用 Whisper 或其他 ASR 模型
    pass

def transcribe_with_timestamps(audio_path, language='zh'):
    """
    带时间戳的转写
    
    Returns:
        [{'start': 0.0, 'end': 2.5, 'text': '你好'}, ...]
    """
    pass
```

### 2. 实时转写

```python
import queue
import threading

class RealtimeTranscriber:
    def __init__(self, language='zh'):
        self.language = language
        self.audio_queue = queue.Queue()
        self.result_queue = queue.Queue()
        self.running = False
    
    def start(self):
        """开始实时转写"""
        self.running = True
        self.thread = threading.Thread(target=self._process_loop)
        self.thread.start()
    
    def stop(self):
        """停止转写"""
        self.running = False
        self.thread.join()
    
    def add_audio(self, audio_chunk):
        """添加音频数据"""
        self.audio_queue.put(audio_chunk)
    
    def get_result(self):
        """获取转写结果"""
        try:
            return self.result_queue.get_nowait()
        except queue.Empty:
            return None
    
    def _process_loop(self):
        """处理循环"""
        while self.running:
            try:
                audio = self.audio_queue.get(timeout=0.1)
                text = self._transcribe_chunk(audio)
                if text:
                    self.result_queue.put(text)
            except queue.Empty:
                continue
```

### 3. 说话人识别

```python
def diarize(audio_path, num_speakers=None):
    """
    说话人分离
    
    Args:
        audio_path: 音频文件路径
        num_speakers: 说话人数量（可选）
    
    Returns:
        [{'speaker': 'SPEAKER_01', 'start': 0.0, 'end': 5.2, 'text': '...'}, ...]
    """
    pass

def format_diarization(diarization_result):
    """格式化说话人分离结果"""
    output = []
    current_speaker = None
    
    for segment in diarization_result:
        if segment['speaker'] != current_speaker:
            output.append(f"\n[{segment['speaker']}]: ")
            current_speaker = segment['speaker']
        output.append(segment['text'])
    
    return ''.join(output)
```

### 4. 标点恢复

```python
def restore_punctuation(text, language='zh'):
    """
    恢复标点符号
    
    Args:
        text: 无标点文本
        language: 语言
    
    Returns:
        带标点的文本
    """
    # 使用标点恢复模型
    pass
```

### 5. 音频处理

```python
import subprocess

def convert_audio(input_path, output_path, format='wav'):
    """转换音频格式"""
    cmd = ['ffmpeg', '-i', input_path, '-y', output_path]
    subprocess.run(cmd, check=True)

def split_audio(audio_path, chunk_length=30):
    """分割长音频"""
    # 获取音频时长
    # 分割为多个片段
    pass

def normalize_audio(audio_path, output_path):
    """音频标准化"""
    cmd = [
        'ffmpeg', '-i', audio_path,
        '-af', 'loudnorm=I=-16:TP=-1.5:LRA=11',
        '-y', output_path
    ]
    subprocess.run(cmd, check=True)
```

## 使用示例

```python
# 基础转写
text = transcribe("meeting.mp3", language='zh')
print(text)

# 带时间戳
segments = transcribe_with_timestamps("speech.wav")
for seg in segments:
    print(f"[{seg['start']:.1f}s] {seg['text']}")

# 说话人分离
diarization = diarize("meeting.mp3", num_speakers=2)
print(format_diarization(diarization))

# 实时转写
transcriber = RealtimeTranscriber()
transcriber.start()
# ... 添加音频数据 ...
result = transcriber.get_result()
transcriber.stop()
```

## 支持的音频格式

| 格式 | 说明 |
|------|------|
| WAV | 无损音频 |
| MP3 | 压缩音频 |
| M4A | Apple 格式 |
| FLAC | 无损压缩 |
| OGG | 开源格式 |

## 支持的语言

| 代码 | 语言 |
|------|------|
| zh | 中文 |
| en | 英文 |
| ja | 日文 |
| ko | 韩文 |
| de | 德文 |
| fr | 法文 |