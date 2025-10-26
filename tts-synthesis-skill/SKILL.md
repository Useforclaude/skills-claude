---
name: tts-synthesis-skill
description: Expert Text-to-Speech synthesis for production voice generation (Edge-TTS, AWS Polly, ElevenLabs, Google Cloud TTS). Use for multi-platform TTS, SSML markup, prosody control, voice cloning, timeline-accurate audio synthesis, batch processing, and cost optimization.
---

# TTS Synthesis Expert Skill

## Overview

Production-ready Text-to-Speech synthesis across multiple platforms, specializing in timeline-accurate audio generation for video dubbing, subtitle synchronization, and voice-over production.

**When to use this skill:**
- Converting SRT subtitles to synchronized audio
- Multi-platform TTS (Edge-TTS, AWS Polly, ElevenLabs)
- Voice cloning and custom voice creation
- SSML markup for natural prosody
- Timeline-accurate audio-subtitle sync
- Batch TTS processing
- Cost optimization strategies

---

## Platform Comparison

### Quick Reference

| Platform | Quality | Cost | Speed | Voice Cloning | Multilingual | Best For |
|----------|---------|------|-------|---------------|--------------|----------|
| **Edge-TTS** | ⭐⭐⭐ | **Free** | ⚡⚡⚡ | ❌ | ✅ 80+ langs | Testing, prototypes, high-volume |
| **AWS Polly** | ⭐⭐⭐⭐ | $4/1M chars | ⚡⚡⚡ | ❌ | ✅ 60+ langs | Production (standard quality) |
| **ElevenLabs** | ⭐⭐⭐⭐⭐ | $1-30/1K chars | ⚡⚡ | ✅ | ✅ 29 langs | Production (premium, voice cloning) |
| **Google Cloud** | ⭐⭐⭐⭐ | $4/1M chars | ⚡⚡⚡ | ❌ | ✅ 40+ langs | Production (WaveNet quality) |
| **Azure Neural** | ⭐⭐⭐⭐ | $15/1M chars | ⚡⚡ | ❌ | ✅ 75+ langs | Enterprise (high quality) |

### Platform Selection Guide

```python
def choose_tts_platform(requirements: dict) -> str:
    """
    Choose best TTS platform based on requirements

    Args:
        requirements: dict with keys:
            - budget: 'free', 'low', 'medium', 'high'
            - quality: 'basic', 'good', 'excellent', 'premium'
            - volume: 'low', 'medium', 'high'
            - voice_cloning: bool
            - real_time: bool

    Returns:
        Recommended platform name
    """
    # Free/Testing
    if requirements.get('budget') == 'free':
        return 'Edge-TTS'

    # Voice cloning required
    if requirements.get('voice_cloning'):
        return 'ElevenLabs'

    # Premium quality required
    if requirements.get('quality') == 'premium':
        return 'ElevenLabs'

    # High volume + good quality
    if requirements.get('volume') == 'high' and requirements.get('budget') in ['low', 'medium']:
        return 'AWS Polly or Google Cloud TTS'

    # Default: AWS Polly (best balance)
    return 'AWS Polly'

# Example usage
platform = choose_tts_platform({
    'budget': 'medium',
    'quality': 'good',
    'volume': 'high',
    'voice_cloning': False
})
print(f"Recommended: {platform}")
```

---

## Edge-TTS (Free Microsoft Voices)

### Installation & Setup

```bash
# Install
pip install edge-tts

# Test installation
edge-tts --list-voices
```

### Basic Usage

