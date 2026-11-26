# Senior layer: media

Use for a full project or a senior review. It adds to the other references. Each rule gives the rule, why, a check, and a tag. `[verified: URL]` means the page was opened. `[practice]` is common professional practice: teach it as a rule of thumb, never as a fact or a standard.

## Image direction

- **Value before colour.** Block in 3 to 5 values first. Why: if it reads in grey it reads in colour. Check: desaturate the image; the hero must still separate from the background. `[practice]`
- **One variable per iteration.** Change light, or crop, or palette, never two at once. Why: you cannot learn what worked from a double change. Check: the log names the single change per round. `[practice]`
- **Build a reference board.** 6 to 12 images, each with one line on what you take from it (light, crop, texture). Why: words alone drift to the average. Check: every prompt phrase traces to a board line. `[practice]`
- **Lock palette and light direction in words, then edit.** Use inpaint or edit mode, not a full reroll, once the frame is right. Check: the set shares one light direction. `[practice]`
- **Fix type, hands and small detail by hand.** Check: zoom to 200 percent on each. `[practice]`

## Video

- **Shot list, one purpose per shot.** Columns: number, size, subject, action, move, seconds, purpose (one verb: establish, reveal, react), audio. Why: a shot with no purpose is filler. Check: every row has a purpose, and no two neighbours share size and angle. `[practice]`
- **Rule of Six is a heuristic, not a measurement.** Murch ranks a cut by emotion 51, story 23, rhythm 10, eye trace 7, 2D plane 5, 3D space 4. He calls the weights "slightly tongue-in-cheek". Give up the lowest item first, emotion last. Check: when a cut breaks a rule, say which one and why a higher one won. `[verified: https://stavry.github.io/docs/in-the-blink-of-an-eye.pdf]` Treat the weights as illustrative.
- **Grade in order.** Exposure and white balance, then contrast, then the look (one LUT across clips). Why: a look on a bad base amplifies the error. Check: on scopes, blacks sit near 0 to 5 percent and whites near 90 to 100 percent. `[practice]`
- **Pace for the piece.** Short form: a hook in the first 1 to 3 seconds, a change of picture every 2 to 4 seconds, end on the payoff, not a logo. Check: mute it; the story still reads from pictures. `[practice]`

## Audio

- **Broadcast: EBU R 128.** Programme loudness -23.0 LUFS (tolerance 0.5 LU, 1.0 LU for live), true peak no higher than -1 dBTP. LUFS equals LKFS. Check: a BS.1770 meter reads integrated loudness and true peak. `[verified: https://tech.ebu.ch/docs/r/r128.pdf]`
- **Spotify.** Tracks are normalised to -14 LUFS by default (Loud -11, Quiet -19). Master near -14 LUFS integrated with true peak below -1 dBTP; if the master is louder than -14, keep true peak below -2 dBTP. Check: measure the master, not the preview. `[verified: https://support.spotify.com/us/artists/article/loudness-normalization/]`
- **YouTube.** YouTube publishes no target. Third parties measure about -14 LUFS, with loud uploads turned down and quiet ones left alone. Why it matters: a very quiet upload sounds weak next to others. Check: ship -14 LUFS with true peak at or below -1 dBTP, and say it is a working default. `[practice]`
- **Mix as practice, in order.** Level, pan, EQ (cut before boost), dynamics, space, automation. Compare with a reference at matched loudness, or the louder one wins. Check: listen on a phone speaker and earbuds. `[practice]`
- **Layer sounds.** Impact is a transient plus a body plus a tail; vary pitch a little on repeats; leave silence before a hit; duck music under voice. Check: mute each layer in turn; each must be missed. `[practice]`

## Voice direction

- **Give the line a want and an obstacle**, for example "say it as if you are trying not to wake someone". Mark pauses and stresses. Take three reads at different intensities and pick the one whose pitch moves most. Check: read it aloud before generating; mark where you breathe. `[practice]`

## Build on

Use these when installed. Each has an inline fallback.

- `motion-design` (MIT): 12 principles and duration table. Fallback: ease-out in, ease-in out, 150 to 400 ms for most motion.
- `canvas-design` (Apache-2.0): poster and art philosophy. Fallback: one focal point, three masses.
- `brandkit` (MIT): brand-board prompt structure. Fallback: logo, palette, type, one mockup.
- `animation-forge`: no licence found. Link only; do not copy text.
- Unity skills (Unity Companion License): ideas only; no text copied.

## Credits

No text copied from other skills. Murch, EBU and Spotify figures are quoted from the pages named above.
