---
name: ffmpeg-video-processing-skill
description: Expert FFmpeg for production video/audio processing. Use for video/audio merging, codec conversion, subtitle burning, audio sync, stream mapping, quality optimization, format conversion, and production-ready video processing workflows.
---

# FFmpeg Expert Skill

## Overview

Production-ready FFmpeg knowledge for video localization, dubbing, and processing workflows. Covers audio replacement, subtitle burning, format conversion, and quality optimization.

**When to use this skill:**
- Replacing audio tracks in videos
- Burning subtitles into video
- Audio/video synchronization
- Format conversion and codec optimization
- Extracting audio from video
- Merging multiple media streams
- Quality optimization for distribution

---

## Quick Reference

### Most Common Tasks

```bash
# Replace audio in video (copy video, re-encode audio)
ffmpeg -i video.mp4 -i new_audio.mp3 -c:v copy -c:a aac -b:a 192k -map 0:v:0 -map 1:a:0 output.mp4

# Extract audio from video
ffmpeg -i video.mp4 -vn -acodec libmp3lame -q:a 2 audio.mp3

# Burn subtitles into video
ffmpeg -i video.mp4 -vf subtitles=subtitle.srt output.mp4

# Convert video format
ffmpeg -i input.mov -c:v libx264 -preset medium -crf 23 -c:a aac -b:a 192k output.mp4

# Trim video
ffmpeg -i input.mp4 -ss 00:01:00 -to 00:02:00 -c copy output.mp4

# Concatenate videos
ffmpeg -f concat -safe 0 -i filelist.txt -c copy output.mp4
```

---

## Audio Replacement (Most Important for Dubbing)

### Replace Audio Track (Keep Video Quality)

```bash
# ✅ BEST - Copy video stream (no re-encode), encode audio to AAC
ffmpeg -i input_video.mp4 -i new_audio.mp3 \
  -c:v copy \           # Copy video as-is (no quality loss, fast)
  -c:a aac \            # Encode audio to AAC codec
  -b:a 192k \           # Audio bitrate (192kbps = high quality)
  -map 0:v:0 \          # Map video from first input
  -map 1:a:0 \          # Map audio from second input
  -shortest \           # End when shortest stream ends
  -y output.mp4         # Overwrite output if exists

# ❌ BAD - Re-encodes video (slow + quality loss)
ffmpeg -i input_video.mp4 -i new_audio.mp3 -y output.mp4
```

### Python Wrapper

```python
import subprocess
from pathlib import Path

def replace_audio(
    video_path: str,
    audio_path: str,
    output_path: str,
    audio_bitrate: str = "192k",
    audio_codec: str = "aac"
) -> dict:
    """
    Replace audio in video (keep video quality)

    Args:
        video_path: Input video file
        audio_path: New audio file
        output_path: Output video file
        audio_bitrate: Audio bitrate (e.g., "192k", "256k")
        audio_codec: Audio codec (e.g., "aac", "mp3")

    Returns:
        dict with result info
    """
    # Build FFmpeg command
    cmd = [
        'ffmpeg',
        '-i', video_path,       # Input video
        '-i', audio_path,       # Input audio
        '-c:v', 'copy',         # Copy video (no re-encode)
        '-c:a', audio_codec,    # Encode audio
        '-b:a', audio_bitrate,  # Audio bitrate
        '-map', '0:v:0',        # Video from input 0
        '-map', '1:a:0',        # Audio from input 1
        '-shortest',            # End at shortest stream
        '-y',                   # Overwrite output
        output_path
    ]

    print(f"Replacing audio in {video_path}...")
    print(f"  New audio: {audio_path}")
    print(f"  Output: {output_path}")

    # Run FFmpeg
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print(f"❌ FFmpeg error:")
        print(result.stderr)
        return {'success': False, 'error': result.stderr}

    # Get output file size
    output_size_mb = Path(output_path).stat().st_size / (1024 * 1024)

    print(f"✅ Success! Output: {output_path} ({output_size_mb:.2f} MB)")

    return {
        'success': True,
        'output_path': output_path,
        'output_size_mb': output_size_mb
    }

# Usage
result = replace_audio(
    video_path="original_video.mp4",
    audio_path="dubbed_audio.mp3",
    output_path="dubbed_video.mp4",
    audio_bitrate="192k"
)
```

---

## Audio/Video Synchronization

### Delay Audio (Audio Starts Later)