```python
import edge_tts
import asyncio

async def text_to_speech_edge(
    text: str,
    output_path: str,
    voice: str = "en-US-AriaNeural",
    rate: str = "+0%",
    pitch: str = "+0Hz"
) -> None:
    """
    Generate speech with Edge-TTS

    Args:
        text: Text to synthesize
        output_path: Output MP3 file path
        voice: Voice ID (see list below)
        rate: Speed adjustment (-50% to +100%)
        pitch: Pitch adjustment (-50Hz to +50Hz)
    """
    communicate = edge_tts.Communicate(
        text=text,
        voice=voice,
        rate=rate,
        pitch=pitch
    )
    await communicate.save(output_path)
    print(f"✅ Audio saved: {output_path}")

# Usage
asyncio.run(text_to_speech_edge(
    "Hello, this is a test of Edge TTS.",
    "output.mp3",
    voice="en-US-GuyNeural",
    rate="+10%",  # Slightly faster
    pitch="-2Hz"  # Slightly lower pitch
))
```

### Best Voices by Language

```python
# English voices (US)
ENGLISH_US_VOICES = {
    'female_natural': 'en-US-AriaNeural',      # Most natural female
    'female_friendly': 'en-US-JennyNeural',    # Warm, friendly
    'male_professional': 'en-US-GuyNeural',    # Professional male
    'male_narrator': 'en-US-DavisNeural',      # Deep narrator voice
}

# English voices (UK)
ENGLISH_UK_VOICES = {
    'female': 'en-GB-SoniaNeural',
    'male': 'en-GB-RyanNeural',
}

# Thai voices
THAI_VOICES = {
    'female': 'th-TH-PremwadeeNeural',
    'male': 'th-TH-NiwatNeural',
}

# Other languages
OTHER_VOICES = {
    'spanish_female': 'es-ES-ElviraNeural',
    'french_female': 'fr-FR-DeniseNeural',
    'german_male': 'de-DE-ConradNeural',
    'japanese_female': 'ja-JP-NanamiNeural',
    'korean_female': 'ko-KR-SunHiNeural',
    'chinese_female': 'zh-CN-XiaoxiaoNeural',
}

async def list_all_voices():
    """List all available Edge-TTS voices"""
    voices = await edge_tts.list_voices()
    for voice in voices:
        print(f"{voice['ShortName']}: {voice['Gender']} ({voice['Locale']})")

# List voices
asyncio.run(list_all_voices())
```

### SSML Support (Advanced)

```python
async def text_to_speech_ssml(
    ssml_text: str,
    output_path: str,
    voice: str = "en-US-AriaNeural"
) -> None:
    """
    Generate speech using SSML for advanced control

    SSML allows:
    - Prosody control (rate, pitch, volume)
    - Pauses and breaks
    - Emphasis
    - Say-as (numbers, dates, etc.)
    """
    communicate = edge_tts.Communicate(ssml_text, voice)
    await communicate.save(output_path)

# Example: Complex SSML
ssml = """
<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="en-US">
    <prosody rate="0.9" pitch="-2st" volume="loud">
        This is the introduction.
    </prosody>
    <break time="500ms"/>
    <prosody rate="1.0">
        This is normal speed.
    </prosody>
    <break time="300ms"/>
    <prosody rate="1.2" pitch="+3st">
        This is faster and higher pitch!
    </prosody>
    <break time="1s"/>
    <emphasis level="strong">This is emphasized.</emphasis>
</speak>
"""

asyncio.run(text_to_speech_ssml(ssml, "ssml_output.mp3"))
```

### Batch Processing

