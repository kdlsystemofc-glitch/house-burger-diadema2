"""Converte as fotos usadas para WebP (800 e 1600 px, sem ampliar) e gera assets.md."""
from PIL import Image, ImageOps
import os
OUT = 'site/assets'
# slot, nome de saída, origem, tipo
SLOTS = [
 ('S1 hero desktop',   'hero-patio',     'imagens/WhatsApp Image 2026-08-14 at 20.34.26.jpeg', 'FOTO REAL (F03)'),
 ('S1 hero mobile',    'hero-corredor',  'imagens/WhatsApp Image 2026-10-03 at 20.28.04.jpeg', 'FOTO REAL (F07)'),
 ('S2 textura brasa',  'plate-brasa',    'design/plates/plate-brasa.png',                      'PLATE P1 (gerado por IA, abstrato)'),
 ('S2 foto',           'cheddar-carne',  'imagens/imgi_21_500611195_1226652749141854_6442541329772902850_n.jpg', 'FOTO REAL (F15) - direito de uso pendente'),
 ('S3 burger destaque','burger-australiano','imagens/imgi_22_500453565_1730242104253561_4119354191733513748_n.jpg', 'FOTO REAL (F17) - fallback do A1, sem recorte; direito de uso pendente'),
 ('S3 mosaico 1',      'burger-empanado','imagens/imgi_18_632296417_18427711729187683_536758917969547754_n.jpg', 'FOTO REAL (F13) - direito de uso pendente'),
 ('S3 mosaico 2',      'burger-crispy',  'imagens/imgi_34_AHRPTWnL-p9XGucqmA138vOzzVaxbE6Oka3kex9QwvKzds-rJ6woRzLLaq7KLS_BSHfXUMGeJ2fzjpasTWVILYpMR0cfss0vjLUCV99cuVOyhq5BwyHr7P6Zh52SEd0yWiNaAZfI96LY=w203-h304-k-no.jpg', 'FOTO REAL (F21, Google, baixa res.) - direito de uso pendente'),
 ('S3 mosaico 3',      'drink',          'imagens/imgi_31_AHRPTWk7ANv2M0Mi1E9pH3e_LJnLLHVHYUDOauIQA0OWEA-OfsB1LVaKq4YrPithq8D-9UsyvX9G4d4zyK8MygTDSAgQqwI1xu3pAUZZl8CEdfhZjMBR5q8wqvAS26ZB1d0-iyZefo4=w203-h270-k-no.jpg', 'FOTO REAL (F20, Google, baixa res.) - direito de uso pendente'),
 ('S4 ambiente grande','patio-mesa',     'imagens/WhatsApp Image 2026-10-03 at 20.28.34.jpeg', 'FOTO REAL (F08) - pessoa ao fundo, pequena'),
 ('S4 ambiente 2',     'patio-toco',     'imagens/WhatsApp Image 2026-08-14 at 20.34.09.jpeg', 'FOTO REAL (F02)'),
 ('S4 ambiente 3',     'salao',          'imagens/WhatsApp Image 2026-08-14 at 20.35.57.jpeg', 'FOTO REAL (F04)'),
 ('S4 ambiente 4',     'corredor-entrada','imagens/WhatsApp Image 2026-08-14 at 20.33.43.jpeg', 'FOTO REAL (F01)'),
 ('S5 fachada',        'fachada',        'imagens/WhatsApp Image 2026-10-03 at 20.26.10.jpeg', 'FOTO REAL (F05) - pessoa: autorização pendente'),
 ('Logo',              'logo',           'imagens/imgi_2_410571612_743075111058415_2558024689146206935_n.jpg', 'FOTO REAL (F19, 150 px) - fallback do A3; logo em alta pendente'),
]
rows = []
for slot, name, src, kind in SLOTS:
    im = ImageOps.exif_transpose(Image.open(src)).convert('RGB')
    outs = []
    for target in (800, 1600):
        w = min(target, im.width)
        h = round(im.height * w / im.width)
        fn = f'{name}-{target}.webp'
        im.resize((w, h), Image.LANCZOS).save(os.path.join(OUT, fn), 'WEBP', quality=80, method=6)
        outs.append(f'{fn} ({w}×{h}, {os.path.getsize(os.path.join(OUT, fn))//1024} KB)')
    rows.append(f'| {slot} | {" / ".join(outs)} | `{src}` | {kind} |')
md = ['# assets.md — inventário de imagens', '',
      'Gerado por `python scripts/assets.py`. Versão "1600" = largura original quando a foto é menor (não ampliamos).', '',
      '| Slot | Arquivo(s) em site/assets/ | Origem | Tipo |', '|---|---|---|---|'] + rows + [
      '| S1 vídeo | tour.mp4 | `imagens/WhatsApp Video 2026-10-03 at 22.28.16.mp4` | VÍDEO REAL (V01), recomprimido H.264, sem áudio alterado |',
      '| S1 vídeo poster | tour-poster.webp | quadro de V01 (ffmpeg) | VÍDEO REAL (V01) |', '',
      '## Imagens recriadas por IA', '',
      '- Nenhuma foto real foi recriada ou ampliada por IA.',
      '- `plate-brasa` é um PLATE gerado por IA, abstrato, sem objeto real (decoração, R3).', '',
      '## Fallbacks', '',
      '- A1 (recorte do burger) não recebido: F17 inteira com máscara radial CSS.',
      '- A2 (hero widescreen) não recebido: F03 original, 1280 px.',
      '- A3 (logo em alta) não recebido: F19, 150 px, exibida em ≤ 96 px CSS.']
open('assets.md', 'w', encoding='utf-8').write('\n'.join(md) + '\n')
print('\n'.join(rows))
