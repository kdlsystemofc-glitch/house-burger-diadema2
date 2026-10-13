# DESIGN.md — House Burger Diadema

> Fonte de dados: `CLIENTE.MD` (texto bruto do perfil do Google Maps). `CLIENTE-bruto.md` não existe;
> por decisão do humano (2026-10-12, "siga com o que temos") o mesmo arquivo vale como bruto e real.
> Todo dado incerto vira `<!-- PENDÊNCIA: ... -->` e entra em PENDENCIAS-CLIENTE.md.

## Índice de fotos reais (IDs usados neste documento)

| ID | Arquivo (IMAGENS/) | Tamanho | Conteúdo | Uso |
|---|---|---|---|---|
| F01 | WhatsApp Image 2026-08-14 at 20.33.43.jpeg | 720×1280 | Corredor de entrada à noite, arandelas acesas, cidade ao fundo | Hero mobile (alternativa) |
| F02 | WhatsApp Image 2026-08-14 at 20.34.09.jpeg | 1280×720 | Pátio coberto, toco iluminado, bicicleta decorativa | Ambiente |
| F03 | WhatsApp Image 2026-08-14 at 20.34.26.jpeg | 1280×720 | Pátio + balcão/bar ao fundo | Hero desktop |
| F04 | WhatsApp Image 2026-08-14 at 20.35.57.jpeg | 720×1280 | Salão interno, mesas, luminária pendente | Ambiente |
| F05 | WhatsApp Image 2026-10-03 at 20.26.10.jpeg | 1200×1600 | Fachada nº 351, letreiro neon "House Burger Diadema", pessoa na porta | Visite / Rodapé |
| F06 | WhatsApp Image 2026-10-03 at 20.27.19.jpeg | 1200×1600 | Pessoa no corredor de entrada | Reserva (pessoa: autorização) |
| F07 | WhatsApp Image 2026-10-03 at 20.28.04.jpeg | 1200×1600 | Corredor longo do pátio, céu noturno, luzes quentes | Hero mobile |
| F08 | WhatsApp Image 2026-10-03 at 20.28.34.jpeg | 1200×1600 | Pátio com mesa redonda, toco iluminado, TV | Ambiente |
| F09 | WhatsApp Image 2026-10-03 at 20.43.49.jpeg | 1200×1600 | Salão interno com pessoa | Reserva (pessoa: autorização) |
| F10 | imgi_12_AHRPTWmZ…s451-k-no.jpg | 451×338 | Salão grande com churrasqueira (Google) | NÃO USAR até confirmar se é a casa |
| F11 | imgi_16_499552927…_n.jpg | 540×960 | Burger cheddar, marca d'água "@3CLUBBURGER" | NÃO USAR (marca d'água de terceiro) |
| F12 | imgi_17_622130804…_n.jpg | 1440×979 | Chef com 3 burgers; boné e parede "Club Burger" | Só com autorização (marca Club Burger) |
| F13 | imgi_18_632296417…_n.jpg | 1065×1065 | Burger empanado + pratos, mesa de madeira | Cardápio |
| F14 | imgi_19_502765791…_n.jpg | 540×960 | Burger pão escuro + cheddar escorrendo, marca d'água | NÃO USAR (usar F17) |
| F15 | imgi_21_500611195…_n.jpg | 540×960 | Cheddar sendo derramado na carne | Manifesto |
| F16 | imgi_21_AHRPTWmeEw…s435-k-no.jpg | 435×290 | Dois burgers na mesa (Google, baixa res.) | Reserva (só miniatura) |
| F17 | imgi_22_500453565…_n.jpg | 540×960 | Burger pão escuro (australiano?) + cheddar escorrendo, sem marca d'água | Destaque flutuante |
| F18 | imgi_23_AHRPTWnT…s516-k-no.jpg | 516×290 | Mesa com burgers e batata (Google, baixa res.) | Reserva (só miniatura) |
| F19 | imgi_2_410571612…_n.jpg | 150×150 | Logo branco sobre preto | Logo (baixa res. → pendência) |
| F20 | imgi_31_AHRPTWk7…w203-h270-k-no.jpg | 202×270 | Drink laranja, parede verde "Carpe Diem" | Cardápio (miniatura) |
| F21 | imgi_34_AHRPTWnL…w203-h304-k-no.jpg | 202×304 | Burger com crispy verde | Cardápio (miniatura) |
| F22 | imgi_38_AHRPTWnj…w203-h270-k-no.jpg | 202×270 | Salão escuro com luz roxa (Google) | NÃO USAR até confirmar se é a casa |
| V01 | WhatsApp Video 2026-10-03 at 22.28.16.mp4 | 480×854, 79 s | Tour: corredor → pátio → banheiro/hall decorado | Botão "play" do hero (ver pergunta 2) |