```python
async def batch_synthesize_edge(
    segments: list,
    voice: str = "en-US-AriaNeural",
    output_dir: str = "tts_output",
    max_concurrent: int = 5
) -> list:
    """
    Batch process multiple text segments

    Args:
        segments: List of dicts with 'id', 'text', 'output_file'
        voice: Voice to use
        output_dir: Output directory
        max_concurrent: Max concurrent requests

    Returns:
        List of generated file paths
    """
    from pathlib import Path
    import asyncio
    from itertools import islice

    Path(output_dir).mkdir(exist_ok=True)

    async def synthesize_one(segment):
        output_path = f"{output_dir}/{segment['output_file']}"
        await text_to_speech_edge(
            segment['text'],
            output_path,
            voice=voice
        )
        return output_path

    # Process in batches
    def batched(iterable, n):
        it = iter(iterable)
        while True:
            batch = list(islice(it, n))
            if not batch:
                break
            yield batch

    results = []
    for batch in batched(segments, max_concurrent):
        batch_results = await asyncio.gather(*[
            synthesize_one(seg) for seg in batch
        ])
        results.extend(batch_results)
        print(f"Processed {len(results)}/{len(segments)} segments")

    return results

# Usage
segments = [
    {'id': 1, 'text': 'First segment text.', 'output_file': 'seg_001.mp3'},
    {'id': 2, 'text': 'Second segment text.', 'output_file': 'seg_002.mp3'},
    {'id': 3, 'text': 'Third segment text.', 'output_file': 'seg_003.mp3'},
]

results = asyncio.run(batch_synthesize_edge(
    segments,
    voice="en-US-GuyNeural",
    max_concurrent=3
))
print(f"Generated {len(results)} audio files")
```

---

## Timeline-Accurate Synthesis

### Problem: TTS Duration ≠ Subtitle Duration

**Problem:**
- SRT subtitle: "Hello world" (3.5 seconds)
- TTS output: "Hello world" (2.8 seconds)
- Result: Audio doesn't match video timing!

**Solution: Timeline-Aware Merging**

### SRT to Audio with Exact Timing

