# Storyboard Output Specification

Use this reference for full storyboard packages and production handoffs.

## Production Brief

Include:

- Title
- Format, target duration, aspect ratio, language
- Genre, tone, audience/rating
- Visual style
- Delivery target, such as AI video, animation, live action, ad, short, reel
- Assumptions made

## Story

Include:

- Logline: one sentence
- Premise: one short paragraph
- Theme: one sentence
- Three-act beat outline:
  - Act 1 setup
  - Act 2 escalation
  - Act 3 resolution
- Full short story treatment: concise, filmable, visual

## Characters

For each character:

- Character ID
- Name
- Role in story
- Age range
- Personality and motivation
- Physical design
- Wardrobe and color palette
- Props or symbols
- Voice/dialogue style
- Continuity anchors that must not change

## Character Image Prompts

For each character:

- Character ID
- Front-view design prompt
- Optional side/back-view prompt if useful
- Expression sheet prompt if useful
- Negative prompt

Write prompts as reusable production assets. They should not depend on the plot context.

## Visual Bible

Include:

- Global visual style prompt
- Camera language
- Lighting rules
- Color palette
- Texture/material references
- Environment rules
- Aspect ratio and framing rules
- Negative prompt shared by all images

## Storyboard

For each panel, use this schema:

```markdown
### SHOT-001 - Short Title

- Duration: 4s
- Story Beat: What changes in this shot.
- Shot Size: Extreme wide / wide / full / medium / close-up / extreme close-up.
- Camera Angle: Eye level / low angle / high angle / overhead / Dutch angle.
- Lens / Framing: Lens feel and composition.
- Camera Movement: Static / push-in / pull-back / pan / tilt / tracking / handheld.
- Blocking: Character and object placement.
- Action: Visible action during the shot.
- Emotion: Character emotional state.
- Environment: Location and background details.
- Lighting: Light source, contrast, mood.
- Dialogue / VO / SFX: Spoken words, voiceover, sound effects, or silence.
- Transition: Cut, match cut, dissolve, whip pan, fade, etc.
- Image Prompt: A still-frame prompt that can generate this exact panel.
- Video Prompt: A motion prompt for generating the shot as video.
- Negative Prompt: Shot-specific exclusions.
```

## Video Production Table

After the detailed storyboard, include a table with:

| Shot ID | Duration | Shot Type | Camera Motion | Characters | Location | Action | Dialogue/Audio | Image Prompt | Video Prompt |
|---|---:|---|---|---|---|---|---|---|---|

Keep table cells concise enough to be copied into production tools.

## Asset Checklist

Include:

- Character assets
- Background/location plates
- Props
- Text/graphics
- Audio needs
- VFX or motion needs

## Continuity And Prompt Notes

Include:

- Character continuity warnings
- Wardrobe/palette locks
- Environment continuity
- Prompt reuse guidance
- Shots likely to need manual review or regeneration
