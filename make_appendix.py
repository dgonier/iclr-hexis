#!/usr/bin/env python3
"""Generate sections_instrument_appendix.tex from sections_instrument/appendix.tex.

Drops three peripheral subsections from the submission build and emits their
labels into a single stub subsection so no cross-reference dangles.
Edit sections_instrument/appendix.tex; never edit the generated file.
"""
import re
from pathlib import Path

HERE = Path(__file__).parent
SRC = HERE / "sections_instrument" / "appendix.tex"
DST = HERE / "sections_instrument_appendix.tex"

DROP = [
    "Numeric-credence negative result",
    "Probe decodability",
    "Dead ends",
]

text = SRC.read_text()

# Split into (subsection title, body) chunks, keeping any preamble before the first.
parts = re.split(r"(?m)^(\\subsection\{)", text)
head = parts[0]
chunks = []
for i in range(1, len(parts), 2):
    chunks.append(parts[i] + parts[i + 1])

kept, dropped_labels, dropped_titles = [], [], []
for chunk in chunks:
    title = re.match(r"\\subsection\{(.*?)\}", chunk, re.S).group(1)
    if title in DROP:
        dropped_titles.append(title)
        dropped_labels += re.findall(r"\\label\{([^}]*)\}", chunk)
    else:
        kept.append(chunk)

if len(dropped_titles) != len(DROP):
    missing = set(DROP) - set(dropped_titles)
    raise SystemExit(f"ERROR: subsections not found in source: {missing}")

stub = (
    "\n\\subsection{Peripheral material omitted in this version}\n"
    "\\label{app:omitted}\n"
    "Omitted here: " + "; ".join(dropped_titles) + ".\n"
    + "".join(f"\\phantomsection\\label{{{l}}}%\n"
              for l in dropped_labels if l != "app:omitted")
)

DST.write_text(head + "".join(kept).rstrip() + "\n\n" + stub)
print(f"wrote {DST.name}: kept {len(kept)} subsections, "
      f"dropped {len(dropped_titles)}, rehomed {len(dropped_labels)} labels")
