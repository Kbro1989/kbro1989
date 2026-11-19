# ⚡ Pick of Gods · Kbro1989

**Self-taught systems archaeologist. 20+ years of learning everything. Builder of thinking machines.**

[![Site](https://img.shields.io/badge/🌐_Site-POG2_Dev-0a0a0a?style=for-the-badge&logo=cloudflare&logoColor=F6821F)](https://pog2.dev)
[![YouTube](https://img.shields.io/badge/YouTube-@kbrops-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://youtube.com/@kbrops)
[![Patreon](https://img.shields.io/badge/Patreon-PickofGods-FF424D?style=for-the-badge&logo=patreon&logoColor=white)](https://patreon.com/PickofGods)
[![X](https://img.shields.io/badge/X-@browder__ke33437-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/browder_ke33437)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0005--7167--420X-A6CE39?style=for-the-badge&logo=orcid&logoColor=white)](https://orcid.org/0009-0005-7167-420X)

[![MIT v1.1.0](https://img.shields.io/badge/License-MIT_v1.1.0-blue?style=flat-square)](LICENSE)
[![Repos](https://img.shields.io/badge/repositories-188-6e40c9?style=flat-square)]()
[![Domains](https://img.shields.io/badge/Domains-14-00c7b7?style=flat-square)]()
[![Domains](https://img.shields.io/badge/Domains-14-00c7b7?style=flat-square)](#domains)

**Independent Systems Engineer | Computational Design & Reverse Engineering | AI and Distributed Infrastructure**

I reverse-engineer, design, and build software systems across AI, distributed infrastructure, scientific computing, interactive environments, and embedded systems.

My work is driven by a recurring question:

**How can different technologies, models, and systems become parts of a coherent, resilient architecture?**

I work from the underlying mechanisms upward: protocols, data structures, state machines, runtimes, interfaces, and the infrastructure that connects them.

---

## 🧠 The Approach

I don't approach software as isolated applications.

I look for the systems underneath them: how they represent state, exchange information, make decisions, recover from failure, and evolve over time.

That has led me into several connected areas:

- Building AI agents and orchestration infrastructure.
- Reverse-engineering legacy software, game clients, caches, and protocols.
- Designing distributed applications using Cloudflare Workers and Durable Objects.
- Developing mathematical and scientific computing pipelines.
- Exploring computational graphics, procedural content, and generative media.
- Designing embedded and cyber-physical control architectures.

The unifying theme is **systems integration through understanding fundamentals**.

I am self-taught, project-driven, and have spent more than 20 years learning across technical disciplines. My portfolio reflects that breadth: original projects, upstream contributions, research explorations, forks, and experimental implementations.

---

## 🗺️ Engineering at a Glance

Quick navigation to the main disciplines and their primary repositories.

| Discipline | Primary Repositories |
| --- | --- |
| Reverse engineering | [openrsc-vinilla](https://github.com/Kbro1989/openrsc-vinilla), [rsmv](https://github.com/Kbro1989/rsmv), [Pog2-Data](https://github.com/Kbro1989/Pog2-Data) |
| Scientific computing | [Upgraded-Depth-Anything-V2](https://github.com/MackinationsAi/Upgraded-Depth-Anything-V2), [quantum-simulation](https://github.com/rasidi3112/quantum-simulation) |
| Computational mathematics | [KING-WEN-I-CHING-IMMUTABLE-TABLES](https://github.com/Kbro1989/KING-WEN-I-CHING-IMMUTABLE-TABLES) |
| Distributed infrastructure | [OpenJarvis](https://github.com/Kbro1989/OpenJarvis), [cloudflare-code-agent](https://github.com/Kbro1989/cloudflare-code-agent), [CfOllama](https://github.com/Kbro1989/CfOllama) |
| AI architecture | [OpenJarvis](https://github.com/Kbro1989/OpenJarvis), [hermes-agent](https://github.com/Kbro1989/hermes-agent), [Megatron-LM](https://github.com/Kbro1989/Megatron-LM) |
| Embedded systems | [MHD-Propulsion-Controller-Simulator](https://github.com/Kbro1989/MHD-Propulsion-Controller-Simulator) |
| Symbolic computation | [I-Ching_Oracle](https://github.com/Kbro1989/I-Ching_Oracle), [KING-WEN-I-CHING-IMMUTABLE-TABLES](https://github.com/Kbro1989/KING-WEN-I-CHING-IMMUTABLE-TABLES) |

---


## 🏗️ POG2 — The Sovereign Systems Platform

[**POG2**](https://github.com/Kbro1989/POG2) is the central architecture connecting much of my current work.

The goal is a modular environment where local computation, cloud services, AI models, persistent state, and specialized tools can cooperate without making any single provider or runtime a permanent dependency.

### Architectural direction

| Layer | Responsibility | Technologies |
| --- | --- | --- |
| Local runtime | Sovereign execution, local models, development workflows | Python, Ollama, CLI, desktop |
| Agent orchestration | Routing, task coordination, specialized capabilities | TypeScript, Python, agent tools |
| Edge infrastructure | Distributed execution and service interfaces | Cloudflare Workers |
| Persistent state | Durable application and world state | Durable Objects, KV, D1, R2 |
| Communication | Real-time application and agent communication | WebSockets, HTTP, APIs |
| Data and knowledge | Structured entities, retrieval, validation | Python, TypeScript, APIs |
| Interfaces | Dashboards, applications, development surfaces | HTML, JavaScript, TypeScript |

### Core components

| Repository | Purpose |
| --- | --- |
| [POG2](https://github.com/Kbro1989/POG2) | Main platform and documentation |
| [Pog2-Core](https://github.com/Kbro1989/Pog2-Core) | Core runtime and modular processing architecture |
| [Pog2-Data](https://github.com/Kbro1989/Pog2-Data) | Data and entity ingestion |
| [Pog2-Atlas](https://github.com/Kbro1989/Pog2-Atlas) | Spatial world and region management |
| [Pog2-Pedagogy](https://github.com/Kbro1989/Pog2-Pedagogy) | Quest-based learning and progression data |
| [Pog2-Guttenberg-](https://github.com/Kbro1989/Pog2-Guttenberg-) | Literary ingestion and narrative generation |
| [D-sovereign-](https://github.com/Kbro1989/D-sovereign-) | Distributed state-management experiments |

### Design principles

- **Sovereign-first:** prefer local execution where practical.
- **Cloud as a resource:** use remote infrastructure when it adds capability or reach.
- **Modularity:** specialized components should have explicit responsibilities and interfaces.
- **Resilience:** design for failure, recovery, and alternative execution paths.
- **Provenance:** preserve where information, decisions, and results originate.
- **No fake completion:** distinguish prototypes, implemented functionality, and verified behavior.

### Internal Subsystem Architecture

| Variable / Component | Subsystem Responsibility | Architectural Role |
| --- | --- | --- |
| Runtime topology | `CNS / MEMORY / SENSORY / MOTOR / REGISTRY` | Decoupled five-tier modular execution |
| Processing | `CNSGodheadPulseVolley` | Central orchestration pulse and event distribution |
| Routing | `TernaryRouter` | Three-valued state-based routing |
| Agent coordination | `PlayerAgent`, `ModelRolodex` | Multi-agent lifecycle and model catalog management |
| Symbolic state | `HexagramManager` | Deterministic 64-state transition handling |
| Security boundary | `ExteriorGate` | External-agent admission and perimeter isolation |
| Error contract | `Result<T>` | Explicit monadic error handling without uncaught panics |
| Verification | `NodeTester`, `healthCheck` | Runtime subsystem verification and health telemetry |
| Recovery | Four-tier circuit-breaker fallback | Progressive degradation and fault recovery |

### External Agent Security Boundary

POG2 evaluates untrusted foreign agents through an explicit perimeter admission pipeline:

`Foreign Agent → Handshake → Child Provenance → Domain Lock / Monitoring → ExteriorGate → Allow or LOCKDOWN`

Associated threat detection classifications include:
- `EXTERNAL_BINARY`
- `FILE_TARGETING`
- `SOURCE_ESCALATION`
- `PROMPT_INJECTION`
- `OBFUSCATION`
- `DATA_EXFILTRATION`

*Qualification:* The architecture produces security classifications and admission decisions; it does not automatically establish that every threat has been prevented.

The intended architecture is not a claim that every component is already integrated or independently validated. It is the direction guiding the engineering.

---

## 📐 Engineering Evidence & Technical Milestones

My projects are not limited to application interfaces. They involve the underlying structures, numerical methods, data models, and infrastructure that make those applications work.

**Epistemic distinction:** A measured result, a tested implementation, an architectural specification, and an experimental target are four different kinds of evidence.

Selected engineering milestones:

### Scientific Computing
- Extended an upstream quantum simulation framework ([rasidi3112/quantum-simulation](https://github.com/rasidi3112/quantum-simulation)) with multidimensional grid and wavefunction abstractions, 3D split-step solving, absorbing boundary layers, and GPU acceleration.
- **Merged upstream on August 20, 2026** (Merge commit `9a6d528`: 893 lines added, 14 files changed, 25/25 unit tests green).
- Added multi-run benchmarking, statistical performance reporting, and numerical correctness validation.

### Computational Mathematics
- Built a frozen mathematical parsing benchmark covering **3,409 equations** across 14 research papers.
- Achieved **3,393 fully supported** (99.53%) and 16 partially supported equations on that frozen population (zero duplicates).
- Developed MathML, AST extraction, equation recovery, and mathematical document association tooling.
- Evaluated preservation of nested and extensible mathematical delimiters (D1–D6 structural recovery engine, 1,505-image blind render manifest).

### Game Data Archaeology
- Developed a RuneScape cache extraction and interpretation forensic pipeline.
- Historical RS3 cache substrate inventory: **approximately 229,000 records** (32,512 NPCs, 59,984 items, ~136,000 objects from revision 221+).
- Handled opcode interpretation, version-aware cache structures, model extraction, GLTF asset generation, and reconstructed geometry validation.

### Distributed Systems
- Developed Cloudflare Workers and Durable Objects integrations for edge execution and persistent state.
- Explored real-time multiplayer state synchronization referencing the 640 ms RuneScape Classic game-cycle reference.
- Integrated persistent state (Durable Objects, KV, D1), WebSockets, and hybrid local/cloud execution patterns.

### AI Infrastructure
- Developed agent orchestration, model selection (`ModelRolodex`), tool registries (`ToolRegistry`), and execution infrastructure (`MCPEngine`).
- Explored local-first inference (Ollama) with cloud-based execution and deployment alternatives.
- Designed explicit security boundaries (`ExteriorGate`), provenance tracking, and a four-tier circuit-breaker fallback.

### Embedded and Cyber-Physical Systems
- Designed an MHD propulsion controller architecture targeting the **Xilinx Zynq UltraScale+ XCZU7EV MPSoC FPGA**.
- Defined seven named HDL subsystem responsibilities spanning control sequencing, telemetry encoding, sensor acquisition, and AXI4-Lite interfaces.
- Explored software/hardware boundaries, Hamiltonian thermal modeling, and deterministic state-machine implementation.

**Evidence policy:** Numerical results are tied to their specific datasets and evaluation versions. Implemented, tested, merged, deployed, experimental, and proposed functionality are reported separately.

---

## 🗺️ The Technical Landscape

These are the 14 principal areas represented across my projects. They overlap, but each brings a different set of engineering problems.

| # | Area | Representative work |
| --- | --- | --- |
| 1 | **Distributed and Edge Systems** | Workers, Durable Objects, KV, D1, R2, WebSocket services |
| 2 | **AI and Agent Architecture** | Model routing, agent orchestration, tools, local/cloud execution |
| 3 | **Real-Time Multiplayer Systems** | Game ticks, state synchronization, world regions, player persistence |
| 4 | **Reverse Engineering and Forensics** | Cache analysis, opcode versioning, protocol and asset inspection |
| 5 | **Game Engine and Simulation Systems** | Quest engines, ability systems, world state, game logic |
| 6 | **Computer Graphics and 3D** | Three.js, WebGL, model extraction, rendering and asset pipelines |
| 7 | **Computer Vision and Image Processing** | Segmentation, clustering, image analysis and processing |
| 8 | **Creative and Generative Technology** | Audio/video pipelines, procedural media, narrative generation |
| 9 | **Embedded and FPGA Systems** | VHDL, SystemVerilog, AXI4-Lite, Zynq architecture |
| 10 | **Cyber-Physical and Propulsion Systems** | MHD simulation, control architecture, telemetry and safety logic |
| 11 | **Data and Knowledge Engineering** | Structured ingestion, entity resolution, validation and event data |
| 12 | **Education and Pedagogy** | Quest-based learning, skill progression, competency tracking |
| 13 | **Platform Engineering and DevOps** | CI/CD, deployment pipelines, CLI tooling, multi-environment releases |
| 14 | **Security and Resilience** | Fault handling, validation, recovery, zero-trust design |

---

## ⚔️ RuneScape — Reverse Engineering, Preservation and Multiplayer Systems

One of my longest-running technical interests is understanding how complex game systems work beneath their interfaces.

The RuneScape ecosystem gives me a practical environment for exploring legacy protocols, cache formats, game state, client behavior, real-time synchronization, and 3D assets.

### Selected projects

| Repository | Focus |
| --- | --- |
| [openrsc-vinilla](https://github.com/Kbro1989/openrsc-vinilla) | OpenRSC server and Cloudflare integration |
| [rsc-globe1-pure](https://github.com/Kbro1989/rsc-globe1-pure) | Multiplayer globe worker |
| [rsc-dashboard](https://github.com/Kbro1989/rsc-dashboard) | Server monitoring and visualization |
| [rsmv](https://github.com/Kbro1989/rsmv) | RuneScape cache tools and 3D model extraction |
| [hello-ai-worker-rsmv](https://github.com/Kbro1989/hello-ai-worker-rsmv) | RSMV and Cloudflare AI integration |
| [ElderScape](https://github.com/Kbro1989/ElderScape) | Game-building and AI-assisted development |
| [Elder-Scape](https://github.com/Kbro1989/Elder-Scape) | Game-builder implementation |
| [Rs3-ai-api](https://github.com/Kbro1989/Rs3-ai-api) | RS3 data and API integration |
| [Alt-1_Helper-Bridge](https://github.com/Kbro1989/Alt-1_Helper-Bridge) | Game overlay integration |
| [Pick_Of_Gods](https://github.com/Kbro1989/Pick_Of_Gods) | RS3 assistant and tooling |

### Engineering interests

- Legacy cache and asset forensics.
- Version-aware opcode and data interpretation.
- Client/server boundaries and protocol behavior.
- Authentic real-time game timing.
- Durable player state and multiplayer synchronization.
- 3D model extraction, inspection, and editing.
- AI-assisted game interaction and world-state interpretation.

A recurring design target is the original RuneScape Classic **640 ms game cycle**. I use that timing as a reference point when exploring compatibility and real-time system behavior.

### Quantitative Cache Forensics (`Pog2-Data`)

Developed a structured game-data substrate from RuneScape cache revision 221+, encompassing approximately 229,000 NPC, item, and object records:

| Entity Type | Extracted Records | Source & Forensics |
| --- | --- | --- |
| NPCs | 32,512 | Revision 221+ opcode extraction & field interpretation |
| Items | 59,984 | Attribute mapping, stackable properties, equip slots |
| Objects | ~136,000 | World interaction boundaries & model references |
| **Total** | **~229,000** | Forensic RSMV pipeline extraction |

### Forensic Reconstruction Pipeline (`rsmv`)

Rather than treating game models as static assets, the extraction workflow implements a six-stage forensic chain:

1. **Raw bytes and opcode sequences:** Byte-level stream parsing and version-aware opcode dispatch.
2. **Parser and field interpretation:** Separation of packed bitfields, color indices, and texture coordinates.
3. **Consumer and entity identification:** Cross-referencing definition IDs with downstream game engine entities.
4. **Model and identifier resolution:** Resolving composite mesh references, animations, and bone weights.
5. **Geometry reconstruction:** Building valid indexed mesh geometry and generating standard GLTF assets.
6. **Visual validation:** Comparing reconstructed visual outputs against game client ground truth.

*Methodological invariant:* Never promote inferred structures into canonical definitions without corroborating evidence.

### Autonomous Game-World Evolution (`rscaievolution-png`)

Experimental agent-driven game-world evolution combining semantic entity data, autonomous goals, temporal progression, asset transformation, and distributed state synchronization:

| Variable / Subsystem | Purpose | Architecture / Stack |
| --- | --- | --- |
| `evolutionStage` | Discrete world-progression from stage 0 to 240 | Durable Object state authority |
| Eras | Historical epoch brackets from 0 to 12 | Temporal world-rule shifts |
| Semantic item tags | Behavioral classification of game entities | Multi-attribute metadata indexing |
| Gronk agent state | Autonomous NPC decision and memory representation | State-machine agent runtime |
| Dual inventories | Separate inventory-state handling (active vs bank/stash) | Atomic transaction updates |
| Autonomous goals | Agent-directed objectives and path resolution | Heuristic goal evaluation |
| `sync-pog-ids.js` | Synchronizes POG-Ultimate JSON definitions with RSC constants | Pipeline ID reconciliation |

---

## ☯️ King Wen — Symbolic Systems as Executable Architecture

The King Wen work explores how symbolic structures can be represented as deterministic computational systems.

The I Ching provides a constrained state space: 64 hexagrams, six lines per hexagram, and transformations between states.

Rather than treating the system as a simple lookup table, I explore its representation through state machines, temporal routing, data integrity, and computational interfaces.

### Selected repositories

| Repository | Focus |
| --- | --- |
| [KING-WEN-I-CHING-IMMUTABLE-TABLES](https://github.com/Kbro1989/KING-WEN-I-CHING-IMMUTABLE-TABLES) | Immutable hexagram and line tables |
| [I-Ching_Oracle](https://github.com/Kbro1989/I-Ching_Oracle) | Oracle application and state-routing architecture |
| [KW-K2](https://github.com/Kbro1989/KW-K2) | King Wen and Kimi-K2 integration exploration |
| [Bathospire-Professor-](https://github.com/Kbro1989/Bathospire-Professor-) | Cursive learning and educational tooling |
| [king-wen-legal](https://github.com/Kbro1989/king-wen-legal) | Project documentation and legal materials |

The broader design explores:

- 64-state hexagram representation.
- Six-line state transformations.
- Past, Present, and Future temporal dimensions.
- Ternary routing and state resolution.
- Immutable reference data and validation.
- Interfaces between symbolic reasoning and executable software.

The central principle is simple: **a symbolic system should have explicit rules, traceable state transitions, and reproducible outputs**.

### Frozen Mathematical Parser Benchmark

Rigorous evaluation conducted against a frozen mathematical population:

| Metric | Measured Result | Qualification |
| --- | --- | --- |
| Evaluation papers | 14 research papers | Peer-reviewed ArXiv mathematics / physics corpus |
| Total equations evaluated | 3,409 equations | Frozen set (2,023 v1 + 395 v2 + 991 v4; zero duplicates) |
| Fully supported equations | 3,393 equations | **99.53%** fully supported share |
| Partially supported equations | 16 equations | Documented edge-case syntax / multiline alignments |

*Epistemic boundary:* This metric measures performance against that specific frozen population, not universal mathematical OCR accuracy.

### Extraction & Recovery Tooling

A pipeline of modular utilities built to bridge raw LaTeX, MathML, ASTs, and symbolic tables:
- `semantic_math_extractor.py` & `mathml_parser.py`: Semantic XML/LaTeX expression parsing.
- `math_recovery_tool.py` & `recover_training_data.py`: Corpus training data reconstitution.
- `arxiv_html_parser.py` & `math_pdf_association.py`: Document-level spatial expression alignment.
- `math_to_kingwen_adapter.py`: Mathematical AST to hexagram state-space transformation.
- `delimiter_aware_structural_recovery.py`: AST extraction preserving nested boundary scopes.

*Corpus footprint:* Evaluated across 203 semantic paper records, 4,043 extracted expressions, ~162,000 proof-chain elements, 245 text corpus files, and 82,224 generated records (1,536 per paper across 54 processed papers; 6.8 GB artifact footprint).

### Mathematical Adapter Milestone (Commit `c40286c`)

Attempted transformation of mathematical expressions into structured symbolic representations (1,310 files; +63,899 / -1,622 lines):

| Evaluation Dimension | Result (991-Case Regression) | Status |
| --- | --- | --- |
| Extraction accuracy | 991 / 991 | PASS |
| Identity & provenance tracking | 991 / 991 | PASS |
| State routing | 956 / 991 | PARTIAL |
| Full semantic recovery | 448 pass / 543 fail | UNRESOLVED |

*Qualification:* Successful extraction and identity checks do not establish complete semantic equivalence or correct recovery.

### Structural Delimiter Preservation

Preserving mathematical structure—particularly extensible delimiters (e.g. tall parentheses enclosing matrices rather than flattened inline punctuation):
- D1–D6 structural recovery engine tested against 667/667 v1 cross-paper test cases.
- 1,505-image blind render manifest; 3,644 rendered images across two cohorts (1,869 and 1,775 images) via PyMuPDF 1.25.3 & OpenCV 4.11.0 (zoom: 4.0).
- Rahmani benchmark paper (1212.0957): 575/575 manifest entries verified.
- **Evaluation status:** While the G0 adapter passed 9/9 targeted unit tests, full-corpus G0 certification remained pending as of the November audit. Structural delimiter preservation is rigorously documented as **NOT VERIFIED**.

---

## 🤖 AI, Agents and Model Infrastructure

My AI work focuses on infrastructure around models, not just model interaction.

I experiment with how models can be selected, connected to tools, coordinated across tasks, and deployed across local and cloud environments.

### Selected repositories

| Repository | Focus |
| --- | --- |
| [CfOllama](https://github.com/Kbro1989/CfOllama) | Ollama and Cloudflare integration |
| [cloudflare-code-agent](https://github.com/Kbro1989/cloudflare-code-agent) | AI-assisted code generation |
| [POG-CLI-CODER](https://github.com/Kbro1989/POG-CLI-CODER) | Command-line coding workflows |
| [ai-game-studio](https://github.com/Kbro1989/ai-game-studio) | AI-assisted game development |
| [Willow-AI-Coding-Playground](https://github.com/Kbro1989/Willow-AI-Coding-Playground) | AI coding environment |
| [willow-ai-game-dev-hybrid](https://github.com/Kbro1989/willow-ai-game-dev-hybrid) | Local/cloud game-development experiments |
| [OpenJarvis](https://github.com/Kbro1989/OpenJarvis) | Forked local-first AI platform |
| [hermes-agent](https://github.com/Kbro1989/hermes-agent) | Forked agent runtime and workflow exploration |

### Core AI Subsystems & Infrastructure

Rather than treating AI as an isolated prompt endpoint, the infrastructure implements explicit orchestration, verification, and execution primitives:

| Component | Architecture Responsibility | Implementation Role |
| --- | --- | --- |
| `MCPEngine` | Model Context Protocol execution | Structured tool and resource invocation |
| `ToolRegistry` | Tool registration & capability discovery | Dynamic schema-based tool routing |
| `OrchestrateEngine` | Multi-agent task coordination | Topological dependency and execution ordering |
| `MultiModelExecutor` | Multi-model invocation & routing | Polyglot model dispatch (local & remote) |
| `IntentVerifier` | Behavioral intent validation | Constraint validation prior to state mutations |
| `ModelRolodex` | Model catalog and selection heuristic | Context-aware model discovery |
| `GhostLimb` | Autonomous worker runtime module | Background task processing |
| `TernaryRouter` | Three-valued routing logic | State resolution across ambiguous execution paths |
| `EndpointHealer` | Resilience and connection self-healing | Automatic fallback upon model timeout/error |
| Hermes integration | `pog2-sovereign` agent registration | Sovereign agent protocol integration |

I also study and work with upstream projects across model training, agent frameworks, model interfaces, and developer tooling.

**A fork is not the same thing as an original implementation.** I maintain forks for experimentation, integration, adaptation, and understanding upstream systems; original development is identified separately.

---

## 🔬 Scientific and Mathematical Computing

Scientific computing is an important part of my work because it forces software to answer to mathematical and numerical constraints.

Examples include:

- Mathematical document extraction and equation parsing.
- Structural preservation of mathematical notation.
- Numerical simulation and solver architecture.
- Data validation and reproducible evaluation.
- GPU/CPU correctness comparisons.
- Computational modeling and visualization.

### Upstream Merged Contribution: `rasidi3112/quantum-simulation`

I contributed a complete multidimensional solver architecture to [rasidi3112/quantum-simulation](https://github.com/rasidi3112/quantum-simulation), merged into upstream production on **August 20, 2026** (Merge commit `9a6d528`):

| Implementation Component | Subsystem Description |
| --- | --- |
| `Grid3D` | Three-dimensional spatial grid discretization with configurable boundaries |
| `WaveFunction3D` | 3D complex wavefunction state representation and norm tracking |
| `SplitStep3DSolver` | 3D split-step Fourier solver for time-dependent Schrödinger equation |
| `Gaussian2D/3DBarrier` | Multidimensional potential energy barrier configurations |
| ABL 3D | Three-dimensional absorbing boundary layer preventing unphysical reflection |
| 3D Observables | Expectation value measurement and quantum probability current tracking |
| Examples 05 & 06 | Multidimensional wavepacket tunneling demonstrations |
| GPU Backend | GPU-accelerated 3D split-step execution via PyTorch/CuPy |

#### Quantitative Upstream Impact

| Metric | Measured Value |
| --- | --- |
| **Lines added** | **893** |
| **Files changed** | **14** |
| **Reported unit tests** | **25 / 25 Green** |
| **Commits merged** | **3 (Merge commit `9a6d528`)** |
| **Maintainer verification** | Explicitly validated CPU/GPU parity, energy conservation, and numerical stability |

Follow-up work introduced multi-run benchmarking, statistical performance reporting, and numerical correctness validation across varied grid dimensions. This demonstrated the ability to understand an unfamiliar scientific codebase, extend core physical abstractions, implement high-performance GPU algorithms, verify physical invariants, and maintain upstream open-source contributions.





---

## ⚡ Embedded Systems and Cyber-Physical Architecture

I also explore the boundary between software architecture and physical systems.

One project investigates an MHD propulsion controller and simulation architecture, with a Zynq UltraScale+ ZU7EV as a hardware target.

### Hardware Target: Zynq UltraScale+ XCZU7EV MPSoC

The intended hardware architecture specifies seven named HDL subsystems across the programmable logic (PL) and processing system (PS) boundary:

| Subsystem | Architectural Responsibility | Hardware / Interface Protocol |
| --- | --- | --- |
| ContactorSequencer | Switching sequence management | Deterministic high-voltage bus staging |
| ChokeDriver | Choke-control interface | Inductive flyback suppression & PWM timing |
| SensorAcquisition | Sensor input acquisition | Synchronous multichannel ADC frame decoding |
| TelemetryEncoder | Telemetry representation | High-throughput serialized packet encoding |
| AXI4LiteSlave | Register and control interface | Memory-mapped PS/PL AXI4-Lite bus interface |
| HexagramStateMachine | Symbolic state control | Constrained 64-state deterministic transitions |
| GhostSplatPredictor | Predictive state processing | Feed-forward parameter extrapolation |

*Hardware concepts:* VHDL, SystemVerilog, AXI4-Lite, PL/PS interfaces, synchronous sensor acquisition, telemetry encoding, Hamiltonian thermal modeling, and high-voltage safety interlocks.

Related simulation and control work explores Hamiltonian thermal modeling, system behavior, telemetry, and high-voltage safety considerations.

These are engineering and research explorations. A hardware target or HDL module should not be interpreted as proof of a fabricated, commissioned, or safety-certified physical system.

---

## 🎨 Graphics, Creative Technology and Generative Media

I build tools that connect computation with visual and creative workflows.

Areas include:

- Three.js and WebGL.
- 3D asset inspection and editing.
- Procedural image generation.
- Image segmentation and clustering.
- Audio and video processing.
- FFmpeg-based media workflows.
- Narrative and document generation.
- Creative automation.

Selected projects:

| Repository | Focus |
| --- | --- |
| [Color-by-number](https://github.com/Kbro1989/Color-by-number) | Generative art application |
| [Ultimate-Kirby-](https://github.com/Kbro1989/Ultimate-Kirby-) | Image and audio transformation experiments |
| [CelestialArtisanBot](https://github.com/Kbro1989/CelestialArtisanBot) | Generative art and creative automation |
| [rsmv](https://github.com/Kbro1989/rsmv) | 3D model inspection and extraction |

---

## ☁️ Deployment and Infrastructure

Cloudflare is a major part of my edge-infrastructure work.

I use Workers and Pages to explore deployment patterns that connect frontends, APIs, stateful services, and external systems.

I am particularly interested in the distinction between:

- Local applications and local execution.
- Cloud-hosted applications.
- Edge Workers and service endpoints.
- Durable Objects and persistent coordination.
- WebSocket lifecycle and connection behavior.
- GitHub-based development and deployment pipelines.

The objective is to make the same broader system usable across different execution environments without assuming that every workload belongs in the cloud.

### Deployment platforms

| Platform | Role |
| --- | --- |
| Cloudflare Workers / Pages | Edge compute, KV, D1, Durable Objects, R2 |
| Fly.io | Container deployment for stateful services |
| Local runtime | Sovereign execution, local models, development workflows |

### Selected deployed applications

| Application | Platform |
| --- | 
| [POG2](https://pog2.dev) | Main platform |
| [rsc-dashboard](https://rsc-dashboard.pages.dev/) | Pages |
| [rsc-authentic-client](https://rsc-authentic-client.pages.dev/) | Worker endpoint |
| [willow-ai-coding-playground](https://willow-ai-coding-playground.pages.dev/) | Pages |
| [openrsc-vinilla](https://github.com/Kbro1989/openrsc-vinilla) | Repository and deployment project |
| [elderscape-modeleditor](https://github.com/Kbro1989/elderscape-modeleditor) | Worker project |
| [kingwen-oracle](https://github.com/Kbro1989/I-Ching_Oracle) | Oracle application |

---

## 📊 Portfolio Snapshot

Repository inventory snapshot: November 18, 2026. Counts are a point-in-time inventory, not a measure of code quality or contribution size.

| Metric | Count |
| --- | --- |
| Total repositories | 62 |
| Source repositories | 57 |
| Forked repositories | 131 |
| Principal technical areas | 14 |

The repository inventory includes original projects, forks, experiments, integrations, and development tools.

This README highlights selected projects rather than attempting to describe every repository. The complete inventory is available through the [GitHub repositories page](https://github.com/Kbro1989?tab=repositories).

---

## 📈 Technical Progression

The technical work across these repositories follows a structured progression across five engineering phases:

1. **Reverse Engineering & Archaeological Analysis:** Extraction, opcode interpretation, and binary/cache forensic reconstruction (e.g., RuneScape cache revision 221+, `rsmv`, `Pog2-Data`).
2. **Computational Representation & Invariant Structures:** Formalizing discrete structures, ASTs, and deterministic mappings (e.g., King Wen immutable tables, mathematical delimiters, ternary state routing).
3. **Simulation, Numerics & Prediction:** Numerical modeling, multidimensional partial differential equations, and predictive trajectories (e.g., upstream 3D quantum split-step solvers, `GhostSplat` trajectory prediction).
4. **Distributed Execution & Orchestrated Infrastructure:** Highly concurrent execution, edge compute, state synchronization, and security gates (e.g., Cloudflare Workers/KV/Durable Objects, `MCPEngine`, `ExteriorGate` zero-trust admission).
5. **Physical-System Exploration & Hardware Synthesis:** Target architecture definition, register mapping, and RTL/HDL subsystem specification (e.g., Zynq UltraScale+ XCZU7EV MPSoC, FPGA state machines, and sensor acquisition).

---

## 🧭 How I Work

I value engineering discipline over impressive-looking claims.

My preferred workflow is:

1. **Inspect:** understand the existing architecture, code, data, and constraints.
2. **Trace:** identify dependencies, state transitions, interfaces, and failure paths.
3. **Implement:** make targeted changes that respect the system's existing contracts.
4. **Test:** use explicit tests, benchmarks, and validation criteria.
5. **Document:** preserve decisions, provenance, limitations, and reproducibility.
6. **Verify:** distinguish what works from what is merely designed or proposed.

I try to avoid mock implementations presented as finished systems, silent assumptions, and performance claims without measurement context.

I am interested in systems that can be inspected, tested, extended, and understood—not just demonstrated.

---

## 🏢 Organizations

| Organization | Purpose |
| --- | --- |
| [Pick of Gods](https://github.com/pick-of-gods) | Original POG infrastructure and projects |

---


### Build systems that understand their own structure.

<div align="center">

Built on **Cloudflare**. Licensed under **MIT v1.1.0** where applicable.

*"The same hexagram state machine runs in TypeScript on Cloudflare and in VHDL on a Zynq UltraScale+."*

</div>

---


**Pick of Gods · Kbro1989**

[Website](https://pog2.dev) · [GitHub](https://github.com/Kbro1989) · [YouTube](https://youtube.com/@kbrops)

*Independent work. Open-source collaboration. Experimental systems engineering.*


---

## 📊 Technical Evidence & Audit Index

For a full breakdown of subsystems, verification statuses, numerical results, and provenance, refer to the [Engineering Evidence Matrix](https://github.com/Kbro1989/kbro1989/blob/main/EVIDENCE_MATRIX.md) (`EVIDENCE_MATRIX.md`).

The evidence matrix classifies all engineering records across four distinct epistemic tiers:
- **Measured Result:** Empirically benchmarked, logged, and reproducible numerical outcomes.
- **Tested Implementation:** Fully realized codebase with automated unit/integration test coverage.
- **Architectural Specification:** Formal design interfaces, state schemas, and protocol definitions.
- **Experimental Target:** Forward-looking research hypotheses and prototype target hardware profiles.

---
## 🚀 Deployed Apps → Repository Map

| Deployed App | Type | Repository |
|---|---|---|
| Development organization | Organization | Development (free plan) |
| `jarvis-router` | Worker | `OpenJarvis` |
| `openjarvis-kingwen-globe` | Worker | `OpenJarvis` |
| `kingwen-oracle` | Worker | `I-Ching_Oracle` / `KING-WEN-I-CHING-IMMUTABLE-TABLES` |
| `antigravity-bridge-relay` | Worker | `open-design` / `Antigravity-Ultimate` |
| `willow-ai-coding-playground` | Pages | `Willow-AI-Coding-Playground` |
| `rscaievolution-png` | Pages | `rscaievolution-png` |
| `rsc-globe1-pure` | Pages | `rsc-globe1-pure` |
| `rsc-dashboard` | Pages | `rsc-dashboard` |
| `rs3-ai-api` | Pages | `Rs3-ai-api` |
| `mhdpropulsioncontrollersimulator` | Worker | `MHD-Propulsion-Controller-Simulator` |
| `d-sovereign` | Pages | `D-sovereign-` |
| `elderscape-modeleditor` | Worker | `elderscape-modeleditor` |
| `color-by-number` | Pages | `Color-by-number` |
| `astro-blog-starter-template` | Pages | `astro-blog-starter-template` |
| `bathospire-professor` | Pages | `Bathospire-Professor-` |
| `alt-1-helper-bridge` | Pages | `Alt-1_Helper-Bridge` |
| `ai-game-studio` | Pages | `ai-game-studio` |
| `openrsc-vinilla` | Pages | `openrsc-vinilla` |
| `ichingoracle` | Worker | `I-Ching_Oracle` |
| `rsmv` | Pages | `rsmv` |
| `rsmv1` | Pages | `rsmv` |
| `pog2` | Pages | `POG2` |
| `cloudflare-code-agent` | Worker | `cloudflare-code-agent` |
| `multiplayer-globe-template` | Pages | `multiplayer-globe-template` |
| `willow-ai-game-dev` | Pages | `willow-ai-game-dev` |
| `willow-hybrid-game-dev` | Pages | `willow-ai-game-dev-hybrid` |
| `elderscape` | Pages | `Elder-Scape` / `ElderScape` |
| `hello-ai` | Worker | `hello-ai` |
| `hello-ai-worker-rsmv` | Worker | `hello-ai-worker-rsmv` |
| `hello-ai-production` | Worker | `hello-ai` |
| `pick-of-gods` | Worker | `pick-of-gods` |
| `to-do-list-kv-template` | Worker | `to-do-list-kv-template-123` |
| `rs3-ai-bot-api` | Worker | `rs3-ai-bot-api` |

---

## GRAPH FOOTER — COMPLETE INVENTORY OF 62 REPOSITORIES
====================================================================================================

[SOURCE REPOSITORIES: 001–057]
├── 001 [S] POG2 (Public · HTML)
├── 002 [S] KING-WEN-I-CHING-IMMUTABLE-TABLES (Public · Python)
├── 003 [S] crimson-mode-81d1 (Public · JavaScript)
├── 004 [S] off-line-shap-e (Public)
├── 005 [S] Browder-Broder-er--Family-Tree (Public · HTML)
├── 006 [S] RS3Bplugins (Private · Lua)
├── 007 [S] KW-K2 (Public · HTML)
├── 008 [S] MHD-Propulsion-Controller-Simulator-main (Public · JavaScript)
├── 009 [S] king-wen-legal (Public · HTML)
├── 010 [S] Alt-1_Helper-Bridge (Public · HTML)
├── 011 [S] kingwen-oracle (Public · HTML)
├── 012 [S] kbro1989 (Public)
├── 013 [S] RUNESCAPE-WIDGETS (Public · HTML)
├── 014 [S] CfOllama (Public · TypeScript)
├── 015 [S] Willow-AI-Coding-Playground (Public · TypeScript)
├── 016 [S] King-Wen-Worker (Public)
├── 017 [S] I-Ching_Oracle (Public · TypeScript)
├── 018 [S] MHD-Propulsion-Controller-Simulator (Private · TypeScript)
├── 019 [S] Video-Automation-Remotion (Public · TypeScript)
├── 020 [S] willow-ai-game-dev (Public · TypeScript)
├── 021 [S] willow-ai-game-dev-hybrid (Public · TypeScript)
├── 022 [S] Ultimate-Kirby- (Public)
├── 023 [S] rscaievolution-png (Public · JavaScript)
├── 024 [S] rsc-globe1-pure (Public · JavaScript)
├── 025 [S] rsc-dashboard (Public · HTML)
├── 026 [S] rs3DiscAlt1HelperMemory (Public · JavaScript)
├── 027 [S] rs3-discord-bot (Public)
├── 028 [S] Rs3-ai-api (Public · JavaScript)
├── 029 [S] Pog2-Guttenberg- (Public)
├── 030 [S] Pog2-Data (Public)
├── 031 [S] Pog2-Core (Public · TypeScript)
├── 032 [S] Pog2-Atlas (Private)
├── 033 [S] POG-CLI-CODER (Public · JavaScript)
├── 034 [S] Pick_Of_Gods (Public · Python)
├── 035 [S] pick-of-gods (Public · JavaScript)
├── 036 [S] Kbro1989.github.io (Public · The Unlicense)
├── 037 [S] hello-ai (Public · JavaScript)
├── 038 [S] elderscape-modeleditor (Public · HTML)
├── 039 [S] hello-ai-worker-rsmv (Public)
├── 040 [S] ElderScape (Public · JavaScript)
├── 041 [S] Elder-Scape (Public · HTML)
├── 042 [S] D-sovereign- (Public · TypeScript)
├── 043 [S] Color-by-number (Public · TypeScript)
├── 044 [S] cloudflare-code-agent (Public · TypeScript)
├── 045 [S] CelestialArtisanBot (Public · Boost Software License 1.0)
├── 046 [S] bot.ps1 (Public · JavaScript)
├── 047 [S] Bathospire-Professor- (Public · TypeScript)
├── 048 [S] astro-blog-starter-template (Public · Astro)
├── 049 [S] Antigravity-Ultimate (Public · JavaScript)
├── 050 [S] ai-image-model (Public)
├── 051 [S] ai-game-studio (Public · TypeScript)
├── 052 [S] openrsc-vinilla (Public · JavaScript)
├── 053 [S] 2026-creative-strategy-summit (Public · HTML)
├── 054 [S] Pog2-Pedagogy (Public)
├── 055 [S] Willow-AI-Coding-Playground. (Public)
├── 056 [S] eldesrscape-modelviewer (Public)
└── 057 [S] models (Private)

[FORKED REPOSITORIES: 058–188]
├── 058 [F] trureturing <- the-omega-institute/trureturing (Public · Lean)
├── 059 [F] graphify <- Graphify-Labs/graphify (Public · Python)
├── 060 [F] unsuper_tts_asr <- RayeRen/unsuper_tts_asr (Public · HTML)
├── 061 [F] multilingual-kd-pytorch <- RayeRen/multilingual-kd-pytorch (Public · Python)
├── 062 [F] fastspeech-poster <- RayeRen/fastspeech-poster (Public)
├── 063 [F] data-mining-python <- RayeRen/data-mining-python (Public · HTML)
├── 064 [F] ml-for-3d-course <- huggingface/ml-for-3d-course (Public · MDX)
├── 065 [F] OpenJarvis <- open-jarvis/OpenJarvis (Public · Python)
├── 066 [F] pygraphviz <- pygraphviz/pygraphviz (Public · Python)
├── 067 [F] rs3-Watchdog <- GrynjolfLabs/rs3-Watchdog (Public · Lua)
├── 068 [F] rsmv <- skillbert/rsmv (Public · TypeScript)
├── 069 [F] maya-usd <- Autodesk/maya-usd (Public · Wolfram Language)
├── 070 [F] quantum-simulation <- rasidi3112/quantum-simulation (Public · Python)
├── 071 [F] hyperframes <- heygen-com/hyperframes (Public · TypeScript)
├── 072 [F] remotion <- remotion-dev/remotion (Public · TypeScript)
├── 073 [F] react-spring <- pmndrs/react-spring (Public · TypeScript)
├── 074 [F] pixijs <- pixijs/pixijs (Public · TypeScript)
├── 075 [F] alt1 <- skillbert/alt1 (Public · TypeScript)
├── 076 [F] libZotero <- fcheslack/libZotero (Public · JavaScript)
├── 077 [F] Token-Print <- Sudharsanselvaraj/Token-Print (Public · TypeScript)
├── 078 [F] cookbook <- google-gemini/cookbook (Public · Jupyter Notebook)
├── 079 [F] runelite-watchdog <- adamk33n3r/runelite-watchdog (Public · Java)
├── 080 [F] prompt2rig <- blendi-remade/prompt2rig (Public · JavaScript)
├── 081 [F] entity-hider <- Rcm37/entity-hider (Public · Lua)
├── 082 [F] job-gauges-official-api <- NadyaNayme/job-gauges-official-api (Public · Lua)
├── 083 [F] tripo-python-sdk <- Tripo-Developer/tripo-python-sdk (Public · Python)
├── 084 [F] cinder <- NorfolkNChance/cinder (Public · Python)
├── 085 [F] colibri <- JustVugg/colibri (Public · C)
├── 086 [F] universal-modder <- pick-of-gods/universal-modder (Public · Python)
├── 087 [F] rsc-editor <- iraqnroll/rsc-editor (Public · TypeScript)
├── 088 [F] Reverse-Engineer-anything <- NabilRFG12/Reverse-Engineer-anything (Public · TypeScript)
├── 089 [F] BigData_Arxiv_Analysis <- AureleoPKU/BigData_Arxiv_Analysis (Public · Python)
├── 090 [F] zotero-docs <- zotero/zotero-docs (Public · HTML)
├── 091 [F] mwparserfromhell <- earwig/mwparserfromhell (Public · Python)
├── 092 [F] Kimi-K2 <- MoonshotAI/Kimi-K2 (Public · Other)
├── 093 [F] gibberlink <- PennyroyalTea/gibberlink (Public · TypeScript)
├── 094 [F] MUGEN <- pick-of-gods/MUGEN (Public · Python)
├── 095 [F] shap-e <- openai/shap-e (Public · Python)
├── 096 [F] runelite <- NorfolkNChance/runelite (Public · Java)
├── 097 [F] zotero-api-client <- pick-of-gods/zotero-api-client (Public · JavaScript)
├── 098 [F] skills-1 <- anthropics/skills (Public · Python)
├── 099 [F] OpenUSD <- PixarAnimationStudios/OpenUSD (Public · C++)
├── 100 [F] godot <- Alberto12345678999/godot (Public · C++)
├── 101 [F] fafbseg <- natverse/fafbseg (Public · R)
├── 102 [F] knowledge-work-plugins <- anthropics/knowledge-work-plugins (Public · Python)
├── 103 [F] image2cpp <- javl/image2cpp (Public · JavaScript)
├── 104 [F] mathlib4 <- leanprover-community/mathlib4 (Public · Lean)
├── 105 [F] trl <- huggingface/trl (Public · Python)
├── 106 [F] bevy <- bevyengine/bevy (Public · Rust)
├── 107 [F] DeCAL <- AureleoPKU/DeCAL (Public · Python)
├── 108 [F] ollama <- ollama/ollama (Public · Go)
├── 109 [F] FPCO-Dialog <- lab-klc/FPCO-Dialog (Public)
├── 110 [F] voicebox <- pick-of-gods/voicebox (Public · JavaScript)
├── 111 [F] 3D-Vision-Benchmark <- UFPR-IPASP-PR/3D-Vision-Benchmark (Public · Python)
├── 112 [F] github-changelog-generator <- seando-adsk/github-changelog-generator (Public · Ruby)
├── 113 [F] jacobian-lens <- anthropics/jacobian-lens (Public · Python)
├── 114 [F] ArtificialRosettaStone <- pick-of-gods/ArtificialRosettaStone (Public · TeX)
├── 115 [F] spectral-diffusion-playground <- pick-of-gods/spectral-diffusion-playground (Public · Python)
├── 116 [F] malecns <- natverse/malecns (Public · R)
├── 117 [F] Pix2Text <- breezedeus/Pix2Text (Public · Jupyter Notebook)
├── 118 [F] anime <- juliangarnier/anime (Public · JavaScript)
├── 119 [F] Pumpkin <- vyPal/Pumpkin (Public · Rust)
├── 120 [F] coconatfly <- natverse/coconatfly (Public · R)
├── 121 [F] react-base-table <- Autodesk/react-base-table (Public · TypeScript)
├── 122 [F] rag-copilot-app <- tejus09/rag-copilot-app (Public · Python)
├── 123 [F] Kimi-K2.5 <- MoonshotAI/Kimi-K2.5 (Public · Other)
├── 124 [F] kimi-code <- MoonshotAI/kimi-code (Public · TypeScript)
├── 125 [F] kosong <- MoonshotAI/kosong (Public)
├── 126 [F] kimi-cli <- MoonshotAI/kimi-cli (Public · Python)
├── 127 [F] EasyEdit <- zjunlp/EasyEdit (Public · Jupyter Notebook)
├── 128 [F] cavegemma <- JuliusBrussee/cavegemma (Public · Python)
├── 129 [F] Megatron-LM <- NVIDIA/Megatron-LM (Public · Python)
├── 130 [F] octobuild <- NorfolkNChance/octobuild (Public · Rust)
├── 131 [F] to-do-list-kv-template-123 <- cloudflare/to-do-list-kv-template-123 (Public · JavaScript)
├── 132 [F] templates <- cloudflare/templates (Public · JavaScript)
├── 133 [F] skills <- vercel-labs/skills (Public · TypeScript)
├── 134 [F] rs3-ai-bot-api <- pick-of-gods/rs3-ai-bot-api (Public · TypeScript)
├── 135 [F] my-chat-agent <- pick-of-gods/my-chat-agent (Public · TypeScript)
├── 136 [F] multiplayer-globe-template <- pick-of-gods/multiplayer-globe-template (Public · TypeScript)
├── 137 [F] llm-chat-app-template <- pick-of-gods/llm-chat-app-template (Public · JavaScript)
├── 138 [F] hermes-agent <- NousResearch/hermes-agent (Public · Python)
├── 139 [F] ai-sec-resources <- Arcanum-Sec/ai-sec-resources (Public · HTML)
├── 140 [F] ai-chat <- pick-of-gods/ai-chat (Public · TypeScript)
├── 141 [F] open-design <- nexu-io/open-design (Public · TypeScript)
├── 142 [F] kingwenfinance <- pick-of-gods/kingwenfinance (Public · Python)
├── 143 [F] archive-org-api-knowledge-base <- LARIkoz/archive-org-api-knowledge-base (Public)
├── 144 [F] Core-Framework <- Open-RSC/Core-Framework (Public · Java)
├── 145 [F] lore-desktop <- NorfolkNChance/lore-desktop (Public · Rust)
├── 146 [F] experimental-projects <- trizen/experimental-projects (Public · Perl)
├── 147 [F] ai-video-avatar <- VinceBmmrt/ai-video-avatar (Public · TypeScript)
├── 148 [F] video <- ed-donner/video (Public · TypeScript)
├── 149 [F] ScopeEdit <- lab-klc/ScopeEdit (Public · Python)
├── 150 [F] world-of-claudecraft <- NorfolkNChance/world-of-claudecraft (Public · TypeScript)
├── 151 [F] TES5Edit <- TES5Edit/TES5Edit (Public · Pascal)
├── 152 [F] vla-lab <- lz-googlefycy/vla-lab (Public · Python)
├── 153 [F] CheXmix <- StanfordMIMI/CheXmix (Public · Python)
├── 154 [F] neuprintr <- natverse/neuprintr (Public · R)
├── 155 [F] cuda-gdb <- NVIDIA/cuda-gdb (Public · C)
├── 156 [F] NemoClaw <- mainroach/NemoClaw (Public · TypeScript)
├── 157 [F] evals <- openai/evals (Public · Python)
├── 158 [F] personal-website <- NorfolkNChance/personal-website (Public · Python)
├── 159 [F] openai-realtime-solar-system <- openai/openai-realtime-solar-system (Public · TypeScript)
├── 160 [F] GeoMotionGPT <- pick-of-gods/GeoMotionGPT (Public · Python)
├── 161 [F] OpenClaw-Kimi2.5-FreeAPI <- Ryuki0x1/OpenClaw-Kimi2.5-FreeAPI (Public · Shell)
├── 162 [F] K2-Vendor-Verifier <- MoonshotAI/K2-Vendor-Verifier (Public · Python)
├── 163 [F] oeis-tui <- hako/oeis-tui (Public · Rust)
├── 164 [F] tensorflow-riemopt <- master/tensorflow-riemopt (Public · Python)
├── 165 [F] viral-twin <- pick-of-gods/viral-twin (Public)
├── 166 [F] Miles <- cheneyYoon/Miles (Public · Python)
├── 167 [F] collisionvis <- splash-damage/collisionvis (Public · C++)
├── 168 [F] mesop-app <- NorfolkNChance/mesop-app (Public · Python)
├── 169 [F] SimTeach <- chrisma71/SimTeach (Public · TypeScript)
├── 170 [F] Red9_StudioPack_Python3 <- markj3d/Red9_StudioPack_Python3 (Public · Python)
├── 171 [F] NorfolkNChance.github.io <- NorfolkNChance/NorfolkNChance.github.io (Public · HTML)
├── 172 [F] Upgraded-Depth-Anything-V2 <- MackinationsAi/Upgraded-Depth-Anything-V2 (Public · Python)
├── 173 [F] spinningup <- openai/spinningup (Public · Python)
├── 174 [F] point-e <- openai/point-e (Public · Python)
├── 175 [F] glide-text2im <- openai/glide-text2im (Public · Python)
├── 176 [F] Red9_StudioPack <- markj3d/Red9_StudioPack (Public · Python)
├── 177 [F] diffusion <- hojonathanho/diffusion (Public · Python)
├── 178 [F] runelite-open-osrs <- open-osrs/runelite (Public · Java)
├── 179 [F] Automatic-Number-Plate-Recognition-Using-YOLOv7-EasyOCR <- ANPR-ORG/Automatic-Number-Plate-Recognition-Using-YOLOv7-EasyOCR (Public · Jupyter Notebook)
├── 180 [F] plugins <- open-osrs/plugins (Public · Java)
├── 181 [F] gta-re3 <- hackpascal/gta-re3 (Public · C++)
├── 182 [F] fairseq-1 <- RayeRen/fairseq-1 (Public · Python)
├── 183 [F] GrNet <- zhiwu-huang/GrNet (Public · MATLAB)
├── 184 [F] tradigitools <- markj3d/tradigitools (Public · C++)
├── 185 [F] wavenet_vocoder <- RayeRen/wavenet_vocoder (Public · Python)
├── 186 [F] translators <- fcheslack/translators (Public · JavaScript)
├── 187 [F] tensor2tensor <- RayeRen/tensor2tensor (Public · Python)
└── 188 [F] training-exercise <- pick-of-gods/training-exercise (Public · JavaScript)

SUMMARY: 62 Source [S] + 126 Forked [F] = 188 Total Repositories | View: Kbro1989 (https://github.com/Kbro1989?tab=repositories)

====================================================================================================


