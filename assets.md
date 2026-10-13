# assets.md — inventário de imagens

Gerado por `python scripts/assets.py`. Versão "1600" = largura original quando a foto é menor (não ampliamos).

| Slot | Arquivo(s) em site/assets/ | Origem | Tipo |
|---|---|---|---|
| S1 hero desktop | hero-patio-800.webp (800×450, 33 KB) / hero-patio-1600.webp (1280×720, 62 KB) | `imagens/WhatsApp Image 2026-08-14 at 20.34.26.jpeg` | FOTO REAL (F03) |
| S1 hero mobile | corredor-entrada-800.webp (720×1280, 36 KB) | `imagens/WhatsApp Image 2026-08-14 at 20.33.43.jpeg` | FOTO REAL (F01). Trocada na Fase 1: F07 tinha uma pessoa atrás do título |
| S2 textura brasa | plate-brasa-1600.webp (1024×357, 10 KB) | `design/plates/plate-brasa.png` | PLATE P1 (gerado por IA, abstrato) |
| S3 mosaico (cheddar) | cheddar-carne-800.webp (540×960, 25 KB) / cheddar-carne-1600.webp (540×960, 25 KB) | `imagens/imgi_21_500611195_1226652749141854_6442541329772902850_n.jpg` | FOTO REAL (F15) - direito de uso pendente |
| S3 burger destaque | burger-australiano-800.webp (540×960, 39 KB) / burger-australiano-1600.webp (540×960, 39 KB) | `imagens/imgi_22_500453565_1730242104253561_4119354191733513748_n.jpg` | FOTO REAL (F17) - fallback do A1, sem recorte; direito de uso pendente |
| S3 mosaico 1 | burger-empanado-800.webp (800×800, 59 KB) / burger-empanado-1600.webp (1065×1065, 91 KB) | `imagens/imgi_18_632296417_18427711729187683_536758917969547754_n.jpg` | FOTO REAL (F13) - direito de uso pendente |
| S3 mosaico 2 | burger-crispy-800.webp (202×304, 9 KB) / burger-crispy-1600.webp (202×304, 9 KB) | `imagens/imgi_34_AHRPTWnL-p9XGucqmA138vOzzVaxbE6Oka3kex9QwvKzds-rJ6woRzLLaq7KLS_BSHfXUMGeJ2fzjpasTWVILYpMR0cfss0vjLUCV99cuVOyhq5BwyHr7P6Zh52SEd0yWiNaAZfI96LY=w203-h304-k-no.jpg` | FOTO REAL (F21, Google, baixa res.) - direito de uso pendente |
| S3 mosaico 3 | drink-800.webp (202×270, 19 KB) / drink-1600.webp (202×270, 19 KB) | `imagens/imgi_31_AHRPTWk7ANv2M0Mi1E9pH3e_LJnLLHVHYUDOauIQA0OWEA-OfsB1LVaKq4YrPithq8D-9UsyvX9G4d4zyK8MygTDSAgQqwI1xu3pAUZZl8CEdfhZjMBR5q8wqvAS26ZB1d0-iyZefo4=w203-h270-k-no.jpg` | FOTO REAL (F20, Google, baixa res.) - direito de uso pendente |
| S4 ambiente grande | patio-mesa-800.webp (800×1067, 65 KB) / patio-mesa-1600.webp (1200×1600, 114 KB) | `imagens/WhatsApp Image 2026-10-03 at 20.28.34.jpeg` | FOTO REAL (F08) - pessoa ao fundo, pequena |
| S4 ambiente 2 | patio-toco-800.webp (800×450, 31 KB) / patio-toco-1600.webp (1280×720, 58 KB) | `imagens/WhatsApp Image 2026-08-14 at 20.34.09.jpeg` | FOTO REAL (F02) |
| S4 ambiente 3 | salao-800.webp (720×1280, 52 KB) / salao-1600.webp (720×1280, 52 KB) | `imagens/WhatsApp Image 2026-08-14 at 20.35.57.jpeg` | FOTO REAL (F04) |
| S5 fachada | fachada-800.webp (800×1067, 67 KB) / fachada-1600.webp (1200×1600, 114 KB) | `imagens/WhatsApp Image 2026-10-03 at 20.26.10.jpeg` | FOTO REAL (F05) - pessoa: autorização pendente |
| Logo | logo-800.webp (150×150, 4 KB) / logo-1600.webp (150×150, 4 KB) | `imagens/imgi_2_410571612_743075111058415_2558024689146206935_n.jpg` | FOTO REAL (F19, 150 px) - fallback do A3; logo em alta pendente |
| S1 vídeo | tour.mp4 (4,3 MB, preload=none) | `imagens/WhatsApp Video 2026-10-03 at 22.28.16.mp4` | VÍDEO REAL (V01), recomprimido H.264, sem áudio alterado |
| S1 vídeo poster | tour-poster.webp | quadro de V01 (ffmpeg) | VÍDEO REAL (V01) |

## Imagens recriadas por IA

- Nenhuma foto real foi recriada ou ampliada por IA.
- `plate-brasa` é um PLATE gerado por IA, abstrato, sem objeto real (decoração, R3).

## Fallbacks

- A1 (recorte do burger) não recebido: F17 inteira com máscara radial CSS.
- A2 (hero widescreen) não recebido: F03 original, 1280 px.
- A3 (logo em alta) não recebido: F19, 150 px, exibida em ≤ 96 px CSS.

## Arquivos não usados

- Versões duplicadas "-1600" de fotos pequenas são idênticas às "-800" (a foto original é menor). Remover na Fase 4.

## Fase 1, revisão de fidelidade

| Slot | Arquivo | Origem | Tipo |
|---|---|---|---|
| S1 vídeo de fundo (loop) | hero-loop.webm (812 KB) / hero-loop.mp4 (980 KB), 480×854, 21 s, sem áudio | trecho 0–21 s de `imagens/WhatsApp Video 2026-10-03 at 22.28.16.mp4` | VÍDEO REAL (V01), recortado e recomprimido |
| S1 pôster | hero-loop-poster.webp | 1º quadro do loop | VÍDEO REAL (V01) |
| S4 foto única | patio-toco-800/1600.webp | F02 | FOTO REAL |
| S2/S3 burger flutuante | burger-recorte.webp (508×595, 61 KB, com alfa) | `imagens/imgi_18_632296417_18427711729187683_536758917969547754_n.jpg` (F13) → `design/plates/f13-recorte.png` | FOTO REAL com **fundo removido por IA de segmentação** (rembg/isnet). Pixels do burger intactos. Confirmar com o cliente antes de publicar (direito de uso + recorte). |
