"""Amostra cores do mockup e calcula contraste WCAG 2.x dos pares de texto."""
from PIL import Image
im = Image.open('design/mockup-full.png').convert('RGB')
def bright(box, n=60, hue=None):
    px = list(im.crop(box).get_flattened_data())
    if hue: px = [p for p in px if hue(p)]
    px = sorted(px, key=sum)[-n:]
    return '#%02X%02X%02X' % tuple(sum(p[i] for p in px)//len(px) for i in range(3))
print('cheese-bright', bright((250,740,520,840), 300, lambda p: p[0]>p[1]>p[2]+60))
print('flame-bright', bright((540,380,680,600), 300, lambda p: p[0]>p[1]+40))
print('ember-coal', bright((0,520,300,680), 300, lambda p: p[0]>p[1]+60))

def lum(h):
    c = [int(h[i:i+2],16)/255 for i in (1,3,5)]
    c = [x/12.92 if x <= 0.03928 else ((x+0.055)/1.055)**2.4 for x in c]
    return 0.2126*c[0]+0.7152*c[1]+0.0722*c[2]
def ratio(a,b):
    la, lb = sorted((lum(a),lum(b)), reverse=True)
    return (la+0.05)/(lb+0.05)
pairs = [
 ('cream sobre coal',  '#F1DCC7','#0B0A09', 4.5),
 ('ivory sobre coal',  '#FBF5E9','#0B0A09', 4.5),
 ('mute (mockup) sobre coal','#867C70','#0B0A09', 4.5),
 ('mute (corrigido) sobre coal','#A89B8C','#0B0A09', 4.5),
 ('mute (corrigido) sobre night','#A89B8C','#060F16', 4.5),
 ('ember sobre coal (texto)','#DB6F24','#0B0A09', 4.5),
 ('cheese sobre coal (texto)','#F2A93B','#0B0A09', 4.5),
 ('coal sobre cheese (botão)','#0B0A09','#F2A93B', 4.5),
 ('coal sobre ember (botão)','#0B0A09','#DB6F24', 4.5),
 ('ivory sobre ember (botão)','#FBF5E9','#DB6F24', 4.5),
 ('cream sobre brick','#F1DCC7','#7E4B2C', 4.5),
 ('cream sobre overlay 70% coal em foto clara (pior caso #3A2E25)','#F1DCC7','#3A2E25', 4.5),
]
for name,f,b,req in pairs:
    r = ratio(f,b); print(f'{name:62s} {f} / {b}  {r:5.2f}:1  {"PASSA" if r>=req else "REPROVA"}')
