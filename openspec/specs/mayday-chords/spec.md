## ADDED Requirements

### Requirement: Chord lookup for any Mayday song
The system SHALL output a full chord chart (verse/chorus/bridge) in both standard notation and Roman numeral analysis for any song in lyrics-db.

#### Scenario: User looks up chords for "温柔"
- **WHEN** user requests chord analysis for "温柔"
- **THEN** system outputs Key, Roman numeral progression per segment, and ASCII chord diagram via chord-diagram.py

### Requirement: Key change analysis
The system SHALL explain how Mayday uses key changes in climactic moments (e.g., 倔强 chorus key-up, 你不是真正的快乐 semitone rise).

#### Scenario: User asks about "倔强" key change
- **WHEN** user asks "how does 倔强 use key changes"
- **THEN** system identifies the key-up point in the bridge/chorus and explains the emotional effect

### Requirement: Learning roadmap
The system SHALL recommend a practice sequence ordered by difficulty for guitar learners.

#### Scenario: Beginner wants to learn Mayday songs
- **WHEN** user states they are a beginner
- **THEN** system outputs a 3-step plan starting with easy songs (low BPM, no key changes)
