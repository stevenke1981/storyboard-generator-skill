---
name: storyboard-generator
description: End-to-end story and storyboard package generation for video production, including optional Codex-driven image generation. Use when the user asks to create or expand a story into characters, character design sheets, character/person image prompts, generated character images, generated storyboard panels, video-ready storyboard panels, shot-by-shot camera descriptions, scene continuity, image-generation prompts, or production handoff tables for AI video, animation, film, ads, comics, shorts, reels, or cinematic sequences.
---

# Storyboard Generator

## Overview

Create a complete storyboard package that can move directly into image and video generation. Preserve the user's requested language, genre, aspect ratio, and production target unless they conflict.

This skill has two delivery modes:

- **Prompt-package mode:** write the story, character prompts, storyboard, and production handoff without generating bitmap images.
- **Codex image-generation mode:** when the user asks to create actual character images, person images, storyboard images, panels, keyframes, or visual assets, generate the package first, then call Codex image generation for the requested assets and save them in the project/output folder.

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

6. Generate images when requested:
   - Use Codex image-generation mode if the user asks for `產生圖`, `人物圖`, `角色圖`, `分鏡圖`, `storyboard images`, `panels`, `keyframes`, `character sheets`, `直接生成`, or equivalent wording.
   - Read and follow the `imagegen` skill before generating images. Prefer the built-in `image_gen` tool for normal image generation. Use the CLI `gpt-image-2` path only when the user explicitly asks for `gpt-image-2`, `ChatGPT Image 2`, API/CLI/model-specific control, or after the user confirms a required fallback.
   - Generate character assets first, then storyboard panels. Character assets should include at least one clean front-view design image for each main character before panel generation, unless the user asks only for panels.
   - For many panels, generate a practical subset first unless the user explicitly asks for all panels. Default subset: all main character sheets plus 4 key storyboard panels covering setup, escalation, climax, and resolution. If the user asks for all images, generate all requested images in sequential order.
   - Save generated assets inside the user's requested project/output folder. Use stable filenames such as `characters/CHAR-A-lin-qing-front.png` and `storyboard/SHOT-001.png`. Never leave project-bound assets only in Codex's default generated-images location.
   - Include a manifest table that maps each saved image path to the character ID or shot ID, prompt, negative prompt, and generation mode used.
   - If the image tool is unavailable, still produce the prompts and manifest template, and explicitly state that image generation could not run.

7. Produce the handoff:
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

When Codex image-generation mode is used, also output:

10. `Generated Image Manifest`

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

## Codex Image Generation Rules

- Treat generated images as production assets, not decorative previews.
- Generate in dependency order: global style lock -> character/person sheets -> background plates if needed -> storyboard panels.
- Repeat character continuity anchors directly in every image prompt. Do not rely on "same character" by itself.
- Keep character sheets neutral and reusable: full body, clean background, front view, optional side/back and expression sheet.
- Keep storyboard panel prompts as one still frame only. Do not include temporal action in image prompts; put motion only in video prompts.
- Use 16:9 for storyboard panels unless the user specifies another aspect ratio. Use square or portrait only for character sheets if the user asks or the generation target benefits from it.
- For anime or comic requests, lock style consistently across every generated prompt: line quality, coloring, lighting, character proportions, and background detail.
- For large batches, name assets with zero-padded IDs and write prompts to a prompt bank before generating, so failed or regenerated images can be traced.
- If the user explicitly requests ChatGPT Image 2 / `gpt-image-2`, use the imagegen skill's CLI fallback guidance and require `OPENAI_API_KEY`; otherwise use the built-in `image_gen` tool by default.
- If using built-in `image_gen`, move or copy final selected outputs from Codex's default generated-images location into the project/output folder before finishing.
- Do not overwrite existing generated assets unless the user asks for replacement; create versioned filenames such as `SHOT-001-v2.png`.

## Quality Gate

Before finishing, check that:

- The plot has a clear beginning, escalation, climax, and resolution.
- Every main character has a reusable image prompt.
- Every panel can be generated as an image without reading the rest of the document.
- Every video prompt includes motion and duration.
- The storyboard table has no missing shot IDs, durations, or prompts.
- Visual continuity does not drift across panels.
- If images were requested, all generated file paths exist in the output folder and the manifest maps each file to its prompt.