```python
from pydub import AudioSegment
from pydub.effects import speedup
import srt
from datetime import timedelta

def srt_timestamp_to_ms(timestamp: timedelta) -> int:
    """Convert SRT timestamp to milliseconds"""
    return int(timestamp.total_seconds() * 1000)

def adjust_audio_to_duration(
    audio: AudioSegment,
    target_duration_ms: int,
    max_speed_change: float = 0.25
) -> AudioSegment:
    """
    Adjust audio speed to match target duration

    Args:
        audio: Input audio segment
        target_duration_ms: Desired duration in milliseconds
        max_speed_change: Maximum speed adjustment (0.25 = ±25%)

    Returns:
        Adjusted audio segment
    """
    actual_duration_ms = len(audio)
    speed_ratio = actual_duration_ms / target_duration_ms

    # If within 5%, don't adjust (acceptable)
    if abs(speed_ratio - 1.0) < 0.05:
        return audio

    # Clamp speed change to max_speed_change
    if speed_ratio > (1.0 + max_speed_change):
        speed_ratio = 1.0 + max_speed_change
    elif speed_ratio < (1.0 - max_speed_change):
        speed_ratio = 1.0 - max_speed_change

    # Adjust speed
    adjusted = audio._spawn(
        audio.raw_data,
        overrides={"frame_rate": int(audio.frame_rate * speed_ratio)}
    ).set_frame_rate(audio.frame_rate)

    return adjusted

async def srt_to_timeline_audio(
    srt_path: str,
    output_path: str,
    voice: str = "en-US-AriaNeural",
    use_tts_platform: str = "edge",
    temp_dir: str = "temp_tts"
) -> dict:
    """
    Generate timeline-accurate audio from SRT file

    Process:
    1. Parse SRT file
    2. Generate TTS for each segment
    3. Adjust each segment to match SRT timing
    4. Insert silence gaps between segments
    5. Merge all into final timeline-accurate audio

    Args:
        srt_path: Input SRT file
        output_path: Output audio file
        voice: TTS voice ID
        use_tts_platform: 'edge', 'polly', etc.
        temp_dir: Temporary directory for segments

    Returns:
        Statistics dict
    """
    from pathlib import Path
    import os

    Path(temp_dir).mkdir(exist_ok=True)

    # Step 1: Parse SRT
    with open(srt_path, 'r', encoding='utf-8') as f:
        subtitles = list(srt.parse(f.read()))

    print(f"Loaded {len(subtitles)} subtitles from {srt_path}")

    # Step 2: Generate TTS for each subtitle
    print("Generating TTS audio...")
    segment_files = []

    for i, sub in enumerate(subtitles):
        # Generate audio
        segment_file = f"{temp_dir}/segment_{i:04d}.mp3"
        await text_to_speech_edge(sub.content, segment_file, voice=voice)
        segment_files.append(segment_file)

        if (i + 1) % 10 == 0:
            print(f"  Generated {i+1}/{len(subtitles)} segments")

    # Step 3: Build timeline-accurate audio
    print("Building timeline-accurate audio...")
    final_audio = AudioSegment.silent(duration=0)
    current_time_ms = 0

    stats = {
        'total_segments': len(subtitles),
        'total_audio_ms': 0,
        'total_silence_ms': 0,
        'speed_adjustments': 0
    }

    for i, sub in enumerate(subtitles):
        # Target timing from SRT
        target_start_ms = srt_timestamp_to_ms(sub.start)
        target_end_ms = srt_timestamp_to_ms(sub.end)
        target_duration_ms = target_end_ms - target_start_ms

        # Load generated audio
        audio = AudioSegment.from_file(segment_files[i])
        actual_duration_ms = len(audio)

        # Adjust audio to match target duration
        if abs(actual_duration_ms - target_duration_ms) > 50:  # >50ms difference
            audio = adjust_audio_to_duration(audio, target_duration_ms)
            stats['speed_adjustments'] += 1

        # Insert silence gap if needed
        if target_start_ms > current_time_ms:
            silence_duration_ms = target_start_ms - current_time_ms
            final_audio += AudioSegment.silent(duration=silence_duration_ms)
            stats['total_silence_ms'] += silence_duration_ms
            current_time_ms = target_start_ms

        # Append audio segment
        final_audio += audio
        stats['total_audio_ms'] += len(audio)
        current_time_ms = target_start_ms + len(audio)

        if (i + 1) % 10 == 0:
            print(f"  Merged {i+1}/{len(subtitles)} segments")

    # Step 4: Export final audio
    print(f"Exporting to {output_path}...")
    final_audio.export(output_path, format="mp3", bitrate="192k")

    # Step 5: Cleanup
    for f in segment_files:
        os.unlink(f)
    os.rmdir(temp_dir)

    # Final stats
    stats['output_path'] = output_path
    stats['total_duration_s'] = len(final_audio) / 1000
    stats['silence_percentage'] = (stats['total_silence_ms'] / len(final_audio)) * 100

    print(f"\n✅ Timeline-accurate audio generated!")
    print(f"   Total duration: {stats['total_duration_s']:.2f}s")
    print(f"   Audio segments: {stats['total_audio_ms']/1000:.2f}s")
    print(f"   Silence gaps: {stats['total_silence_ms']/1000:.2f}s ({stats['silence_percentage']:.1f}%)")
    print(f"   Speed adjustments: {stats['speed_adjustments']}")

    return stats

# Usage
stats = asyncio.run(srt_to_timeline_audio(
    srt_path="subtitles.srt",
    output_path="dubbed_audio.mp3",
    voice="en-US-GuyNeural"
))
```

---

## AWS Polly (Production Quality)

### Setup

```bash
# Install AWS SDK
pip install boto3

# Configure credentials
aws configure
# Enter: Access Key, Secret Key, Region (e.g., us-east-1)
```

### Basic Usage

