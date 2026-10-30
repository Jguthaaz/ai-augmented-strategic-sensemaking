# AI-Augmented Strategic Sensemaking
**From the Art of the Possible to the Art of the Actionable.**

A developing consulting methodology for turning fragmented evidence and diverse executive perspectives into better-grounded strategic choices.

Created by **Jorge Alberto Gutierrez Haaz**, drawing on experience designing and facilitating 400+ executive co-creation workshops across Mexico and Central America.

[Leer en español](README.es.md) · [Pilot scope](docs/pilot-charter.md) · [Worked example](examples/customer-retention/README.md) · [Roadmap](ROADMAP.md)

## The business challenge
Leadership teams can have extensive information and powerful AI tools while still struggling to compare evidence, challenge dominant assumptions, surface disagreements, and decide what to do next. A polished SWOT does not establish which claims are supported.

The consultant's contribution is to frame the question, connect evidence with context, design productive conversations, and help the team turn uncertainty into testable action.

## What this project offers
- A practical playbook connecting diagnosis, hypothesis testing, and executive sensemaking.
- Reusable templates for evidence, hypotheses, decisions, and validation.
- A proposed agent architecture with explicit permissions and human review.
- A fully fictional customer-retention case.
- An evaluation plan that measures decision usefulness as well as preparation effort.

## Architecture and functional guide
Read the [Spanish project guide](docs/PROJECT-GUIDE.es.md) for the implemented architecture, a worked query, verification results, limits, and next steps.

## Start here
1. Read the [pilot charter](docs/pilot-charter.md).
2. Walk through the [synthetic case](examples/customer-retention/README.md).
3. Use the [hypothesis card](templates/hypothesis-card.md) and [evidence register](templates/evidence-register.csv).
4. Plan the discussion with the [workshop guide](docs/workshop-guide.md).
5. Compare outcomes using the [evaluation plan](docs/evaluation.md).

## Proposed workflow
Frame the strategic question → authorize and organize sources → check comparability → explore hypotheses → review exceptions → facilitate collective sensemaking → agree priorities and validation actions.

AI supports research, comparison, and synthesis. The consultant reviews strategic interpretations and facilitates the conversation. Client leaders retain decision authority.

## Project status
**Version 0.2: methodology plus a tested, local read-only MCP server.** The [MCP module](mcp/README.md) exposes four tools over stdio using synthetic evidence. Eight logic tests and a real SDK client handshake/tool-call check passed. Connection inside Cline is verified: all four tools were called in an end-to-end synthetic-data task, producing a cited Spanish synthesis. No autonomous consulting agent or validated client business outcomes are claimed.

Microsoft tools are an implementation option, not a verified deployment. This repository contains no client files, course handouts, or proprietary materials. It is an independent synthesis informed by professional experience and learning; it is not an official course framework or institutional endorsement.

## Contents
| Area | Contents |
|---|---|
| [MCP module](mcp/README.md) | Executable read-only evidence tools, three hypotheses, setup and tests |
| [Hugging Face demo](https://huggingface.co/spaces/jguthaaz/strategic-sensemaking-lab) | Separate static simulation; not connected to the local MCP server |
| [Playbook](docs/playbook.md) | Audit, Gauge, Engineer, Navigate, Track applied to this pilot |
| [Architecture](docs/agent-architecture.md) | Roles, handoffs, state, and escalation |
| [Governance](docs/governance.md) | Source authorization, review, isolation, and release controls |
| [Templates](templates/) | Copy-ready working artifacts |
| [Example](examples/customer-retention/) | Fictional evidence, hypotheses, and workshop decision |
| [Roadmap](ROADMAP.md) | From manual baseline to a bounded prototype |

## Contributing
See [contribution guidance](CONTRIBUTING.md). Use synthetic examples only. No reuse license is granted in this initial version; agree licensing with the author before redistribution or commercial reuse.
