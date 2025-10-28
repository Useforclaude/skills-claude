---
name: automation-workflows-skill
description: Master automation workflows for repetitive tasks using Make, n8n, Zapier, Python, and Bash. Use for content automation, video production pipelines, data processing, marketing workflows, AI content generation, batch operations, webhook integrations, API orchestration, and production-ready automation systems. Also use for Thai keywords "ทำให้อัตโนมัติ", "ระบบอัตโนมัติ", "อัตโนมัติ", "ประมวลผลหลายไฟล์", "batch process", "workflow", "ลำดับงาน", "ลดขั้นตอน", "ทำงานซ้ำ", "ไม่ต้องทำเอง", "Make.com", "n8n", "Zapier", "Python script", "Bash script", "ประหยัดเวลา", "ทำงานรวด", "ระบบทำงานเอง".
---

# 🤖 Automation Workflows Skill - Production-Grade Task Automation

**Version:** 1.0
**Last Updated:** 2025-10-26
**Expertise Level:** Automation Engineer / DevOps
**Platforms:** Make.com, n8n, Zapier, Python, Bash, GitHub Actions

---

## 📋 Table of Contents

1. [Platform Comparison](#platform-comparison)
2. [Workflow Design Patterns](#workflow-design-patterns)
3. [Content Automation](#content-automation)
4. [Video Production Automation](#video-production-automation)
5. [Data Processing Automation](#data-processing-automation)
6. [Marketing Automation](#marketing-automation)
7. [Development Automation](#development-automation)
8. [API Integration Strategies](#api-integration-strategies)
9. [Error Handling & Monitoring](#error-handling--monitoring)
10. [Security Best Practices](#security-best-practices)
11. [Cost Optimization](#cost-optimization)
12. [Production Deployment](#production-deployment)

---

## 🎯 Platform Comparison

### Quick Reference Table

| Platform | Type | Price | Best For | Pros | Cons |
|----------|------|-------|----------|------|------|
| **Make.com** | Visual | $9-299/mo | Complex workflows | Visual editor, powerful router | Learning curve |
| **n8n** | Open-source | Free/Self-hosted | Privacy, customization | Self-hosted, unlimited | Requires server setup |
| **Zapier** | Cloud | $20-599/mo | Simple integrations | Easy to use, 5000+ apps | Expensive at scale |
| **Python** | Code | Free | Custom logic | Full control, unlimited | Requires coding |
| **Bash** | Code | Free | System operations | Fast, native | Limited complexity |
| **GitHub Actions** | CI/CD | Free tier | Dev workflows | Git integration | GitHub-centric |

---

### When to Use Which Platform

**Use Make.com when:**
- You need visual workflow builder
- Complex branching/routing logic
- Non-technical team members need access
- Budget allows $9-50/month

**Use n8n when:**
- Privacy/data sovereignty required
- High-volume operations (cost-effective)
- Need custom integrations
- Have server infrastructure

**Use Zapier when:**
- Simple trigger-action workflows
- Need specific app integrations (Zapier has most)
- Budget allows higher cost
- No-code requirement

**Use Python when:**
- Complex data processing
- AI/ML integration required
- Custom business logic
- Need full control

**Use Bash when:**
- File system operations
- Command-line tool orchestration
- Server maintenance
- Simple sequential tasks

---

## 🎨 Workflow Design Patterns

### 1. Trigger-Action Pattern (Simple)

**Structure:**
```
Trigger → Action → Done
```

**Example: New Email → Save to Database**
```yaml
# n8n workflow
Trigger: Gmail - New Email
Action: Database - Insert Row
```

**Use cases:**
- Save form submissions to database
- Send notification on new file upload
- Log webhook events

---

### 2. Trigger-Filter-Action Pattern (Conditional)

**Structure:**
```
Trigger → Filter → Action A (if true)
                 → Action B (if false)
```

**Example: New Lead → Qualify → Route to Sales/Marketing**
```python
# Python pseudo-code
def process_lead(lead):
    if lead['score'] >= 80:
        send_to_sales(lead)
    else:
        add_to_nurture_campaign(lead)
```

**Use cases:**
- Lead scoring and routing
- Content approval workflows
- Error handling (retry vs alert)

---

### 3. Multi-Step Processing Pipeline

**Structure:**
```
Trigger → Step 1 → Step 2 → Step 3 → ... → Done
```

**Example: Video Production Pipeline**
```bash
# Bash pipeline
#!/bin/bash

# Step 1: Download video
youtube-dl "$VIDEO_URL" -o input.mp4

# Step 2: Transcribe with Whisper
whisper input.mp4 --model large-v3 --language th --output_format srt

# Step 3: Translate subtitles
python translate_srt.py input.srt output_en.srt

# Step 4: Synthesize TTS
python tts_from_srt.py output_en.srt audio_en.mp3

# Step 5: Replace audio
ffmpeg -i input.mp4 -i audio_en.mp3 -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 output.mp4

# Step 6: Upload to storage
aws s3 cp output.mp4 s3://my-bucket/videos/
```

**Use cases:**
- Video production automation
- Data ETL pipelines
- Multi-step content generation

---

### 4. Fan-Out Pattern (Parallel Processing)

**Structure:**
```
Trigger → Split → [Task 1, Task 2, Task 3] (parallel) → Merge → Done
```

**Example: Generate Social Media Content for All Platforms**
```javascript
// Make.com scenario
Input: Blog post URL

Fan-out:
  - Generate Twitter thread (parallel)
  - Generate LinkedIn post (parallel)
  - Generate Instagram caption (parallel)
  - Generate Facebook post (parallel)

Merge: Collect all outputs
Action: Schedule to respective platforms
```

**Use cases:**
- Multi-platform content distribution
- Parallel API calls
- Batch image processing

---

### 5. Event-Driven Architecture

**Structure:**
```
Event Source → Event Bus → Multiple Subscribers
```

**Example: E-commerce Order Events**
```
New Order Event →
  ├─ Inventory System (deduct stock)
  ├─ Email Service (send confirmation)
  ├─ Analytics (track conversion)
  ├─ Shipping (create label)
  └─ Accounting (record revenue)
```

**Implementation (n8n + Webhook):**
```json
{
  "nodes": [
    {
      "name": "Webhook",
      "type": "n8n-nodes-base.webhook",
      "parameters": {
        "path": "new-order"
      }
    },
    {
      "name": "Update Inventory",
      "type": "n8n-nodes-base.httpRequest"
    },
    {
      "name": "Send Email",
      "type": "n8n-nodes-base.emailSend"
    },
    {
      "name": "Track Analytics",
      "type": "n8n-nodes-base.httpRequest"
    }
  ]
}
```

**Use cases:**
- Microservices communication
- Real-time notifications
- Multi-system synchronization

---

## 📝 Content Automation

### 1. Automated Blog Post Generation (AI-Powered)

**Workflow:**
```
Google Sheets (topics) → OpenAI (generate) → WordPress (publish) → Social Media (share)
```

**n8n Implementation:**
```json
{
  "nodes": [
    {
      "name": "Schedule Trigger",
      "type": "n8n-nodes-base.cron",
      "parameters": {
        "triggerTimes": {
          "item": [
            {
              "hour": 9,
              "minute": 0
            }
          ]
        }
      }
    },
    {
      "name": "Get Topic from Sheet",
      "type": "n8n-nodes-base.googleSheets",
      "parameters": {
        "operation": "read",
        "range": "A2:B2"
      }
    },
    {
      "name": "Generate Content (OpenAI)",
      "type": "n8n-nodes-base.openAi",
      "parameters": {
        "resource": "text",
        "operation": "complete",
        "prompt": "Write a 1000-word blog post about: {{$json[\"topic\"]}}",
        "model": "gpt-4"
      }
    },
    {
      "name": "Publish to WordPress",
      "type": "n8n-nodes-base.wordpress",
      "parameters": {
        "operation": "create",
        "title": "{{$json[\"title\"]}}",
        "content": "{{$json[\"content\"]}}"
      }
    },
    {
      "name": "Share on Twitter",
      "type": "n8n-nodes-base.twitter",
      "parameters": {
        "text": "New post: {{$json[\"title\"]}} {{$json[\"url\"]}}"
      }
    }
  ]
}
```

**Python Alternative (More Control):**
```python
import openai
import requests
from datetime import datetime

# Configuration
OPENAI_API_KEY = "your-key"
WORDPRESS_URL = "https://yourblog.com"
WORDPRESS_AUTH = ("username", "password")

def generate_blog_post(topic):
    """Generate blog post using OpenAI."""
    openai.api_key = OPENAI_API_KEY

    prompt = f"""Write a comprehensive 1000-word blog post about: {topic}

    Include:
    - Engaging introduction
    - 3-5 main sections with headers
    - Practical examples
    - Conclusion with call-to-action

    Format in HTML."""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert content writer."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=2000
    )

    return response.choices[0].message.content

def publish_to_wordpress(title, content):
    """Publish post to WordPress via REST API."""
    url = f"{WORDPRESS_URL}/wp-json/wp/v2/posts"

    data = {
        "title": title,
        "content": content,
        "status": "publish"
    }

    response = requests.post(url, auth=WORDPRESS_AUTH, json=data)
    return response.json()

# Main workflow
if __name__ == "__main__":
    topics = [
        "10 Marketing Automation Strategies for 2025",
        "How to Build a Content Pipeline with AI",
        "Video Production Automation: Complete Guide"
    ]

    for topic in topics:
        print(f"Generating: {topic}")
        content = generate_blog_post(topic)

        result = publish_to_wordpress(topic, content)
        print(f"Published: {result['link']}")
```

---

### 2. Social Media Content Calendar Automation

**Workflow:**
```
Notion (content calendar) → Buffer/Hootsuite (schedule) → Analytics (track)
```

**Make.com Scenario:**
```
1. Trigger: Every Monday 9 AM
2. Get upcoming posts from Notion database
3. For each post:
   - Generate platform-specific variants (Twitter, LinkedIn, Instagram)
   - Generate images (Canva API or DALL-E)
   - Schedule to Buffer/Hootsuite
4. Send summary email to team
```

**Python Implementation:**
```python
import requests
from datetime import datetime, timedelta
from notion_client import Client

# Configuration
NOTION_TOKEN = "your-notion-token"
NOTION_DATABASE_ID = "your-database-id"
BUFFER_TOKEN = "your-buffer-token"

# Initialize Notion
notion = Client(auth=NOTION_TOKEN)

def get_upcoming_posts():
    """Get posts scheduled for next 7 days."""
    today = datetime.now()
    next_week = today + timedelta(days=7)

    results = notion.databases.query(
        database_id=NOTION_DATABASE_ID,
        filter={
            "and": [
                {
                    "property": "Publish Date",
                    "date": {
                        "on_or_after": today.isoformat()
                    }
                },
                {
                    "property": "Publish Date",
                    "date": {
                        "before": next_week.isoformat()
                    }
                },
                {
                    "property": "Status",
                    "select": {
                        "equals": "Ready"
                    }
                }
            ]
        }
    )

    return results['results']

def adapt_for_platform(content, platform):
    """Adapt content for specific platform."""
    if platform == "twitter":
        # Limit to 280 chars, add hashtags
        return content[:250] + " #marketing #automation"

    elif platform == "linkedin":
        # More professional, longer form
        return f"{content}\n\nWhat are your thoughts? Share in comments."

    elif platform == "instagram":
        # Visual focus, hashtags
        return f"{content}\n\n📸✨\n\n#contentmarketing #automation #digitalmarketing"

    return content

def schedule_to_buffer(content, platform, scheduled_time):
    """Schedule post to Buffer."""
    url = "https://api.bufferapp.com/1/updates/create.json"

    data = {
        "access_token": BUFFER_TOKEN,
        "text": content,
        "profile_ids[]": get_profile_id(platform),
        "scheduled_at": int(scheduled_time.timestamp())
    }

    response = requests.post(url, data=data)
    return response.json()

# Main automation
posts = get_upcoming_posts()

for post in posts:
    title = post['properties']['Title']['title'][0]['plain_text']
    content = post['properties']['Content']['rich_text'][0]['plain_text']
    publish_date = post['properties']['Publish Date']['date']['start']

    # Schedule to all platforms
    platforms = ['twitter', 'linkedin', 'instagram']

    for platform in platforms:
        adapted_content = adapt_for_platform(content, platform)
        result = schedule_to_buffer(adapted_content, platform, publish_date)
        print(f"Scheduled {title} to {platform}: {result}")
```

---

### 3. Automated Newsletter Generation

**Workflow:**
```
RSS Feeds → Curate Top Articles → Generate Summary (AI) → Mailchimp → Send
```

**Python Script:**
```python
import feedparser
import openai
from mailchimp_marketing import Client as MailchimpClient

# Configuration
OPENAI_API_KEY = "your-key"
MAILCHIMP_API_KEY = "your-key"
MAILCHIMP_SERVER = "us1"
MAILCHIMP_LIST_ID = "your-list-id"

# Initialize clients
openai.api_key = OPENAI_API_KEY
mailchimp = MailchimpClient()
mailchimp.set_config({
    "api_key": MAILCHIMP_API_KEY,
    "server": MAILCHIMP_SERVER
})

def fetch_articles_from_feeds(feeds, limit=10):
    """Fetch latest articles from RSS feeds."""
    articles = []

    for feed_url in feeds:
        feed = feedparser.parse(feed_url)

        for entry in feed.entries[:limit]:
            articles.append({
                "title": entry.title,
                "link": entry.link,
                "summary": entry.summary if hasattr(entry, 'summary') else '',
                "published": entry.published
            })

    # Sort by publish date, get top 5
    articles.sort(key=lambda x: x['published'], reverse=True)
    return articles[:5]

def generate_newsletter_content(articles):
    """Generate newsletter content using AI."""
    articles_text = "\n\n".join([
        f"Title: {a['title']}\nLink: {a['link']}\nSummary: {a['summary']}"
        for a in articles
    ])

    prompt = f"""Create an engaging newsletter from these articles:

{articles_text}

Format:
- Catchy introduction paragraph
- For each article: Title (linked), 2-sentence summary, why it matters
- Closing paragraph with CTA

Use friendly, enthusiastic tone. Output in HTML."""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a newsletter editor."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content

def send_newsletter(subject, html_content):
    """Send newsletter via Mailchimp."""
    campaign = mailchimp.campaigns.create({
        "type": "regular",
        "recipients": {"list_id": MAILCHIMP_LIST_ID},
        "settings": {
            "subject_line": subject,
            "from_name": "Your Newsletter",
            "reply_to": "newsletter@yourdomain.com"
        }
    })

    mailchimp.campaigns.set_content(campaign['id'], {
        "html": html_content
    })

    mailchimp.campaigns.send(campaign['id'])
    return campaign

# Main automation
if __name__ == "__main__":
    # Define RSS feeds to monitor
    feeds = [
        "https://techcrunch.com/feed/",
        "https://www.theverge.com/rss/index.xml",
        "https://feeds.arstechnica.com/arstechnica/index"
    ]

    # Fetch and curate
    articles = fetch_articles_from_feeds(feeds)

    # Generate newsletter
    content = generate_newsletter_content(articles)

    # Send
    from datetime import datetime
    subject = f"Your Weekly Tech Digest - {datetime.now().strftime('%B %d, %Y')}"
    campaign = send_newsletter(subject, content)

    print(f"Newsletter sent! Campaign ID: {campaign['id']}")
```

---

## 🎬 Video Production Automation

### 1. Complete Video Dubbing Pipeline

**Workflow:**
```
Input Video → Transcribe (Whisper) → Translate → TTS (Edge-TTS) → Audio Sync → Replace Audio → Output
```

**Full Production Script:**
```bash
#!/bin/bash
# video_dubbing_pipeline.sh
# Complete automation for video dubbing

set -e  # Exit on error

# ============================================
# Configuration
# ============================================
INPUT_VIDEO="$1"
SOURCE_LANG="${2:-th}"  # Default: Thai
TARGET_LANG="${3:-en}"  # Default: English
OUTPUT_DIR="output"
TEMP_DIR="temp"

# Voices
TTS_VOICE_MALE="en-US-GuyNeural"
TTS_VOICE_FEMALE="en-US-JennyNeural"

# ============================================
# Setup
# ============================================
mkdir -p "$OUTPUT_DIR" "$TEMP_DIR"

echo "🎬 Starting Video Dubbing Pipeline"
echo "=================================="
echo "Input: $INPUT_VIDEO"
echo "Source Language: $SOURCE_LANG"
echo "Target Language: $TARGET_LANG"
echo ""

# ============================================
# Step 1: Extract Audio
# ============================================
echo "📥 Step 1/6: Extracting audio..."
ffmpeg -i "$INPUT_VIDEO" \
  -vn -acodec pcm_s16le \
  -ar 44100 -ac 2 \
  "$TEMP_DIR/original_audio.wav" \
  -y -loglevel error

echo "✅ Audio extracted"

# ============================================
# Step 2: Transcribe with Whisper
# ============================================
echo "🎤 Step 2/6: Transcribing with Whisper..."
whisper "$TEMP_DIR/original_audio.wav" \
  --model large-v3 \
  --language "$SOURCE_LANG" \
  --output_format srt \
  --output_dir "$TEMP_DIR" \
  --word_timestamps True

mv "$TEMP_DIR/original_audio.srt" "$TEMP_DIR/source.srt"
echo "✅ Transcription complete"

# ============================================
# Step 3: Translate Subtitles
# ============================================
echo "🌐 Step 3/6: Translating subtitles..."
python3 <<EOF
import re
from deep_translator import GoogleTranslator

def parse_srt(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = r'(\d+)\n(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})\n(.*?)(?=\n\n|\Z)'
    matches = re.findall(pattern, content, re.DOTALL)

    subtitles = []
    for match in matches:
        subtitles.append({
            'index': int(match[0]),
            'start': match[1],
            'end': match[2],
            'text': match[3].strip()
        })

    return subtitles

def translate_srt(source_path, target_path, source_lang, target_lang):
    translator = GoogleTranslator(source=source_lang, target=target_lang)
    subtitles = parse_srt(source_path)

    with open(target_path, 'w', encoding='utf-8') as f:
        for sub in subtitles:
            translated_text = translator.translate(sub['text'])

            f.write(f"{sub['index']}\n")
            f.write(f"{sub['start']} --> {sub['end']}\n")
            f.write(f"{translated_text}\n\n")

translate_srt('$TEMP_DIR/source.srt', '$TEMP_DIR/target.srt', '$SOURCE_LANG', '$TARGET_LANG')
print("✅ Translation complete")
EOF

# ============================================
# Step 4: Synthesize TTS Audio
# ============================================
echo "🔊 Step 4/6: Generating TTS audio..."
python3 <<EOF
import asyncio
import edge_tts
from datetime import datetime, timedelta
import re

def parse_timestamp(ts):
    """Convert SRT timestamp to seconds."""
    h, m, s_ms = ts.split(':')
    s, ms = s_ms.split(',')
    total_seconds = int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000
    return total_seconds

def parse_srt(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = r'(\d+)\n(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})\n(.*?)(?=\n\n|\Z)'
    matches = re.findall(pattern, content, re.DOTALL)

    subtitles = []
    for match in matches:
        subtitles.append({
            'index': int(match[0]),
            'start_time': parse_timestamp(match[1]),
            'end_time': parse_timestamp(match[2]),
            'text': match[3].strip()
        })

    return subtitles

async def synthesize_segment(text, output_path, voice):
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_path)

async def synthesize_all_segments(srt_path, voice):
    subtitles = parse_srt(srt_path)

    tasks = []
    for sub in subtitles:
        output_path = f"$TEMP_DIR/segment_{sub['index']:04d}.mp3"
        tasks.append(synthesize_segment(sub['text'], output_path, voice))

    await asyncio.gather(*tasks)

# Run synthesis
asyncio.run(synthesize_all_segments('$TEMP_DIR/target.srt', '$TTS_VOICE_MALE'))
print("✅ TTS synthesis complete")
EOF

# ============================================
# Step 5: Merge Audio Segments with Timeline Sync
# ============================================
echo "🔗 Step 5/6: Merging audio with timeline sync..."
python3 <<EOF
import subprocess
import re
from pathlib import Path

def parse_timestamp(ts):
    h, m, s_ms = ts.split(':')
    s, ms = s_ms.split(',')
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000

def parse_srt(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = r'(\d+)\n(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})\n(.*?)(?=\n\n|\Z)'
    matches = re.findall(pattern, content, re.DOTALL)

    return [(int(m[0]), parse_timestamp(m[1]), parse_timestamp(m[2])) for m in matches]

def get_audio_duration(filepath):
    cmd = ['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
           '-of', 'default=noprint_wrappers=1:nokey=1', str(filepath)]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return float(result.stdout.strip())

# Parse SRT for timeline
segments = parse_srt('$TEMP_DIR/target.srt')

# Build concat file with silence
concat_file = '$TEMP_DIR/concat.txt'
with open(concat_file, 'w') as f:
    current_time = 0

    for idx, start_time, end_time in segments:
        segment_path = f'$TEMP_DIR/segment_{idx:04d}.mp3'

        # Add silence if there's a gap
        if start_time > current_time:
            silence_duration = start_time - current_time
            f.write(f"file 'silence_{idx}.mp3'\n")

            # Generate silence
            subprocess.run([
                'ffmpeg', '-f', 'lavfi', '-i', f'anullsrc=r=44100:cl=stereo',
                '-t', str(silence_duration), '-y',
                f'$TEMP_DIR/silence_{idx}.mp3'
            ], capture_output=True)

        # Add segment
        f.write(f"file 'segment_{idx:04d}.mp3'\n")

        # Update current time
        audio_duration = get_audio_duration(segment_path)
        current_time = start_time + audio_duration

# Concatenate all segments
subprocess.run([
    'ffmpeg', '-f', 'concat', '-safe', '0',
    '-i', concat_file,
    '-c', 'copy', '-y',
    '$TEMP_DIR/merged_audio.mp3'
], capture_output=True)

print("✅ Audio merged with timeline sync")
EOF

# ============================================
# Step 6: Replace Video Audio
# ============================================
echo "🎥 Step 6/6: Replacing video audio..."
OUTPUT_FILE="$OUTPUT_DIR/$(basename "$INPUT_VIDEO" .mp4)_dubbed_$TARGET_LANG.mp4"

ffmpeg -i "$INPUT_VIDEO" \
  -i "$TEMP_DIR/merged_audio.mp3" \
  -c:v copy \
  -c:a aac \
  -b:a 192k \
  -map 0:v:0 \
  -map 1:a:0 \
  -shortest \
  -y \
  "$OUTPUT_FILE" \
  -loglevel error

echo "✅ Video audio replaced"

# ============================================
# Cleanup
# ============================================
echo ""
echo "🧹 Cleaning up temporary files..."
rm -rf "$TEMP_DIR"

# ============================================
# Summary
# ============================================
echo ""
echo "🎉 Pipeline Complete!"
echo "=================================="
echo "Output: $OUTPUT_FILE"

# Get file size
FILE_SIZE=$(du -h "$OUTPUT_FILE" | cut -f1)
echo "Size: $FILE_SIZE"

# Get duration
DURATION=$(ffprobe -v error -show_entries format=duration \
  -of default=noprint_wrappers=1:nokey=1 "$OUTPUT_FILE" | cut -d. -f1)
echo "Duration: ${DURATION}s"
echo ""
echo "✅ All done!"
```

**Usage:**
```bash
chmod +x video_dubbing_pipeline.sh
./video_dubbing_pipeline.sh input.mp4 th en
```

---

### 2. Batch Video Processing (100+ Videos)

**Scenario:** Process entire YouTube channel for dubbing

**Workflow:**
```
Get video list → Download (parallel) → Process each → Upload to storage → Update database
```

**Python Orchestrator:**
```python
import subprocess
import asyncio
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import yt_dlp
import boto3

# Configuration
MAX_PARALLEL = 4
S3_BUCKET = "dubbed-videos"
OUTPUT_BUCKET = "output"

def download_video(url, output_dir):
    """Download video using yt-dlp."""
    ydl_opts = {
        'format': 'best',
        'outtmpl': f'{output_dir}/%(id)s.%(ext)s',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filepath = ydl.prepare_filename(info)

    return filepath

def process_video(video_path, source_lang, target_lang):
    """Process single video through dubbing pipeline."""
    cmd = [
        './video_dubbing_pipeline.sh',
        video_path,
        source_lang,
        target_lang
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        raise Exception(f"Processing failed: {result.stderr}")

    # Get output path (last line of stdout)
    output_path = result.stdout.strip().split('\n')[-1].split(': ')[-1]
    return output_path

def upload_to_s3(filepath, bucket, key):
    """Upload file to S3."""
    s3 = boto3.client('s3')
    s3.upload_file(filepath, bucket, key)
    return f"s3://{bucket}/{key}"

async def process_video_async(url, source_lang, target_lang):
    """Process single video (async wrapper)."""
    try:
        # Download
        print(f"⬇️  Downloading: {url}")
        video_path = download_video(url, "downloads")

        # Process
        print(f"⚙️  Processing: {video_path}")
        output_path = process_video(video_path, source_lang, target_lang)

        # Upload
        print(f"⬆️  Uploading: {output_path}")
        key = Path(output_path).name
        s3_url = upload_to_s3(output_path, S3_BUCKET, key)

        print(f"✅ Complete: {s3_url}")
        return {"url": url, "output": s3_url, "status": "success"}

    except Exception as e:
        print(f"❌ Failed: {url} - {str(e)}")
        return {"url": url, "error": str(e), "status": "failed"}

async def process_batch(urls, source_lang, target_lang, max_parallel=4):
    """Process multiple videos with concurrency limit."""
    semaphore = asyncio.Semaphore(max_parallel)

    async def bounded_process(url):
        async with semaphore:
            return await process_video_async(url, source_lang, target_lang)

    tasks = [bounded_process(url) for url in urls]
    results = await asyncio.gather(*tasks)

    return results

# Main execution
if __name__ == "__main__":
    # Example: Process 100 videos
    video_urls = [
        "https://youtube.com/watch?v=xxx",
        "https://youtube.com/watch?v=yyy",
        # ... 98 more URLs
    ]

    results = asyncio.run(process_batch(
        video_urls,
        source_lang="th",
        target_lang="en",
        max_parallel=MAX_PARALLEL
    ))

    # Summary
    success_count = sum(1 for r in results if r['status'] == 'success')
    failed_count = len(results) - success_count

    print(f"\n📊 Batch Processing Summary")
    print(f"===========================")
    print(f"Total: {len(results)}")
    print(f"Success: {success_count}")
    print(f"Failed: {failed_count}")

    # Save results
    import json
    with open('batch_results.json', 'w') as f:
        json.dump(results, f, indent=2)
```

---

### 3. Automated Video Editing (Template-Based)

**Use Case:** Generate 100 product demo videos from templates

**Tools:** FFmpeg + Python + Template System

**Template Structure:**
```
[Intro 5s] → [Product Shot 10s] → [Features 15s] → [CTA 5s] → [Outro 5s]
```

**Python Script:**
```python
import subprocess
from pathlib import Path
import json

class VideoTemplate:
    def __init__(self, template_config):
        self.config = template_config

    def render(self, data, output_path):
        """Render video from template and data."""
        segments = []

        # Intro
        intro_clip = self.create_intro(data['product_name'])
        segments.append(intro_clip)

        # Product shot
        product_clip = self.overlay_text(
            video_path=data['product_video'],
            text=data['product_name'],
            duration=10
        )
        segments.append(product_clip)

        # Features (dynamic)
        for idx, feature in enumerate(data['features']):
            feature_clip = self.create_feature_slide(
                feature['title'],
                feature['description'],
                feature['icon']
            )
            segments.append(feature_clip)

        # CTA
        cta_clip = self.create_cta(data['cta_text'], data['cta_url'])
        segments.append(cta_clip)

        # Outro
        outro_clip = self.config['outro_template']
        segments.append(outro_clip)

        # Concatenate all
        self.concatenate_segments(segments, output_path)

        return output_path

    def create_intro(self, product_name):
        """Generate intro with animated text."""
        output = f"temp/intro_{product_name}.mp4"

        cmd = f"""
        ffmpeg -f lavfi -i color=c=black:s=1920x1080:d=5 \
          -vf "drawtext=text='{product_name}':fontsize=72:fontcolor=white:x=(w-text_w)/2:y=(h-text_h)/2:enable='between(t,1,4)'" \
          -y {output}
        """

        subprocess.run(cmd, shell=True, capture_output=True)
        return output

    def overlay_text(self, video_path, text, duration):
        """Overlay text on video."""
        output = f"temp/overlay_{Path(video_path).stem}.mp4"

        cmd = f"""
        ffmpeg -i {video_path} -t {duration} \
          -vf "drawtext=text='{text}':fontsize=48:fontcolor=white:x=50:y=50:box=1:boxcolor=black@0.5:boxborderw=10" \
          -y {output}
        """

        subprocess.run(cmd, shell=True, capture_output=True)
        return output

    def create_feature_slide(self, title, description, icon_path):
        """Create feature slide with icon and text."""
        output = f"temp/feature_{title.replace(' ', '_')}.mp4"

        # Use FFmpeg complex filter to composite icon + text
        cmd = f"""
        ffmpeg -f lavfi -i color=c=#1a1a2e:s=1920x1080:d=5 \
          -i {icon_path} \
          -filter_complex "[1]scale=200:-1[icon];[0][icon]overlay=100:300[bg];[bg]drawtext=text='{title}':fontsize=64:fontcolor=white:x=350:y=300[titled];[titled]drawtext=text='{description}':fontsize=32:fontcolor=gray:x=350:y=400" \
          -y {output}
        """

        subprocess.run(cmd, shell=True, capture_output=True)
        return output

    def create_cta(self, cta_text, cta_url):
        """Create call-to-action slide."""
        output = f"temp/cta.mp4"

        cmd = f"""
        ffmpeg -f lavfi -i color=c=#ff6b6b:s=1920x1080:d=5 \
          -vf "drawtext=text='{cta_text}':fontsize=72:fontcolor=white:x=(w-text_w)/2:y=400,drawtext=text='{cta_url}':fontsize=48:fontcolor=white:x=(w-text_w)/2:y=600" \
          -y {output}
        """

        subprocess.run(cmd, shell=True, capture_output=True)
        return output

    def concatenate_segments(self, segments, output_path):
        """Concatenate all segments into final video."""
        concat_file = "temp/concat.txt"

        with open(concat_file, 'w') as f:
            for segment in segments:
                f.write(f"file '{Path(segment).absolute()}'\n")

        cmd = f"""
        ffmpeg -f concat -safe 0 -i {concat_file} \
          -c:v libx264 -preset medium -crf 23 \
          -y {output_path}
        """

        subprocess.run(cmd, shell=True, capture_output=True)

# Usage
template = VideoTemplate({
    'outro_template': 'assets/outro.mp4'
})

# Generate 100 product videos
products = [
    {
        'product_name': 'Product A',
        'product_video': 'footage/product_a.mp4',
        'features': [
            {'title': 'Fast', 'description': '10x faster processing', 'icon': 'icons/speed.png'},
            {'title': 'Secure', 'description': 'End-to-end encryption', 'icon': 'icons/lock.png'},
        ],
        'cta_text': 'Get Started Today!',
        'cta_url': 'www.product-a.com'
    },
    # ... 99 more products
]

for idx, product in enumerate(products):
    output_path = f"output/product_{idx+1:03d}.mp4"
    template.render(product, output_path)
    print(f"✅ Generated: {output_path}")
```

---

## 📊 Data Processing Automation

### 1. Web Scraping Pipeline

**Workflow:**
```
Cron → Scrape Websites → Clean Data → Save to Database → Send Alert
```

**Python Script (with Selenium for dynamic content):**
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import psycopg2
import smtplib
from email.mime.text import MIMEText

# Configuration
DATABASE_URL = "postgresql://user:pass@localhost/db"
SMTP_CONFIG = {
    'host': 'smtp.gmail.com',
    'port': 587,
    'username': 'your@email.com',
    'password': 'your-password'
}

def scrape_website(url):
    """Scrape dynamic website using Selenium."""
    # Setup headless Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get(url)
        driver.implicitly_wait(10)  # Wait for JS to load

        # Extract data
        products = []
        elements = driver.find_elements(By.CLASS_NAME, "product-card")

        for element in elements:
            try:
                title = element.find_element(By.CLASS_NAME, "title").text
                price = element.find_element(By.CLASS_NAME, "price").text
                rating = element.find_element(By.CLASS_NAME, "rating").text
                link = element.find_element(By.TAG_NAME, "a").get_attribute("href")

                products.append({
                    'title': title,
                    'price': float(price.replace('$', '').replace(',', '')),
                    'rating': float(rating),
                    'link': link,
                    'scraped_at': datetime.now()
                })
            except Exception as e:
                print(f"Error extracting product: {e}")
                continue

        return products

    finally:
        driver.quit()

def clean_data(products):
    """Clean and validate scraped data."""
    df = pd.DataFrame(products)

    # Remove duplicates
    df.drop_duplicates(subset=['link'], inplace=True)

    # Remove invalid prices
    df = df[df['price'] > 0]

    # Normalize ratings to 0-5 scale
    df['rating'] = df['rating'].clip(0, 5)

    return df

def save_to_database(df):
    """Save data to PostgreSQL."""
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()

    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO products (title, price, rating, link, scraped_at)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (link) DO UPDATE SET
                price = EXCLUDED.price,
                rating = EXCLUDED.rating,
                scraped_at = EXCLUDED.scraped_at
        """, (row['title'], row['price'], row['rating'], row['link'], row['scraped_at']))

    conn.commit()
    cursor.close()
    conn.close()

def send_alert(subject, message):
    """Send email alert."""
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = SMTP_CONFIG['username']
    msg['To'] = 'recipient@email.com'

    server = smtplib.SMTP(SMTP_CONFIG['host'], SMTP_CONFIG['port'])
    server.starttls()
    server.login(SMTP_CONFIG['username'], SMTP_CONFIG['password'])
    server.send_message(msg)
    server.quit()

# Main automation
if __name__ == "__main__":
    urls = [
        "https://example.com/products",
        "https://competitor.com/items",
    ]

    all_products = []

    for url in urls:
        print(f"Scraping: {url}")
        products = scrape_website(url)
        all_products.extend(products)

    # Clean data
    df = clean_data(all_products)

    # Save to database
    save_to_database(df)

    # Send summary email
    summary = f"""
    Scraping Complete
    =================
    Total products: {len(df)}
    Average price: ${df['price'].mean():.2f}
    Highest rated: {df.loc[df['rating'].idxmax(), 'title']}
    """

    send_alert("Daily Scraping Report", summary)
    print("✅ Pipeline complete!")
```

**Schedule with Cron:**
```bash
# Run every day at 2 AM
0 2 * * * cd /path/to/project && python3 scrape_pipeline.py
```

---

### 2. API Data Aggregation

**Use Case:** Aggregate data from multiple APIs (Twitter, Reddit, News)

**n8n Workflow:**
```json
{
  "nodes": [
    {
      "name": "Schedule",
      "type": "n8n-nodes-base.cron",
      "parameters": {
        "triggerTimes": {"item": [{"hour": 6}]}
      }
    },
    {
      "name": "Fetch Twitter",
      "type": "n8n-nodes-base.twitter",
      "parameters": {
        "operation": "search",
        "searchText": "#automation"
      }
    },
    {
      "name": "Fetch Reddit",
      "type": "n8n-nodes-base.reddit",
      "parameters": {
        "resource": "subreddit",
        "operation": "getPosts",
        "subreddit": "automation"
      }
    },
    {
      "name": "Fetch News",
      "type": "n8n-nodes-base.httpRequest",
      "parameters": {
        "url": "https://newsapi.org/v2/everything?q=automation"
      }
    },
    {
      "name": "Merge Data",
      "type": "n8n-nodes-base.merge",
      "parameters": {
        "mode": "append"
      }
    },
    {
      "name": "Analyze Sentiment (AI)",
      "type": "n8n-nodes-base.openAi",
      "parameters": {
        "operation": "complete",
        "prompt": "Analyze sentiment (positive/negative/neutral): {{$json.text}}"
      }
    },
    {
      "name": "Save to Airtable",
      "type": "n8n-nodes-base.airtable",
      "parameters": {
        "operation": "append"
      }
    }
  ]
}
```

---

## 📈 Marketing Automation

### 1. Lead Scoring & Routing

**Workflow:**
```
New Lead (Webhook) → Calculate Score → If > 80 → Send to Sales
                                     → If 50-80 → Nurture Campaign
                                     → If < 50 → Newsletter Only
```

**Make.com Scenario:**
```
Trigger: Webhook (new lead from form)

Router:
  Route 1 (Score >= 80):
    - Create deal in CRM (HubSpot)
    - Assign to sales rep
    - Send Slack notification to sales channel
    - Send personalized email from sales rep

  Route 2 (Score 50-79):
    - Add to nurture campaign (Mailchimp)
    - Send lead magnet email
    - Tag as "warm lead"

  Route 3 (Score < 50):
    - Add to newsletter list
    - Tag as "cold lead"

All routes:
  - Log to Google Sheets
  - Update analytics dashboard
```

**Python Implementation:**
```python
def calculate_lead_score(lead):
    """Calculate lead score based on attributes."""
    score = 0

    # Company size
    if lead.get('company_size', '') == 'Enterprise (1000+)':
        score += 30
    elif lead.get('company_size', '') == 'Mid-market (100-1000)':
        score += 20
    elif lead.get('company_size', '') == 'SMB (10-100)':
        score += 10

    # Job title
    if any(title in lead.get('job_title', '').lower() for title in ['ceo', 'cto', 'vp', 'director']):
        score += 25
    elif 'manager' in lead.get('job_title', '').lower():
        score += 15

    # Industry
    if lead.get('industry') in ['Technology', 'SaaS', 'E-commerce']:
        score += 20

    # Engagement
    if lead.get('email_opens', 0) > 5:
        score += 10
    if lead.get('website_visits', 0) > 3:
        score += 10
    if lead.get('downloaded_resources', 0) > 0:
        score += 15

    return min(score, 100)  # Cap at 100

def route_lead(lead):
    """Route lead based on score."""
    score = calculate_lead_score(lead)
    lead['score'] = score

    if score >= 80:
        # Hot lead - send to sales
        create_deal_in_crm(lead)
        assign_to_sales_rep(lead)
        send_slack_alert(f"🔥 Hot lead: {lead['name']} (Score: {score})")

    elif score >= 50:
        # Warm lead - nurture campaign
        add_to_nurture_campaign(lead)
        send_lead_magnet(lead)

    else:
        # Cold lead - newsletter
        add_to_newsletter(lead)

    # Log all leads
    log_to_database(lead)

    return lead
```

---

### 2. Abandoned Cart Recovery

**Workflow:**
```
Cart Abandoned → Wait 1 hour → Send Email 1 (gentle reminder)
              → Wait 24 hours → Send Email 2 (discount offer)
              → Wait 48 hours → Send Email 3 (last chance)
```

**n8n Workflow:**
```json
{
  "nodes": [
    {
      "name": "Webhook - Cart Abandoned",
      "type": "n8n-nodes-base.webhook"
    },
    {
      "name": "Wait 1 Hour",
      "type": "n8n-nodes-base.wait",
      "parameters": {"amount": 1, "unit": "hours"}
    },
    {
      "name": "Check if Purchased",
      "type": "n8n-nodes-base.httpRequest",
      "parameters": {
        "url": "https://api.yourstore.com/orders/{{$json.user_id}}"
      }
    },
    {
      "name": "If Not Purchased",
      "type": "n8n-nodes-base.if",
      "parameters": {
        "conditions": {
          "boolean": [
            {"value1": "{{$json.purchased}}", "value2": false}
          ]
        }
      }
    },
    {
      "name": "Send Email 1",
      "type": "n8n-nodes-base.emailSend",
      "parameters": {
        "subject": "You left something in your cart!",
        "text": "Complete your purchase..."
      }
    },
    {
      "name": "Wait 24 Hours",
      "type": "n8n-nodes-base.wait",
      "parameters": {"amount": 24, "unit": "hours"}
    },
    {
      "name": "Send Email 2 (Discount)",
      "type": "n8n-nodes-base.emailSend",
      "parameters": {
        "subject": "10% off your cart!",
        "text": "Use code SAVE10..."
      }
    },
    {
      "name": "Wait 48 Hours",
      "type": "n8n-nodes-base.wait",
      "parameters": {"amount": 48, "unit": "hours"}
    },
    {
      "name": "Send Email 3 (Final)",
      "type": "n8n-nodes-base.emailSend",
      "parameters": {
        "subject": "Last chance - cart expiring soon!",
        "text": "Final reminder..."
      }
    }
  ]
}
```

---

## 🔐 Security Best Practices

### 1. API Key Management

**❌ Never Do This:**
```python
# Hardcoded API key - DANGEROUS!
OPENAI_API_KEY = "sk-1234567890abcdef"
```

**✅ Use Environment Variables:**
```python
import os
from dotenv import load_dotenv

load_dotenv()  # Load from .env file

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in environment")
```

**.env file:**
```bash
OPENAI_API_KEY=sk-1234567890abcdef
DATABASE_URL=postgresql://user:pass@localhost/db
AWS_ACCESS_KEY_ID=AKIA...
AWS_SECRET_ACCESS_KEY=...
```

**.gitignore:**
```
.env
secrets/
*.key
```

---

### 2. Webhook Security

**Verify webhook signatures:**
```python
import hmac
import hashlib

def verify_webhook_signature(payload, signature, secret):
    """Verify webhook came from trusted source."""
    expected_signature = hmac.new(
        secret.encode(),
        payload.encode(),
        hashlib.sha256
    ).hexdigest()

    return hmac.compare_digest(expected_signature, signature)

# Usage in Flask
from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    payload = request.get_data(as_text=True)
    signature = request.headers.get('X-Hub-Signature-256', '')

    if not verify_webhook_signature(payload, signature, WEBHOOK_SECRET):
        abort(403, 'Invalid signature')

    # Process webhook
    data = request.json
    process_event(data)

    return {'status': 'success'}
```

---

### 3. Rate Limiting

**Prevent API abuse:**
```python
from ratelimit import limits, sleep_and_retry
from requests import Session

# Max 10 calls per minute
@sleep_and_retry
@limits(calls=10, period=60)
def call_api(url):
    """Rate-limited API call."""
    response = requests.get(url)
    return response.json()

# Usage
for url in urls:
    data = call_api(url)  # Automatically rate-limited
```

---

### 4. Error Handling & Retry Logic

**Exponential backoff:**
```python
import time
from functools import wraps

def retry_with_backoff(retries=3, backoff_in_seconds=1):
    """Retry decorator with exponential backoff."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            x = 0
            while True:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if x == retries:
                        raise

                    wait = backoff_in_seconds * 2 ** x
                    print(f"Error: {e}. Retrying in {wait}s...")
                    time.sleep(wait)
                    x += 1
        return wrapper
    return decorator

# Usage
@retry_with_backoff(retries=5, backoff_in_seconds=2)
def fetch_data_from_api(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
```

---

## 📊 Monitoring & Logging

### 1. Structured Logging

**Use JSON logs for automation:**
```python
import logging
import json
from datetime import datetime

class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_data = {
            'timestamp': datetime.utcnow().isoformat(),
            'level': record.levelname,
            'message': record.getMessage(),
            'module': record.module,
            'function': record.funcName,
        }

        if record.exc_info:
            log_data['exception'] = self.formatException(record.exc_info)

        return json.dumps(log_data)

# Setup logger
logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
handler.setFormatter(JSONFormatter())
logger.addHandler(handler)
logger.setLevel(logging.INFO)

# Usage
logger.info("Automation started", extra={'workflow_id': '123'})
logger.error("API call failed", extra={'url': 'https://api.example.com'})
```

---

### 2. Monitoring Dashboard (Prometheus + Grafana)

**Expose metrics:**
```python
from prometheus_client import Counter, Histogram, start_http_server
import time

# Define metrics
workflow_runs = Counter('workflow_runs_total', 'Total workflow executions', ['status'])
workflow_duration = Histogram('workflow_duration_seconds', 'Workflow execution time')

# Start metrics server
start_http_server(8000)

# Instrument your automation
@workflow_duration.time()
def run_workflow():
    try:
        # Your workflow logic
        time.sleep(2)

        workflow_runs.labels(status='success').inc()
        return {'status': 'success'}

    except Exception as e:
        workflow_runs.labels(status='failed').inc()
        raise
```

**Grafana dashboard:**
```
- Total workflow runs (success vs failed)
- Workflow duration (p50, p95, p99)
- Error rate over time
- API call latency
```

---

## 💰 Cost Optimization

### 1. Choose Right Tool for Volume

**Cost comparison (1M operations/month):**
```
Make.com: $299/mo (Premium plan, 100K ops) × 10 = $2,990/mo
n8n (self-hosted): $50/mo (VPS) + $0 (unlimited ops) = $50/mo
Python (serverless): AWS Lambda free tier (1M requests) = $0

Recommendation:
- < 10K ops/mo: Zapier/Make (ease of use)
- 10K - 100K ops/mo: Make.com or n8n
- > 100K ops/mo: n8n (self-hosted) or Python
```

---

### 2. Batch Operations

**❌ Inefficient - 1 API call per item:**
```python
for item in items:  # 1000 items
    api.create(item)  # 1000 API calls = expensive
```

**✅ Efficient - Batch API calls:**
```python
# Batch 100 items per call
batch_size = 100
for i in range(0, len(items), batch_size):
    batch = items[i:i+batch_size]
    api.create_batch(batch)  # 10 API calls = 100x cheaper
```

---

### 3. Cache Results

**Save API costs with caching:**
```python
from functools import lru_cache
import redis

# In-memory cache (simple)
@lru_cache(maxsize=1000)
def get_user_data(user_id):
    # Expensive API call
    return api.get_user(user_id)

# Redis cache (distributed)
redis_client = redis.Redis(host='localhost', port=6379)

def get_cached(key, fetch_func, ttl=3600):
    """Get from cache or fetch and cache."""
    cached = redis_client.get(key)

    if cached:
        return json.loads(cached)

    # Fetch fresh data
    data = fetch_func()

    # Cache for 1 hour
    redis_client.setex(key, ttl, json.dumps(data))

    return data

# Usage
user = get_cached(f'user:{user_id}', lambda: api.get_user(user_id))
```

---

## 🚀 Production Deployment

### 1. Docker Containerization

**Dockerfile for automation:**
```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install FFmpeg (for video automation)
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

# Copy application
COPY . .

# Run automation
CMD ["python", "automation.py"]
```

**docker-compose.yml:**
```yaml
version: '3.8'

services:
  automation:
    build: .
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
      - DATABASE_URL=${DATABASE_URL}
    volumes:
      - ./data:/app/data
      - ./logs:/app/logs
    restart: unless-stopped

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

  postgres:
    image: postgres:15-alpine
    environment:
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

---

### 2. GitHub Actions CI/CD

**.github/workflows/deploy.yml:**
```yaml
name: Deploy Automation

on:
  push:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest

      - name: Run tests
        run: pytest

  deploy:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Build Docker image
        run: docker build -t automation:latest .

      - name: Deploy to server
        run: |
          docker-compose down
          docker-compose up -d
```

---

### 3. Scheduled Workflows

**Cron + Logging:**
```bash
#!/bin/bash
# run_automation.sh

# Configuration
LOG_DIR="/var/log/automation"
DATE=$(date +%Y-%m-%d_%H-%M-%S)
LOG_FILE="$LOG_DIR/automation_$DATE.log"

# Create log directory
mkdir -p "$LOG_DIR"

# Run automation with logging
{
    echo "==================================="
    echo "Automation started at $(date)"
    echo "==================================="

    python3 /path/to/automation.py

    EXIT_CODE=$?

    echo "==================================="
    echo "Automation finished at $(date)"
    echo "Exit code: $EXIT_CODE"
    echo "==================================="

    # Send alert if failed
    if [ $EXIT_CODE -ne 0 ]; then
        echo "Automation failed!" | mail -s "Automation Error" admin@example.com
    fi

} 2>&1 | tee "$LOG_FILE"

# Cleanup old logs (keep last 30 days)
find "$LOG_DIR" -name "automation_*.log" -mtime +30 -delete
```

**Crontab:**
```bash
# Run every day at 2 AM
0 2 * * * /path/to/run_automation.sh

# Run every hour
0 * * * * /path/to/hourly_automation.sh

# Run every 15 minutes
*/15 * * * * /path/to/frequent_automation.sh
```

---

## 🎓 Advanced Patterns

### 1. State Machine Workflow

**Use for complex multi-step processes:**
```python
from enum import Enum

class OrderState(Enum):
    CREATED = "created"
    PAID = "paid"
    PROCESSING = "processing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"

class OrderStateMachine:
    def __init__(self, order_id):
        self.order_id = order_id
        self.state = OrderState.CREATED

    def transition(self, event):
        """Handle state transitions."""
        transitions = {
            (OrderState.CREATED, 'payment_received'): self._handle_payment,
            (OrderState.PAID, 'start_processing'): self._handle_processing,
            (OrderState.PROCESSING, 'shipped'): self._handle_shipment,
            (OrderState.SHIPPED, 'delivered'): self._handle_delivery,
        }

        handler = transitions.get((self.state, event))
        if handler:
            handler()
        else:
            raise ValueError(f"Invalid transition: {self.state} + {event}")

    def _handle_payment(self):
        # Send confirmation email
        send_email(self.order_id, "Payment confirmed")

        # Update inventory
        deduct_inventory(self.order_id)

        # Update state
        self.state = OrderState.PAID

    def _handle_processing(self):
        # Create shipping label
        create_label(self.order_id)

        # Notify warehouse
        notify_warehouse(self.order_id)

        self.state = OrderState.PROCESSING

    # ... other handlers
```

---

## 📚 Resources & Tools

### Learning Resources
- **Make.com Academy:** https://www.make.com/en/academy
- **n8n Documentation:** https://docs.n8n.io/
- **Zapier University:** https://zapier.com/university
- **Automation Anywhere University:** https://university.automationanywhere.com/

### Tools & Platforms
- **Make.com** - Visual automation builder
- **n8n** - Open-source workflow automation
- **Zapier** - No-code automation (5000+ apps)
- **Integromat** - Advanced automation (now Make.com)
- **Apache Airflow** - Data pipeline orchestration
- **Prefect** - Modern workflow orchestration
- **Temporal** - Durable execution framework

### APIs & Integrations
- **RapidAPI** - 40,000+ APIs marketplace
- **Postman** - API testing and automation
- **Webhook.site** - Test webhooks instantly
- **Pipedream** - Serverless integration platform

---

## ✅ Production Checklist

Before deploying automation to production:

**Planning:**
- [ ] Defined clear success criteria
- [ ] Documented workflow diagram
- [ ] Identified failure points
- [ ] Planned rollback strategy

**Security:**
- [ ] API keys in environment variables (not hardcoded)
- [ ] Webhook signature verification
- [ ] Rate limiting implemented
- [ ] Input validation on all external data

**Error Handling:**
- [ ] Try-catch blocks on all API calls
- [ ] Retry logic with exponential backoff
- [ ] Dead letter queue for failed items
- [ ] Alerts for critical errors

**Monitoring:**
- [ ] Logging (JSON structured logs)
- [ ] Metrics (success rate, duration, errors)
- [ ] Alerts (email/Slack for failures)
- [ ] Dashboard (Grafana/custom)

**Testing:**
- [ ] Unit tests for core logic
- [ ] Integration tests with real APIs (sandbox)
- [ ] Load testing for high-volume scenarios
- [ ] Manual testing end-to-end

**Documentation:**
- [ ] README with setup instructions
- [ ] Workflow diagram
- [ ] API documentation
- [ ] Runbook for common issues

**Cost Optimization:**
- [ ] Batch operations where possible
- [ ] Caching for repeated data
- [ ] Right-sized compute resources
- [ ] Monitoring costs (set budgets/alerts)

---

## 🎯 Quick Start Examples

### Example 1: Daily Content Automation (5 minutes setup)

**Goal:** Auto-post daily motivation quote to Twitter

**Setup (Make.com):**
```
1. New scenario
2. Add Schedule trigger (every day 9 AM)
3. Add HTTP module → GET https://api.quotable.io/random
4. Add Twitter module → Post tweet
   Text: "{{content}}" - {{author}}
5. Activate
```

**Done!** Auto-posts every morning.

---

### Example 2: Video Subtitle Generation (10 minutes)

**Goal:** Auto-generate SRT subtitles for MP4 videos

**Bash script:**
```bash
#!/bin/bash
# auto_subtitle.sh

VIDEO="$1"

# Extract audio
ffmpeg -i "$VIDEO" -vn -acodec pcm_s16le -ar 44100 audio.wav -y

# Transcribe
whisper audio.wav --model medium --output_format srt

# Cleanup
rm audio.wav

echo "✅ Subtitles: ${VIDEO%.mp4}.srt"
```

**Usage:**
```bash
chmod +x auto_subtitle.sh
./auto_subtitle.sh myvideo.mp4
```

---

### Example 3: Form to Spreadsheet (No code, 2 minutes)

**Goal:** Save Google Form responses to Sheet + send email

**Setup (Zapier):**
```
1. Trigger: Google Forms - New Response
2. Action: Google Sheets - Create Row
3. Action: Gmail - Send Email
   To: {{email}}
   Subject: Thanks for your submission!
4. Turn on
```

**Done!** Fully automated.

---

## 🤝 Contributing & Community

Want to improve this skill? Contribute automation examples, fix errors, or suggest new patterns!

**Community:**
- Make.com Community: https://community.make.com/
- n8n Forum: https://community.n8n.io/
- r/automation: https://reddit.com/r/automation

---

**Last Updated:** 2025-10-26
**Version:** 1.0
**License:** MIT
**Author:** Claude Code Skills Team

🤖 **This skill is production-ready and maintained. Happy automating!**
