## ADDED Requirements

### Requirement: Direct Q&A from trivia database
The system SHALL answer factual questions about Mayday by searching the trivia-db.json (762 entries) and returning concise answers with source attribution.

#### Scenario: User asks about冠佑's real name
- **WHEN** user asks "冠佑的本名是什么"
- **THEN** system responds "刘谚明（后更名为刘冠佑）" with source from knowledge-base/band-members.md

#### Scenario: Answer not in database
- **WHEN** user asks a question not covered by trivia-db
- **THEN** system searches the web, responds with the answer, and clearly marks the source as "external/web"

### Requirement: Interactive quiz mode
The system SHALL run a 10-question quiz at user-selected difficulty (easy/medium/hard/nightmare) with per-question feedback and a final Mayday-themed rating.

#### Scenario: User starts a medium quiz
- **WHEN** user triggers quiz mode with difficulty "medium"
- **THEN** system randomly selects 10 medium-difficulty questions, presents one at a time, scores each response, and shows final rating (10/10 = 第五位团员, 7-9 = 资深五迷, 4-6 = 路人粉, 0-3 = 还不快去听歌)

### Requirement: Accept answer variants
The system SHALL accept reasonable answer variants (e.g., "玛莎" = "蔡升晏", "冠佑" = "刘谚明" = "刘冠佑").

#### Scenario: User answers with variant name
- **WHEN** quiz answer is "冠佑" and user types "刘谚明"
- **THEN** system accepts the answer as correct
