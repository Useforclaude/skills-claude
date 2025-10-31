---
name: whisper-transcription-skill
description: Expert Whisper audio transcription for production use (OpenAI Whisper large-v3 + Faster-Whisper). Use for Thai transcription optimization, multilingual transcription, VAD integration, chunking strategies, hallucination removal, GPU optimization, SRT generation, Faster-Whisper (4-5x speed boost), batch processing, and production-ready audio-to-text workflows. Also use for Thai keywords "วิดีโอ", "คลิป", "ภาพเคลื่อนไหว", "วีดีโอ", "คอนเทนต์", "เนื้อหา", "สร้างเนื้อหา", "content", "AI วิดีโอ", "สร้างวิดีโอ AI", "วิดีโอ AI", "AI สร้างวิดีโอ", "ถอดเสียง", "ถอดข้อความ", "transcribe", "faster-whisper"
---

# Whisper Transcription Expert Skill

## Overview

Expert-level knowledge for production Whisper transcription, specializing in Thai language optimization, GPU efficiency, and high-accuracy audio-to-text conversion for video localization workflows.

**New:** Includes **Faster-Whisper** integration (4-5x speed boost, 62% less RAM, same accuracy)

**When to use this skill:**
- Transcribing Thai audio/video to SRT
- Optimizing Whisper accuracy for specific languages
- **Using Faster-Whisper for 4-5x speed boost** ⚡
- Implementing VAD (Voice Activity Detection)
- Managing long audio files with smart chunking
- Removing Whisper hallucinations
- GPU memory optimization
- **Batch processing multiple videos** (tmux/background)
- Production transcription pipelines

---

## Table of Contents

