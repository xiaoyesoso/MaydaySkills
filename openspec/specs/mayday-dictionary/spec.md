## ADDED Requirements

### Requirement: Term lookup with fuzzy search
The system SHALL look up fan terminology in dictionary.json and return full definition, origin, examples, related terms, and tags. If no exact match, it SHALL perform fuzzy search and present candidates.

#### Scenario: Exact match lookup
- **WHEN** user queries "升 key 战神"
- **THEN** system returns the full entry: definition, origin, examples, related terms

#### Scenario: Fuzzy search
- **WHEN** user queries "升" (partial)
- **THEN** system lists all terms starting with or containing "升" (升 key / 升 key 战神 / 升 key 段位)

### Requirement: Daily word feature
The system SHALL provide a "每日一词" feature that selects one term per day (deterministic via date hash) with full explanation and a real usage scenario.

#### Scenario: User requests daily word
- **WHEN** user says "今天教我一个新的五迷术语"
- **THEN** system outputs one randomly selected term with full释义 + 例句 + usage scenario

### Requirement: Multi-category term organization
The system SHALL organize all dictionary entries into at least 6 categories: concert-slang, song-easter-egg, band-nickname, timeline-event, meme, era-tag.

#### Scenario: Browse by category
- **WHEN** user asks "演唱会有哪些黑话"
- **THEN** system lists all terms in the concert-slang category with brief definitions

### Requirement: Term not found handling
The system SHALL suggest web search when a term is not in dictionary.json, and offer users a way to suggest new entries.

#### Scenario: Unknown term
- **WHEN** user queries a term not in the dictionary
- **THEN** system responds "未收录，要不要联网查？" and offers a contribution template
