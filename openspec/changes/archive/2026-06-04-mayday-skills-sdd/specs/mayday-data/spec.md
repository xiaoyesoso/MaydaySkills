## ADDED Requirements

### Requirement: Data visualization from multiple sources
The system SHALL visualize Mayday's album sales, streaming trends, concert attendance, and search popularity as charts via data-fetcher.py JSON output.

#### Scenario: User requests album trend
- **WHEN** user asks "哪张专辑串流最高"
- **THEN** system runs `data-fetcher.py album-trend`, parses JSON, renders a bar chart, and provides a plain-text summary

### Requirement: Spotify integration with graceful fallback
The system SHALL fetch live Spotify popularity data when SPOTIFY_CLIENT_ID/SECRET are set; otherwise return deterministic stub data with `_meta.source: "stub"`.

#### Scenario: Spotify credentials configured
- **WHEN** env vars are set and user runs `spotify-popularity`
- **THEN** system returns live data with `_meta.source: "spotify"` and caches for 6 hours

#### Scenario: No Spotify credentials
- **WHEN** env vars are missing
- **THEN** system returns stub data with `_meta.source: "stub"` so charts still render

### Requirement: YouTube integration with graceful fallback
The system SHALL fetch YouTube view counts when YOUTUBE_API_KEY is set; otherwise return stub data.

#### Scenario: User queries YouTube views for a song
- **WHEN** user asks "《突然好想你》在YouTube上的播放量"
- **THEN** system runs `youtube-views 突然好想你` and returns ranked video results with view counts

### Requirement: Era comparison
The system SHALL produce side-by-side metrics for two user-specified time periods.

#### Scenario: User compares two eras
- **WHEN** user asks "比较 2004-2008 vs 2016-2020"
- **THEN** system outputs avg album sales, tour frequency, award count, and theme distribution for each era
