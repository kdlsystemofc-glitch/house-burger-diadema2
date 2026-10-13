import subprocess
import os

src = "kling_20261013_VIDEO_Cinematic__5086_0.mp4"
work = "design/video"
os.makedirs(work, exist_ok=True)
master_loop = f"{work}/master-loop.mp4"

# 1) Generate master loop with smooth crossfade
dur = 0.8
offset = 7.041667 - 2 * dur

print("1/5) Criando master loop com fusao continua em altissima qualidade...")
subprocess.run([
    "ffmpeg", "-loglevel", "error", "-y", "-i", src,
    "-filter_complex",
    f"[0:v]split[a][b];[a]trim=start={dur},setpts=PTS-STARTPTS[A];[b]trim=0:{dur},setpts=PTS-STARTPTS[B];[A][B]xfade=transition=fade:duration={dur}:offset={offset:.3f},format=yuv420p[v]",
    "-map", "[v]", "-an", "-c:v", "libx264", "-crf", "12", "-preset", "slow",
    master_loop
], check=True)

# 2) Desktop versions - Alta Definicao (1920x1080) com CAS (Contrast Adaptive Sharpening)
# Corta os 70px de baixo (marca d'agua), escala em Lanczos para 1920x..., enquadra e aplica CAS para nitidez cristalina
vf_desk = "crop=iw:ih-70:0:0,scale=1920:-2:flags=lanczos,crop=1920:1080:0:(ih-1080)*0.35,cas=0.35,format=yuv420p"

print("2/5) Gerando site/assets/hero-loop-wide.mp4 e .webm em 1080p Full HD...")
subprocess.run([
    "ffmpeg", "-loglevel", "error", "-y", "-i", master_loop,
    "-vf", vf_desk, "-an",
    "-c:v", "libx264", "-crf", "18", "-preset", "slow", "-profile:v", "high", "-pix_fmt", "yuv420p", "-movflags", "+faststart",
    "site/assets/hero-loop-wide.mp4"
], check=True)

subprocess.run([
    "ffmpeg", "-loglevel", "error", "-y", "-i", master_loop,
    "-vf", vf_desk, "-an",
    "-c:v", "libvpx-vp9", "-b:v", "0", "-crf", "22", "-row-mt", "1", "-deadline", "good",
    "site/assets/hero-loop-wide.webm"
], check=True)

subprocess.run([
    "ffmpeg", "-loglevel", "error", "-y", "-ss", "00:00:00.2", "-i", master_loop,
    "-vf", vf_desk,
    "-frames:v", "1", "-c:v", "libwebp", "-quality", "85",
    "site/assets/hero-loop-wide-poster.webp"
], check=True)

# 3) Mobile versions (720x1280) com CAS para nitidez em telas retina/OLED
vf_mob = "crop=iw:ih-70:0:0,scale=-2:1280:flags=lanczos,crop=720:1280:(iw-720)*0.5:(ih-1280)*0.5,cas=0.35,format=yuv420p"

print("3/5) Gerando site/assets/hero-loop-720.mp4 e .webm em alta fidelidade...")
subprocess.run([
    "ffmpeg", "-loglevel", "error", "-y", "-i", master_loop,
    "-vf", vf_mob, "-an",
    "-c:v", "libx264", "-crf", "19", "-preset", "slow", "-profile:v", "high", "-pix_fmt", "yuv420p", "-movflags", "+faststart",
    "site/assets/hero-loop-720.mp4"
], check=True)

subprocess.run([
    "ffmpeg", "-loglevel", "error", "-y", "-i", master_loop,
    "-vf", vf_mob, "-an",
    "-c:v", "libvpx-vp9", "-b:v", "0", "-crf", "24", "-row-mt", "1", "-deadline", "good",
    "site/assets/hero-loop-720.webm"
], check=True)

subprocess.run([
    "ffmpeg", "-loglevel", "error", "-y", "-ss", "00:00:00.2", "-i", master_loop,
    "-vf", vf_mob,
    "-frames:v", "1", "-c:v", "libwebp", "-quality", "85",
    "site/assets/hero-loop-720-poster.webp"
], check=True)

print("Renderizacao em altissima qualidade finalizada!")
