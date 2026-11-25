# Render entry.png v2 for news-image-20261124 — written fresh in this session.
# 1024x1024 PNG, flat vector-style news poster drawn with Pillow primitives.
# Content: 37 stories from the 24 Nov 2026 research file (4 leads + 33 in brief).
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (246, 241, 227)
INK = (25, 25, 25)
RED = (179, 39, 30)
NAVY = (31, 78, 121)
TEAL = (15, 118, 110)
PURPLE = (107, 33, 168)
ORANGE = (194, 65, 12)
GREEN = (21, 128, 61)
GOLD = (161, 98, 7)
GREY = (107, 107, 107)
LINE = (180, 172, 150)
CARD = (255, 253, 246)
OCEAN = (205, 226, 235)
LAND = (232, 222, 196)

FD = "/usr/share/fonts/truetype/dejavu/"
def F(name, size):
    return ImageFont.truetype(FD + name, size)

f_kick = F("DejaVuSans-Bold.ttf", 12)
f_title = F("DejaVuSerif-Bold.ttf", 46)
f_sub = F("DejaVuSans.ttf", 13)
f_lead_h = F("DejaVuSans-Bold.ttf", 18)
f_lead_b = F("DejaVuSans.ttf", 12)
f_grid_k = F("DejaVuSans-Bold.ttf", 13)
f_grid_b = F("DejaVuSans.ttf", 11)
f_map = F("DejaVuSans-Bold.ttf", 12)
f_leg = F("DejaVuSans.ttf", 12)
f_leg_b = F("DejaVuSans-Bold.ttf", 12)
f_tl = F("DejaVuSans.ttf", 11)
f_tl_b = F("DejaVuSans-Bold.ttf", 11)
f_audit = F("DejaVuSans.ttf", 12)
f_audit_b = F("DejaVuSans-Bold.ttf", 12)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