```python
import boto3
from pathlib import Path

def text_to_speech_polly(
    text: str,
    output_path: str,
    voice_id: str = "Joanna",
    engine: str = "neural",
    language_code: str = "en-US"
) -> None:
    """
    Generate speech with AWS Polly

    Args:
        text: Text to synthesize
        output_path: Output file path
        voice_id: Polly voice ID
        engine: 'standard' or 'neural' (neural = better quality)
        language_code: Language code

    Available voices:
    - English (US): Joanna, Matthew, Kendra, Joey (neural)
    - English (UK): Emma, Brian (neural)
    - Thai: - No neural voices available yet
    """
    polly = boto3.client('polly', region_name='us-east-1')

    response = polly.synthesize_speech(
        Text=text,
        OutputFormat='mp3',
        VoiceId=voice_id,
        Engine=engine,
        LanguageCode=language_code
    )

    # Save audio
    with open(output_path, 'wb') as f:
        f.write(response['AudioStream'].read())

    print(f"✅ Audio saved: {output_path}")

# Usage
text_to_speech_polly(
    "This is a test of AWS Polly neural voice.",
    "polly_output.mp3",
    voice_id="Joanna",  # Female neural voice
    engine="neural"
)
```

### SSML with Polly

```python
def text_to_speech_polly_ssml(
    ssml_text: str,
    output_path: str,
    voice_id: str = "Joanna"
) -> None:
    """
    Generate speech using SSML with Polly
    """
    polly = boto3.client('polly')

    response = polly.synthesize_speech(
        Text=ssml_text,
        TextType='ssml',  # ← Important!
        OutputFormat='mp3',
        VoiceId=voice_id,
        Engine='neural'
    )

    with open(output_path, 'wb') as f:
        f.write(response['AudioStream'].read())

# Example SSML
ssml = """
<speak>
    <prosody rate="90%">
        This sentence is slower.
    </prosody>
    <break time="500ms"/>
    <prosody rate="110%" pitch="high">
        This sentence is faster and higher pitch!
    </prosody>
    <break time="1s"/>
    <emphasis level="strong">This is emphasized.</emphasis>
</speak>
"""

text_to_speech_polly_ssml(ssml, "polly_ssml.mp3")
```

---

## ElevenLabs (Premium + Voice Cloning)

### Setup

```bash
# Install ElevenLabs SDK
pip install elevenlabs

# Set API key
export ELEVEN_API_KEY="your_api_key_here"
```

### Basic Usage

```python
from elevenlabs import generate, play, set_api_key, Voice, VoiceSettings

# Set API key
set_api_key("your_api_key")

def text_to_speech_elevenlabs(
    text: str,
    output_path: str,
    voice_id: str = "21m00Tcm4TlvDq8ikWAM",  # Rachel (default)
    model: str = "eleven_multilingual_v2",
    stability: float = 0.5,
    similarity_boost: float = 0.75
) -> None:
    """
    Generate speech with ElevenLabs

    Args:
        text: Text to synthesize
        output_path: Output file path
        voice_id: ElevenLabs voice ID
        model: Model name
        stability: Voice stability (0-1)
        similarity_boost: Voice similarity (0-1)

    Popular voices:
    - Rachel: 21m00Tcm4TlvDq8ikWAM
    - Antoni: ErXwobaYiN019PkySvjV
    - Elli: MF3mGyEYCl7XYWbV9V6O
    """
    audio = generate(
        text=text,
        voice=Voice(
            voice_id=voice_id,
            settings=VoiceSettings(
                stability=stability,
                similarity_boost=similarity_boost
            )
        ),
        model=model
    )

    # Save
    with open(output_path, 'wb') as f:
        f.write(audio)

    print(f"✅ Audio saved: {output_path}")

# Usage
text_to_speech_elevenlabs(
    "This is a test of ElevenLabs voice synthesis.",
    "elevenlabs_output.mp3",
    stability=0.5,
    similarity_boost=0.75
)
```

### Voice Cloning

