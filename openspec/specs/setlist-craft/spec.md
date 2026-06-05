## ADDED Requirements

### Requirement: Custom setlist generation with mood curve
The system SHALL generate a custom setlist of N songs following a user-specified or preset mood curve (Energy × Valence per slot), satisfying must-include and must-exclude constraints.

#### Scenario: Birthday party setlist
- **WHEN** user specifies occasion "birthday", 20 songs, mood curve "calm→high", must_include ["干杯"], must_exclude ["突然好想你"]
- **THEN** system outputs 20-song ordered setlist with per-song E/V values, total duration, and ASCII mood curve visualization

### Requirement: Preset mood curve templates
The system SHALL provide at least 5 preset mood curves: 平到嗨, 抒情之夜, 情绪过山车, 治愈wave, 巡演级.

#### Scenario: User selects preset curve
- **WHEN** user chooses "情绪过山车" preset
- **THEN** system uses the preset E/V curve values for each slot and fills accordingly

### Requirement: Constraint solver for track selection
The system SHALL use `scripts/build-setlist.py` to solve the constraint satisfaction problem: match songs to curve slots while respecting must_include/exclude and total duration targets.

#### Scenario: Must-include conflicts with curve
- **WHEN** a must-include song's E/V doesn't fit the target curve slot
- **THEN** system warns the user and offers to adjust the curve or swap the constraint

### Requirement: PDF export
The system SHALL optionally export the setlist as a printable PDF card via `scripts/render-pdf.py`.

#### Scenario: User requests PDF
- **WHEN** user asks for a printable version
- **THEN** system generates a PDF with song list, mood curve, and encore suggestions
