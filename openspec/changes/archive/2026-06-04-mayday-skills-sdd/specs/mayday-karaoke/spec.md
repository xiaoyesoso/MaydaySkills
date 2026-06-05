## ADDED Requirements

### Requirement: Song difficulty scoring
The system SHALL compute a difficulty score (0–10) for any song in lyrics-db using the formula: `0.4×normalize(highest_note) + 0.2×normalize(bpm) + 0.2×key_change_count + 0.2×normalize(continuous_singing)`.

#### Scenario: Score "倔强"
- **WHEN** user requests difficulty for "倔强"
- **THEN** system returns score (e.g., 8/10 "困难") with breakdown: highest note A4, BPM 132, 1 key change, sustained chorus

### Requirement: Vocal guide with annotations
The system SHALL annotate each song segment with difficulty markers: 🔴 high note, 🟡 vocal transition, 💨 breath point, 🎯 chorus key-up.

#### Scenario: Guide for "温柔"
- **WHEN** user requests a vocal guide for "温柔"
- **THEN** system outputs segment-by-segment annotations marking the high notes and breath points

### Requirement: Song recommendation by vocal range
The system SHALL filter and rank songs from lyrics-db based on user's stated vocal range, excluding songs whose highest note exceeds the user's range.

#### Scenario: User with limited range requests recommendations
- **WHEN** user states vocal range C3-G4
- **THEN** system returns 5–10 singable songs sorted by difficulty ascending

### Requirement: N-day practice plan
The system SHALL generate a structured practice plan (daily 30-min sessions) for learning a specific song over N days.

#### Scenario: 30-day plan for "倔强" chorus
- **WHEN** user requests a 30-day plan for "倔强"
- **THEN** system outputs a day-by-day plan: week 1 segment practice, week 2 slow full-song, week 3 full-speed, week 4 breath control, each with specific targets