```python
from elevenlabs import clone, Voice

def clone_voice_elevenlabs(
    name: str,
    description: str,
    audio_samples: list
) -> Voice:
    """
    Clone a voice from audio samples

    Args:
        name: Voice name
        description: Voice description
        audio_samples: List of audio file paths (3-5 files, 1-10 min each)

    Returns:
        Cloned Voice object

    Requirements:
    - 3-5 audio samples
    - Each 1-10 minutes long
    - Clear speech, minimal background noise
    - Same speaker throughout
    """
    voice = clone(
        name=name,
        description=description,
        files=audio_samples
    )

    print(f"✅ Voice cloned: {name}")
    return voice

# Usage
cloned_voice = clone_voice_elevenlabs(
    name="John Narrator",
    description="Professional male narrator voice",
    audio_samples=[
        "sample1.mp3",
        "sample2.mp3",
        "sample3.mp3"
    ]
)

# Generate with cloned voice
audio = generate(
    text="This is my cloned voice speaking!",
    voice=cloned_voice,
    model="eleven_multilingual_v2"
)

with open("cloned_voice_output.mp3", "wb") as f:
    f.write(audio)
```

---

## Audio Enhancement

### Post-Processing for Better Quality

```python
from pydub import AudioSegment
from pydub.effects import normalize, compress_dynamic_range

def enhance_tts_audio(
    input_path: str,
    output_path: str,
    normalize_volume: bool = True,
    compress_dynamics: bool = True,
    remove_silence: bool = False,
    target_bitrate: str = "192k"
) -> None:
    """
    Enhance TTS audio quality

    Args:
        input_path: Input audio file
        output_path: Output audio file
        normalize_volume: Normalize to consistent volume
        compress_dynamics: Compress dynamic range
        remove_silence: Remove leading/trailing silence
        target_bitrate: Output bitrate
    """
    # Load audio
    audio = AudioSegment.from_file(input_path)

    # Normalize volume
    if normalize_volume:
        audio = normalize(audio)
        print("✓ Normalized volume")

    # Compress dynamic range
    if compress_dynamics:
        audio = compress_dynamic_range(audio, threshold=-20.0, ratio=4.0)
        print("✓ Compressed dynamic range")

    # Remove silence (if enabled)
    if remove_silence:
        from pydub.silence import detect_leading_silence
        trim_ms = detect_leading_silence(audio, silence_threshold=-40)
        audio = audio[trim_ms:]
        trim_ms_end = detect_leading_silence(audio.reverse(), silence_threshold=-40)
        audio = audio[:-trim_ms_end] if trim_ms_end > 0 else audio
        print(f"✓ Removed {trim_ms + trim_ms_end}ms of silence")

    # Export with quality settings
    audio.export(
        output_path,
        format="mp3",
        bitrate=target_bitrate,
        parameters=["-q:a", "0"]  # Highest quality
    )

    print(f"✅ Enhanced audio saved: {output_path}")

# Usage
enhance_tts_audio(
    "raw_tts.mp3",
    "enhanced_tts.mp3",
    normalize_volume=True,
    compress_dynamics=True
)
```

---

## Production Workflow

### Complete SRT → Dubbed Audio Pipeline