---

## 1. Mockup vs. realidade

Tudo abaixo do mockup é **inventado ou genérico** e não vai para o site:

- **Textos em inglês**: "FORGED IN FIRE & FLAME", "EXPERIENCE THE NIGHT // DIADEMA", "00:19 REEL". Slogans inventados → no site viram PENDÊNCIA de slogan (ou rótulo factual).
- **"00:19 REEL"**: o "0:19" do CLIENTE.MD é a duração de um vídeo no Google, não nosso. O vídeo real (V01) tem 79 s.
- **Bloco de horários** no rodapé ("Abre às 17:00 / 2630 às 17:00 / 00:00 à 17:00 / Dimdô…"): texto corrompido gerado por IA. Real: só "Abre às 17:00" (instantâneo do Google). Dias e fechamento → PENDÊNCIA.
- **Bar com luminárias pendentes e prateleiras (topo)**: não é a casa. O real é pátio com arandelas/corredor (F03, F07).
- **Brasas e chamas na grelha (meio)**: foto de banco de imagem/IA. Não há foto real de grelha a carvão, e o método de preparo (carvão/brasa) **não está confirmado**. Não vamos sugerir "na brasa" em texto.
- **Burger flutuante**: genérico, gerado. O real equivalente é F17 (pão escuro + cheddar), recortado.
- **Salão com lareira de tijolo e clientes (rodapé)**: não existe nas fotos; a casa tem salão interno simples (F04, F09) e pátio (F02, F08). Clientes reconhecíveis = proibido inventar.
- **Fumaça cobrindo o hero**: efeito genérico (vapor de banco de imagem). Não será usado.
- **Ausências no mockup** que o site precisa ter (dados reais existem): botões Pedir delivery / Pedir e retirar (houseburgerdiadema.ola.click), Ligar ((11) 94216-3332), Rotas, endereço, nota 4,4 (171), destaques do cardápio.

## 2. Elemento(s) de assinatura decorativo(s)

| Elemento no mockup | Dificuldade em CSS/SVG responsivo | Decisão |
|---|---|---|
| **Faixa de brasas/chamas** atravessando a página entre hero e destaque | **Difícil** (fotorrealismo) | **Versão simplificada AGORA:** "linha de brasa": faixa full-bleed de `radial-gradient` em camadas (laranja `--c-ember` → `--c-coal`), com grão estático de SVG `feTurbulence` (como data-URI em `background-image`, sem `filter` em ancestral). Altura `clamp(6rem, 18vw, 16rem)`. **Não animada** (R9). Opcional: PLATE P1 por cima, como textura abstrata. |
| **Fumaça** | Difícil, e genérica | **Descartada** (critério da Fase 3: efeito genérico). Substituída por vinheta escura nas bordas (CSS). |
| **Brilho quente das luminárias** | Fácil | `radial-gradient` âmbar no topo do hero, sobre a foto real. |
| **Tipografia em caixa-alta creme com leve brilho** | Fácil | `text-shadow` âmbar suave (sem `filter`). |
| **Burger "flutuando" entre seções** | Médio | Foto real F17 recortada (A1), posicionada com margem negativa sobrepondo duas seções; sombra = `radial-gradient` elíptico abaixo. |