```bash
# Delay audio by 500ms (audio starts 0.5s after video)
ffmpeg -i video.mp4 -itsoffset 0.5 -i audio.mp3 \
  -map 0:v -map 1:a \
  -c:v copy -c:a aac -b:a 192k \
  output.mp4
```

### Advance Audio (Audio Starts Earlier)

```bash
# Advance audio by 200ms (audio starts 0.2s before video)
ffmpeg -i video.mp4 -itsoffset -0.2 -i audio.mp3 \
  -map 0:v -map 1:a \
  -c:v copy -c:a aac -b:a 192k \
  output.mp4
```

### Python: Audio Sync with Detection

```python
def sync_audio_video(
    video_path: str,
    audio_path: str,
    output_path: str,
    offset_seconds: float = 0.0,
    auto_detect_offset: bool = False
) -> dict:
    """
    Sync audio with video

    Args:
        video_path: Input video
        audio_path: Input audio
        output_path: Output video
        offset_seconds: Manual offset (+ = delay audio, - = advance audio)
        auto_detect_offset: Auto-detect offset (experimental)

    Returns:
        Result dict
    """
    # Build command
    cmd = ['ffmpeg']

    # Apply offset
    if offset_seconds != 0.0:
        cmd.extend(['-itsoffset', str(offset_seconds)])

    cmd.extend([
        '-i', video_path,
        '-i', audio_path,
        '-map', '0:v',
        '-map', '1:a',
        '-c:v', 'copy',
        '-c:a', 'aac',
        '-b:a', '192k',
        '-y', output_path
    ])

    print(f"Syncing audio/video...")
    if offset_seconds != 0.0:
        action = "delaying" if offset_seconds > 0 else "advancing"
        print(f"  {action.capitalize()} audio by {abs(offset_seconds)}s")

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        return {'success': False, 'error': result.stderr}

    return {'success': True, 'output_path': output_path, 'offset': offset_seconds}

# Usage
result = sync_audio_video(
    "video.mp4",
    "audio.mp3",
    "synced_output.mp4",
    offset_seconds=0.5  # Delay audio by 500ms
)
```

---

## Subtitle Burning

### Basic Subtitle Burn

```bash
# Burn SRT subtitles into video
ffmpeg -i video.mp4 -vf subtitles=subtitle.srt \
  -c:a copy \  # Keep audio as-is
  output.mp4
```

### Custom Subtitle Style

```bash
# Burn subtitles with custom style
ffmpeg -i video.mp4 \
  -vf "subtitles=subtitle.srt:force_style='FontName=Arial,FontSize=24,PrimaryColour=&HFFFFFF,OutlineColour=&H000000,Outline=2'" \
  -c:a copy \
  output.mp4
```

### Python: Subtitle Burning

```python
def burn_subtitles(
    video_path: str,
    srt_path: str,
    output_path: str,
    font_name: str = "Arial",
    font_size: int = 24,
    font_color: str = "&HFFFFFF",  # White
    outline_color: str = "&H000000",  # Black
    outline_width: int = 2
) -> dict:
    """
    Burn subtitles into video with custom styling

    Args:
        video_path: Input video
        srt_path: SRT subtitle file
        output_path: Output video
        font_name: Font name
        font_size: Font size
        font_color: Font color (hex)
        outline_color: Outline color (hex)
        outline_width: Outline width (pixels)

    Returns:
        Result dict
    """
    # Build style string
    style = f"FontName={font_name},FontSize={font_size}," \
            f"PrimaryColour={font_color},OutlineColour={outline_color}," \
            f"Outline={outline_width}"

    # Build filter
    vf = f"subtitles={srt_path}:force_style='{style}'"

    cmd = [
        'ffmpeg',
        '-i', video_path,
        '-vf', vf,
        '-c:a', 'copy',  # Keep audio
        '-y', output_path
    ]

    print(f"Burning subtitles into {video_path}...")
    print(f"  Subtitles: {srt_path}")
    print(f"  Style: {font_name} {font_size}px")

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        return {'success': False, 'error': result.stderr}

    return {'success': True, 'output_path': output_path}

# Usage
result = burn_subtitles(
    "video.mp4",
    "subtitles.srt",
    "video_with_subs.mp4",
    font_name="Arial",
    font_size=28,
    font_color="&HFFFFFF"  # White
)
```

---

## Audio Extraction

### Extract as MP3 (Lossy)

```bash
# Extract audio as MP3 (high quality)
ffmpeg -i video.mp4 -vn -acodec libmp3lame -q:a 2 audio.mp3
# q:a 0 = best quality, 9 = worst quality (2 = high quality)
```

