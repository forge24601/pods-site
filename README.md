# POD Society website (example build)

Static site for Positive Outreach Development Society, Inc. (POD Society), published by GitHub Pages at
https://forge24601.github.io/pods-site/. POD Society's live site is https://www.podsocietyinc.org/ (Webador); this
build is the proposed replacement, with their content as of October 2026.

## Editing

Pages are written in `src/` (page body only; the first line is a metadata comment with the title, description and
which menu item is current). The shared header, menu and footer are in `tools/build.py`. After editing:

    python3 tools/build.py

writes the finished pages at the repo root. Styles: `css/site.css`. Photos: `images/` (POD Society's own, from their
site and events).

## Pages

index, about, programs, forge, reentry-home, successful-reentry, job-skills, impact, events, resources,
get-involved, contact.

`reentry-home`, `successful-reentry` and `job-skills` are a preview of the planned Reentry Home and the draft FORGE
Successful Reentry program. Anything marked with a yellow highlight (`<span class="tbd">`) is a placeholder still to be
confirmed by POD Society.
