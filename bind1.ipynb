# ==============================================================================
# test_app_v0.1
# just learning python and playing with some random widgets and packages
# nothing interesting here, please ignore
# ==============================================================================

# 1. Install dependencies
!pip install -q yt-dlp imageio-ffmpeg ipywidgets

import os
import shutil
import time
import re
import subprocess
import yt_dlp
import imageio_ffmpeg
import ipywidgets as widgets
from IPython.display import display, FileLink, HTML

# Get standalone binary
FFMPEG_PATH = imageio_ffmpeg.get_ffmpeg_exe()

def extract_shortcode(url: str):
    match = re.search(r'/(?:p|reel|reels)/([A-Za-z0-9_-]+)', url.strip())
    return match.group(1) if match else None

def compress_video(input_path, output_path, quality_setting, media_type):
    if quality_setting == "Best Available Quality" and media_type == "Video (With Audio)":
        shutil.copy(input_path, output_path)
        return

    print(f"   ⚙️ Processing: Quality = {quality_setting} | Audio = {media_type}")
    cmd = [FFMPEG_PATH, '-y', '-i', input_path]

    # Resizing
    if quality_setting == "Medium (under 720p)":
        cmd.extend(['-vf', "scale=-2:'min(720,ih)'", '-c:v', 'libx264', '-crf', '28', '-preset', 'fast'])
    elif quality_setting == "Worst / Smallest Size":
        cmd.extend(['-vf', "scale=-2:'min(480,ih)'", '-c:v', 'libx264', '-crf', '35', '-preset', 'fast'])
    else:
        cmd.extend(['-c:v', 'copy'])

    # Audio
    if media_type == "Video Only (No Audio)":
        cmd.append('-an')
    else:
        if quality_setting != "Best Available Quality":
            cmd.extend(['-c:a', 'copy'])

    if quality_setting != "Best Available Quality":
        cmd.extend(['-pix_fmt', 'yuv420p'])
    cmd.extend(['-movflags', '+faststart'])

    cmd.append(output_path)

    try:
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        print("   ✅ Processing complete.")
    except Exception as e:
        print(f"   ❌ Error ({e}). Copying original instead.")
        shutil.copy(input_path, output_path)

