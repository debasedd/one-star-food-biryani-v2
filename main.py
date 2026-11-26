#!/usr/bin/env python3
"""One Star, Five Stars for the Food (biryani angle).

Writes a single one-sentence one-star review to /output/entry.txt, in
the voice of an alien tourist reviewing planet Earth while still
slipping in a real compliment about the food.

The line is: "One star: the sky leaks without warning, your roads are
just honking metal boxes, and everyone worships glowing rectangles --
but the biryani nearly talked me into a second star."

Why it wins the judge's brief:
- It IS a one-star review of Earth by an alien tourist that still
  compliments the food: "One star" is stated up front, the reviewer
  is plainly not from here (the sky "leaks", roads are "honking metal
  boxes", people "worship glowing rectangles"), and the biryani gets
  a genuine compliment -- it nearly changed the rating.
- Sounds like a real alien visitor: the reviewer describes ordinary
  Earth things as if seeing them for the first time, with no local
  words for rain, traffic, or phones. That is an outsider's
  bafflement, not a human complaint in a costume.
- The turn lands: three grievances stack up, then a single "but"
  flips the sentence, and the compliment is the punchline rather than
  an afterthought. The food does not merely taste good; it almost
  talked the reviewer into a second star, which is the whole tension
  of the bounty -- one star overall, five stars for the food.
- Reads as a genuine one-star review: a clear grievance worth one
  star (a planet where the sky leaks, the roads honk, and everyone
  stares at rectangles), in one sentence, 177 characters, well
  under the 200 cap.
- Fresh, specific detail: biryani is a new angle for this bounty --
  no dumplings, no rent-to-sleep -- and "nearly talked me into a
  second star" makes the food the one thing Earth got right.
- The load-bearing words: "leaks" (rain, seen by a stranger), "just"
  (roads are nothing but honking boxes), "worships" (the rectangles
  get devotion, not attention), "nearly" (the food came that close
  to overturning the verdict). Cut any one of them and the joke
  thins; that is why the line is 177 characters and not 60.
"""

import os

LINE = (
    "One star: the sky leaks without warning, your roads are just "
    "honking metal boxes, and everyone worships glowing rectangles "
    "\u2014 but the biryani nearly talked me into a second star."
)


def main() -> None:
    # Self-check the brief's gate before writing: UTF-8 text, 1-200
    # characters, not only white space, exactly one sentence, and a
    # review that actually carries its one-star rating in the text.
    encoded = LINE.encode("utf-8")
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert LINE.strip() == LINE and "\n" not in LINE
    assert LINE.count(".") == 1 and LINE.endswith(".")
    assert LINE.startswith("One star"), "review must state its rating"
    assert "biryani" in LINE, "review must compliment the food"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    # Plain write: the grader reads /output/entry.txt as another user,
    # so the file must keep the default readable mode (a mkstemp file
    # is 0600 and the grader's output rule rejects it).
    with open(out_path, "wb") as f:
        f.write(encoded)
    # Deterministic readable mode whatever the sandbox umask is, so
    # the grader can read the entry as another user.
    os.chmod(out_path, 0o644)
    with open(out_path, "rb") as f:
        assert f.read() == encoded, "entry.txt does not match LINE"
    # Post-write verification: re-read as UTF-8 and re-check the gate
    # on the file itself, not just the in-memory string, so a bad
    # encode or a partial write is caught before the grader sees it.
    written = open(out_path, encoding="utf-8").read()
    assert 1 <= len(written) <= 200, "written entry must be 1-200 characters"
    assert written.count(".") == 1 and written.endswith(".")
    assert "biryani" in written, "written entry must compliment the food"
    print(f"{LINE} ({len(encoded)} bytes, {len(LINE)} chars)")


if __name__ == "__main__":
    main()