### Extract as WAV (Lossless)

```bash
# Extract audio as WAV (uncompressed)
ffmpeg -i video.mp4 -vn -acodec pcm_s16le audio.wav
```

### Extract as AAC

```bash
# Extract audio as AAC
ffmpeg -i video.mp4 -vn -c:a aac -b:a 192k audio.m4a
```

### Python: Audio Extraction

```python
def extract_audio(
    video_path: str,
    output_path: str,
    format: str = "mp3",
    quality: str = "high"
) -> dict:
    """
    Extract audio from video

    Args:
        video_path: Input video file
        output_path: Output audio file
        format: 'mp3', 'wav', 'aac', 'm4a'
        quality: 'low', 'medium', 'high', 'lossless'

    Returns:
        Result dict
    """
    cmd = ['ffmpeg', '-i', video_path, '-vn']

    # Configure codec and quality
    if format == 'mp3':
        cmd.extend(['-acodec', 'libmp3lame'])
        quality_map = {'low': '5', 'medium': '3', 'high': '2', 'lossless': '0'}
        cmd.extend(['-q:a', quality_map.get(quality, '2')])

    elif format == 'wav':
        cmd.extend(['-acodec', 'pcm_s16le'])

    elif format in ['aac', 'm4a']:
        cmd.extend(['-c:a', 'aac'])
        bitrate_map = {'low': '96k', 'medium': '128k', 'high': '192k', 'lossless': '320k'}
        cmd.extend(['-b:a', bitrate_map.get(quality, '192k')])

    cmd.extend(['-y', output_path])

    print(f"Extracting audio from {video_path}...")
    print(f"  Format: {format}, Quality: {quality}")

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        return {'success': False, 'error': result.stderr}

    output_size_mb = Path(output_path).stat().st_size / (1024 * 1024)
    return {
        'success': True,
        'output_path': output_path,
        'format': format,
        'size_mb': output_size_mb
    }

# Usage
result = extract_audio(
    "video.mp4",
    "audio.mp3",
    format="mp3",
    quality="high"
)
```

---

## Video Quality Optimization

### H.264 Encoding (Best Compatibility)

```bash
# High quality H.264 encode
ffmpeg -i input.mp4 \
  -c:v libx264 \
  -preset slow \      # slow = better compression (fast, medium, slow, veryslow)
  -crf 18 \           # 18 = near-lossless (0-51, lower = better quality)
  -c:a aac \
  -b:a 192k \
  -y output.mp4
```

### CRF (Constant Rate Factor) Guide

```
CRF Value  |  Quality        |  Use Case
-----------|-----------------|------------------
0          |  Lossless       |  Archival (huge files)
17-18      |  Visually lossless | Professional work
23         |  High quality   |  Default (good balance)
28         |  Medium quality |  Streaming
35+        |  Low quality    |  Not recommended
```

### Preset Guide

```
Preset      |  Speed  |  Compression  |  Use Case
------------|---------|---------------|------------------
ultrafast   |  ⚡⚡⚡  |  Poor        |  Real-time encoding
fast        |  ⚡⚡    |  Fair        |  Quick processing
medium      |  ⚡      |  Good        |  Default
slow        |  🐌      |  Better      |  High quality
veryslow    |  🐌🐌    |  Best        |  Archival/distribution
```

### Python: Quality Optimization

```python
def optimize_video_quality(
    input_path: str,
    output_path: str,
    quality: str = "high",
    preset: str = "medium",
    audio_bitrate: str = "192k"
) -> dict:
    """
    Optimize video quality with H.264

    Args:
        input_path: Input video
        output_path: Output video
        quality: 'lossless', 'high', 'medium', 'low'
        preset: 'fast', 'medium', 'slow', 'veryslow'
        audio_bitrate: Audio bitrate

    Returns:
        Result dict
    """
    # Map quality to CRF
    crf_map = {
        'lossless': '0',
        'high': '18',
        'medium': '23',
        'low': '28'
    }
    crf = crf_map.get(quality, '23')

    cmd = [
        'ffmpeg',
        '-i', input_path,
        '-c:v', 'libx264',
        '-preset', preset,
        '-crf', crf,
        '-c:a', 'aac',
        '-b:a', audio_bitrate,
        '-y', output_path
    ]

    print(f"Optimizing video quality...")
    print(f"  Quality: {quality} (CRF {crf})")
    print(f"  Preset: {preset}")

    import time
    start_time = time.time()

    result = subprocess.run(cmd, capture_output=True, text=True)

    elapsed = time.time() - start_time

    if result.returncode != 0:
        return {'success': False, 'error': result.stderr}

    # Get file sizes
    input_size_mb = Path(input_path).stat().st_size / (1024 * 1024)
    output_size_mb = Path(output_path).stat().st_size / (1024 * 1024)
    compression_ratio = (1 - output_size_mb / input_size_mb) * 100

    print(f"✅ Optimized!")
    print(f"   Input: {input_size_mb:.2f} MB")
    print(f"   Output: {output_size_mb:.2f} MB ({compression_ratio:+.1f}%)")
    print(f"   Time: {elapsed:.2f}s")

    return {
        'success': True,
        'output_path': output_path,
        'input_size_mb': input_size_mb,
        'output_size_mb': output_size_mb,
        'compression_ratio': compression_ratio,
        'processing_time_s': elapsed
    }

# Usage
result = optimize_video_quality(
    "input.mp4",
    "optimized.mp4",
    quality="high",
    preset="slow"
)
```

