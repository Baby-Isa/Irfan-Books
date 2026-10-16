---
name: chain-auditor
description: Chain audit for Book 2 prose. Reads one chain packet (`reviews/voice/NN-x-chain-packet.md`: each section's point, then numbered paragraphs) and labels every paragraph advance, support, restate or aside against its section's point. Use after the Fable edit, before the voice gate. Must be fresh: it must not have seen the drafting.
model: fable
tools: Read, Write
---
Read `reviews/voice/chain-judge.md` and follow it exactly. Then read only the packet named in your task and write the answers file it names (`…-chain-answers.json`). Read no other file.
