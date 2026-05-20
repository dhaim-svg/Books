# VSCode + Claude Toolkit for a Cozy LitRPG Murder Mystery: Free Tools, Skills & Workflow

## TL;DR
- **Use the existing "story-skills" Claude Code plugin (danjdewhurst/story-skills) plus the "Markdown Fiction Writer" VSCode extension as your spine**, layered on a Pandoc-based folder-of-Markdown manuscript and a Git repo for version control — this gives you Scrivener-like organization, AI-assisted drafting that respects your story bible, and clean DOCX/EPUB exports without paying for Sudowrite or NovelCrafter.
- **Treat your story bible as data, not chat history**: keep `bible/`, `characters/`, `worldbuilding/`, and `plot/` as Markdown files in your repo so Claude Code (free for Pro users via the Claude.ai subscription, or pay-as-you-go via API) reads them every session — this is the only reliable way to keep your LitRPG system rules, the central murder twist, and character voices consistent across 80–100K words.
- **For privacy and zero recurring cost, pair Continue.dev + Ollama (running Qwen2.5 or Llama 3.1 locally) for inline suggestions, and reserve cloud Claude only for high-leverage editorial passes (developmental edits, continuity audits, twist-foreshadowing checks)** — local models are good enough for "next-sentence" autocomplete on cozy prose, while Claude/Sonnet remains markedly better for whole-chapter critique.

---

## Key Findings

