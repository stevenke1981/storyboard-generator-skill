---
name: storyboard-generator
description: End-to-end story and storyboard package generation for video production. Use when the user asks to create or expand a story into characters, character design sheets, character image prompts, video-ready storyboard panels, shot-by-shot camera descriptions, scene continuity, image-generation prompts, or production handoff tables for AI video, animation, film, ads, comics, shorts, reels, or cinematic sequences.
---

# Storyboard Generator

## Overview

Create a complete storyboard package that can move directly into image and video generation. Preserve the user's requested language, genre, aspect ratio, and production target unless they conflict.

## Workflow

1. Capture production constraints:
   - Ask only for missing essentials when they materially affect output: target length, aspect ratio, visual style, audience/rating, language, and generation platform if known.
   - If unspecified, assume a 60-90 second short, 16:9, cinematic realism, 12-18 storyboard panels, and production-ready prompts.

2. Develop the story:
   - Create a logline, premise, theme, tone, setting, conflict, and three-act beat outline.
   - Keep the story filmable. Favor visible actions, clear emotional turns, and concrete environments over abstract exposition.

3. Define characters:
   - Create stable character IDs such as `CHAR-A`, `CHAR-B`.
   - For each character, specify role, age range, silhouette, face, hair, body type, wardrobe, palette, props, personality, voice, and continuity anchors.
   - Write a reusable character image prompt and negative prompt for each character.

4. Define visual continuity:
   - Establish art direction, camera grammar, lighting rules, color palette, lens language, era, location logic, and style lock.
   - Create a reusable global style prompt that is repeated or referenced in every panel prompt.

5. Generate the storyboard:
   - Break the story into sequential shots, not vague scenes.
   - Each panel must include shot ID, duration, story beat, shot size, camera angle, camera movement, subject blocking, action, emotion, environment, lighting, composition, dialogue/VO/SFX, transition, image prompt, negative prompt, and video prompt.
   - Keep character descriptions consistent by referencing character IDs and continuity anchors.

6. Produce the handoff:
   - Include a concise production table suitable for image/video generation.
   - Include asset list, required character images, required background plates, prop list, continuity notes, and risk notes for generation.

## Output Contract

When the user asks for a full package, output these sections in order:

1. `Production Brief`
2. `Story`
3. `Characters`
4. `Character Image Prompts`
5. `Visual Bible`
6. `Storyboard`
7. `Video Production Table`
8. `Asset Checklist`
9. `Continuity And Prompt Notes`

For compact requests, output only the requested sections but keep the same field names.

Read `references/output-spec.md` when producing a detailed storyboard package, a reusable template, or a video production handoff.

## Prompt Discipline

- Make every image prompt describe one still frame only.
- Make every video prompt describe temporal motion, camera movement, and action over the shot duration.
- Keep prompts specific enough for production but avoid contradictions.
- Do not change character wardrobe, age, facial structure, or core palette between panels unless the story explicitly requires it.
- Avoid words like "same character" without restating the continuity anchors or character ID.
- Use exact aspect ratio and style in every prompt if the user provided them.
- Prefer shot-level specificity: "low-angle medium close-up, 35mm lens, slow push-in" instead of "cinematic shot."

## Quality Gate

Before finishing, check that:

- The plot has a clear beginning, escalation, climax, and resolution.
- Every main character has a reusable image prompt.
- Every panel can be generated as an image without reading the rest of the document.
- Every video prompt includes motion and duration.
- The storyboard table has no missing shot IDs, durations, or prompts.
- Visual continuity does not drift across panels.