def download_reel(shortcode, download_type, video_quality):
    target_dir = shortcode
    os.makedirs(target_dir, exist_ok=True)

    url = f"https://www.instagram.com/reel/{shortcode}/"
    ydl_opts = {
        'outtmpl': os.path.join(target_dir, f'{shortcode}.%(ext)s'),
        'writedescription': True,
        'writeinfojson': True,
        'quiet': True,
        'no_warnings': True,
        'ffmpeg_location': FFMPEG_PATH,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    downloaded = os.listdir(target_dir)
    video_files = [f for f in downloaded if f.endswith(('.mp4', '.mkv', '.webm'))]
    desc_files = [f for f in downloaded if f.endswith('.description')]
    json_files = [f for f in downloaded if f.endswith('.info.json')]

    # 1. Process Video
    if video_files:
        in_vid = os.path.join(target_dir, video_files[0])
        out_vid = os.path.join('final_downloads', f"{shortcode}.mp4")
        compress_video(in_vid, out_vid, video_quality, download_type)
    else:
        print(f"   ⚠️ No video file found for {shortcode}.")

    # 2. Process Caption
    if desc_files:
        shutil.copy(os.path.join(target_dir, desc_files[0]), os.path.join('final_downloads', f"{shortcode}.txt"))
        print(f"   📝 Saved: {shortcode}.txt")

    # 3. Process Metadata
    if json_files:
        shutil.copy(os.path.join(target_dir, json_files[0]), os.path.join('final_downloads', f"{shortcode}.json"))
        print(f"   📊 Saved: {shortcode}.json")

    # Cleanup temporary folder
    if os.path.exists(target_dir):
        shutil.rmtree(target_dir)

def start_download_process(download_type, video_quality, delay_seconds, pasted_links):
    links = []

    # Priority 1: Pasted links
    if pasted_links.strip():
        print("🔗 Using links pasted directly into the box...")
        raw_items = re.split(r'[\r\n,]+', pasted_links)
        links = [item.strip() for item in raw_items if item.strip()]

    # Priority 2: Automatically read from links.txt
    elif os.path.exists("links.txt"):
        print("📂 Found 'links.txt' in directory! Reading links...")
        with open("links.txt", "r", encoding="utf-8", errors="ignore") as f:
            links = [line.strip() for line in f.readlines() if line.strip()]

    if not links:
        print("❌ Error: No links found!")
        print("👉 Please paste links into the text box above OR upload a 'links.txt' file.")
        return

    print(f"\n📦 Found {len(links)} links. Delay set to {delay_seconds}s per item.")
    print(f"⚙️ Active Mode: {download_type} | Quality: {video_quality}\n")

    os.makedirs('final_downloads', exist_ok=True)

    for index, raw_url in enumerate(links, start=1):
        shortcode = extract_shortcode(raw_url)
        print("─" * 52)

        if not shortcode:
            print(f"⚠️ [{index}/{len(links)}] Skipped invalid: {raw_url}")
            continue

        print(f"⬇️ [{index}/{len(links)}] jariewajr iajij i i ji sf: {shortcode}")

        try:
            download_reel(shortcode, download_type, video_quality)
            print(f"✅ Success: {shortcode}")
        except Exception as e:
            print(f"❌ Error for {shortcode}: {e}")

        time.sleep(delay_seconds)

    # --- 2. ZIP & JUPYTER DOWNLOAD LINK ---
    total_saved = len(os.listdir('final_downloads'))
    if total_saved > 0:
        zip_filename = 'what_is_this.zip'
        print("\n" + "═" * 52)
        print(f"🎉 Complete! Processed {total_saved} files.")
        print(f"📦 Zipping files into '{zip_filename}'...")
        shutil.make_archive('what_is_this', 'zip', 'final_downloads')

        print("\n⬇️ Click the link below to download your zip file directly to your PC:")
        display(HTML(f'<h3>👉 <a href="{zip_filename}" target="_blank" download>Click Here to Download: {zip_filename}</a></h3>'))
        display(FileLink(zip_filename))

        print("\n💡 NOTE:")
        print(f"   You can also right-click '{zip_filename}' in the left file dashboard")
        print("   and select 'Download' at any time.")
    else:
        print("\n❌ No files were processed.")

# ==================== INTERACTIVE GUI CONTROLS ====================
style = {'description_width': '210px'}
layout = widgets.Layout(width='480px')

w_type = widgets.Dropdown(
    options=["Video Only (No Audio)", "Video (With Audio)"],
    value="Video Only (No Audio)",
    description="Media / Audio:",
    style=style,
    layout=layout
)

w_quality = widgets.Dropdown(
    options=["Worst / Smallest Size", "Medium (under 720p)", "Best Available Quality"],
    value="Worst / Smallest Size",
    description="Quality:",
    style=style,
    layout=layout
)

w_delay = widgets.IntSlider(
    value=5,
    min=1,
    max=15,
    step=1,
    description="fdsfkjskf jk jk jk jsik jjk:",
    style=style,
    layout=layout
)

w_links = widgets.Textarea(
    value="",
    placeholder="paste here...",
    description="kjk jjijiaj3ijawirjeoif oijriew:",
    style=style,
    layout=widgets.Layout(width='650px', height='80px')
)

w_button = widgets.Button(
    description="🚀 Start",
    button_style="success",
    tooltip="Click to start",
    layout=widgets.Layout(width='220px', height='42px', margin='10px 0 10px 215px')
)

output_area = widgets.Output()

def on_click_start(btn):
    with output_area:
        output_area.clear_output()
        w_button.disabled = True
        w_button.description = "⏳ Processing..."
        try:
            start_download_process(
                download_type=w_type.value,
                video_quality=w_quality.value,
                delay_seconds=w_delay.value,
                pasted_links=w_links.value
            )
        finally:
            w_button.disabled = False
            w_button.description = "🚀 Start"

w_button.on_click(on_click_start)

# Display interactive UI panel
ui = widgets.VBox([
    widgets.HTML("<h2>🛠️ fdsarjeaj kakejarijeaijiejj i</h2>"),
    widgets.HTML("<p><i>Select options and click <b>Start</b>:</i></p>"),
    w_type,
    w_quality,
    w_delay,
    w_links,
    w_button,
    output_area
])

display(ui)