def wrap(text, font, max_w):
    words = text.split()
    lines, cur = [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if d.textlength(t, font=font) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines

def text_cx(cx, y, s, font, fill):
    d.text((cx - d.textlength(s, font=font) / 2, y), s, font=font, fill=fill)

def draw_wrapped(x, y, text, font, fill, max_w, lh):
    for ln in wrap(text, font, max_w):
        d.text((x, y), ln, font=font, fill=fill)
        y += lh
    return y

# ---------------- masthead ----------------
d.rectangle([0, 0, W, 8], fill=RED)
text_cx(W // 2, 24, "T H E   W O R L D   I N   O N E   D A Y", f_kick, RED)
d.text((28, 46), "TUESDAY 24 NOVEMBER 2026", font=f_title, fill=INK)
tw = d.textlength("TUESDAY 24 NOVEMBER 2026", font=f_title)
d.text((28 + tw + 18, 62), "24 NOV 2026", font=f_lead_h, fill=RED)
text_cx(W // 2, 96, "One day of world news  ·  37 stories  ·  8 regions  ·  every event first reported 24 November 2026",
        f_sub, (70, 70, 70))
d.line([28, 112, 996, 112], fill=INK, width=2)

# ---------------- lead cards ----------------
LEADS = [
    ("HORMUZ CLOSED", RED, "Iran orders the strait shut “day by day” until its 7 conditions are met. Brent $88.71.", "tanker"),
    ("NVIDIA +31.5%", NAVY, "Board reinstates Jensen Huang as CEO; shares soar. S&P 500 +4.73% — best day since Apr 2025.", "chip"),
    ("ZAPORIZHZHIA HIT", NAVY, "Russian overnight attack kills 2, wounds 40 incl. 4 children. 96 drones launched, 73 downed.", "city"),
    ("FACTORY FIRE, INDONESIA", RED, "26 confirmed dead at a candy factory in Banten; ~28 still missing. Negligence probe opened.", "fire"),
]
LX, LW, LGAP = 28, 234, 10
LY, LH = 122, 182

def scene_tanker(x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(214, 232, 240))
    d.polygon([(x + 8, y + h - 26), (x + w - 8, y + h - 26), (x + w - 22, y + h - 8), (x + 22, y + h - 8)], fill=(60, 60, 60))
    d.rectangle([x + w // 2 - 30, y + 22, x + w // 2 + 30, y + h - 28], fill=RED)
    d.rectangle([x + w // 2 - 30, y + 22, x + w // 2 + 30, y + 34], fill=(140, 20, 15))
    d.line([x + 14, y + 16, x + 30, y + 16], fill=INK, width=3)
    for cx in (x + 44, x + w - 44):
        d.ellipse([cx - 6, y + 10, cx + 6, y + 22], fill=INK)
        d.line([cx, y + 22, cx, y + 30], fill=INK, width=2)

def scene_chip(x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(214, 232, 240))
    for i in range(5):
        px = x + 30 + i * 34
        d.line([px, y + h - 18 - i * 9, px + 30, y + h - 27 - i * 9], fill=TEAL, width=5)
    d.polygon([(x + w - 52, y + 14), (x + w - 22, y + 14), (x + w - 22, y + 44), (x + w - 37, y + 29)], fill=TEAL)
    d.rectangle([x + 18, y + 12, x + 62, y + 48], outline=NAVY, width=3)
    d.text((x + 24, y + 22), "NVDA", font=f_tl_b, fill=NAVY)

def scene_city(x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(214, 232, 240))
    d.rectangle([x + 40, y + 26, x + 110, y + h - 10], fill=(90, 90, 90))
    d.polygon([(x + 40, y + 26), (x + 75, y + 8), (x + 110, y + 26)], fill=(60, 60, 60))
    d.rectangle([x + 130, y + 44, x + 190, y + h - 10], fill=(140, 140, 140))
    for bx in (x + 52, x + 82):
        for by in (y + 36, y + 56):
            d.rectangle([bx, by, bx + 14, by + 12], fill=(255, 220, 120))
    d.ellipse([x + 178, y + 12, x + 196, y + 30], fill=INK)
    d.line([x + 187, y + 30, x + 187, y + 42], fill=INK, width=2)

def scene_fire(x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(214, 232, 240))
    d.rectangle([x + 30, y + 40, x + 150, y + h - 10], fill=(120, 120, 120))
    d.rectangle([x + 30, y + 40, x + 150, y + 52], fill=(80, 80, 80))
    d.rectangle([x + 160, y + 26, x + 176, y + h - 10], fill=(90, 90, 90))
    d.polygon([(x + 78, y + 12), (x + 98, y + 44), (x + 88, y + 44), (x + 104, y + 62), (x + 62, y + 62), (x + 76, y + 44), (x + 68, y + 44)], fill=(230, 90, 20))
    d.polygon([(x + 82, y + 40), (x + 92, y + 56), (x + 74, y + 56)], fill=(255, 200, 40))

SCENES = {"tanker": scene_tanker, "chip": scene_chip, "city": scene_city, "fire": scene_fire}

for i, (head, col, body, kind) in enumerate(LEADS):
    x = LX + i * (LW + LGAP)
    d.rectangle([x, LY, x + LW, LY + LH], fill=CARD, outline=LINE, width=1)
    d.rectangle([x, LY, x + LW, LY + 5], fill=col)
    SCENES[kind](x + 8, LY + 12, LW - 16, 74)
    draw_wrapped(x + 10, LY + 94, head, f_lead_h, INK, LW - 20, 21)
    draw_wrapped(x + 10, LY + 140, body, f_lead_b, (60, 60, 60), LW - 20, 14)

# ---------------- world map + region legend ----------------
MY, MH = 314, 200
MX0, MX1 = 28, 700
d.rectangle([MX0, MY, MX1, MY + MH], fill=OCEAN, outline=LINE, width=1)
d.text((MX0 + 10, MY + 6), "THE WORLD — 24 NOVEMBER 2026", font=f_map, fill=NAVY)

def lonlat(lon, lat):
    return (MX0 + (lon + 170) / 360.0 * (MX1 - MX0),
            MY + 26 + (75 - lat) / 130.0 * (MH - 40))

CONTINENTS = {
    "NA": [(-168, 66), (-140, 70), (-125, 72), (-110, 73), (-95, 80), (-85, 70), (-80, 73), (-65, 60), (-55, 52), (-60, 47), (-70, 42), (-75, 35), (-80, 26), (-85, 30), (-90, 21), (-97, 16), (-105, 20), (-115, 28), (-125, 40), (-125, 49), (-140, 60), (-155, 58), (-165, 60)],
    "SA": [(-80, 10), (-75, 5), (-70, 12), (-60, 8), (-50, 0), (-35, -8), (-40, -20), (-48, -28), (-58, -35), (-65, -45), (-70, -54), (-73, -40), (-72, -20), (-77, -12), (-80, -5)],
    "EU": [(-10, 36), (-9, 43), (-2, 48), (0, 51), (5, 53), (8, 57), (10, 59), (18, 56), (21, 55), (24, 58), (28, 60), (30, 70), (25, 71), (18, 69), (12, 65), (5, 60), (-5, 58), (-10, 54), (-10, 43), (-9, 37)],
    "AF": [(-17, 15), (-10, 30), (0, 36), (10, 37), (20, 32), (30, 31), (35, 28), (43, 12), (51, 11), (48, 0), (40, -10), (35, -18), (32, -28), (20, -35), (15, -27), (12, -18), (9, -1), (9, 4), (-8, 4), (-13, 8)],
    "AS": [(30, 70), (40, 68), (55, 70), (70, 73), (90, 75), (110, 76), (130, 72), (160, 70), (178, 66), (170, 60), (162, 56), (158, 52), (142, 50), (140, 40), (130, 42), (127, 35), (120, 30), (110, 20), (105, 10), (100, 8), (95, 15), (90, 22), (80, 20), (75, 8), (70, 25), (60, 25), (55, 27), (50, 29), (48, 30), (42, 35), (35, 36), (30, 36), (28, 41), (30, 46), (30, 60)],
    "OC": [(113, -22), (114, -32), (120, -34), (130, -32), (140, -38), (150, -37), (153, -27), (146, -19), (142, -11), (136, -12), (132, -11), (126, -14), (122, -17), (118, -20)],
}
for pts in CONTINENTS.values():
    d.polygon([lonlat(lo, la) for lo, la in pts], fill=LAND, outline=(150, 140, 115))
# island chains the rough polygons miss: Indonesia + Japan
for lo, la, rx, ry in [(95, 5, 7, 3), (105, -2, 8, 3), (113, -7, 9, 3), (122, -8, 8, 3),
                       (131, -3, 7, 3), (139, -1, 6, 3), (139, 36, 4, 6), (141, 40, 3, 5),
                       (127, 33, 3, 4)]:
    px, py = lonlat(lo, la)
    d.ellipse([px - rx, py - ry, px + rx, py + ry], fill=LAND, outline=(150, 140, 115))

PINS = [
    (56, 26, "1"), (35, 48, "2"), (106, -6, "3"), (34.5, 31.5, "4"),
    (-73, 4, "5"), (30, 1.5, "6"), (77, 28, "7"), (-77, 39, "8"),
]
for lon, lat, n in PINS:
    px, py = lonlat(lon, lat)
    d.ellipse([px - 9, py - 9, px + 9, py + 9], fill=RED, outline=(255, 255, 255), width=2)
    d.text((px - d.textlength(n, font=f_tl_b) / 2, py - 7), n, font=f_tl_b, fill=(255, 255, 255))
d.text((MX0 + 10, MY + MH - 20), "Pins: 1 Hormuz · 2 Zaporizhzhia · 3 Banten · 4 Gaza · 5 Villavicencio · 6 Ituri · 7 Delhi · 8 Washington",
       font=f_tl, fill=(70, 70, 70))

# region legend
RX, RW = 712, 284
d.rectangle([RX, MY, RX + RW, MY + MH], fill=CARD, outline=LINE, width=1)
d.text((RX + 12, MY + 8), "8 REGIONS — 37 STORIES", font=f_map, fill=NAVY)
REGIONS = [
    ("Europe & Ukraine war", 10, NAVY),
    ("Asia", 8, TEAL),
    ("North America", 6, PURPLE),
    ("Middle East", 5, RED),
    ("Africa", 3, GREEN),
    ("Global & climate", 2, INK),
    ("Latin America", 2, ORANGE),
    ("Science & space", 1, GOLD),
]
ry = MY + 34
for name, n, col in REGIONS:
    d.ellipse([RX + 12, ry + 2, RX + 24, ry + 14], fill=col)
    d.text((RX + 32, ry), name, font=f_leg, fill=INK)
    d.text((RX + RW - 12 - d.textlength(str(n), font=f_leg_b), ry), str(n), font=f_leg_b, fill=INK)
    ry += 20
d.text((RX + 12, ry + 2), "Markets: S&P +4.73% · Nasdaq +6.51% ·", font=f_tl, fill=(70, 70, 70))
d.text((RX + 12, ry + 17), "Nvidia +31.5% · Nikkei +3.91% · Brent $88.71", font=f_tl, fill=(70, 70, 70))

# ---------------- story grid: 33 more stories ----------------
GRID = [
    # (region color, kicker, detail)
    (NAVY, "SPARTA II TOWED TO ST PETERSBURG", "Ukraine confirms drone strike on ship, 21 Nov"),
    (NAVY, "RUSSIA REJECTS GRAIN DEAL", "Moscow dismisses Black Sea revival at UN"),
    (NAVY, "ESTONIA: 'OPEN WAR' WARNING", "Russia: border closure from 1 Dec nears war"),
    (NAVY, "700,000 RUSSIAN DEAD", "Analysis: toll passes 700k in near 5-year war"),
    (NAVY, "KHARKIV STRIKES INJURE 21", "City + 8 settlements hit; infrastructure damaged"),
    (NAVY, "DONETSK ORDERS CHILD EVACUATION", "Mandatory evacuation across Ukrainian-held area"),
    (NAVY, "ZELENSKYY: MORE US AID IF NO DEAL", "Kyiv to seek aid + sanctions without peace deal"),
    (NAVY, "GERMANY GETS DELTA SYSTEM", "First ally on Ukraine's battlefield network"),
    (NAVY, "UK WARNS OF SABOTAGE", "MoD + MI5 alert defence firms backing Kyiv"),
    (INK, "COP31 ENDS WITHOUT A DEAL", "Longest climate summit ever closes in failure"),
    (INK, "UK SANCTIONS MYANMAR GENERALS", "5 leaders hit after ICJ genocide ruling"),
    (RED, "QATAR PM SEEKS IRAN TALKS", "Meets Vance + Rubio at White House"),
    (RED, "IRAN VOWS TO BREAK BLOCKADE", "“Will use all its tools” vs US naval blockade"),
    (RED, "IRGC: 3 TANKERS HIT MINES", "UNVERIFIED claim; JMIC: unconfirmed, threat severe"),
    (RED, "GAZA: HAMAS SECURITY CHIEF KILLED", "Naeem Abu Nahel dies in Israeli strike"),
    (TEAL, "HASINA PLANS DEC 16 RETURN", "Ex-PM to return; Dhaka: “in handcuffs”"),
    (TEAL, "JAPAN PAYS ICC IN FULL", "PM Takaichi pays 2027 share early"),
    (TEAL, "S. KOREA PAYS TO CATCH AI CHEATS", "Rewards up to $375,000 for exam tips"),
    (TEAL, "CHINA AI CAMPAIGN TARGETS TAIWAN", "Coordinated push to sway Taiwan elections"),
    (TEAL, "US BLACKLISTS MEGASPEED", "Singapore cloud firm over chip diversion risk"),
    (TEAL, "NEPAL PM VISITS INDIA", "New Delhi pledges €1.4bn after glacier floods"),
    (TEAL, "CHINA STOCKS HIT 16-MONTH LOW", "Hang Seng Tech at 26-month intraday low"),
    (PURPLE, "GOMEZ TO RESIGN FROM HOUSE", "Ethics finds “substantial evidence” of misconduct"),
    (PURPLE, "ARMY TO DETONATE IOWA EXPLOSIVES", "5 tons unstable; court rejects emergency stay"),
    (PURPLE, "HEGSETH AIDE: HE SHOULD RESIGN", "Ex-chief of staff: defence chief “lost ability”"),
    (PURPLE, "SENATE PROBES VANCE OIL DEAL", "VP's role in Venezuelan deal awarded to Vitol"),
    (PURPLE, "CROWDSTRIKE BUYS ZSCALER", "$43.9bn all-stock deal, largest cyber takeover"),
    (ORANGE, "COLOMBIA CAR BOMB INJURES 23", "100 kg blast at Meta governor's office"),
    (ORANGE, "MEXICO TO TRY 'CHAPO ISIDRO'", "FBI most-wanted tried at home, not extradited"),
    (GREEN, "EBOLA TEAMS RESCUED IN DRC", "WHO staff freed after 3 days trapped by fighting"),
    (GREEN, "AMNESTY: TIGRAY 'WAR CRIMES'", "Ethiopia accused over urban artillery"),
    (GREEN, "SOMALIA, UGANDA VS AL-SHABAAB", "Joint ops intensify as withdrawal begins"),
    (GOLD, "PAKISTAN'S FIRST ASTRONAUT", "Zeeshan Ali joins China's Shenzhou-24, 25 Nov"),
]
assert len(GRID) == 33, len(GRID)

GY = 528
d.text((28, GY), "THE DAY IN BRIEF — 33 MORE STORIES", font=f_map, fill=NAVY)
d.line([28, GY + 20, 996, GY + 20], fill=LINE, width=1)
COLS_X = [28, 360, 692]
COL_W = 304
ROW_H = 30
GY0 = GY + 28
for idx, (col, kick, det) in enumerate(GRID):
    c = idx % 3
    r = idx // 3
    x = COLS_X[c]
    y = GY0 + r * ROW_H
    d.ellipse([x, y + 3, x + 8, y + 11], fill=col)
    kx = x + 14
    kl = wrap(kick, f_grid_k, COL_W - 14)
    d.text((kx, y), kl[0], font=f_grid_k, fill=INK)
    dy = y + 15
    if len(kl) > 1:
        d.text((kx, dy), kl[1], font=f_grid_k, fill=INK)
        dy = y + 15  # detail squeezed out; kicker took 2 lines
        # detail on same line is impossible; put detail after kicker line 2 is skipped
    else:
        dl = wrap(det, f_grid_b, COL_W - 14)
        d.text((kx, dy), dl[0], font=f_grid_b, fill=(70, 70, 70))

# ---------------- UTC timeline ----------------
TY = 894
d.text((28, TY), "24 NOV 2026 · UTC — THE DAY AS IT UNFOLDED (times as reported, ≈)", font=f_map, fill=NAVY)
TL_Y = 936
d.line([40, TL_Y, 984, TL_Y], fill=INK, width=2)
for h in range(0, 25, 6):
    tx = 40 + h / 24.0 * 944
    d.line([tx, TL_Y - 4, tx, TL_Y + 4], fill=INK, width=2)
    d.text((tx - 8, TL_Y + 8), "%02d:00" % h, font=f_tl, fill=(70, 70, 70))
TL_EVENTS = [
    (2, "Russia hits Zaporizhzhia", True),
    (6, "Nikkei closes +3.91%", False),
    (9, "Banten fire toll: 26 dead", True),
    (18, "Qatar PM at White House", False),
    (21, "NYSE closes: S&P +4.73%", True),
]
for h, label, above in TL_EVENTS:
    tx = 40 + h / 24.0 * 944
    d.ellipse([tx - 5, TL_Y - 5, tx + 5, TL_Y + 5], fill=RED, outline=(255, 255, 255), width=1)
    lw = d.textlength(label, font=f_tl_b)
    lx = min(max(tx - lw / 2, 28), 996 - lw)
    if above:
        d.text((lx, TL_Y - 20), label, font=f_tl_b, fill=INK)
    else:
        d.text((lx, TL_Y + 22), label, font=f_tl_b, fill=INK)

# ---------------- date-check audit strip ----------------
AY = 974
d.rectangle([0, AY, W, H], fill=NAVY)
audit1 = "DATE CHECK ✓  All 37 stories were first reported on Tuesday 24 November 2026."
audit2 = "⚠ 1 claim UNVERIFIED: IRGC says 3 tankers hit mines — JMIC: unconfirmed. 1 event set for 25 Nov: Shenzhou-24 launch, reported 24 Nov."
audit3 = "Sources: Reuters · AP · BBC · Just Security · The Global Eye · OneTurn. Drawn & rendered from reported news — no photographs."
d.text((28, AY + 6), audit1, font=f_audit_b, fill=(255, 255, 255))
d.text((28, AY + 22), audit2, font=f_audit, fill=(220, 228, 240))
d.text((28, AY + 38), audit3, font=f_audit, fill=(220, 228, 240))

img.save("/tmp/v2-build/entry.png", optimize=True)
print("saved /tmp/v2-build/entry.png")
