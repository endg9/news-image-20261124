#!/usr/bin/env python3
"""Render the news-image-20261124 front page (1024x1024 PNG) from stories.json.

Fresh code, written 24 Nov 2026 for this edition only. Deterministic: no
timestamps, no randomness, no network. Usage: python3 render.py [out.png]

Layout: masthead, lead + Asia markets row, 3x2 story grid, MORE FROM TODAY
briefs band, TONIGHT strip, DATE CHECK box, footer.
"""
import json
import sys
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (248, 244, 232)
PANEL = (255, 253, 246)
INK = (22, 22, 22)
MUTED = (90, 86, 76)
RED = (168, 30, 34)
BLUE = (23, 74, 124)
RULE = (22, 22, 22)
LIGHT = (214, 206, 188)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS_O = "/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns list of lines that fit max_w."""
    lines, cur = [], ""
    for word in text.split():
        trial = f"{cur} {word}".strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def fit_lines(draw, text, fnt, max_w, max_lines):
    """Wrap and clip to max_lines, adding an ellipsis on the last line."""
    lines = wrap(draw, text, fnt, max_w)
    if len(lines) <= max_lines:
        return lines
    lines = lines[:max_lines]
    last = lines[-1]
    while last and draw.textlength(last + " …", font=fnt) > max_w:
        last = last.rsplit(" ", 1)[0] if " " in last else last[:-1]
    lines[-1] = last + " …"
    return lines


def draw_numbers(draw, nums, x, y, w, value_size=30, box_h=64, boxed=True):
    """Draw big index numerals in a row of boxes (or bare, if boxed=False)."""
    n = len(nums)
    gap = 10
    bw = (w - gap * (n - 1)) // n
    vf = font(SANS_B, value_size)
    lf = font(SANS_B, 12)
    nf = font(SANS, 11)
    for i, num in enumerate(nums):
        bx = x + i * (bw + gap)
        if boxed:
            draw.rounded_rectangle([bx, y, bx + bw, y + box_h], radius=4,
                                   outline=RULE, width=1, fill=PANEL)
        vw = draw.textlength(num["value"], font=vf)
        draw.text((bx + (bw - vw) / 2, y + 2), num["value"], font=vf, fill=RED)
        if not boxed:
            sub = num["label"] + ("  ·  " + num["note"] if num.get("note") else "")
            sw = draw.textlength(sub, font=nf)
            draw.text((bx + (bw - sw) / 2, y + value_size + 8), sub,
                      font=nf, fill=MUTED)
            continue
        if box_h <= 48:
            # compact: label + level on one line under the value
            sub = num["label"] + ("  " + num["note"] if num.get("note") else "")
            sub = fit_lines(draw, sub, nf, bw - 6, 1)[0]
            sw = draw.textlength(sub, font=nf)
            draw.text((bx + (bw - sw) / 2, y + box_h - 16), sub,
                      font=nf, fill=INK)
        else:
            lw = draw.textlength(num["label"], font=lf)
            draw.text((bx + (bw - lw) / 2, y + box_h - 28), num["label"],
                      font=lf, fill=INK)
            if num.get("note"):
                nw = draw.textlength(num["note"], font=nf)
                draw.text((bx + (bw - nw) / 2, y + box_h - 14), num["note"],
                          font=nf, fill=MUTED)


def draw_card(draw, s, x, y, w, h):
    draw.rounded_rectangle([x, y, x + w, y + h], radius=4,
                           outline=RULE, width=1, fill=PANEL)
    tf = font(SANS_B, 12)
    hf = font(SERIF_B, 19)
    bf = font(SANS, 13)
    sf = font(SANS_O, 11)
    pad = 12
    draw.text((x + pad, y + 8), s["tag"], font=tf, fill=RED)
    head = fit_lines(draw, s["headline"], hf, w - 2 * pad, 2)
    hy = y + 28
    for ln in head:
        draw.text((x + pad, hy), ln, font=hf, fill=INK)
        hy += 23
    body = fit_lines(draw, s["body"], bf, w - 2 * pad, 3)
    by = hy + 4
    for ln in body:
        draw.text((x + pad, by), ln, font=bf, fill=INK)
        by += 16
    src = fit_lines(draw, s["source"], sf, w - 2 * pad, 1)[0]
    draw.text((x + pad, y + h - 16), src, font=sf, fill=MUTED)