1. **There are now genuine fiction-writing Claude Skills, not just adapted coding skills.** Three actively maintained, free repos (`danjdewhurst/story-skills`, `haowjy/creative-writing-skills`, and `rhavekost/author-toolkit`'s `fiction-workshop`) implement story-bible-aware multi-stage workflows specifically for novelists, all built on the open SKILL.md standard adopted by Claude Code, Codex, Cursor, Gemini CLI, Copilot, and others.
2. **VSCode now has a credible "Scrivener-lite" stack.** `zoctarine/vscode-fiction-writer` ("Markdown Fiction Writer") provides dialogue syntax, document statistics, focus/typewriter mode, file-tagging, and YAML metadata; combined with Foam (wikilinks + graph) and Markdown All in One, it covers the core Scrivener features that fiction writers actually use.
3. **The proven manuscript workflow is "folder of Markdown chapters → Pandoc → DOCX/EPUB".** Multiple published novelists use exactly this pipeline — Jay Penner's blog post is titled "How I've written over 1 million words across 16 novels using Visual Studio Code and Markdown—30–40% faster than Word or Scrivener" (jaypenner.com). `jp-fosterson/pandoc-novel` is a turnkey template that produces KDP-ready PDF, EPUB, and SFFMS-format manuscripts via `make`.
4. **Avoid Dendron — it's in maintenance only.** Kevin Lin announced on February 8, 2023 in the Dendron Discord (per randomgeekery.org): "the tldr: we spent the past two years building a better way for humans to manage knowledge. While we made great strides there, as a business, we were ultimately not able to find product market fit for a venture backed business… we've made the decision to do a pivot and pursue other business problems." Foam, while less feature-rich, is still actively developed and is the safer PKM choice for a long novel project. (NovelWriter, a separate standalone Qt app — vkbo/novelWriter — is also actively maintained and worth considering as an alternative front-end onto the same Markdown files.)
5. **For local privacy, the Continue.dev + Ollama combo works for prose, not just code.** Continue is model-agnostic; pointing it at a general-purpose Ollama model (Llama 3.1 8B or Qwen 2.5 7B at Q4_K_M, ~5–8 GB VRAM) gives you free, offline, ghost-text autocompletion inside `.md` files. Cline (formerly Claude Dev) is the more autonomous alternative if you want agent-style editing of multiple chapter files at once.
6. **Lorebook tooling from the SillyTavern/NovelAI world ports cleanly to a VSCode + Claude Code project.** Existing Wikipedia-based lorebook generators (`grahamwaters/lorebook_generator_for_novelai`, `TaleirOfDeynai/NAI-Lore-Helper`) can be repurposed to seed your bible, and the *concept* of keyword-triggered context injection is exactly what Claude Skills already do natively, with no need for a separate vector DB for a single novel.

---

## Details

### A) VSCode extensions for fiction writing

**Tier 1 — Install these first (free, actively used by novelists):**

| Extension | What it does | Why it matters for a cozy murder mystery |
|---|---|---|
| **Markdown Fiction Writer** (`vsc-zoctarine.markdown-fiction-writer`, GitHub: `zoctarine/vscode-fiction-writer`) | Document statistics, dialogue syntax with em-dash markers, file tagging, YAML metadata, "Writing Mode" (Zen + typewriter + custom theme), export | The single most fiction-specific VSCode extension. Author labels it Beta but it's been stable through 2024–2025. Repository activity since the last release should be confirmed before adoption. |
| **Markdown All in One** (`yzhang.markdown-all-in-one`) | Keyboard shortcuts for bold/italics, TOC generation, list editing, math, auto-preview | Replaces the missing "rich-text" feel of Word; bold/italic shortcuts are the single biggest quality-of-life gain over plain Notepad. |
| **Foam** (`foam.foam-vscode`, MIT, actively maintained) | Wikilinks `[[character]]`, backlinks, daily notes, knowledge graph, embeds | Lets you link `[[Detective Vera]]` from Chapter 7 to her profile in `characters/vera.md` and see backlinks — your story bible becomes navigable. |
| **LanguageTool** (`davidlday.languagetool-linter` is the most active fork; the older `adamvoss.vscode-languagetool` is unmaintained) | Offline grammar/style check via local LanguageTool server | Free Grammarly alternative; runs locally so your manuscript never leaves the machine. The `LTeX+` server-mode setup also lets you connect to LanguageTool's free public API if you don't want to run Java locally. |
| **Code Spell Checker** (`streetsidesoftware.code-spell-checker`) | Inline spell check with custom dictionaries | Add character names ("Elara," "Veridian") to a project-level dictionary so they don't underline forever. |
| **Word Count** (`ms-vscode.wordcount` — Microsoft's sample) and **WordCounter** (`kirozen.wordcounter`) | Status-bar word counts | The Microsoft sample only counts active Markdown files. `kirozen.wordcounter` adds reading-time, character count, paragraph stats — closer to Scrivener's session targets. **`always-onward.writersWordCountVscode` ("Wordcount for writers")** adds daily/weekly tracking against goals — the closest free analogue to Scrivener's project targets. |
| **Markdown PDF** (`yzane.markdown-pdf`) and **vscode-pandoc** (`DougFinke.vscode-pandoc` original, `ChrisChinchilla.vscode-pandoc` is the more recently updated fork) | One-click export to DOCX/PDF/HTML via Pandoc | The fork updates Pandoc invocation patterns and adds Docker support; pick the fork. |
| **Writer Mode** (`noaal.writer-mode`) | Zen + typewriter scrolling + writing-specific theme switching | Fixes VS Code's default Zen Mode by adding centered editor and font-size override. The `Markdown Fiction Writer` extension also bundles its own "Writing Mode" with similar features — pick one. |

**Tier 2 — Useful adjuncts:**

- **Excalidraw** (`pomdtr.excalidraw-editor`) for hand-drawn whiteboard maps of suspects/timelines.
- **Todo Tree** (`Gruntfuggly.todo-tree`) — tag `// TODO: foreshadow the locked-room twist here` and the panel becomes your revision punch-list. (You'll want to use HTML comments `<!-- TODO ... -->` in Markdown so the TODO doesn't render in exports.)
- **GitDoc** (`vsls-contrib.gitdoc`) auto-commits/pushes on save — a "track changes on steroids" backup story.
- **VS Code for Writers** extension pack (`danspinola.vscode-for-writers`) — bundles spell check, Markdown, and a few writing tweaks; useful as a starter if you want a one-click setup.

**Tier 3 — Skip:**

- **Dendron** (`dendron.dendron`) — explicitly in maintenance mode since Feb 8, 2023 (per founder Kevin Lin's Discord announcement quoted above). Don't start a multi-year project on it.
- **Code Typewriter Effect** (`junsantilla.code-typewriter-effect`) — a visual gimmick that types characters one-at-a-time; not actual typewriter scrolling.
- The **VSCode Marketplace "StoryCraftr"** extension promises AI outlining/character development inside VS Code, but its repository activity should be checked before adoption — be cautious about marketplace extensions making AI promises with thin support.

### B) AI-assisted writing tools (free / open source)

**Cloud — Claude (free Pro tier or pay-as-you-go API):**

The single most important shift in 2025–2026 is **Agent Skills** — Anthropic published the SKILL.md spec on December 18, 2025; per a March 23, 2026 paperclipped.de retrospective, "48 hours: Microsoft integrated Agent Skills into VS Code via Copilot. OpenAI added support to ChatGPT and Codex CLI. The GitHub repository crossed 20,000 stars." Within ~90 days 32 tools (Codex, Cursor, Gemini CLI, Junie, Goose, Kiro, etc.) shipped support. (Adoption figures and specific dates vary by source; see the Caveats section.) Skills are folders with a `SKILL.md` (YAML frontmatter + Markdown instructions) that the model loads progressively — only ~100 tokens for the metadata at startup, then full instructions only when activated.

For your novel, the three skill repos that matter:

1. **`danjdewhurst/story-skills`** (MIT, 11 stars, 13 commits) — **Recommended starting point.** Five skills: `story-init` (scaffolds project structure), `character-management`, `worldbuilding`, `plot-structure` (three-act, hero's journey, save-the-cat, kishōtenketsu), and `chapter-writing` (outline-first, pulls context from all story files). Install in Claude Code with two commands: `/plugin marketplace add danjdewhurst/story-skills` then `/plugin install story-skills@story-skills`. Includes a worked example `examples/the-last-ember/` with three characters, magic system, plot arc, and first chapter prose.
2. **`haowjy/creative-writing-skills`** (Apache-2.0, 31 stars; latest release v0.0.4 on Nov 2, 2025) — README on the `main` branch describes 6 skills (`cw-router`, `cw-prose-writing`, `cw-story-critique`, `cw-style-skill-creator`, `cw-brainstorming`, `cw-official-docs`) with slash commands `/bs`, `/write`, `/wiki`, `/critique`. Search-indexed content references an alternative architecture with 11 named agents (muse, brainstormer, character-sim, outliner, writer, critic, revision-writer, reader-sim, continuity-checker, chronicler, style-creator) — this may be on a branch or in pending docs; verify before relying on it. Install: `claude plugin marketplace add haowjy/creative-writing-skills` then `claude plugin install creative-writing-skills@creative-writing-skills`.
3. **`rhavekost/author-toolkit` → `fiction-workshop`** skill (~61 GitHub stars per mcpmarket.com listing, license/last-commit not directly confirmed) — three-stage workflow ("Story Bible Building, Chapter Development, and Reader Testing") with editorial personas: **Developmental Editor, Line Editor, Character Consultant, and Continuity** (the SKILL.md routes prose tasks: "Structure/pacing → Developmental | Prose → Line | Voice → Character | Facts → Continuity"). Install via Skill.Fish: `npx skillfish add rhavekost/author-toolkit fiction-workshop`. The most editor-mindset of the three.

**Other useful AI-side repos:**

- **`ThomasHoussin/Claude-Book`** — multi-agent novel framework with explicit `bible/` (permanent) vs `state/` (per-chapter) directory split, a perplexity-improver to reduce AI-detectable patterns, EPUB/MOBI/AZW3 build script, and subagents for consistency checks. Hacker News–featured. Originally French but works in English.
- **`forsonny/Claude-Code-Novel-Writer`** — fully autonomous "write a 100K-word fantasy novel with no human input" system. **Not recommended for your use case** — you have a story bible and a specific twist; you want a co-author, not autopilot.
- **`anthropics/skills`** (the official Anthropic skills repo) — useful patterns; their `skill-creator` skill is the easiest way to author your own personalized skills (e.g., a `cozy-litrpg-prose` skill that captures your specific voice and genre conventions).

**Local — Continue.dev + Ollama for offline / private inline suggestions:**

Continue is model-agnostic, MIT-licensed, and connects to any LLM backend. The setup pattern most relevant for fiction:

```yaml
# config.yaml — use a general model for chat, a small model for tab autocomplete
models:
  - name: Llama 3.1 8B
    provider: ollama
    model: llama3.1:8b
    roles: [chat, edit, apply]
    defaultCompletionOptions:
      temperature: 0.7        # higher for prose than for code
      contextLength: 8192
  - name: Qwen2.5 1.5B
    provider: ollama
    model: qwen2.5-coder:1.5b  # small/fast = good autocomplete even on prose
    roles: [autocomplete]
  - name: Nomic Embed
    provider: ollama
    model: nomic-embed-text
    roles: [embed]            # for @codebase-style retrieval over your bible
```

Important caveat: code-tuned models like StarCoder and Codellama produce odd suggestions on narrative prose. Use general instruction-tuned models (Llama 3.1, Qwen 2.5 base, Mistral 7B) — not code-specific ones — for prose autocomplete.

**Cline** (`saoudrizwan.claude-dev`, Apache 2.0; per deployhq.com as of May 2026: "5M+ installs, 61.2k GitHub stars, currently shipping at v3.81") is the more autonomous option — it can edit multiple chapter files in a single task, asks for approval at each step, and supports Anthropic, OpenAI, Gemini, AWS Bedrock, Ollama, and LM Studio. For a novel, Plan/Act mode is genuinely useful: in Plan mode it reads `bible/` + several chapters with no risk of edits, then in Act mode it makes the changes. Use it for tasks like "find and rewrite every scene where the magic system contradicts `bible/magic-system.md`."

**SillyTavern / NovelAI lorebook ecosystem (worth knowing about, not directly recommended):**

- `grahamwaters/lorebook_generator_for_novelai` (Wikipedia → lorebook auto-population) — useful if your cozy LitRPG uses real-world locations or historical periods you want auto-summarized.
- `TaleirOfDeynai/NAI-Lore-Helper` (advanced regex-keyed lorebooks) — for complex keyword-trigger logic.
- The general "lorebook" pattern (keyword in story → relevant entry injected into context) is *exactly* what Claude Skills do natively, so for a Claude-centric workflow you don't need a separate lorebook tool. But if you ever want to switch to a local LLM with smaller context, lorebook-style retrieval becomes essential, and these tools are battle-tested.

### C) Story bible / lorebook / consistency tools

For a single novel with a single twist, you do **not** need a vector database or full RAG setup. Plain Markdown files + Claude's native context handling is sufficient up to ~150K words. The key structural pattern (used by Claude-Book, story-skills, and Claude-Code-Novel-Writer alike):

```
my-novel/
├── CLAUDE.md                    # Master instructions: genre, POV, style, twist (in spoiler block)
├── bible/                       # PERMANENT — never changes mid-draft
│   ├── style.md                 # voice, tense, POV rules, no-no words
│   ├── genre.md                 # cozy LitRPG mystery conventions
│   ├── characters/              # one .md per character
│   │   ├── _template.md
│   │   └── detective-vera.md
│   ├── worldbuilding/
│   │   ├── litrpg-system.md     # leveling, classes, the rules MUST be consistent
│   │   ├── locations/
│   │   └── timeline.md
│   └── plot/
│       ├── arc-overview.md
│       ├── twist.md             # the murder reveal — load only when needed
│       └── foreshadowing.md     # checklist of clues planted vs. paid off
├── state/                       # TRANSIENT — versioned per chapter
│   └── chapter-NN/              # what's known to whom at this point
├── manuscript/
│   ├── chapter-01.md
│   ├── chapter-02.md
│   └── ...
└── notes/                       # research, beta-reader feedback
```

This is the structure `ThomasHoussin/Claude-Book` uses, and it generalizes well. The critical insight from that repo: separate **permanent** bible (style, characters, system rules) from **transient** state (what each character knows at chapter N) — otherwise the AI will leak your twist or contradict earlier chapters' epistemology.

**For tracking what each character knows when (vital for a murder mystery):** create `state/chapter-NN/known-facts.md` with three columns — Fact / Who Knows / How Revealed. Update it after every chapter. This is the single most valuable consistency artifact for a mystery; no tool will catch a knowledge-leak the way a per-chapter ledger will.

**Aeon Timeline alternative, free:** the open-source `vkbo/novelWriter` (separate standalone app, GPLv3) has built-in cross-referencing, character/location indexing, and Novel View — you can keep the same Markdown files and open them in either VSCode or novelWriter as needed.

### D) Manuscript management workflow

**Pandoc compile pipeline** — the proven novelist workflow:

```bash
# combine chapters into single manuscript and export
pandoc manuscript/chapter-*.md \
  --reference-doc=templates/manuscript-reference.docx \
  -o build/cozy-litrpg-mystery.docx
```

Use `jp-fosterson/pandoc-novel` (template repo) for a complete `make`-based build that produces:
- KDP-ready printable PDF (via LaTeX)
- EPUB (for beta readers and self-publishing)
- SFFMS-format manuscript PDF (the standard submission format if you ever query agents)

Note: Jay Penner's previously hosted **QuillDrop** web service has been discontinued. Per jaypenner.com/quilldrop: "The QuillDrop service has been discontinued. Thank you for your interest… the core logic of QuillDrop has been enhanced and now lives on as a powerful command-line tool I use to produce all my books." Use `jp-fosterson/pandoc-novel` or roll your own Pandoc reference-doc workflow instead.

**Git workflow for a novelist** (proven by Chris Rosser, Jay Penner, and others):

- `main` branch = current canonical draft.
- `draft-2`, `draft-3` branches when you start a major rewrite.
- Tag each beta-reader release: `git tag beta-reader-v1`.
- Use `git diff` to see exactly what changed between drafts — better than Word's "Track Changes" because it survives indefinitely.
- A private GitHub repo is free and gives you offsite backup. (Verify GitHub's current free private repo policy; this is widely available but check before relying on it.)
- For beta-reader feedback, accept comments as Markdown footnotes or pull requests if your readers are technical; otherwise export to DOCX, take comments in Word, then manually integrate.

**File naming:** `chapter-01.md` through `chapter-NN.md` is sortable, Pandoc-friendly, and survives reorganization. Avoid descriptive names in filenames (`chapter-the-detective-arrives.md`) because chapter purposes change during revision; put descriptive names in the YAML frontmatter instead:

```yaml
---
chapter: 1
title: "The Detective Arrives"
pov: Vera
location: village-square
status: draft-2
words: 3120
---
```

### E) Claude Skills relevant to fiction writing on skills.sh / agentskills.io / SkillsMP

Beyond the three fiction-specific repos above, several general-purpose skills are useful in a novel workflow:

- **`skill-creator`** (from `anthropics/skills`) — the meta-skill that interviews you about a repeated task and produces a SKILL.md. Use this to capture YOUR voice: "I want a skill called `cozy-litrpg-voice` that maintains my specific narrator tone — third-limited, present tense, gentle humor, no graphic violence, integrate game-system terms in italics."
- **Style-calibration skills** in `Imbad0202/academic-research-skills` and various content-writer repos — adapted to fiction, the pattern is "show me 2,000 words of your writing, and I'll generate a style guide that captures your sentence-length distribution, vocabulary, and rhythm."
- **`obra/superpowers`** — general Claude Code skills library; the `/brainstorm`, `/write-plan`, `/execute-plan` commands work well for plot-level brainstorming sessions.
- **Skill registries to browse:** `agentskills.io` (the open-standard home), `skills.sh` (Vercel's marketplace, focused on developer skills but searchable), `skillsmp.com`, `agentskill.sh`, and `skillsllm.com`. None has a deep fiction-writing category yet — most fiction skills are discovered via GitHub search rather than these registries.

**Caveat on skills.sh specifically:** the marketplace is heavily developer-skewed (frontend-design, azure-ai, remotion-best-practices are the top installs). The fiction-writing category is small but growing; expect to discover most relevant skills via GitHub topic search (`creative-writing`, `fiction`, `claude-code-plugin`) rather than the registry's UI.

### F) Reddit / community recommendations & pitfalls

The recurring patterns across r/writing, r/ClaudeAI, r/LocalLLaMA, and Hacker News discussions:

**Things real writers do:**
- Treat AI as scaffolding, not as a final-prose generator. Kenny Kane (multi-book author): "Claude is an exceptional writing partner when you treat it as a system, not a shortcut. It excels at structure, iteration, and maintaining consistent voice across long-form projects. It fails spectacularly when you ask it to replace your thinking."
- Use AI heaviest at outline and revision; lightest at first-draft prose. The "kitbashing" technique (Future Fiction Academy) is to have Claude produce 3–5 versions of a paragraph and you assemble the best sentences — far better than accepting any single AI draft.
- **Genre fit matters.** Cozy mystery + LitRPG is an established commercial genre with predictable beats — Claude handles it markedly better than literary or experimental fiction. This is good news for your project.

**Pitfalls to avoid:**
- Re-explaining context every session is the #1 time waster. Skills + a `CLAUDE.md` with permanent project context fixes this.
- Letting AI write the twist or the climactic reveal scene yourself. Save those for human-only drafting; AI tends toward predictable resolutions.
- Trusting the model's claimed "memory" of your bible. Always verify by asking "what is Vera's middle name?" before a session — if it gets it wrong, you've discovered a context-loading bug.
- Over-tuning the local LLM. A 7B model on consumer hardware is genuinely useful for autocomplete and brainstorming, but will flatten your prose if you let it write paragraphs. Use it for *sentences* and *suggestions*, not chapters.
- Mobile editing. There is no real VSCode for iOS/Android; Working Copy + iA Writer or 1Writer over a synced folder (iCloud, Dropbox, syncthing) is the practical mobile escape hatch.

---

## Recommendations

### Stage 1 (this week) — Set up the writing environment

1. **Install the VSCode core stack:** Markdown Fiction Writer, Markdown All in One, Foam, LanguageTool Linter (with a local LanguageTool jar), Code Spell Checker, vscode-pandoc (Chinchilla fork), Wordcount for writers, Excalidraw, Todo Tree.
2. **Initialize the project structure** — clone `jp-fosterson/pandoc-novel` as your build skeleton, but replace the `text/` directory with the `bible/`+`manuscript/`+`state/` split from `ThomasHoussin/Claude-Book`.
3. **Initialize Git** — `git init`, push to a private GitHub repo. Add `.gitignore` for build artifacts. Set up GitDoc for auto-commit-on-save.
4. **Migrate your existing story bible** into `bible/characters/*.md`, `bible/worldbuilding/litrpg-system.md`, etc. Put the twist in `bible/plot/twist.md` and use Foam wikilinks to connect everything.
5. **Test the export pipeline** — write 500 dummy words, run the Pandoc make target, confirm DOCX/EPUB output looks correct.

**Benchmark to advance:** You can write a chapter, see live word count, get spell/grammar squiggles, and one-command-export to DOCX.

### Stage 2 (next two weeks) — Add Claude Skills

1. **Install Claude Code** (free with Claude Pro, or via API key with usage credits).
2. **Install `danjdewhurst/story-skills` first** — it's the simplest, has 5 well-scoped skills, and matches the file structure you just built.
3. **Add `rhavekost/author-toolkit` `fiction-workshop`** alongside it — its three-stage editorial personas (Developmental, Line, Character, Continuity) complement story-skills' more generative skills.
4. **Write a `CLAUDE.md`** at project root with: genre ("cozy LitRPG murder mystery"), POV/tense rules, the "do not spoil the twist unless I'm in a `plot/twist.md` editing session" guardrail, and pointers to the bible files.
5. **Use `skill-creator`** to author one custom skill: `cozy-litrpg-voice` that captures your specific narrator voice (paste 2K words of your existing prose, let it extract patterns).

**Benchmark to advance:** You can ask Claude Code "draft scene 3 of chapter 7 from Vera's POV" and it correctly pulls from the bible without spoiling the twist.

### Stage 3 (ongoing) — Local LLM for privacy and zero-cost autocomplete

1. **Install Ollama**, pull `llama3.1:8b` (general prose) and `qwen2.5:1.5b` (small/fast for autocomplete).
2. **Install Continue.dev**, configure with the YAML above. Test inline suggestions on a `.md` chapter file.
3. **Reserve cloud Claude for high-leverage tasks only:** developmental edits, line edits on completed chapters, continuity audits ("read manuscript/chapter-01.md through chapter-12.md and flag any contradictions with bible/litrpg-system.md"), and twist-foreshadowing checks.

**Benchmark to advance:** You can write entire scenes offline with no telemetry leaving your machine; you only invoke Claude for editorial passes.

### What would change these recommendations

- If your novel grows beyond ~150K words or becomes a series, switch to **Cline** + a vector store (the `@codebase` indexing in Continue uses Nomic Embed locally and works on Markdown).
- If you decide to monetize via serial publishing (Royal Road, KU), consider migrating to `vkbo/novelWriter` as a secondary editor for its built-in scene/chapter view — your Markdown files remain compatible.
- If LanguageTool's grammar coverage feels weak, the free **Grammarly browser extension** still works on a copy-pasted chapter; not local but free.
- If your hardware can't run Ollama (need ~8 GB VRAM for 7B models at Q4), drop the local-LLM tier and rely on Claude alone — your manuscript privacy then depends on Anthropic's data retention policy (Skills/Claude Code are not covered by Zero Data Retention by default).

---

## Caveats

1. **The Claude Skills ecosystem is ~6 months old at the time of this report (May 2026)** — the SKILL.md spec was published Dec 18, 2025. Repos may be young, with low star counts (story-skills: 11 stars, creative-writing-skills: 31). Treat them as scaffolds you'll fork and customize, not as battle-tested products. Anthropic itself warns: "We strongly recommend using Skills only from trusted sources" — audit any third-party SKILL.md before installing, since it can direct Claude to invoke tools or execute code.
2. **The Markdown Fiction Writer extension is labelled Beta** by its author with a warning that "major restructuring of settings and features will follow" — back up your settings before upgrading versions. The repo's last release date should be checked before adoption.
3. **Some search-indexed information about haowjy/creative-writing-skills references an 11-agent "Meridian" architecture** (muse, brainstormer, character-sim, etc.) that does not match the current `main`-branch README's 6-skill structure. The 11-agent system may live on a branch or in pending docs; verify against the live repo before committing to that architecture.
4. **For `rhavekost/author-toolkit` (Fiction Writing Workshop)**, the GitHub repo couldn't be directly fetched during this research; details (61 GitHub stars, three-stage workflow, persona names) come from secondary listings on mcpmarket.com and agentskills.so that quote the SKILL.md verbatim. Confirm the repo is active before depending on it.
5. **Adoption claims for the SKILL.md standard** ("32 tools in 90 days," "100K GitHub stars on anthropics/skills," "Vercel's skills.sh marketplace lists 89,753 skills") come from a March 2026 paperclipped.de retrospective and skills.sh promotional materials. Numbers should be cross-checked against current registries before quoting in publication; the trend is unambiguous but specific figures may vary.
6. **Claude Code's privacy model:** by default, "Agent Skills is not covered by ZDR arrangements. Skill definitions and execution data are retained according to Anthropic's standard data retention policy" (Anthropic platform docs). For a manuscript you intend to publish, this is unlikely to be a real problem (it's the same data-handling that applies to any Claude conversation), but it's not the airtight privacy of fully local Ollama.
7. **No tool catches every continuity error.** Even with a story bible, RAG, and an editorial skill, you will need beta readers and a human pass for: tone consistency, foreshadowing payoff, emotional pacing, cozy-genre tonal compliance (no graphic content sneaking in), and the murder-mystery's fairness rule (the reader must have all clues to solve it themselves). AI is a force multiplier, not a substitute.
8. **VSCode's mobile gap is real.** If you write on iPad or phone often, build your sync workflow (iCloud Drive, Working Copy, syncthing) into Stage 1, not as an afterthought. iA Writer and 1Writer both handle Markdown well on mobile and respect your folder structure.