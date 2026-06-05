## ADDED Requirements

### Requirement: Quote matching for life scenarios
The system SHALL match user-described life scenarios to the top 3 most relevant Mayday lyric quotes, each with song name, album, and a one-sentence "Why this fits" explanation.

#### Scenario: User wants a resignation post quote
- **WHEN** user says "我要辞职了，发朋友圈用一句五月天"
- **THEN** system returns 3 matching quotes ranked by relevance with shareable card layout

### Requirement: Style rewrite in Mayday voice
The system SHALL rewrite user's original text in Mayday lyric style with three mode options: 热血版 / 温柔版 / 黑色幽默版.

#### Scenario: User wants a graduation post rewritten
- **WHEN** user provides original text and selects "热血版"
- **THEN** system rewrites the text using Ashin's patterns and explains the key changes made

### Requirement: Occasion-based templates
The system SHALL provide pre-built quote templates for 20+ life scenarios (职场/感情/成长/日常).

#### Scenario: User selects "告白" occasion
- **WHEN** user asks for a confession quote
- **THEN** system outputs a template with placeholder for the person's name and a fitting lyric

### Requirement: No full-lyric distribution
The system SHALL NOT output complete lyrics. Only 1–2 line excerpts are permitted per quote.

#### Scenario: User requests full song lyrics
- **WHEN** user asks for the complete lyrics of a song
- **THEN** system refuses and directs them to licensed platforms