## 3. Paleta (HEX amostrado do mockup) + contraste WCAG

Amostragem e cálculo: `python scripts/contrast.py`.

| Token | HEX | Origem no mockup | Uso |
|---|---|---|---|
| `--c-coal` | `#0B0A09` | fundo meio/rodapé (#030406 / #05080D, aquecido) | fundo base |
| `--c-night` | `#060F16` | céu/fundo do topo | fundo do hero |
| `--c-cream` | `#F1DCC7` | título "HOUSE BURGER DIADEMA" | títulos |
| `--c-ivory` | `#FBF5E9` | pico de brilho dos títulos | texto de destaque |
| `--c-mute` | `#A89B8C` | corrigido a partir de #867C70 (texto secundário) | texto secundário |
| `--c-ember` | `#DB6F24` | chama | acento, botão principal |
| `--c-cheese` | `#F2A93B` | cheddar (entre #BA7108 e #FCDA91) | acento 2, preço/status |
| `--c-brick` | `#7E4B2C` | tijolo | superfícies quentes |
| `--c-wood` | `#31160D` | madeira da mesa | fundo de seção alternado |

Resultado do script (texto normal ≥ 4.5:1):

| Par | Razão | Status |
|---|---|---|
| cream / coal | 14.89 | PASSA |
| ivory / coal | 18.22 | PASSA |
| mute original #867C70 / coal | 4.83 | passa no limite → **trocado por #A89B8C (7.28)** por segurança sobre fotos |
| mute #A89B8C / night | 7.11 | PASSA |
| ember / coal (texto) | 5.95 | PASSA |
| cheese / coal (texto) | 9.90 | PASSA |
| coal / cheese (botão) | 9.90 | PASSA |
| coal / ember (botão) | 5.95 | PASSA |
| **ivory / ember (botão)** | **3.06** | **REPROVA → corrigido: botão ember usa texto `--c-coal`** |
| cream / brick | 5.39 | PASSA |
| cream / foto com overlay 70% coal (pior caso #3A2E25) | 9.89 | PASSA → regra: texto sobre foto sempre com overlay ≥ 70% |

## 4. Tipografia

- **Títulos: Cormorant (600/700, caixa-alta, tracking 0.04em)**: serifada de alto contraste, a mais próxima da letra do mockup (romana clássica, creme e elegante). Ela dá o tom "noite" sem cair no clichê "stencil de hamburgueria".
- **Texto: Manrope (400/600)**: sem serifa geométrica-humanista, muito legível em telas pequenas e em fundo escuro. Contrasta com a Cormorant sem brigar.
- Nunca Inter/Roboto/Arial. Fallback: `Georgia, serif` / `system-ui, sans-serif`.

## 5. Tabela por seção

Ordem do mockup, mais o bloco de dados reais obrigatório. O texto vem do CLIENTE.MD, com o número da linha.

| # | Seção | Layout | Camadas | Texto real (CLIENTE.MD) |
|---|---|---|---|---|
| S1 | **Hero** (`secao-01`) | Tela cheia `100svh`, título central, ações abaixo; mobile empilhado | FOTO REAL F03 (desktop) / F07 (mobile) via `<picture>`; CSS overlay coal 70% + glow âmbar; botão play → V01 | h1 "House Burger Diadema" (L1); "Hambúrguer" (L4); status "Abre às 17:00" (L63, rótulo "Hoje"); botões "Pedir delivery" / "Pedir e retirar" (L55-56 → L72 houseburgerdiadema.ola.click); "Ligar" (L61, L73) |
| S2 | **Manifesto / fogo** (`secao-02`) | Faixa larga com título central + foto lateral (desktop 2 colunas, mobile 1) | CSS/SVG "linha de brasa" (seção 2) + FOTO REAL F15 + PLATE P1 opcional | Título: `<!-- PENDÊNCIA: slogan -->`. Texto de apoio: "Hambúrguer · Centro, Diadema - SP" (L4, L64). Nada sobre "brasa/carvão" até confirmar. |
| S3 | **Destaque + cardápio** (`secao-03`) | Burger recortado sobrepondo S2/S3; lista de destaques em 2 colunas (desktop) / 1 (mobile); mosaico de fotos | FOTO REAL F17 (recorte A1), F13, F21, F20; CSS sombra elíptica | "Destaques do cardápio" (L74): Mr Salad Com 2 Carnes, Saquerinha de Morango, Pão Australiano, Gorgonburger, "Harmburguer Gourmet" (grafia a confirmar), House Burger (L76-86). Preços: PENDÊNCIA. Botão "Ver o cardápio" (L99 → ola.click). Fotos **sem legenda de nome de prato** (não sabemos qual é qual). |
| S4 | **Ambiente** (`secao-04`) | Galeria assimétrica (1 grande + 3 menores), selos de atributos | FOTO REAL F08, F02, F04, F01; CSS | "Pratos para happy hour" · "Espaço privativo para eventos" · "Necessidade de fazer reserva" (L62, texto final a confirmar); nota Google "4,4 (171 avaliações)" (L66-68); 2 avaliações: "Bom hambúrguer, galera gente boa, preço de acordo com a qualidade." e "Pessoal muito atencioso, lanches muito bons e ambiente agradável." (L110, L114). A avaliação com crítica (L112) não entra. Link "Mais avaliações no Google" (L115). |
| S5 | **Visite / rodapé** (`secao-05`) | 2 colunas (foto da fachada + dados) / mobile empilhado; rodapé com logo | FOTO REAL F05; logo F19 (ou SVG do cliente); CSS | Endereço "R. Moacyr Goulart Cunha Caldas, 351 - Centro, Diadema - SP, 09911-450" (L64); "Abre às 17:00" (L63) + `<!-- PENDÊNCIA: dias e horário de fechamento -->`; telefone (L73); site (L72); "Rotas" (L58 → link Google Maps pelo endereço); título: `<!-- PENDÊNCIA: frase de fechamento -->` |

Microcopy de interface ("Cardápio", "Ambiente", "Como chegar", "Horário", "Pedir agora") é rótulo de navegação, não dado factual. Decidido por R11.

## 6. Plano de imagens

| Slot | Fonte |
|---|---|
| S1 hero desktop | FOTO REAL: IMAGENS/WhatsApp Image 2026-08-14 at 20.34.26.jpeg (F03), ajuste A2 opcional |
| S1 hero mobile | FOTO REAL: IMAGENS/WhatsApp Image 2026-10-03 at 20.28.04.jpeg (F07) |
| S1 vídeo | FOTO REAL (vídeo): IMAGENS/WhatsApp Video 2026-10-03 at 22.28.16.mp4 (V01), carregado só ao clicar |
| S2 textura brasa | CSS/SVG (padrão) + PLATE P1 (opcional): design/plates/plate-brasa.png |
| S2 foto | FOTO REAL: IMAGENS/imgi_21_500611195_1226652749141854_6442541329772902850_n.jpg (F15) |
| S3 burger flutuante | FOTO REAL: IMAGENS/imgi_22_500453565_1730242104253561_4119354191733513748_n.jpg (F17) → ajuste A1 (recorte) → design/plates/f17-recorte.png |
| S3 mosaico | FOTO REAL: imgi_18_632296417…_n.jpg (F13), imgi_34_AHRPTWnL…jpg (F21), imgi_31_AHRPTWk7…jpg (F20) |
| S4 ambiente | FOTO REAL: WhatsApp 2026-10-03 at 20.28.34 (F08, grande), WhatsApp 2026-08-14 at 20.34.09 (F02), WhatsApp 2026-08-14 at 20.35.57 (F04), WhatsApp 2026-08-14 at 20.33.43 (F01) |
| S5 fachada | FOTO REAL: WhatsApp Image 2026-10-03 at 20.26.10.jpeg (F05); pessoa na foto → autorização |
| Logo | FOTO REAL: imgi_2_410571612_743075111058415_2558024689146206935_n.jpg (F19, 150 px) → preferir arquivo vetorial do cliente; ajuste A3 só como fallback |
| Favicon/OG (Fase 5) | derivado do logo, sem foto com direito pendente |

### Prompts prontos

**PLATE P1: textura abstrata de brasa** (salvar como `design/plates/plate-brasa.png`, 2560×900)
```
Abstract dark background texture, 2560x900, landscape. Near-black warm base (#0B0A09).
Soft out-of-focus glowing ember particles and orange-red heat glow (#DB6F24, #F2A93B) concentrated
along the bottom third, fading to pure black at the top edge and at both side edges.
Heavy bokeh, no recognizable objects: no charcoal pieces, no grill, no flames shapes, no smoke,
no food, no text, no logos, no people. Subtle film grain. Seamless left-right edges.
```

**A1: recorte do burger F17** (salvar como `design/plates/f17-recorte.png`, PNG com transparência)
```
Mantenha tudo idêntico: mesmo hambúrguer, mesmo pão, mesmo cheddar, mesma luz, cor e textura.
Só remova o fundo (mesa, papel e fundo desfocado) e entregue PNG com fundo transparente.
Não redesenhe, não complete partes cortadas, não adicione brilho, fumaça nem sombra.
Se a borda inferior do cheddar tocar o papel, corte rente ao cheddar.
```
(Se o recorte exigir "completar" partes do pão → anotar em assets.md: "recriada por IA, confirmar com o cliente antes de publicar".)

**A2: ampliar F03 para hero widescreen** (opcional, `design/plates/f03-wide.png`, 2560×1440) → **recriada por IA**
```
Mantenha tudo idêntico: mesmo pátio, mesmas paredes, mesmas luzes, mesmo balcão, mesmas cores e
mesma iluminação noturna. Só aumente a resolução para 2560x1440 e estenda levemente as bordas
esquerda e direita com a mesma parede e piso, sem adicionar objetos, pessoas, textos ou placas novas.
```

**A3: logo F19 em alta** (fallback se o cliente não enviar o vetor, `design/plates/logo-recriado.svg/png`) → **recriada por IA**
```
Mantenha tudo idêntico: mesmo desenho de hambúrguer em linha, mesmo círculo duplo, mesmo texto
"HOUSE BURGUER" e "DIADEMA", mesma fonte e proporções. Só redesenhe em alta resolução (2000x2000),
traço branco puro sobre fundo transparente, bordas nítidas. Não altere grafia nem elementos.
```
Atenção: a logo F19 diz "BURGUER" e o letreiro da fachada (F05) diz "BURGER". Confirmar a grafia oficial com o cliente.

**Não ajustar:** F11/F14 (não remover marca d'água de terceiro: usar F17 no lugar); F12 (não apagar marca "Club Burger": depende de autorização).

## 7. Animação por seção (Fase 3)

| Seção | Entrada | Flutuação (só quality high) | Parallax (≤ 24px, 0.05–0.10) |
|---|---|---|---|
| S1 Hero | Visível sem JS (R8). Título e botões: fade + translateY 16px, 700 ms, defasagem 80 ms, só como realce | nenhuma | foto de fundo 0.05 (camada própria, sem texto dentro) |
| S2 Manifesto | título 800 ms; foto F15 600 ms, defasada 120 ms | nenhuma | foto F15 0.08 |
| S3 Destaque | burger recortado: pouso suave de translateY 40px → 0, 900 ms; lista defasada 60 ms por item | burger: translateY ±4px, 6 s, loop (1 loop) | sombra elíptica 0.05 |
| S4 Ambiente | fotos da galeria defasadas 90 ms, 700 ms; selos 600 ms | nenhuma | foto grande 0.06 |
| S5 Visite | dados 600 ms, foto 700 ms | nenhuma | nenhum |
| Linha de brasa | **nunca animada** (R9) | — | — |

Descartados por serem genéricos: fumaça, vapor, faísca subindo, brilho "shine" em botão.

## 8. Perguntas (decisões subjetivas)

1. **Tom visual:** mantenho o clima "noite premium" do mockup (preto, creme, serifada), ou puxo mais para o neon/street da fachada (letreiro "Open Burger" colorido)?
2. **Vídeo do tour (V01, 79 s, vertical, 480p):** uso no botão "play" do hero, que abre o vídeo em tela cheia, ou deixo sem vídeo?
3. **Pessoas nas fotos** (F05 fachada, F06, F09): quer o dono/equipe aparecendo no site? Se sim, peço autorização ao cliente; se não, uso só fotos sem pessoas.
4. **Avaliações do Google:** mostro a nota 4,4 (171) e 2 trechos de avaliação, ou só o link "Ver avaliações no Google"?
5. **Ordem das seções:** cardápio antes do ambiente (como planejado), ou ambiente primeiro (a casa é o diferencial)?

## Registro de decisões (R11)

- Mesmo arquivo como bruto e real: instrução do humano.
- Avaliação com crítica (L112) não usada: a página é de venda e o trecho é de terceiro. Não é dado necessário.
- "Linha de brasa" em CSS em vez de foto: R3 e R9, e responsiva sem custo de imagem.
- F10 e F22 fora: não há prova de que são a mesma casa (espaço, teto e luz diferentes das fotos do cliente).
- Fotos de cardápio sem nome de prato: não sabemos qual foto é qual item (R11).
- Fatias do mockup em `design/secoes/`: cortes em y = 0–350, 350–640, 620–890, 870–1140, 1140–1376 (sobreposição 20 px, por causa do burger que atravessa S2/S3).

## Decisões da Fase 1 (as perguntas do §8 ficaram sem resposta; adotei o padrão, revisável)

- P1 recebido: `design/plates/plate-brasa.png` (1024×357, gerado por IA, abstrato, sem objeto real). Uso só como textura decorativa da "linha de brasa".
- A1 não recebido: **fallback** = foto real F17 inteira, com máscara radial em CSS (`mask-image`) no lugar do recorte. Não há edição de pixel.
- A2 não recebido: **fallback** = F03 original (1280 px), sem ampliação. Em telas maiores fica levemente suave atrás do overlay 70%.
- A3 não recebido: **fallback** = logo F19 original (150 px) só em tamanho pequeno (≤ 96 px CSS). PENDÊNCIA: logo em alta.
- Pergunta 1 (tom): mantido "noite premium" do mockup.
- Pergunta 2 (vídeo): V01 entra atrás de um botão "play" (`preload="none"`, comprimido para web). Sem autoplay.
- Pergunta 3 (pessoas): uso F05 (fachada com pessoa) porque é a única foto da fachada, marcada como PENDÊNCIA de autorização. F06, F09 e F12 ficam fora.
- Pergunta 4 (avaliações): nota + 2 trechos, marcados como PENDÊNCIA de autorização (item 17).
- Pergunta 5 (ordem): cardápio antes do ambiente.
- WebP: largura 800 e 1600 sem ampliar. Se a foto original for menor, a versão "1600" usa a largura original (registrado em assets.md).
- Fontes via Google Fonts `<link>` nesta fase. Na Fase 4 passam a ser locais em WOFF2.
- Microcopy de interface permitido: lista fechada em `scripts/microcopy.json` (o checador de texto usa essa lista).

## Decisões tomadas durante a construção (Fase 1)

- S2 ficou sem a foto F15 (mais fiel ao mockup, que só tem título e brasa). F15 foi para o mosaico da S3.
- Hero mobile: F07 trocada por F01 (F07 tinha pessoa atrás do título).
- Títulos sem slogan: S2 = "Hambúrguer" (categoria do Google); S4 = "Ambiente" (microcopy); S5 = endereço real. Slogans continuam PENDÊNCIA.
- "Necessidade de fazer reserva" ficou fora dos selos até o cliente explicar (texto ambíguo).
- Hero com min-height 100svh (no mockup a 1ª fatia é baixa porque o mockup inteiro é um pôster vertical).
- Grade por seção com conteúdo até 88rem (variável --content), sem wrapper global (R6).
- Estrelas da nota em SVG inline; preenchimento de 4,4 aproximado por gradiente.

## Revisão de fidelidade ao mockup (pedido do humano, 2026-10-12)

| Seção | Mockup | Antes | Agora |
|---|---|---|---|
| S1 | bar escuro, luzes no alto à esquerda, título médio fino, "00:19 REEL" + play pequeno, sem botões | foto do pátio, título enorme e pesado, 3 botões | **vídeo real em loop** (0–21 s do tour, sem som), escurecido à direita e embaixo, brilho no alto à esquerda, título peso 500 menor, rótulo "Tour pela casa" + play pequeno; botões de pedido saíram do hero (ficou só "Pedir agora" no topo) |
| S2 | título de 2 linhas SOBRE a brasa, chama à direita, névoa | título acima da faixa | título "Hambúrguer & happy hour" sobre a faixa; chama e névoa em gradiente CSS (sem fumaça animada) |
| S3 | burger centralizado flutuando sobre a brasa | burger + lista em 2 colunas + mosaico de 4 fotos | burger maior e centralizado; lista centralizada em linha com "·"; mosaico removido (o mockup não tem); botões de pedido vieram para cá |
| S4 | foto larga do salão, full-bleed, fundida no escuro | texto + nota + 2 avaliações + galeria de 3 fotos | 1 foto real larga full-bleed (F02) fundida em cima e embaixo; selos e nota pequenos sobre a parte escura; trechos de avaliação removidos |
| S5 | "X // DIADEMA" grande com glow, "Abre às 17:00" em serifa, linhas pequenas | foto da fachada + dados em colunas | "Centro // Diadema" com glow, "Abre às 17:00" em serifa, endereço e contato em linhas pequenas, Rotas/Ligar; foto da fachada removida (também resolve o risco "Club Burger" e a pessoa) |

Assets que ficaram sem uso (remover na Fase 4): hero-patio, burger-empanado, cheddar-carne, burger-crispy, drink, patio-mesa, salao, fachada, corredor-entrada.
Desvio conhecido: no desktop o vídeo vertical (480 px) é ampliado e cortado; fica suave atrás do overlay. Melhoraria com um vídeo horizontal em 1080p do cliente.
Movimento: com prefers-reduced-motion o vídeo some e fica o pôster. O botão de pausa entra na Fase 3.

## Revisão 2 (pedido do humano, 2026-10-12): fechamento, burger e vídeo

- **Burger:** a máscara oval em F17 trocada por **recorte real de F13** (`design/plates/f13-recorte.png` → `site/assets/burger-recorte.webp`, 508×595). Fundo removido por segmentação automática (rembg, modelo isnet-general-use); os pixels do burger não foram alterados. Ele fica dentro da seção da brasa e a base invade a foto do ambiente, como no mockup. A borda esquerda do pão inferior é levemente reta (a foto original corta ali).
- **Emendas horizontais:** a causa era a borda do plate (que não ocupava a altura toda). Agora o plate encosta na base da seção e o degradê cobre topo e base.
- **Fechamento:** a ordem agora é foto → título, como no mockup. Saíram os selos, a nota e os botões. O título em 2 linhas "House Burger / Centro // Diadema" fica dourado com brilho e sobe sobre a base da foto. Abaixo, "Abre às 17:00" em serifa e duas linhas pequenas e cinzas (endereço; telefone / Pedir delivery / Pedir e retirar / Rotas). O rodapé separado foi removido; o © fica no fim da seção.
- **Vídeo:** autoplay+muted+loop+playsinline por HTML, reforçado por JS (play em canplay, na volta da aba, no 1º toque/rolagem e ao ser pausado). **Não** é mais escondido com prefers-reduced-motion (pedido explícito: "sempre em looping"). Desvio registrado da regra da Fase 3; o botão de pausa entra na Fase 3C.
- **Parallax do vídeo:** a camada desce a 0,35× a rolagem, só transform, sem texto dentro. Desvio da regra "0,05–0,10 / máx. 24px" por pedido explícito do humano. Desliga com prefers-reduced-motion.
- Removidos da página: mosaico, galeria e avaliações (S3/S4 antigos), lista em colunas, `cardapio.css`. Assets sem uso: burger-australiano, hero-patio, burger-empanado, cheddar-carne, burger-crispy, drink, patio-mesa, salao, fachada, corredor-entrada, logo só no cabeçalho. Limpeza na Fase 4.

## Revisão 3 (2026-10-12): página integrada como o mockup

- Novo PLATE do humano: `design/plates/plate-brasa-grelha.png` (gerado por IA: brasa, fumaça, chama, grelha) → `plate-brasa-grelha-800/1600.webp`. Substitui o plate de bokeh.
- Integração: a cena da brasa sobe **14vw sobre a base do hero** (topo transparente por máscara: a fumaça aparece sobre o vídeo). A foto do ambiente sobe **10vw sob a base da brasa** (as duas se dissolvem por máscara). O título de fechamento sobe sobre a base da foto. Nenhuma borda reta entre seções.
- As máscaras ficam no `<picture>` (foto + escurecimento juntos). Nada animado, sem transform/filter/opacity nos ancestrais (R9).
- **Atenção factual:** o plate mostra grelha a carvão, e isso sugere um método de preparo ainda não confirmado (PENDENCIAS-CLIENTE item 13). Se a casa não usar brasa, trocar pelo plate de bokeh (`plate-brasa.png`, ainda no repositório).

## Revisão 4 (2026-10-12): conexão das seções + burger novo

- Burger: trocado pelo `burger-ia` (IA, enviado pelo humano, fundo transparente). Largura clamp(17rem, 36vw, 32rem); ~35% da altura invade a foto do ambiente.
- Conexão: a fumaça sobe 22vw sobre o hero (antes 14vw), a foto sobe 16vw sob a brasa (antes 10vw), o fechamento sobe 26% sobre a foto, as máscaras ficaram mais longas e o hero mobile tem 82svh. Brilho do burger com overflow-x: clip na seção (sem rolagem lateral).

## Revisão 5 (2026-10-12): vídeo do hero tratado

- Trecho 15–30 s (pedido do humano). Cadeia ffmpeg: deshake (o vidstabtransform deste build corrompia os quadros e foi descartado) → hqdn3d → unsharp → eq/colorbalance/curves (quente, pretos fundos) → vinheta → câmera lenta 0,8× com mistura de quadros (a interpolação mci gerava blocos e foi descartada) → loop com fusão de 1,2 s.
- Grão de filme por CSS (SVG estático em .hero::after), sem custo de banda e fora da camada de parallax (R9).
- Master para upscale: `design/video/hero-master.mp4` (480×854, 30 fps, crf 14). Próximo passo do humano: Video2X 2× → devolver o arquivo para eu reencodar a versão web.

## Revisão 6 (2026-10-12): S2 com duas imagens + geometria do mockup + vídeo 4×

- S2 = cena com 2 plates: carvão à esquerda (64% da largura, 72% da altura) e chama/grelha à direita (58%, quase até o hero). Cada uma se dissolve no centro, no topo e na base por máscara composta (intersect). Título e cardápio na faixa escura do meio.
- Burger como no mockup: o topo entra ~22% na base da cena e a base toca ~8% a foto. Entre os dois fica um vão escuro. A foto do ambiente não sobe mais sob a cena (o overlap-photo foi removido).
- Celular: as imagens ficam só na parte de baixo da cena para não passar atrás do texto.
- Vídeo: upscale 4× do humano → `scripts/video-hero.sh` (corte por quadro, pois o .mkv tem tempos esticados) → versão vertical 720p (celular) e recorte horizontal 1080×720 (desktop), escolhidos por `<source media>`.
- Grão do hero com máscara (sumia a emenda clara na base do hero).