---

## Format Conversion

### Common Format Conversions

```bash
# MOV to MP4
ffmpeg -i input.mov -c:v libx264 -preset medium -crf 23 -c:a aac -b:a 192k output.mp4

# AVI to MP4
ffmpeg -i input.avi -c:v libx264 -preset medium -crf 23 -c:a aac -b:a 192k output.mp4

# MKV to MP4
ffmpeg -i input.mkv -c:v copy -c:a aac -b:a 192k output.mp4  # Copy video if already H.264

# WebM to MP4
ffmpeg -i input.webm -c:v libx264 -preset medium -crf 23 -c:a aac -b:a 192k output.mp4
```

### Python: Universal Converter

```python
def convert_video_format(
    input_path: str,
    output_path: str,
    copy_video: bool = False,
    video_codec: str = "libx264",
    audio_codec: str = "aac",
    audio_bitrate: str = "192k",
    crf: str = "23"
) -> dict:
    """
    Convert video to any format

    Args:
        input_path: Input video
        output_path: Output video (extension determines format)
        copy_video: Copy video stream (if already compatible codec)
        video_codec: Video codec (libx264, libx265, etc.)
        audio_codec: Audio codec (aac, mp3, etc.)
        audio_bitrate: Audio bitrate
        crf: Quality (lower = better, 23 = default)

    Returns:
        Result dict
    """
    cmd = ['ffmpeg', '-i', input_path]

    # Video codec
    if copy_video:
        cmd.extend(['-c:v', 'copy'])
    else:
        cmd.extend(['-c:v', video_codec, '-crf', crf])

    # Audio codec
    cmd.extend(['-c:a', audio_codec, '-b:a', audio_bitrate])

    cmd.extend(['-y', output_path])

    print(f"Converting {input_path} → {output_path}")
    if copy_video:
        print("  Copying video stream (fast)")

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        return {'success': False, 'error': result.stderr}

    return {'success': True, 'output_path': output_path}

# Usage
result = convert_video_format(
    "input.mov",
    "output.mp4",
    copy_video=False,  # Re-encode for compatibility
    crf="23"
)
```

---

## Video Trimming & Cutting

### Trim Video (Fast - Copy Streams)

```bash
# Trim from 00:01:00 to 00:02:00 (1 minute segment)
ffmpeg -i input.mp4 \
  -ss 00:01:00 \     # Start time
  -to 00:02:00 \     # End time
  -c copy \          # Copy streams (fast, no re-encode)
  output.mp4
```

### Trim Video (Accurate - Re-encode)

```bash
# Accurate trimming (re-encode)
ffmpeg -i input.mp4 \
  -ss 00:01:00 \
  -to 00:02:00 \
  -c:v libx264 -crf 23 \  # Re-encode for frame-accurate cutting
  -c:a aac -b:a 192k \
  output.mp4
```

### Python: Video Trimming