def main():
    with open("stories.json", encoding="utf-8") as fh:
        data = json.load(fh)
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    d.rectangle([14, 14, W - 15, H - 15], outline=RULE, width=2)
    d.rectangle([20, 20, W - 21, H - 21], outline=RULE, width=1)

    # ---- Masthead: 26..150 ----
    title_f = font(SERIF_B, 54)
    tw = d.textlength(data["title"], font=title_f)
    d.text(((W - tw) / 2, 30), data["title"], font=title_f, fill=INK)
    sub_f = font(SANS, 16)
    sw = d.textlength(data["subtitle"], font=sub_f)
    d.text(((W - sw) / 2, 94), data["subtitle"], font=sub_f, fill=MUTED)
    d.line([(26, 120), (W - 26, 120)], fill=RULE, width=2)
    date_f = font(SANS_B, 15)
    left = data["day"].upper()
    right = "24 NOVEMBER 2026  •  ONE DAY  •  ONE IMAGE"
    d.text((28, 128), left, font=date_f, fill=INK)
    rw = d.textlength(right, font=date_f)
    d.text((W - 28 - rw, 128), right, font=date_f, fill=INK)
    d.line([(26, 150), (W - 26, 150)], fill=RULE, width=1)

    # ---- Lead (left) + Asia (right): 162..348 ----
    lead = data["lead"]
    asia = data["asia"]
    lx, ly, lw = 26, 162, 622
    ax, aw = 664, 334
    row_h = 186
    d.rectangle([lx, ly, lx + lw, ly + row_h], outline=RULE, width=1, fill=PANEL)
    d.rectangle([ax, ly, ax + aw, ly + row_h], outline=RULE, width=1, fill=PANEL)
    tag_f = font(SANS_B, 13)
    sf = font(SANS_O, 11)
    # lead
    d.text((lx + 14, ly + 10), lead["tag"], font=tag_f, fill=RED)
    lh_f = font(SERIF_B, 38)
    while d.textlength(lead["headline"], font=lh_f) > lw - 28 and lh_f.size > 24:
        lh_f = font(SERIF_B, lh_f.size - 1)
    d.text((lx + 14, ly + 32), lead["headline"], font=lh_f, fill=INK)
    lb_f = font(SANS, 16)
    body = fit_lines(d, lead["body"], lb_f, lw - 28, 2)
    by = ly + 80
    for ln in body:
        d.text((lx + 14, by), ln, font=lb_f, fill=INK)
        by += 21
    draw_numbers(d, lead["numbers"], lx + 14, ly + 124, lw - 28,
                 value_size=28, boxed=False)
    d.text((lx + 14, ly + row_h - 14), lead["source"], font=sf, fill=MUTED)
    # asia
    d.text((ax + 14, ly + 10), asia["tag"], font=tag_f, fill=BLUE)
    ah_f = font(SERIF_B, 22)
    ahead = fit_lines(d, asia["headline"], ah_f, aw - 28, 1)
    d.text((ax + 14, ly + 32), ahead[0], font=ah_f, fill=INK)
    ab_f = font(SANS, 14)
    abody = fit_lines(d, asia["body"], ab_f, aw - 28, 1)
    d.text((ax + 14, ly + 60), abody[0] if abody else "", font=ab_f, fill=INK)
    draw_numbers(d, asia["numbers"][:2], ax + 14, ly + 84, aw - 28,
                 value_size=19, box_h=40)
    draw_numbers(d, asia["numbers"][2:], ax + 14, ly + 128, aw - 28,
                 value_size=19, box_h=40)
    d.text((ax + 14, ly + row_h - 14), asia["source"], font=sf, fill=MUTED)

    # ---- Story grid: 3 cols x 2 rows, 360..652 ----
    gx, gy = 26, 360
    gw, gh, gap = 316, 140, 12
    for i, s in enumerate(data["stories"]):
        cx = gx + (i % 3) * (gw + gap)
        cy = gy + (i // 3) * (gh + gap)
        draw_card(d, s, cx, cy, gw, gh)

    # ---- MORE FROM TODAY briefs: 664..748 ----
    briefs = data.get("briefs", [])
    by0 = 664
    d.rectangle([26, by0, W - 26, by0 + 84], outline=RULE, width=1, fill=PANEL)
    bt_f = font(SANS_B, 13)
    d.text((40, by0 + 6), "MORE FROM TODAY", font=bt_f, fill=RED)
    bb_f = font(SANS, 13)
    rows = (len(briefs) + 1) // 2
    for i, b in enumerate(briefs):
        col = i % 2
        row = i // 2
        bx = 40 + col * 480
        by = by0 + 26 + row * 14
        line = fit_lines(d, "•  " + b["headline"], bb_f, 460, 1)[0]
        d.text((bx, by), line, font=bb_f, fill=INK)

    # ---- Tonight strip: 760..820 ----
    t = data["tonight"]
    ty = 760
    d.rectangle([26, ty, W - 26, ty + 60], outline=RULE, width=1, fill=BLUE)
    tf = font(SANS_B, 13)
    d.text((40, ty + 6), t["tag"], font=tf, fill=(255, 214, 120))
    th_f = font(SERIF_B, 20)
    d.text((40, ty + 23), t["headline"], font=th_f, fill=(255, 255, 255))
    tb_f = font(SANS, 13)
    tbody = fit_lines(d, t["body"], tb_f, W - 80, 1)
    d.text((40, ty + 45), tbody[0] if tbody else "", font=tb_f,
           fill=(220, 228, 240))

    # ---- DATE CHECK box: 832..948 ----
    dy = 832
    d.rectangle([26, dy, W - 26, dy + 116], outline=RED, width=2, fill=PANEL)
    dc_f = font(SANS_B, 15)
    d.text((40, dy + 8), "DATE CHECK — DELIBERATELY EXCLUDED", font=dc_f, fill=RED)
    di_f = font(SANS, 13)
    items = data["date_check"]
    half = (len(items) + 1) // 2
    for col in range(2):
        cx = 40 + col * 480
        for j, item in enumerate(items[col * half:(col + 1) * half]):
            d.text((cx, dy + 30 + j * 14), "✕  " + item, font=di_f, fill=INK)

    # ---- Footer ----
    ff = font(SANS, 12)
    ft = data["footer"]
    fw = d.textlength(ft, font=ff)
    d.text(((W - fw) / 2, 958), ft, font=ff, fill=MUTED)
    d.line([(26, 980), (W - 26, 980)], fill=LIGHT, width=1)
    fin_f = font(SANS_B, 12)
    fin = "THE WORLD IN ONE DAY  •  TUESDAY 24 NOVEMBER 2026"
    fw2 = d.textlength(fin, font=fin_f)
    d.text(((W - fw2) / 2, 988), fin, font=fin_f, fill=INK)

    out = sys.argv[1] if len(sys.argv) > 1 else "entry.png"
    img.save(out, "PNG")
    print(f"wrote {out} {W}x{H}")


if __name__ == "__main__":
    main()
