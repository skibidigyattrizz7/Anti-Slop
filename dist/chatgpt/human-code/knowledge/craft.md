# Code craft by sub-area

Skilled engineers optimize for the next reader and the smallest correct change. Know the code well enough to explain every line without the tool.

## Before you write

- Grep the project for the thing you are about to build. Read two neighbors for naming, error style and imports.
- Prefer the standard library and installed dependencies. Add a package only for more than a few lines of work, and check it exists.
- Smallest correct change. Deleting beats adding.

## Names

Name by what the thing is in this program: `studentGrades`, `jumpBufferTime`, `rewardSurvivors`. A good name is long enough to say what the item is or does. Test: could a reader skip the body?

## Comments

Say why: intent, a constraint, a gotcha, a bug link.
Good: `-- Mobile caps emitters at 100/s, so we fake density with bigger particles.`
Delete comments that repeat the line, banner comments, and a docstring that only echoes the signature.

## Errors

- Handle where you can act: retry, fall back, ask the user.
- Otherwise raise or return an error that names what failed and with which input.
- Catch the specific exception. Log with context, then re-raise or exit non-zero.
- Validate at trust boundaries (input, network, files, external APIs). Inside, trust your types.

## Structure

- One job per function. Split on a real seam, not by line count.
- Early return or a lookup table beats a long if/elif ladder.
- No config, flag or class for a use that does not exist yet. Mark known limits: `shortcut: <limit>, <when to upgrade>`.
- Delete dead code.

## Tests and running

- Run the tests, or the code on a real input, after every fix. If you cannot run it, trace one case by hand and say so.
- A new test must be able to fail. Break the code once and watch it fail.
- Use real-looking values (`invoice 4121`), not `foo`/`bar`.

## Security

No secrets in source: read them from env or a secrets store. Parameterize queries, encode output, check auth on the server. Veracode (2026) found models miss XSS and log injection most often, so look there first.

## README

What it is, how to run it (a command that works), one non-obvious thing, what is not done. No badge wall, no emoji headings.

## Commits and PRs

- Commit: imperative, specific. "Fix double reward when player rejoins", not "Improve reward system logic".
- PR: why the change, what you tested and how, what you did not test, what risk remains. One purpose per PR. Do not paste a summary of the diff.
- Say what you could not reproduce. Never report or claim a bug you did not run.

## Longer before and after (Luau, Roblox)

**Before:**
```lua
-- Function to handle the data
local function processData(data)
    -- Check if data exists
    if data ~= nil then
        local success, result = pcall(function()
            -- Loop through the data
            for i, item in ipairs(data) do
                item.Value = item.Value + 1 -- Increment value
            end
        end)
        if not success then
            print("An error occurred")
        end
    end
end
```

**After:**
```lua
-- Coins tick up once per round survived; spectators don't earn.
local function rewardSurvivors(players)
    for _, player in players do
        if not player:GetAttribute("Spectating") then
            player.leaderstats.Coins.Value += 1
        end
    end
end
```

What changed: a name from the game's world, one comment that states a rule, no fake error handling, no nil check on a value the caller owns.