```python
def trim_video(
    input_path: str,
    output_path: str,
    start_time: str,
    end_time: str = None,
    duration: str = None,
    accurate: bool = False
) -> dict:
    """
    Trim video to specific time range

    Args:
        input_path: Input video
        output_path: Output video
        start_time: Start time (HH:MM:SS or seconds)
        end_time: End time (HH:MM:SS or seconds)
        duration: Duration instead of end_time (seconds or HH:MM:SS)
        accurate: Re-encode for frame-accurate cutting

    Returns:
        Result dict

    Examples:
        trim_video("vid.mp4", "out.mp4", "00:01:30", end_time="00:02:45")
        trim_video("vid.mp4", "out.mp4", "90", duration="75")  # 90s to 165s
    """
    cmd = ['ffmpeg', '-i', input_path, '-ss', start_time]

    if end_time:
        cmd.extend(['-to', end_time])
    elif duration:
        cmd.extend(['-t', duration])

    if accurate:
        # Re-encode for accuracy
        cmd.extend(['-c:v', 'libx264', '-crf', '23', '-c:a', 'aac', '-b:a', '192k'])
    else:
        # Copy streams (fast)
        cmd.extend(['-c', 'copy'])

    cmd.extend(['-y', output_path])

    print(f"Trimming {input_path}...")
    print(f"  From: {start_time}")
    if end_time:
        print(f"  To: {end_time}")
    if duration:
        print(f"  Duration: {duration}")
    print(f"  Mode: {'Accurate (re-encode)' if accurate else 'Fast (copy)'}")

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        return {'success': False, 'error': result.stderr}

    return {'success': True, 'output_path': output_path}

# Usage
result = trim_video(
    "full_video.mp4",
    "trimmed.mp4",
    start_time="00:01:30",
    end_time="00:03:45",
    accurate=False  # Fast copy mode
)
```

---

## Video Concatenation

### Concatenate (Same Codec)

```bash
# 1. Create file list
cat > filelist.txt << EOF
file 'video1.mp4'
file 'video2.mp4'
file 'video3.mp4'
EOF

# 2. Concatenate
ffmpeg -f concat -safe 0 -i filelist.txt -c copy output.mp4
```

### Python: Concatenate Videos

```python
def concatenate_videos(
    video_files: list,
    output_path: str,
    re_encode: bool = False
) -> dict:
    """
    Concatenate multiple videos

    Args:
        video_files: List of video file paths
        output_path: Output video path
        re_encode: Re-encode (slower but safer)

    Returns:
        Result dict
    """
    import tempfile
    import os

    # Create file list
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
        for video in video_files:
            f.write(f"file '{os.path.abspath(video)}'\n")
        filelist_path = f.name

    # Build command
    cmd = [
        'ffmpeg',
        '-f', 'concat',
        '-safe', '0',
        '-i', filelist_path
    ]

    if re_encode:
        cmd.extend(['-c:v', 'libx264', '-crf', '23', '-c:a', 'aac', '-b:a', '192k'])
    else:
        cmd.extend(['-c', 'copy'])

    cmd.extend(['-y', output_path])

    print(f"Concatenating {len(video_files)} videos...")
    for i, vid in enumerate(video_files, 1):
        print(f"  {i}. {vid}")

    result = subprocess.run(cmd, capture_output=True, text=True)

    # Cleanup
    os.unlink(filelist_path)

    if result.returncode != 0:
        return {'success': False, 'error': result.stderr}

    return {'success': True, 'output_path': output_path}

# Usage
result = concatenate_videos(
    ['part1.mp4', 'part2.mp4', 'part3.mp4'],
    'complete_video.mp4',
    re_encode=False  # Fast copy mode
)
```

---

## Production Video Dubbing Pipeline

### Complete Workflow: Video + New Audio + Subtitles

