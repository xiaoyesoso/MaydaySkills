## ADDED Requirements

### Requirement: Concert setlist prediction
The system SHALL predict a setlist based on recent shows of the specified tour, marking each song with emoji indicators (🎤 must-sing-along, ⚡ high-energy, 🕯️ light-stick wave, 🎸 guitar showcase).

#### Scenario: User prepares for a specific concert
- **WHEN** user provides tour name + city + date
- **THEN** system outputs a predicted setlist with emoji markers derived from recent 3 shows

### Requirement: Fan tradition coaching
The system SHALL teach official fan chants, encore rhythms (stomping, chanting, light-stick patterns), and tour-specific traditions.

#### Scenario: First-time concertgoer
- **WHEN** user mentions it's their first Mayday concert
- **THEN** system provides a "Fan Traditions 101" guide covering chants, encore protocol, and light-stick etiquette

### Requirement: Venue logistics and packing checklist
The system SHALL provide venue info (capacity, transport, food) and a packing checklist (light stick, charger, tissues, lozenges, ID, ticket backup).

#### Scenario: User asks about venue
- **WHEN** user specifies a venue city
- **THEN** system outputs nearest MRT/station, last-train times, and a checked packing list

### Requirement: Post-concert comfort kit
The system SHALL offer a "post-concert depression" comfort kit with playlist suggestions and community links.

#### Scenario: User reports post-concert sadness
- **WHEN** user expresses feeling down after a concert
- **THEN** system provides a curated recovery playlist and processing tips
