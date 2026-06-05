## ADDED Requirements

### Requirement: AI radio program composition
The system SHALL compose a complete Mayday-themed radio program given a theme, duration (30/60/90/120 min), and optional mood arc, including opening monologue, track transitions, and closing remarks.

#### Scenario: User requests a 30-minute breakup healing radio
- **WHEN** user says "给我做一档30分钟的失恋治愈电台"
- **THEN** system generates a program script with 5–7 tracks, DJ monologues between tracks, mood arc from low→medium→healing, and a program overview

### Requirement: Mood arc engine
The system SHALL support customizable mood arcs (e.g., sad→healing, calm→explosive). Default arcs are derived from the selected theme template.

#### Scenario: User selects "演唱会倒计时" theme
- **WHEN** user chooses the concert countdown template
- **THEN** system uses the built-in arc (medium→high→explosive) and selects tracks accordingly

### Requirement: Track selection reuses mayday-mood matching
The system SHALL use the same 3-axis scoring formula as mayday-mood for track selection at each program segment, referencing mood-taxonomy.md.

#### Scenario: Selecting tracks for a mid-program segment
- **WHEN** the mood arc specifies E:5, V:6 for the 3rd segment
- **THEN** system scores all lyrics-db songs against those target values and picks the best match

### Requirement: DJ voice guide
The system SHALL generate all DJ text (monologues, transitions, closings) following a defined voice guide (warm/philosophical/playful/nostalgic) per dj-voice.md.

#### Scenario: DJ text for a late-night healing program
- **WHEN** theme is "深夜疗愈" with dj_style "warm"
- **THEN** system generates gentle, contemplative DJ text that matches the healing mood

### Requirement: Skip list support
The system SHALL allow users to exclude specific songs from the program.

#### Scenario: User excludes a song
- **WHEN** user specifies skip_songs: ["派对动物"]
- **THEN** system selects alternative tracks and never includes the excluded song
