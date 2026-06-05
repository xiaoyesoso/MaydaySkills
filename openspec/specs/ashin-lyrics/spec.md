## ADDED Requirements

### Requirement: Generate original lyrics in Ashin's style
The system SHALL generate original Chinese lyrics that emulate Ashin's (阿信) writing patterns: first-person-plural voice, micro-moment imagery, progressive intensity, and vowel-rich Mandarin rhyme schemes.

#### Scenario: User requests inspirational lyrics about graduation
- **WHEN** user provides topic "graduation" and tone "inspirational"
- **THEN** system generates 3 draft verses, each annotated with rhyme scheme and Ashin pattern used

#### Scenario: User selects a draft to expand
- **WHEN** user selects draft #2 from the 3 options
- **THEN** system expands it into a full lyric sheet with verse/chorus/bridge labels

### Requirement: Tone parameterization
The system SHALL support three tone modes: inspirational (dream/persistence), melancholic (farewell/regret), passionate (youth/freedom/rebellion).

#### Scenario: Melancholic tone selection
- **WHEN** user selects "melancholic" tone
- **THEN** system loads reference samples from lyrics-db matching valence ≤ 4 and generates accordingly

### Requirement: No verbatim output of existing lyrics
The system SHALL NOT output any existing Mayday lyrics verbatim. All generated content MUST be original.

#### Scenario: User asks to reproduce "倔强" lyrics
- **WHEN** user requests verbatim reproduction of an existing song
- **THEN** system refuses and offers to generate original lyrics in a similar style instead