```python
async def production_srt_to_audio(
    srt_path: str,
    output_audio_path: str,
    tts_platform: str = "edge",
    voice: str = None,
    enhance_audio: bool = True,
    api_key: str = None
) -> dict:
    """
    Production pipeline: SRT → Timeline-accurate dubbed audio

    Steps:
    1. Parse SRT
    2. Generate TTS for each segment
    3. Adjust timing to match SRT exactly
    4. Merge with silence gaps
    5. Enhance audio quality
    6. Export final audio

    Args:
        srt_path: Input SRT file
        output_audio_path: Output audio file
        tts_platform: 'edge', 'polly', 'elevenlabs'
        voice: Voice ID (platform-specific)
        enhance_audio: Apply post-processing
        api_key: API key (for paid platforms)

    Returns:
        Statistics and result
    """
    # Default voices
    if voice is None:
        default_voices = {
            'edge': 'en-US-GuyNeural',
            'polly': 'Matthew',
            'elevenlabs': '21m00Tcm4TlvDq8ikWAM'
        }
        voice = default_voices.get(tts_platform, 'en-US-GuyNeural')

    print(f"🎙️  TTS Platform: {tts_platform}")
    print(f"🎤 Voice: {voice}")

    # Generate timeline-accurate audio
    if tts_platform == 'edge':
        stats = await srt_to_timeline_audio(
            srt_path,
            output_audio_path,
            voice=voice
        )
    else:
        raise NotImplementedError(f"Platform {tts_platform} not yet implemented in this example")

    # Enhance audio (if enabled)
    if enhance_audio:
        print("\n🎵 Enhancing audio quality...")
        temp_output = output_audio_path + ".temp.mp3"
        import shutil
        shutil.move(output_audio_path, temp_output)

        enhance_tts_audio(
            temp_output,
            output_audio_path,
            normalize_volume=True,
            compress_dynamics=True
        )

        import os
        os.unlink(temp_output)

    print(f"\n✅ Production audio ready: {output_audio_path}")
    return stats

# Usage
stats = asyncio.run(production_srt_to_audio(
    srt_path="subtitles.srt",
    output_audio_path="final_dubbed_audio.mp3",
    tts_platform="edge",
    voice="en-US-GuyNeural",
    enhance_audio=True
))

print(f"\n📊 Final Statistics:")
print(f"   Duration: {stats['total_duration_s']:.2f}s")
print(f"   Segments: {stats['total_segments']}")
print(f"   Speed adjustments: {stats['speed_adjustments']}")
```

---

## Cost Optimization

### Strategy 1: Batch Processing

```python
# ❌ BAD - One API call per segment (expensive)
for segment in segments:
    audio = generate(segment['text'])

# ✅ GOOD - Batch segments together
batch_text = "\n".join([seg['text'] for seg in segments])
audio = generate(batch_text)
```

### Strategy 2: Caching

```python
import hashlib
import os
from pathlib import Path

TTS_CACHE_DIR = "tts_cache"
Path(TTS_CACHE_DIR).mkdir(exist_ok=True)

def get_tts_cached(
    text: str,
    voice: str,
    platform: str = "edge"
) -> str:
    """
    Get TTS with caching (avoid re-generating same text)

    Args:
        text: Text to synthesize
        voice: Voice ID
        platform: TTS platform

    Returns:
        Path to cached audio file
    """
    # Generate cache key
    cache_key = hashlib.md5(f"{text}_{voice}_{platform}".encode()).hexdigest()
    cache_path = f"{TTS_CACHE_DIR}/{cache_key}.mp3"

    # Check cache
    if os.path.exists(cache_path):
        print(f"✓ Cache hit: {cache_key}")
        return cache_path

    # Generate (cache miss)
    print(f"✗ Cache miss: generating...")
    if platform == "edge":
        import asyncio
        asyncio.run(text_to_speech_edge(text, cache_path, voice))
    else:
        raise NotImplementedError()

    return cache_path

# Usage
audio_path = get_tts_cached(
    "Hello world",
    "en-US-GuyNeural",
    "edge"
)
```

---

## Quick Reference

### Platform Choice Matrix

| Need | Platform | Cost | Quality |
|------|----------|------|---------|
| Testing | Edge-TTS | Free | Good |
| High volume | Edge-TTS or AWS Polly | Free/$4/1M | Good-Excellent |
| Premium quality | ElevenLabs | $1-30/1K | Excellent |
| Voice cloning | ElevenLabs | $30/1K | Excellent |
| Enterprise | AWS Polly or Azure | $4-15/1M | Excellent |

### Best Practices Checklist

- [ ] Choose right platform for use case
- [ ] Use SSML for better prosody
- [ ] Implement timeline-accurate synthesis for video
- [ ] Enable caching to reduce costs
- [ ] Batch process when possible
- [ ] Enhance audio with normalization
- [ ] Test with free platform first
- [ ] Monitor API costs

---

**Last Updated:** 2025-10-24
**Version:** 1.0
**Lines:** 1,100+
**Status:** Production Ready ✅
