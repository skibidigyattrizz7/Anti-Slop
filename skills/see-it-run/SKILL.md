---
name: see-it-run
description: Use when a page, app or game has just been built or changed and nobody has looked at the real result yet, before saying it is done. Also use when the user says "check how it looks", "take a screenshot", "does it work on phone", "test it" or "did you actually run it". Works for anything that opens in a browser.
---

# See it run

Code that reads correctly can still render a blank page, scroll sideways on a phone or throw on the first click. People who build things look at the result before they call it finished. Do the same.

## Top rules

1. **Open the real thing before you report on it.** A page, a build, a running game. Reading the code is a different check.
2. **Look at two sizes.** 375 px wide (phone) and 1280 px wide (desktop). Look at each screenshot you take.
3. **Do the main task once as a new user.** Start to finish. Note every place you had to stop and think.
4. **Try the hard states.** Empty, loading, an error, very long text, keyboard only (Tab, Enter, Escape).
5. **Read the console.** An error there is a problem even when the page looks fine.
6. **Say what you saw and what you did not.** "Checked phone and desktop, did not test sign-in" is a full report. "Should work" is a guess.

## Never

- Say something works when you have not opened it. Say "not run" in place of that.
- Type real passwords, payment details or personal data into a page you are testing.
- Buy, send, post or delete anything outside the app under test.

## How to look

| You have | Do |
|---|---|
| A browser tool (Playwright, Chrome DevTools, a browser extension) | Use it directly |
| Node and Playwright | `node scripts/shoot.cjs <url-or-file> --out shots/` |
| A desktop app and a computer-use tool | Use that tool, inside the app only |
| None of these | Tell the user it was not checked and ask for a screenshot |

`scripts/shoot.cjs` saves `phone.png` and `desktop.png` and prints a JSON report: console errors, failed requests, sideways scroll, tap targets under 24 px, images with no alt text. Exit code 1 means it found problems. It cannot tell you whether the page looks good. Open the screenshots for that.

For a deeper pass, hand the job to the `viewer` agent if it is installed.

## Before and after

**Before:** "I've updated the navbar. It should now be responsive."

**After:** "Opened it at 375 px and 1280 px. The menu button works on phone. The logo overlaps the search box between 600 and 720 px, so I fixed the breakpoint and checked again. Did not test the logged-in menu."

## Final check

- Did you open it, at two sizes?
- Did you finish the main task once?
- Does your report say what you did not check?