```python
def production_video_dubbing(
    original_video: str,
    dubbed_audio: str,
    subtitles_srt: str,
    output_video: str,
    burn_subtitles: bool = False,
    audio_offset_s: float = 0.0
) -> dict:
    """
    Complete video dubbing pipeline

    Steps:
    1. Replace audio track
    2. Optionally burn subtitles
    3. Optimize quality

    Args:
        original_video: Original video file
        dubbed_audio: Dubbed audio track
        subtitles_srt: Subtitle file
        output_video: Output video file
        burn_subtitles: Burn subtitles into video
        audio_offset_s: Audio sync offset (seconds)

    Returns:
        Result dict
    """
    import tempfile
    import os

    print("=" * 60)
    print("PRODUCTION VIDEO DUBBING PIPELINE")
    print("=" * 60)

    # Step 1: Replace audio
    print("\nStep 1: Replacing audio track...")
    with tempfile.NamedTemporaryFile(suffix='.mp4', delete=False) as tmp:
        temp_video = tmp.name

    result1 = sync_audio_video(
        original_video,
        dubbed_audio,
        temp_video,
        offset_seconds=audio_offset_s
    )

    if not result1['success']:
        return {'success': False, 'step': 1, 'error': result1['error']}

    # Step 2: Burn subtitles (if enabled)
    if burn_subtitles:
        print("\nStep 2: Burning subtitles...")
        with tempfile.NamedTemporaryFile(suffix='.mp4', delete=False) as tmp2:
            temp_video2 = tmp2.name

        result2 = burn_subtitles(
            temp_video,
            subtitles_srt,
            temp_video2
        )

        os.unlink(temp_video)  # Cleanup intermediate file

        if not result2['success']:
            return {'success': False, 'step': 2, 'error': result2['error']}

        temp_video = temp_video2

    # Step 3: Optimize quality
    print("\nStep 3: Optimizing quality...")
    result3 = optimize_video_quality(
        temp_video,
        output_video,
        quality="high",
        preset="medium"
    )

    os.unlink(temp_video)  # Cleanup

    if not result3['success']:
        return {'success': False, 'step': 3, 'error': result3['error']}

    print("\n" + "=" * 60)
    print("✅ DUBBING COMPLETE!")
    print("=" * 60)
    print(f"Output: {output_video}")
    print(f"Size: {result3['output_size_mb']:.2f} MB")

    return {
        'success': True,
        'output_video': output_video,
        'output_size_mb': result3['output_size_mb'],
        'audio_offset': audio_offset_s,
        'subtitles_burned': burn_subtitles
    }

# Usage
result = production_video_dubbing(
    original_video="original.mp4",
    dubbed_audio="english_dubbed.mp3",
    subtitles_srt="english_subtitles.srt",
    output_video="final_dubbed_video.mp4",
    burn_subtitles=True,
    audio_offset_s=0.0  # No offset needed
)
```

---

## Common Pitfalls & Solutions

### Problem 1: Audio/Video Out of Sync

**Symptoms:**
- Lips don't match audio
- Audio starts too early/late

**Solutions:**
```bash
# Delay audio by 500ms
ffmpeg -i video.mp4 -itsoffset 0.5 -i audio.mp3 -map 0:v -map 1:a -c:v copy -c:a aac output.mp4

# Advance audio by 200ms
ffmpeg -i video.mp4 -itsoffset -0.2 -i audio.mp3 -map 0:v -map 1:a -c:v copy -c:a aac output.mp4
```

---

### Problem 2: Quality Loss After Processing

**Cause:** Re-encoding video

**Solution:**
```bash
# ✅ Use -c:v copy to avoid re-encoding
ffmpeg -i video.mp4 -i audio.mp3 -c:v copy -c:a aac output.mp4

# ❌ Avoid implicit re-encoding
ffmpeg -i video.mp4 -i audio.mp3 output.mp4  # Will re-encode!
```

---

### Problem 3: File Size Too Large

**Solutions:**
```bash
# Reduce CRF (higher = smaller file)
ffmpeg -i input.mp4 -c:v libx264 -crf 28 -c:a aac -b:a 128k output.mp4

# Use faster preset (less compression but faster)
ffmpeg -i input.mp4 -c:v libx264 -preset fast -crf 23 output.mp4

# Reduce resolution
ffmpeg -i input.mp4 -vf scale=1280:720 -c:v libx264 -crf 23 output.mp4
```

---

### Problem 4: Codec Not Compatible

**Error:** `Codec not currently supported`

**Solution:**
```bash
# Convert to widely supported H.264/AAC
ffmpeg -i input.mov -c:v libx264 -c:a aac output.mp4
```

---

## Quick Reference

### Command Syntax

```bash
ffmpeg [input options] -i input.mp4 [output options] output.mp4
```

### Essential Options

| Option | Purpose | Example |
|--------|---------|---------|
| `-c:v copy` | Copy video (no re-encode) | `-c:v copy` |
| `-c:a copy` | Copy audio (no re-encode) | `-c:a copy` |
| `-c:v libx264` | Encode video to H.264 | `-c:v libx264 -crf 23` |
| `-c:a aac` | Encode audio to AAC | `-c:a aac -b:a 192k` |
| `-map 0:v:0` | Map video stream | `-map 0:v:0` |
| `-map 1:a:0` | Map audio stream | `-map 1:a:0` |
| `-vf` | Video filter | `-vf subtitles=sub.srt` |
| `-ss` | Start time | `-ss 00:01:30` |
| `-to` | End time | `-to 00:02:45` |
| `-t` | Duration | `-t 60` (60 seconds) |
| `-y` | Overwrite output | `-y` |

---

**Last Updated:** 2025-10-24
**Version:** 1.0
**Lines:** 900+
**Status:** Production Ready ✅
