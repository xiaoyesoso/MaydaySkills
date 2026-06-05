## ADDED Requirements

### Requirement: Generate constrained fan-fiction
The system SHALL generate original short fiction (300–3000 words) set in the Mayday universe based on user-provided premise, length, POV, and tone.

#### Scenario: User requests a "志明与春娇" reunion story
- **WHEN** user provides premise "《志明与春娇》多年后再相遇" with length 800, third-person POV, bittersweet tone
- **THEN** system generates an 800-word story with 1 anchor lyric line (cited), and appends a creation disclaimer

### Requirement: Content safety red lines
The system SHALL refuse to generate content that: contains R18/violence/political content, defames real persons, implies real romantic relationships without "纯虚构" label, uses complete song lyrics, or fabricates verifiable quotes attributed to real persons.

#### Scenario: User requests R18 content
- **WHEN** user asks for explicit content involving band members
- **THEN** system refuses with explanation and offers an alternative within bounds

#### Scenario: User requests CP fiction
- **WHEN** user requests a shipping story about real members
- **THEN** system generates it ONLY with explicit "纯虚构" label and avoids implying real relationships

### Requirement: Creation disclaimer mandatory
The system SHALL append a three-part disclaimer to every output: inspiration source, embedded lyric citation (1 line max), and a statement that the content is fan fiction unrelated to the artists.

#### Scenario: Output always includes disclaimer
- **WHEN** any fanfic is generated
- **THEN** the output ends with: "✨ 灵感来源：《[曲名]》/ 🎵 锚句：「...」/ ⚖️ 创作声明：同人虚构，与艺人本人立场无关；非商业用途"

### Requirement: Character consistency via persona data
The system SHALL use persona/ data (Ashin + future band member personas) to ensure character behavior is consistent with established traits.

#### Scenario: Dialogue in fan fiction
- **WHEN** a character speaks in the story
- **THEN** the dialogue reflects that member's known speech patterns from persona/ data
