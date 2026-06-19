---
name: summarize-document
description: Produce a faithful, concise summary of a long document while preserving key facts, figures, and the author's intended meaning.
version: 1.0.0
tags: [summarization, reading, analysis]
---

# Summarize Document

## Overview

This skill guides an agent through producing a high-fidelity summary of a long
document without distorting its claims.

## When to use

Use when the user provides a long document (report, article, transcript) and
wants a shorter version that preserves the substantive content.

## Instructions

1. Read the full document before writing anything.
2. Identify the thesis, the supporting points, and any quantitative claims.
3. Draft a summary at roughly 10-20% of the original length.
4. Preserve numbers, named entities, and qualifications exactly.
5. Do not introduce facts that are not present in the source.

## Notes

- Prefer the document's own terminology.
- See the [style guide](./STYLE.md) for tone conventions.