1. [Model Selection](#model-selection)
2. [Thai Language Optimization](#thai-language-optimization)
3. [Smart Chunking Strategies](#smart-chunking-strategies)
4. [VAD Integration](#vad-integration)
5. [Hallucination Removal](#hallucination-removal)
6. [GPU Optimization](#gpu-optimization)
7. [SRT Generation](#srt-generation)
8. [Production Best Practices](#production-best-practices)
9. [Platform-Specific Guides](#platform-specific-guides)
10. [Common Pitfalls & Solutions](#common-pitfalls-solutions)

---

## Model Selection

### Available Whisper Models

**Standard OpenAI Whisper:**

| Model | Size | Parameters | Accuracy | Speed | VRAM | Best For |
|-------|------|------------|----------|-------|------|----------|
| tiny | 39 MB | 39M | ⭐ | ⚡⚡⚡ | 1 GB | Testing only |
| base | 74 MB | 74M | ⭐⭐ | ⚡⚡⚡ | 1 GB | Quick drafts |
| small | 244 MB | 244M | ⭐⭐⭐ | ⚡⚡ | 2 GB | General use |
| medium | 769 MB | 769M | ⭐⭐⭐⭐ | ⚡ | 5 GB | Quality work |
| large-v2 | 1.5 GB | 1550M | ⭐⭐⭐⭐⭐ | 🐌 | 10 GB | Production |
| large-v3 | 1.5 GB | 1550M | ⭐⭐⭐⭐⭐+ | 🐌 | 10 GB | Production (Latest) |

**⚡ Faster-Whisper (Recommended for Production):**

| Model | Size | Parameters | Accuracy | Speed | VRAM | Best For |
|-------|------|------------|----------|-------|------|----------|
| large-v3 (INT8) | 1.5 GB | 1550M | ⭐⭐⭐⭐⭐+ | ⚡⚡⚡⚡ | 4 GB | **Production (4-5x faster!)** |
| large-v3 (FP16) | 1.5 GB | 1550M | ⭐⭐⭐⭐⭐+ | ⚡⚡⚡ | 6 GB | High accuracy + speed |

### ⚡ Whisper vs Faster-Whisper Comparison

| Feature | OpenAI Whisper | Faster-Whisper | Winner |
|---------|---------------|----------------|--------|
| **Speed** | 1x (baseline) | **4-5x faster** ⚡ | Faster-Whisper 🏆 |
| **RAM Usage** | 10 GB | **4 GB** (62% less) | Faster-Whisper 🏆 |
| **Accuracy** | 95%+ | 95%+ (same) | Tie ✅ |
| **Installation** | `pip install openai-whisper` | `pip install faster-whisper` | Equal |
| **GPU Support** | PyTorch CUDA | CTranslate2 CUDA | Equal |
| **API** | `whisper.load_model()` | `WhisperModel()` | Different |

**Performance Metrics (10-minute Thai video):**

| Engine | Transcription Time | RAM Usage | GPU Utilization |
|--------|-------------------|-----------|-----------------|
| OpenAI Whisper | ~10 minutes | ~10 GB | 85-95% |
| **Faster-Whisper** | **~2-3 minutes** ⚡ | **~4 GB** | 90-100% |

### Why Faster-Whisper is Better

**Technical Advantages:**

1. **INT8 Quantization**
   - Reduces precision from float32 → int8 (32 bits → 8 bits)
   - **4x smaller memory footprint**
   - Only 0.1% accuracy loss (negligible for Thai)
   - Enables larger batch processing

2. **CTranslate2 Engine**
   - Inference-optimized (vs PyTorch general-purpose)
   - Hardware-aware optimizations (GPU Tensor Cores, CPU AVX2/AVX-512)
   - Better memory management (streaming model loading)
   - Custom CUDA kernels for speed

3. **Better Batching**
   - Parallel segment processing (vs sequential)
   - Dynamic batch size optimization
   - Reduced GPU idle time

4. **Memory Efficiency**
   - Streaming model loading (not all-at-once)
   - Automatic cache management
   - Lower VRAM requirements → bigger batch sizes

**When to Use Each:**

| Use Case | Recommended Engine | Reason |
|----------|-------------------|--------|
| **Production transcription** | ⚡ Faster-Whisper | 4-5x speed, same accuracy |
| **Long videos (>30 min)** | ⚡ Faster-Whisper | Lower RAM, faster processing |
| **Batch processing** | ⚡ Faster-Whisper | Process 4-5x more files/hour |
| **Development/testing** | OpenAI Whisper | Simpler API, more familiar |
| **Research** | OpenAI Whisper | Direct PyTorch access |

### Language-Specific Recommendations

**Thai Language:**
- ✅ **large-v3** - Best accuracy (95%+)
- ⚠️ medium - Acceptable (85-90%)
- ❌ small/base - Poor (<80%)

**English:**
- ✅ large-v3 or medium - Both excellent (98%+)
- ✅ small - Good enough for drafts (92%+)

**Multilingual (Code-switching):**
- ✅ large-v3 only - Required for accurate language detection

### Installation

**Option 1: OpenAI Whisper (Standard)**

```bash
# Install Whisper
pip install -U openai-whisper

# Install dependencies
pip install ffmpeg-python

# For GPU support
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

**Option 2: Faster-Whisper (Recommended for Production) ⚡**

```bash
# Install Faster-Whisper
pip install faster-whisper

# Install dependencies (if not already installed)
pip install ffmpeg-python

# GPU support is included automatically
# No need to install separate PyTorch
```

**Note:** You can install both! They don't conflict with each other.

```bash
# Install both for flexibility
pip install openai-whisper faster-whisper
```

### Basic Usage

**OpenAI Whisper (Standard):**

```python
import whisper

# Load model (once)
model = whisper.load_model("large-v3")

# Transcribe
result = model.transcribe("audio.mp3")

print(result["text"])  # Full transcription
print(result["segments"])  # Timestamped segments
```

**Faster-Whisper (4-5x faster!) ⚡:**

```python
from faster_whisper import WhisperModel

# Load model (once)
# device="cuda" for GPU, "cpu" for CPU
# compute_type="int8" for speed, "float16" for quality
model = WhisperModel("large-v3", device="cuda", compute_type="int8")

# Transcribe (returns generator!)
segments, info = model.transcribe("audio.mp3", language="th")

# Convert to list (if needed)
segments_list = list(segments)

# Print results
for segment in segments_list:
    print(f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}")

# Or convert to OpenAI Whisper format
result = {
    "text": "",
    "segments": [],
    "language": info.language
}

for segment in segments_list:
    result["text"] += segment.text + " "
    result["segments"].append({
        "start": segment.start,
        "end": segment.end,
        "text": segment.text
    })
```

**Faster-Whisper with Word Timestamps:**

```python
from faster_whisper import WhisperModel

model = WhisperModel("large-v3", device="cuda", compute_type="int8")

# Enable word timestamps
segments, info = model.transcribe(
    "audio.mp3",
    language="th",
    word_timestamps=True  # Enable word-level timestamps
)

for segment in segments:
    print(f"Segment: {segment.text}")

    # Word-level timestamps
    if segment.words:
        for word in segment.words:
            print(f"  [{word.start:.2f}s -> {word.end:.2f}s] {word.word}")
```

---

## Thai Language Optimization

### Critical: Initial Prompt

**The single most important factor for Thai accuracy is the initial prompt:**

```python
# ✅ CORRECT - Dramatically improves Thai accuracy
result = model.transcribe(
    audio_path,
    language="th",  # Explicitly set Thai
    initial_prompt="นี่คือการบรรยายเกี่ยวกับ Forex การเทรด และการลงทุน ผู้บรรยายพูดภาษาไทยชัดเจน"
)

# ❌ WRONG - Auto-detect often switches to English mid-sentence
result = model.transcribe(audio_path)
```

**Why Initial Prompt Matters:**
- Provides context for domain vocabulary
- Primes the model for Thai language
- Reduces hallucinations
- Prevents language switching
- **Improves accuracy by 5-10%**

### Domain-Specific Initial Prompts

**Financial/Forex Content:**
```python
initial_prompt = """
นี่คือการบรรยายเกี่ยวกับ Forex การเทรด การลงทุน
คำศัพท์: ราคา กราฟ แนวต้าน แนวรับ เทรนด์ สัญญาณ โบรกเกอร์
ผู้บรรยายพูดภาษาไทยชัดเจน
"""
```

**Technical/Programming Content:**
```python
initial_prompt = """
การสอนเทคโนโลยี โปรแกรมมิ่ง การพัฒนาซอฟต์แวร์
คำศัพท์: โค้ด ฟังก์ชัน ตัวแปร อัลกอริทึม
ผู้บรรยายพูดภาษาไทยชัดเจน
"""
```

**General/Educational Content:**
```python
initial_prompt = """
การบรรยายภาษาไทยทั่วไป เนื้อหาการศึกษา
ผู้บรรยายพูดภาษาไทยชัดเจน มีคำศัพท์ทั่วไป
"""
```

### Full Thai Transcription Template

```python
import whisper
import torch

def transcribe_thai_audio(
    audio_path: str,
    model_name: str = "large-v3",
    initial_prompt: str = None,
    device: str = None
) -> dict:
    """
    Optimized Thai transcription with Whisper

    Args:
        audio_path: Path to audio file
        model_name: Whisper model (default: large-v3)
        initial_prompt: Domain-specific context
        device: 'cuda' or 'cpu' (auto-detect if None)

    Returns:
        dict with 'text', 'segments', 'language'
    """
    # Auto-detect device
    if device is None:
        device = "cuda" if torch.cuda.is_available() else "cpu"

    # Default Thai prompt
    if initial_prompt is None:
        initial_prompt = "นี่คือการบรรยายภาษาไทย ผู้บรรยายพูดชัดเจน"

    # Load model
    print(f"Loading {model_name} on {device}...")
    model = whisper.load_model(model_name, device=device)

    # Transcribe with Thai optimization
    print(f"Transcribing {audio_path}...")
    result = model.transcribe(
        audio_path,
        language="th",              # Force Thai
        initial_prompt=initial_prompt,
        word_timestamps=True,       # Enable word-level timing
        fp16=(device == "cuda"),    # Use FP16 on GPU for 2x speed
        temperature=0.0,            # Deterministic output
        beam_size=5,                # Beam search for accuracy
        best_of=5,                  # Generate 5 candidates
        condition_on_previous_text=True  # Use context from previous segments
    )

    print(f"Transcription complete: {len(result['segments'])} segments")
    return result

# Usage
result = transcribe_thai_audio(
    "thai_forex_lesson.mp3",
    initial_prompt="นี่คือการบรรยายเกี่ยวกับ Forex การเทรด และการลงทุน"
)

print(result["text"])
```

---

## Smart Chunking Strategies

### Problem: Whisper Has Maximum Length

**Whisper optimal length:** ~30 seconds per chunk
**Problem:** Cutting mid-word destroys context

### Solution 1: Silence-Based Chunking

```python
from pydub import AudioSegment
from pydub.silence import detect_nonsilent
from pathlib import Path

def smart_chunk_audio(
    audio_path: str,
    max_duration_ms: int = 30000,
    min_silence_len: int = 500,
    silence_thresh: int = -40,
    output_dir: str = "chunks"
) -> list:
    """
    Split audio at silence points (never mid-word!)

    Args:
        audio_path: Input audio file
        max_duration_ms: Max chunk duration (30s default)
        min_silence_len: Minimum silence to consider (500ms)
        silence_thresh: Silence threshold in dB (-40 default)
        output_dir: Where to save chunks

    Returns:
        List of chunk file paths
    """
    # Load audio
    audio = AudioSegment.from_file(audio_path)
    print(f"Audio duration: {len(audio) / 1000:.2f}s")

    # Detect voice activity (non-silent ranges)
    nonsilent_ranges = detect_nonsilent(
        audio,
        min_silence_len=min_silence_len,
        silence_thresh=silence_thresh
    )

    print(f"Found {len(nonsilent_ranges)} voice segments")

    # Group into chunks at silence points
    chunks = []
    current_chunk_start = 0
    current_duration = 0

    for i, (start, end) in enumerate(nonsilent_ranges):
        segment_duration = end - start

        # Check if adding this segment exceeds max duration
        if current_duration + segment_duration > max_duration_ms:
            # Save current chunk (ends at silence before this segment)
            chunks.append({
                'start': current_chunk_start,
                'end': start,
                'duration': start - current_chunk_start
            })

            # Start new chunk
            current_chunk_start = start
            current_duration = segment_duration
        else:
            current_duration += segment_duration

    # Add final chunk
    if current_duration > 0:
        chunks.append({
            'start': current_chunk_start,
            'end': len(audio),
            'duration': len(audio) - current_chunk_start
        })

    # Export chunks
    Path(output_dir).mkdir(exist_ok=True)
    chunk_files = []

    for i, chunk in enumerate(chunks):
        chunk_audio = audio[chunk['start']:chunk['end']]
        chunk_file = f"{output_dir}/chunk_{i:04d}.wav"
        chunk_audio.export(chunk_file, format="wav")
        chunk_files.append(chunk_file)
        print(f"Chunk {i}: {chunk['duration']/1000:.2f}s → {chunk_file}")

    return chunk_files

# Usage
chunks = smart_chunk_audio("long_audio.mp3", max_duration_ms=25000)
print(f"Created {len(chunks)} chunks")
```

### Solution 2: Overlapping Chunks (Better Context)

```python
def create_overlapping_chunks(
    audio_path: str,
    chunk_duration_ms: int = 25000,
    overlap_ms: int = 2000,
    output_dir: str = "chunks"
) -> list:
    """
    Create overlapping chunks for better context preservation

    Args:
        audio_path: Input audio
        chunk_duration_ms: Chunk size (25s)
        overlap_ms: Overlap between chunks (2s)
        output_dir: Output directory

    Returns:
        List of (chunk_file, start_ms, end_ms)
    """
    audio = AudioSegment.from_file(audio_path)
    total_duration = len(audio)

    chunks = []
    start = 0
    chunk_num = 0

    Path(output_dir).mkdir(exist_ok=True)

    while start < total_duration:
        # Calculate chunk boundaries
        end = min(start + chunk_duration_ms, total_duration)

        # Extract chunk
        chunk_audio = audio[start:end]

        # Export
        chunk_file = f"{output_dir}/chunk_{chunk_num:04d}.wav"
        chunk_audio.export(chunk_file, format="wav")

        chunks.append({
            'file': chunk_file,
            'start_ms': start,
            'end_ms': end,
            'duration_ms': end - start
        })

        print(f"Chunk {chunk_num}: {start/1000:.2f}s - {end/1000:.2f}s")

        # Move start by (chunk_duration - overlap)
        start += (chunk_duration_ms - overlap_ms)
        chunk_num += 1

    return chunks

# Usage
chunks = create_overlapping_chunks(
    "long_audio.mp3",
    chunk_duration_ms=25000,
    overlap_ms=2000
)
```

---

## VAD Integration

### Why Use VAD (Voice Activity Detection)?

**Benefits:**
- ⚡ 2-3x faster (skip silence)
- 💰 Save GPU/API costs
- 📊 Better timestamps (no silence gaps)
- 🎯 Reduce hallucinations (Whisper hallucinates on silence)

### WebRTC VAD Implementation

```python
import webrtcvad
import wave
import contextlib
from pathlib import Path

def remove_silence_vad(
    input_path: str,
    output_path: str,
    aggressiveness: int = 2,
    sample_rate: int = 16000
) -> dict:
    """
    Remove silence using WebRTC VAD

    Args:
        input_path: Input audio file
        output_path: Output audio file (voice only)
        aggressiveness: VAD aggressiveness (0-3, higher = more aggressive)
        sample_rate: Must be 8000, 16000, 32000, or 48000 Hz

    Returns:
        dict with statistics
    """
    from pydub import AudioSegment

    # Load and convert to proper format for VAD
    audio = AudioSegment.from_file(input_path)
    audio = audio.set_frame_rate(sample_rate).set_channels(1)

    # Initialize VAD
    vad = webrtcvad.Vad(aggressiveness)

    # Process in 30ms frames (VAD requirement)
    frame_duration_ms = 30
    frame_length = int(sample_rate * frame_duration_ms / 1000) * 2  # 2 bytes per sample

    # Collect voice frames
    voice_frames = []
    total_frames = 0
    voice_frames_count = 0

    # Convert to raw audio
    raw_audio = audio.raw_data

    for i in range(0, len(raw_audio), frame_length):
        frame = raw_audio[i:i+frame_length]

        # Pad last frame if needed
        if len(frame) < frame_length:
            frame = frame + b'\x00' * (frame_length - len(frame))

        total_frames += 1

        # Check if frame contains speech
        try:
            is_speech = vad.is_speech(frame, sample_rate)
            if is_speech:
                voice_frames.append(frame)
                voice_frames_count += 1
        except:
            # If VAD fails, keep the frame (safer)
            voice_frames.append(frame)
            voice_frames_count += 1

    # Combine voice-only frames
    voice_audio = b''.join(voice_frames)

    # Convert back to AudioSegment
    result = AudioSegment(
        data=voice_audio,
        sample_width=audio.sample_width,
        frame_rate=sample_rate,
        channels=1
    )

    # Export
    result.export(output_path, format="wav")

    # Statistics
    original_duration = len(audio) / 1000  # seconds
    voice_duration = len(result) / 1000
    silence_removed = original_duration - voice_duration
    reduction_pct = (silence_removed / original_duration) * 100

    stats = {
        'original_duration_s': original_duration,
        'voice_duration_s': voice_duration,
        'silence_removed_s': silence_removed,
        'reduction_pct': reduction_pct,
        'total_frames': total_frames,
        'voice_frames': voice_frames_count
    }

    print(f"VAD Results:")
    print(f"  Original: {original_duration:.2f}s")
    print(f"  Voice only: {voice_duration:.2f}s")
    print(f"  Silence removed: {silence_removed:.2f}s ({reduction_pct:.1f}%)")

    return stats

# Usage
stats = remove_silence_vad(
    "input.mp3",
    "voice_only.wav",
    aggressiveness=2  # 0=least aggressive, 3=most aggressive
)
```

### VAD + Whisper Pipeline

```python
def transcribe_with_vad(
    audio_path: str,
    model_name: str = "large-v3",
    vad_aggressiveness: int = 2,
    initial_prompt: str = None
) -> dict:
    """
    Complete pipeline: VAD → Whisper transcription
    """
    import tempfile
    import os

    # Step 1: Remove silence with VAD
    print("Step 1: Removing silence with VAD...")
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
        vad_output = tmp.name

    vad_stats = remove_silence_vad(
        audio_path,
        vad_output,
        aggressiveness=vad_aggressiveness
    )

    # Step 2: Transcribe voice-only audio
    print("\nStep 2: Transcribing voice-only audio...")
    result = transcribe_thai_audio(
        vad_output,
        model_name=model_name,
        initial_prompt=initial_prompt
    )

    # Cleanup
    os.unlink(vad_output)

    # Add VAD stats to result
    result['vad_stats'] = vad_stats

    return result

# Usage
result = transcribe_with_vad(
    "thai_lesson.mp3",
    model_name="large-v3",
    vad_aggressiveness=2,
    initial_prompt="นี่คือการบรรยายภาษาไทย"
)

print(f"Transcription: {result['text']}")
print(f"Time saved: {result['vad_stats']['reduction_pct']:.1f}%")
```

---

## Hallucination Removal

### Common Whisper Hallucinations

**Problem:** Whisper hallucinates when given silence or noise

**Common hallucinations:**
- "ขอบคุณครับ ขอบคุณครับ ขอบคุณครับ..." (repeated thanks)
- "Thank you for watching" (default English phrase)
- "[Music]", "[Applause]", "[Laughter]"
- "www.example.com" (fake URLs)
- "Subscribe and like" (YouTube-like phrases)

### Hallucination Detection & Removal

```python
import re
from collections import Counter

def clean_whisper_transcript(
    text: str,
    remove_repetitions: bool = True,
    remove_markers: bool = True,
    remove_urls: bool = True,
    repetition_threshold: int = 3
) -> str:
    """
    Remove Whisper hallucinations and clean transcript

    Args:
        text: Raw Whisper output
        remove_repetitions: Remove repeated phrases
        remove_markers: Remove [Music], (laughs), etc.
        remove_urls: Remove URLs
        repetition_threshold: How many times = hallucination (default: 3)

    Returns:
        Cleaned text
    """
    original_text = text

    # 1. Remove markers: [Music], [Applause], (coughs), ♪ notes ♪
    if remove_markers:
        patterns = [
            r'\[.*?\]',          # [Music], [Applause]
            r'\(.*?\)',          # (laughs), (coughs)
            r'♪.*?♪',            # ♪ music ♪
            r'\{.*?\}',          # {sound effect}
        ]
        for pattern in patterns:
            text = re.sub(pattern, '', text)

    # 2. Remove URLs
    if remove_urls:
        text = re.sub(r'https?://\S+', '', text)
        text = re.sub(r'www\.\S+\.\S+', '', text)

    # 3. Remove repeated phrases (hallucination detector)
    if remove_repetitions:
        # Find phrases that repeat more than threshold times
        words = text.split()

        # Check 2-5 word phrases
        for phrase_len in range(2, 6):
            phrases = [' '.join(words[i:i+phrase_len])
                      for i in range(len(words) - phrase_len + 1)]
            phrase_counts = Counter(phrases)

            for phrase, count in phrase_counts.items():
                if count >= repetition_threshold:
                    # This phrase repeats too much - likely hallucination
                    text = text.replace(phrase, '', count - 1)  # Keep one copy
                    print(f"Removed repeated phrase: '{phrase}' ({count} times)")

    # 4. Fix spacing
    text = re.sub(r'\s+', ' ', text)  # Multiple spaces → single space
    text = text.strip()

    # 5. Fix Thai punctuation spacing
    text = re.sub(r'\s+([.,!?])', r'\1', text)  # Remove space before punctuation
    text = re.sub(r'([.,!?])(?=[^\s])', r'\1 ', text)  # Add space after punctuation

    # 6. Remove common Thai hallucinations
    thai_hallucinations = [
        r'(ขอบคุณครับ\s*){3,}',    # Repeated "thank you"
        r'(สวัสดีครับ\s*){3,}',     # Repeated "hello"
        r'(จบแล้วครับ\s*){3,}',     # Repeated "finished"
    ]
    for pattern in thai_hallucinations:
        text = re.sub(pattern, '', text)

    # Show what was removed
    chars_removed = len(original_text) - len(text)
    if chars_removed > 0:
        print(f"Cleaned transcript: removed {chars_removed} characters")

    return text

# Usage
raw_text = """
นี่คือการบรรยายเกี่ยวกับ Forex [Music] การเทรดนั้นสำคัญมาก
ขอบคุณครับ ขอบคุณครับ ขอบคุณครับ ขอบคุณครับ
เราต้องดูกราฟให้ดี www.example.com
"""

cleaned = clean_whisper_transcript(raw_text)
print(cleaned)
# Output: "นี่คือการบรรยายเกี่ยวกับ Forex การเทรดนั้นสำคัญมาก เราต้องดูกราฟให้ดี"
```

### Hallucination Prevention (Better than Removal!)

```python
def transcribe_anti_hallucination(
    audio_path: str,
    model_name: str = "large-v3",
    initial_prompt: str = None,
    no_speech_threshold: float = 0.6,
    logprob_threshold: float = -1.0
) -> dict:
    """
    Transcribe with hallucination prevention

    Args:
        audio_path: Input audio
        model_name: Whisper model
        initial_prompt: Context prompt
        no_speech_threshold: Higher = more aggressive silence detection (0-1)
        logprob_threshold: Higher = reject low-confidence outputs

    Returns:
        Transcription result
    """
    model = whisper.load_model(model_name)

    result = model.transcribe(
        audio_path,
        language="th",
        initial_prompt=initial_prompt,
        temperature=0.0,  # Deterministic (less creative hallucinations)
        no_speech_threshold=no_speech_threshold,  # Detect silence better
        logprob_threshold=logprob_threshold,  # Reject low-confidence
        compression_ratio_threshold=2.4,  # Reject overly compressed text
        condition_on_previous_text=True,  # Use context
        fp16=True
    )

    return result
```

---

## GPU Optimization

### Check GPU Availability

```python
import torch

def check_gpu():
    """
    Check GPU availability and specs
    """
    if torch.cuda.is_available():
        gpu_name = torch.cuda.get_device_name(0)
        gpu_memory = torch.cuda.get_device_properties(0).total_memory / 1e9
        print(f"✅ GPU Available: {gpu_name}")
        print(f"   Memory: {gpu_memory:.2f} GB")
        return "cuda"
    else:
        print("❌ No GPU detected - using CPU (will be slow!)")
        return "cpu"

device = check_gpu()
```

### GPU Memory Management

```python
import gc

def transcribe_with_memory_management(
    audio_files: list,
    model_name: str = "large-v3",
    batch_size: int = 1
) -> list:
    """
    Transcribe multiple files with GPU memory cleanup

    Args:
        audio_files: List of audio file paths
        model_name: Whisper model
        batch_size: Files to process before cleanup

    Returns:
        List of transcription results
    """
    device = check_gpu()

    # Load model once
    print(f"Loading {model_name}...")
    model = whisper.load_model(model_name, device=device)

    results = []

    for i, audio_file in enumerate(audio_files):
        print(f"\nProcessing {i+1}/{len(audio_files)}: {audio_file}")

        # Transcribe
        result = model.transcribe(
            audio_file,
            language="th",
            fp16=(device == "cuda"),  # Use FP16 on GPU for 2x speed
            temperature=0.0
        )

        results.append(result)

        # Clean up GPU memory every batch_size files
        if (i + 1) % batch_size == 0 and device == "cuda":
            print("Cleaning GPU memory...")
            torch.cuda.empty_cache()
            gc.collect()

    # Final cleanup
    if device == "cuda":
        torch.cuda.empty_cache()
        gc.collect()

    return results

# Usage
files = ["file1.mp3", "file2.mp3", "file3.mp3"]
results = transcribe_with_memory_management(files, batch_size=1)
```

### FP16 Optimization (2x Faster on GPU)

```python
# ✅ ALWAYS use fp16=True on GPU
result = model.transcribe(
    audio_path,
    fp16=True,  # ← 2x faster with minimal accuracy loss
    language="th"
)

# ❌ DON'T use fp16=True on CPU (will fail)
device = "cuda" if torch.cuda.is_available() else "cpu"
result = model.transcribe(
    audio_path,
    fp16=(device == "cuda"),  # Conditional
    language="th"
)
```

---

## SRT Generation

### Convert Whisper Segments → SRT

```python
def whisper_to_srt(
    segments: list,
    output_path: str,
    max_chars_per_line: int = 42,
    max_duration_s: float = 7.0
) -> None:
    """
    Generate SRT file from Whisper segments

    Args:
        segments: Whisper result['segments']
        output_path: Output SRT file path
        max_chars_per_line: Max characters per subtitle line
        max_duration_s: Max subtitle duration (seconds)
    """
    with open(output_path, 'w', encoding='utf-8') as f:
        for i, segment in enumerate(segments, start=1):
            # SRT index
            f.write(f"{i}\n")

            # Timestamps
            start = format_srt_timestamp(segment['start'])
            end = format_srt_timestamp(segment['end'])
            f.write(f"{start} --> {end}\n")

            # Text (cleaned)
            text = clean_whisper_transcript(segment['text'])

            # Split long text into multiple lines
            lines = split_subtitle_text(text, max_chars_per_line)
            f.write('\n'.join(lines) + '\n\n')

    print(f"SRT saved: {output_path} ({len(segments)} segments)")

def format_srt_timestamp(seconds: float) -> str:
    """
    Convert seconds → SRT timestamp (HH:MM:SS,mmm)

    Args:
        seconds: Time in seconds (float)

    Returns:
        Formatted timestamp string
    """
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds % 1) * 1000)

    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"

def split_subtitle_text(text: str, max_chars: int = 42) -> list:
    """
    Split long subtitle text into multiple lines

    Args:
        text: Subtitle text
        max_chars: Max characters per line

    Returns:
        List of lines
    """
    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        test_line = current_line + " " + word if current_line else word

        if len(test_line) <= max_chars:
            current_line = test_line
        else:
            if current_line:
                lines.append(current_line)
            current_line = word

    if current_line:
        lines.append(current_line)

    return lines

# Usage
result = model.transcribe("audio.mp3", language="th")
whisper_to_srt(result['segments'], "output.srt")
```

### Complete Whisper → SRT Pipeline

```python
def audio_to_srt_complete(
    audio_path: str,
    output_srt_path: str,
    model_name: str = "large-v3",
    language: str = "th",
    initial_prompt: str = None,
    use_vad: bool = True,
    vad_aggressiveness: int = 2
) -> dict:
    """
    Complete pipeline: Audio → Whisper → Clean → SRT

    Args:
        audio_path: Input audio file
        output_srt_path: Output SRT file path
        model_name: Whisper model (default: large-v3)
        language: Language code (default: th)
        initial_prompt: Context for better accuracy
        use_vad: Use VAD to remove silence first
        vad_aggressiveness: VAD level (0-3)

    Returns:
        dict with result and statistics
    """
    import time
    start_time = time.time()

    # Step 1: VAD (optional but recommended)
    if use_vad:
        print("Step 1: Removing silence with VAD...")
        import tempfile
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
            vad_output = tmp.name

        vad_stats = remove_silence_vad(
            audio_path,
            vad_output,
            aggressiveness=vad_aggressiveness
        )
        audio_to_transcribe = vad_output
    else:
        audio_to_transcribe = audio_path
        vad_stats = None

    # Step 2: Transcribe
    print(f"\nStep 2: Transcribing with Whisper {model_name}...")
    result = transcribe_thai_audio(
        audio_to_transcribe,
        model_name=model_name,
        initial_prompt=initial_prompt
    )

    # Step 3: Clean segments
    print("\nStep 3: Cleaning transcript...")
    for segment in result['segments']:
        segment['text'] = clean_whisper_transcript(segment['text'])

    # Update full text
    result['text'] = ' '.join([seg['text'] for seg in result['segments']])

    # Step 4: Generate SRT
    print(f"\nStep 4: Generating SRT → {output_srt_path}...")
    whisper_to_srt(result['segments'], output_srt_path)

    # Cleanup VAD temp file
    if use_vad:
        import os
        os.unlink(vad_output)

    # Statistics
    elapsed_time = time.time() - start_time
    stats = {
        'audio_path': audio_path,
        'output_srt': output_srt_path,
        'model': model_name,
        'language': language,
        'segments_count': len(result['segments']),
        'total_duration_s': result['segments'][-1]['end'] if result['segments'] else 0,
        'processing_time_s': elapsed_time,
        'vad_stats': vad_stats,
        'text_length': len(result['text'])
    }

    print(f"\n✅ Complete!")
    print(f"   Segments: {stats['segments_count']}")
    print(f"   Duration: {stats['total_duration_s']:.2f}s")
    print(f"   Processing time: {elapsed_time:.2f}s")
    if vad_stats:
        print(f"   Time saved by VAD: {vad_stats['reduction_pct']:.1f}%")

    return {
        'result': result,
        'stats': stats
    }

# Usage
result = audio_to_srt_complete(
    audio_path="thai_lesson.mp3",
    output_srt_path="thai_lesson.srt",
    model_name="large-v3",
    language="th",
    initial_prompt="นี่คือการบรรยายเกี่ยวกับ Forex และการเทรด",
    use_vad=True,
    vad_aggressiveness=2
)

print(f"\nTranscript preview:")
print(result['result']['text'][:200] + "...")
```

---

## Production Best Practices

### Pre-Transcription Checklist

Before running Whisper, verify:

```python
def validate_audio_file(audio_path: str) -> dict:
    """
    Validate audio file before transcription

    Returns:
        dict with validation results
    """
    from pydub import AudioSegment
    import os

    # Check file exists
    if not os.path.exists(audio_path):
        return {'valid': False, 'error': 'File not found'}

    # Load audio
    try:
        audio = AudioSegment.from_file(audio_path)
    except Exception as e:
        return {'valid': False, 'error': f'Cannot load audio: {e}'}

    # Get specs
    sample_rate = audio.frame_rate
    channels = audio.channels
    duration_s = len(audio) / 1000
    file_size_mb = os.path.getsize(audio_path) / (1024 * 1024)

    # Validation rules
    issues = []
    warnings = []

    # Sample rate check
    if sample_rate < 16000:
        issues.append(f"Sample rate too low: {sample_rate} Hz (recommend ≥16kHz)")
    elif sample_rate < 22050:
        warnings.append(f"Sample rate low: {sample_rate} Hz (recommend ≥22kHz)")

    # Duration check
    if duration_s < 1:
        issues.append(f"Audio too short: {duration_s:.2f}s")
    elif duration_s > 3600:
        warnings.append(f"Audio very long: {duration_s/60:.1f} min (consider chunking)")

    # File size check
    if file_size_mb > 1000:
        warnings.append(f"Large file: {file_size_mb:.1f} MB")

    # Channels
    if channels > 2:
        warnings.append(f"Multi-channel audio ({channels} channels) - will be mixed to mono")

    validation = {
        'valid': len(issues) == 0,
        'audio_path': audio_path,
        'sample_rate': sample_rate,
        'channels': channels,
        'duration_s': duration_s,
        'file_size_mb': file_size_mb,
        'issues': issues,
        'warnings': warnings
    }

    # Print report
    print(f"Audio Validation: {audio_path}")
    print(f"  Sample rate: {sample_rate} Hz")
    print(f"  Channels: {channels}")
    print(f"  Duration: {duration_s:.2f}s ({duration_s/60:.1f} min)")
    print(f"  File size: {file_size_mb:.2f} MB")

    if issues:
        print(f"\n❌ Issues:")
        for issue in issues:
            print(f"   - {issue}")

    if warnings:
        print(f"\n⚠️  Warnings:")
        for warning in warnings:
            print(f"   - {warning}")

    if validation['valid'] and not warnings:
        print(f"\n✅ Audio file is ready for transcription")

    return validation

# Usage
validation = validate_audio_file("input.mp3")
if not validation['valid']:
    print("Cannot proceed - fix issues first!")
else:
    # Proceed with transcription
    result = transcribe_thai_audio("input.mp3")
```

### Quality Control

```python
def quality_check_transcription(result: dict) -> dict:
    """
    Check transcription quality

    Args:
        result: Whisper transcription result

    Returns:
        Quality metrics
    """
    segments = result['segments']

    # Calculate metrics
    total_segments = len(segments)
    total_duration = segments[-1]['end'] if segments else 0
    avg_segment_duration = total_duration / total_segments if total_segments > 0 else 0

    # Check for potential issues
    issues = []

    # 1. Too many short segments (might be noise)
    short_segments = [s for s in segments if (s['end'] - s['start']) < 0.5]
    if len(short_segments) > total_segments * 0.3:
        issues.append(f"High ratio of very short segments ({len(short_segments)}/{total_segments})")

    # 2. Repeated text (hallucination indicator)
    texts = [s['text'] for s in segments]
    unique_texts = set(texts)
    if len(unique_texts) < len(texts) * 0.7:
        issues.append(f"High text repetition (only {len(unique_texts)} unique out of {len(texts)})")

    # 3. Empty or whitespace-only segments
    empty_segments = [s for s in segments if not s['text'].strip()]
    if empty_segments:
        issues.append(f"Found {len(empty_segments)} empty segments")

    # 4. Suspiciously uniform segment lengths (might be chunking artifacts)
    segment_durations = [s['end'] - s['start'] for s in segments]
    avg_duration = sum(segment_durations) / len(segment_durations)
    uniform_count = sum(1 for d in segment_durations if abs(d - avg_duration) < 0.1)
    if uniform_count > len(segments) * 0.8:
        issues.append(f"Segments too uniform ({uniform_count}/{len(segments)}) - check chunking")

    quality = {
        'total_segments': total_segments,
        'total_duration_s': total_duration,
        'avg_segment_duration_s': avg_segment_duration,
        'unique_text_ratio': len(unique_texts) / len(texts) if texts else 0,
        'issues': issues,
        'quality_score': 100 - (len(issues) * 20)  # Simple scoring
    }

    # Print report
    print(f"\n📊 Quality Check:")
    print(f"   Total segments: {total_segments}")
    print(f"   Duration: {total_duration:.2f}s")
    print(f"   Avg segment: {avg_segment_duration:.2f}s")
    print(f"   Unique text ratio: {quality['unique_text_ratio']:.1%}")

    if issues:
        print(f"\n⚠️  Quality Issues:")
        for issue in issues:
            print(f"   - {issue}")
        print(f"\n   Quality score: {quality['quality_score']}/100")
    else:
        print(f"\n✅ No quality issues detected")
        print(f"   Quality score: 100/100")

    return quality

# Usage
result = transcribe_thai_audio("audio.mp3")
quality = quality_check_transcription(result)

if quality['quality_score'] < 60:
    print("\n⚠️  Low quality - consider re-transcribing with different parameters")
```

---

## Platform-Specific Guides

### Google Colab

```python
# ===== Google Colab Setup =====

# 1. Check GPU
!nvidia-smi

# 2. Install Whisper
!pip install -q git+https://github.com/openai/whisper.git
!pip install -q pydub webrtcvad

# 3. Mount Google Drive
from google.colab import drive
drive.mount('/content/drive')

# 4. Set paths
AUDIO_PATH = "/content/drive/MyDrive/audio/input.mp3"
OUTPUT_SRT = "/content/drive/MyDrive/output/output.srt"

# 5. Transcribe
result = audio_to_srt_complete(
    AUDIO_PATH,
    OUTPUT_SRT,
    model_name="large-v3",
    language="th",
    use_vad=True
)

# 6. Download result
from google.colab import files
files.download(OUTPUT_SRT)
```

### Kaggle

```python
# ===== Kaggle Setup =====

# 1. Check GPU quota
!nvidia-smi

# 2. Install Whisper
!pip install -q openai-whisper pydub webrtcvad

# 3. Input/Output paths
INPUT_DIR = "/kaggle/input/your-dataset/"
OUTPUT_DIR = "/kaggle/working/"

# 4. Transcribe
import os
audio_file = os.path.join(INPUT_DIR, "audio.mp3")
output_srt = os.path.join(OUTPUT_DIR, "output.srt")

result = audio_to_srt_complete(
    audio_file,
    output_srt,
    model_name="large-v3",
    use_vad=True
)

# Note: Kaggle has GPU quota - optimize with batch processing
```

### Paperspace

```python
# ===== Paperspace Setup =====

# 1. Install dependencies
!pip install openai-whisper pydub webrtcvad

# 2. Persistent storage
STORAGE_DIR = "/storage/whisper"
import os
os.makedirs(STORAGE_DIR, exist_ok=True)

# 3. Download model to persistent storage (save quota)
import whisper
model = whisper.load_model("large-v3", download_root=STORAGE_DIR)

# 4. Process files
result = audio_to_srt_complete(
    "/storage/input/audio.mp3",
    "/storage/output/output.srt",
    model_name="large-v3"
)
```

---

## Common Pitfalls & Solutions

### Problem 1: Language Switching Mid-Sentence

**Symptom:**
```
"นี่คือ trading strategy that works very well for ราคาทอง"
(Thai → English → Thai)
```

**Solution:**
```python
# ✅ Force language and use context
result = model.transcribe(
    audio,
    language="th",  # ← Force Thai
    initial_prompt="นี่คือการบรรยายภาษาไทยทั้งหมด ไม่มีภาษาอังกฤษ",
    condition_on_previous_text=True  # ← Use previous context
)
```

---

### Problem 2: Repeated Hallucinations on Silence

**Symptom:**
```
Input: [10 seconds of silence]
Output: "ขอบคุณครับ ขอบคุณครับ ขอบคุณครับ..."
```

**Solution:**
```python
# ✅ Use VAD to remove silence BEFORE Whisper
result = transcribe_with_vad(
    audio_path,
    vad_aggressiveness=2  # Detect silence better
)
```

---

### Problem 3: Poor Timing in SRT

**Symptom:** Subtitles appear too early or too late

**Solution:**
```python
# ✅ Enable word-level timestamps
result = model.transcribe(
    audio,
    word_timestamps=True,  # ← More accurate timing
    prepend_punctuations="\"'"¿([{-",
    append_punctuations="\"'.。,!?:)]}、"
)
```

---

### Problem 4: Out of GPU Memory

**Symptom:** `CUDA out of memory`

**Solution:**
```python
# ✅ Use smaller model or CPU
model = whisper.load_model("medium", device="cpu")

# OR process in smaller chunks
chunks = smart_chunk_audio(audio_path, max_duration_ms=20000)
for chunk in chunks:
    result = model.transcribe(chunk)
    torch.cuda.empty_cache()  # Clean up after each
```

---

### Problem 5: Low Accuracy Despite Using large-v3

**Checklist:**
- [ ] Using `language="th"` explicitly?
- [ ] Using domain-specific `initial_prompt`?
- [ ] Audio quality ≥16kHz?
- [ ] Removed silence with VAD?
- [ ] Using `temperature=0.0` for deterministic output?
- [ ] Using `fp16=True` on GPU?

```python
# ✅ Optimal settings for Thai
result = model.transcribe(
    audio_path,
    language="th",  # ← Must specify
    initial_prompt="นี่คือการบรรยายภาษาไทย...",  # ← Context
    temperature=0.0,  # ← Deterministic
    fp16=True,  # ← GPU optimization
    beam_size=5,  # ← Better accuracy
    best_of=5,  # ← Generate multiple candidates
    word_timestamps=True,  # ← Better timing
    condition_on_previous_text=True  # ← Use context
)
```

---

### Problem 6: Faster-Whisper in Production (Bash Script)

**Use Case:** Batch transcription in tmux/background

**Solution - Faster-Whisper Bash Script:**

```bash
#!/bin/bash
# batch_transcribe_faster.sh

set -e

INPUT_DIR="/path/to/videos"
OUTPUT_DIR="/path/to/output"
WHISPER_MODEL="large-v3"

mkdir -p "$OUTPUT_DIR"

FILES=(
    "video1.mp4"
    "video2.mp4"
    "video3.mp4"
)

for file in "${FILES[@]}"; do
    input_file="$INPUT_DIR/$file"
    basename="${file%.mp4}"

    echo ">>> Processing: $file"

    # Run Faster-Whisper via embedded Python
    python3 << PYTHON
from faster_whisper import WhisperModel
import json
from pathlib import Path

# Load model
print("Loading Faster-Whisper model...")
model = WhisperModel("${WHISPER_MODEL}", device="cuda", compute_type="int8")

# Transcribe
print("Transcribing: ${input_file}")
segments, info = model.transcribe(
    "${input_file}",
    language="th",
    beam_size=5,
    word_timestamps=True
)

# Convert to JSON format (compatible with OpenAI Whisper)
result = {
    "text": "",
    "segments": [],
    "language": "th"
}

for segment in segments:
    result["text"] += segment.text + " "
    result["segments"].append({
        "id": segment.id,
        "seek": segment.seek,
        "start": segment.start,
        "end": segment.end,
        "text": segment.text,
        "tokens": segment.tokens,
        "temperature": segment.temperature,
        "avg_logprob": segment.avg_logprob,
        "compression_ratio": segment.compression_ratio,
        "no_speech_prob": segment.no_speech_prob,
        "words": [
            {
                "word": word.word,
                "start": word.start,
                "end": word.end,
                "probability": word.probability
            }
            for word in (segment.words or [])
        ] if segment.words else []
    })

# Save JSON
output_json = Path("${OUTPUT_DIR}") / "${basename}.json"
with open(output_json, "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print(f"Saved: {output_json}")
print(f"Duration: {info.duration:.2f}s")
print(f"Language: {info.language} ({info.language_probability:.2%})")
PYTHON

    echo "✅ SUCCESS: $file"
done

echo "All Done!"
```

**Run in tmux:**

```bash
# 1. Start tmux session
tmux new -s transcribe

# 2. Run script
bash batch_transcribe_faster.sh

# 3. Detach from tmux (close browser safely)
# Press: Ctrl+B then D

# 4. Check progress later
tmux attach -s transcribe

# 5. Check output
ls -lh /path/to/output/
```

**Why this works:**
- ✅ **4-5x faster** than OpenAI Whisper
- ✅ **62% less RAM** (4 GB vs 10 GB)
- ✅ **Same accuracy** (95%+ for Thai)
- ✅ **Compatible format** (same JSON as OpenAI Whisper)
- ✅ **Runs in background** (tmux detach)
- ✅ **Word-level timestamps** included

---

## Summary: Production Workflow

### Option 1: Faster-Whisper (Recommended) ⚡

```python
# ===== FASTER-WHISPER PRODUCTION WORKFLOW =====

from faster_whisper import WhisperModel
import json
from pathlib import Path

def faster_whisper_production(
    audio_path: str,
    output_json: str,
    language: str = "th",
    model_name: str = "large-v3"
) -> dict:
    """
    Production-ready Faster-Whisper transcription.
    4-5x faster than OpenAI Whisper with same accuracy.
    """

    # Load model (INT8 for speed)
    model = WhisperModel(
        model_name,
        device="cuda",
        compute_type="int8"  # 4-5x faster, 62% less RAM
    )

    # Transcribe with optimal settings
    segments, info = model.transcribe(
        audio_path,
        language=language,
        beam_size=5,
        word_timestamps=True,
        vad_filter=True,  # Remove silence
        vad_parameters=dict(
            threshold=0.5,
            min_speech_duration_ms=250,
            min_silence_duration_ms=2000
        )
    )

    # Convert to OpenAI Whisper format
    result = {
        "text": "",
        "segments": [],
        "language": info.language
    }

    for segment in segments:
        result["text"] += segment.text + " "
        result["segments"].append({
            "id": segment.id,
            "start": segment.start,
            "end": segment.end,
            "text": segment.text,
            "words": [
                {
                    "word": word.word,
                    "start": word.start,
                    "end": word.end,
                    "probability": word.probability
                }
                for word in (segment.words or [])
            ] if segment.words else []
        })

    # Save JSON
    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    return result

# Usage
result = faster_whisper_production(
    "video.mp4",
    "output.json",
    language="th"
)
```

### Option 2: OpenAI Whisper (Standard)

```python
# ===== OPENAI WHISPER PRODUCTION WORKFLOW =====

def production_transcription_pipeline(
    audio_path: str,
    output_srt: str,
    language: str = "th",
    domain_context: str = None
) -> dict:
    """
    Production-ready transcription pipeline

    Steps:
    1. Validate audio file
    2. Remove silence (VAD)
    3. Transcribe with Whisper
    4. Clean hallucinations
    5. Generate SRT
    6. Quality check

    Args:
        audio_path: Input audio file
        output_srt: Output SRT file
        language: Language code (default: th)
        domain_context: Context for initial_prompt

    Returns:
        Complete results with quality metrics
    """
    # Step 1: Validate
    print("=" * 60)
    print("STEP 1: Validating audio file...")
    print("=" * 60)
    validation = validate_audio_file(audio_path)
    if not validation['valid']:
        return {'error': 'Validation failed', 'validation': validation}

    # Step 2: Prepare initial prompt
    if domain_context:
        initial_prompt = f"นี่คือการบรรยายเกี่ยวกับ {domain_context} ผู้บรรยายพูดภาษาไทยชัดเจน"
    else:
        initial_prompt = "นี่คือการบรรยายภาษาไทย ผู้บรรยายพูดชัดเจน"

    # Step 3: Transcribe with all optimizations
    print("\n" + "=" * 60)
    print("STEP 2: Transcribing with Whisper...")
    print("=" * 60)
    result = audio_to_srt_complete(
        audio_path=audio_path,
        output_srt_path=output_srt,
        model_name="large-v3",
        language=language,
        initial_prompt=initial_prompt,
        use_vad=True,
        vad_aggressiveness=2
    )

    # Step 4: Quality check
    print("\n" + "=" * 60)
    print("STEP 3: Quality check...")
    print("=" * 60)
    quality = quality_check_transcription(result['result'])

    # Final report
    print("\n" + "=" * 60)
    print("✅ TRANSCRIPTION COMPLETE")
    print("=" * 60)
    print(f"Input: {audio_path}")
    print(f"Output: {output_srt}")
    print(f"Segments: {result['stats']['segments_count']}")
    print(f"Duration: {result['stats']['total_duration_s']:.2f}s")
    print(f"Processing time: {result['stats']['processing_time_s']:.2f}s")
    print(f"Quality score: {quality['quality_score']}/100")

    return {
        'result': result['result'],
        'stats': result['stats'],
        'quality': quality,
        'validation': validation
    }

# ===== USAGE =====

# Simple usage
result = production_transcription_pipeline(
    audio_path="thai_forex_lesson.mp3",
    output_srt="thai_forex_lesson.srt",
    language="th",
    domain_context="Forex การเทรด และการลงทุน"
)

# Check results
if 'error' not in result:
    print(f"\n✅ Success! SRT saved to: {result['stats']['output_srt']}")
    print(f"Preview: {result['result']['text'][:200]}...")
else:
    print(f"\n❌ Error: {result['error']}")
```

---

## Quick Reference

### Essential Parameters

```python
# Minimal (fastest)
result = model.transcribe(audio_path)

# Recommended for Thai
result = model.transcribe(
    audio_path,
    language="th",
    initial_prompt="นี่คือการบรรยายภาษาไทย"
)

# Production (best quality)
result = model.transcribe(
    audio_path,
    language="th",
    initial_prompt="นี่คือการบรรยายเกี่ยวกับ [domain]",
    temperature=0.0,
    fp16=True,
    beam_size=5,
    best_of=5,
    word_timestamps=True,
    condition_on_previous_text=True,
    no_speech_threshold=0.6,
    logprob_threshold=-1.0
)
```

### Model Comparison Quick Guide

| Need | Model | Why |
|------|-------|-----|
| Testing | base | Fast, good enough for testing |
| English draft | small | Fast, 92%+ accuracy |
| Thai draft | medium | Minimum for acceptable Thai |
| **Thai production** | **large-v3** | **95%+ accuracy** |
| Multilingual | large-v3 | Best language detection |

---

**Last Updated:** 2025-10-24
**Version:** 1.0
**Lines:** 1,600+
**Status:** Production Ready ✅
