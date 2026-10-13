#!/usr/bin/env bash
# Gera o vídeo de fundo do hero a partir do upscale do Video2X (Real-ESRGAN 4x).
# Trecho: quadros 356–712 do original (= 15–30 s a 23,75 fps; o .mkv tem os mesmos quadros com tempos esticados).
# Cadeia sem IA: deshake -> hqdn3d leve -> cor quente/pretos fundos -> vinheta -> câmera lenta 0,8x -> loop com fusão de 1,2 s.
set -euo pipefail
cd "$(dirname "$0")/.."
SRC="imagens/WhatsApp Video 2026-10-03 at 22.28.16.realesrgan.mkv"
WORK="design/video"
mkdir -p "$WORK"

GRADE="hqdn3d=1.5:1:3:2,unsharp=5:5:0.35:5:5:0.0,eq=contrast=1.1:brightness=-0.02:saturation=1.08:gamma=0.97,colorbalance=rs=0.04:bs=-0.05:rm=0.05:gm=0.01:bm=-0.04:rh=0.03:bh=-0.03,curves=master='0/0 0.1/0.06 0.5/0.5 1/1',vignette=angle=PI/5"

# 1) corte por quadro + redução para 1080x1920 + estabilização + cor + câmera lenta
ffmpeg -loglevel error -y -i "$SRC" -an -vf "trim=start_frame=356:end_frame=712,setpts=N/(95/4)/TB,scale=1080:-2:flags=lanczos,crop=1080:1920,deshake=rx=48:ry=48:edge=mirror,crop=iw*0.94:ih*0.94,scale=1080:1920:flags=lanczos,${GRADE},setpts=1.25*PTS,framerate=fps=30:interp_start=0:interp_end=255:scene=100,format=yuv420p" \
  -c:v libx264 -crf 12 -preset medium "$WORK/hero-graded-1080.mp4"

# 2) loop sem corte: o fim se funde no início (1,2 s)
L=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$WORK/hero-graded-1080.mp4")
OFF=$(python -c "print(round($L-2.4,4))")
ffmpeg -loglevel error -y -i "$WORK/hero-graded-1080.mp4" -filter_complex "[0:v]split[a][b];[a]trim=start=1.2,setpts=PTS-STARTPTS[A];[b]trim=0:1.2,setpts=PTS-STARTPTS[B];[A][B]xfade=transition=fade:duration=1.2:offset=${OFF},format=yuv420p[v]" \
  -map "[v]" -c:v libx264 -crf 14 -preset slow -movflags +faststart "$WORK/hero-master-1080.mp4"

M="$WORK/hero-master-1080.mp4"
# 3) mobile: vertical 720x1280
ffmpeg -loglevel error -y -i "$M" -vf "scale=720:1280:flags=lanczos" -an -c:v libvpx-vp9 -b:v 0 -crf 40 -row-mt 1 -deadline good site/assets/hero-loop-720.webm
ffmpeg -loglevel error -y -i "$M" -vf "scale=720:1280:flags=lanczos" -an -c:v libx264 -crf 28 -preset slow -profile:v main -pix_fmt yuv420p -movflags +faststart site/assets/hero-loop-720.mp4
ffmpeg -loglevel error -y -i "$M" -vf "scale=720:1280:flags=lanczos" -frames:v 1 -c:v libwebp -quality 72 site/assets/hero-loop-720-poster.webp
# 4) desktop: recorte horizontal 1080x720 (faixa que o object-position 50% 45% mostra)
CROP="crop=1080:720:0:(ih-720)*0.45"
ffmpeg -loglevel error -y -i "$M" -vf "$CROP" -an -c:v libvpx-vp9 -b:v 0 -crf 38 -row-mt 1 -deadline good site/assets/hero-loop-wide.webm
ffmpeg -loglevel error -y -i "$M" -vf "$CROP" -an -c:v libx264 -crf 26 -preset slow -profile:v main -pix_fmt yuv420p -movflags +faststart site/assets/hero-loop-wide.mp4
ffmpeg -loglevel error -y -i "$M" -vf "$CROP" -frames:v 1 -c:v libwebp -quality 72 site/assets/hero-loop-wide-poster.webp
ls -la site/assets/hero-loop-* "$M"
