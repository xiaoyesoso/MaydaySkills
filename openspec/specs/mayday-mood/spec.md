## ADDED Requirements

### Requirement: Mood-to-song matching via 3-axis taxonomy
The system SHALL parse user's free-text mood description into Energy (1–10), Valence (1–10), and Theme tags, then match against lyrics-db mood data using the formula: `score = -sqrt(ΔE²+ΔV²) + 2·|theme_overlap|`.

#### Scenario: User describes "work pressure, want healing and power"
- **WHEN** user says "最近工作压力大，想被治愈，但也想要点力量"
- **THEN** system maps to E:6, V:5, themes:[growth, dream-chasing] and returns top 3–5 matching songs with mood breakdown and anchor lyric

### Requirement: Mood-based playlist generation
The system SHALL generate a multi-part playlist given a sequence of moods or activities (e.g., "通勤→工作→午休→下班→夜跑").

#### Scenario: User requests activity-based playlist
- **WHEN** user provides an activity sequence
- **THEN** system outputs 5-part playlist with transition logic and optional playlist name

### Requirement: No inertial matching
The system SHALL NOT recommend the same song for all similar queries. When theme overlap is 0, the song SHALL be excluded rather than forced.

#### Scenario: Theme mismatch exclusion
- **WHEN** a song's themes have zero overlap with user mood themes
- **THEN** system excludes that song from recommendations regardless of E/V proximity
