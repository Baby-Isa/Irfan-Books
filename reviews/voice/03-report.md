# Voice gate: Chapter 03 (round 1, 2026-10-12)

## Profile
```

== book2/chapters/03-you-already-know-these-words.md  (1820 words, 35 paragraphs)
   measure                       chapter  exemplar   z
   words/paragraph                  52.0      55.4  -0.5
   words/sentence                   16.7      17.4  -0.4
   sentences over 30 words %         2.8      10.5  -1.1  drift
   'and' per 1k                     20.9      30.9  -0.7
   'but'/'yet' per 1k                1.2       3.9  -0.8
   semicolons per 1k                 2.4       7.7  -0.9
   colons per 1k                     2.4       8.7  -0.8
   dashes per 1k                     0.0       0.0  +0.0
   brackets per 1k                   4.8       3.5  +0.2
   questions per 1k                  0.6       0.3  +0.0
   'you/your' per 1k                 0.6       0.3  +0.4
   'we/us/our' per 1k                8.3      15.5  -0.5
   'let's' per 1k                    1.2       0.6  +0.3
   'this/these' per 1k              17.3      13.9  +0.5
   commas per sentence               0.9       1.0  -0.4
   And/But openers per 1k            0.0       0.3  -0.3
   colon-then-quote per 1k           0.0       0.6  -0.4
   longest paragraph                  92      ≤110
   Function-word Delta: median 0.86 over 9 chunks; 2/9 chunks beyond the exemplar's 90th percentile (0.99).
   Profile verdict: PASS

```

## Blind judge
```
Blind voice test 03: book2/chapters/03-you-already-know-these-words.md (control 7225b76:book2/chapters/01-seeking-not-powers.md)
  control flagged  3/4   (the judge must catch these)
  exemplar flagged 0/4   (false alarms)
  chapter flagged  0/4
  verdict: PASS
```

## Tells acted on
None. No chapter passage was flagged.

# Round 2 onwards (2026-10-13, after the user's review, D42)

## Profile (final text)
```

== book2/chapters/03-you-already-know-these-words.md  (1670 words, 33 paragraphs)
   measure                       chapter  exemplar   z
   words/paragraph                  50.6      55.4  -0.6
   words/sentence                   16.7      17.4  -0.4
   sentences over 30 words %         3.0      10.5  -1.1  drift
   'and' per 1k                     23.5      30.9  -0.5
   'but'/'yet' per 1k                3.3       3.9  -0.2
   semicolons per 1k                 3.3       7.7  -0.7
   colons per 1k                     3.9       8.7  -0.6
   dashes per 1k                     0.0       0.0  +0.0
   brackets per 1k                   4.6       3.5  +0.2
   questions per 1k                  0.7       0.3  +0.0
   'you/your' per 1k                 0.7       0.3  +0.4
   'we/us/our' per 1k                9.1      15.5  -0.4
   'let's' per 1k                    1.3       0.6  +0.4
   'this/these' per 1k              18.2      13.9  +0.7
   commas per sentence               0.9       1.0  -0.3
   And/But openers per 1k            0.0       0.3  -0.3
   colon-then-quote per 1k           0.0       0.6  -0.4
   longest paragraph                 103      ≤110
   Function-word Delta: median 0.89 over 9 chunks; 2/9 chunks beyond the exemplar's 90th percentile (0.99).
   Sheikh named 6 times (3.6 per 1k; cap 5, TONE 23); 'he says'-type verbs: 1
   Profile verdict: PASS

```

## Blind judge 03r2
```
Blind voice test 03r2: book2/chapters/03-you-already-know-these-words.md (control 7225b76:book2/chapters/01-seeking-not-powers.md)
  control flagged  4/4   (the judge must catch these)
  exemplar flagged 0/4   (false alarms)
  chapter flagged  2/4
  verdict: REWRITE
```

## Blind judge 03r3
```
Blind voice test 03r3: book2/chapters/03-you-already-know-these-words.md (control 7225b76:book2/chapters/01-seeking-not-powers.md)
  control flagged  3/4   (the judge must catch these)
  exemplar flagged 0/4   (false alarms)
  chapter flagged  0/4
  verdict: PASS
```

## Blind judge 03r4
```
Blind voice test 03r4: book2/chapters/03-you-already-know-these-words.md (control 7225b76:book2/chapters/01-seeking-not-powers.md)
  control flagged  3/4   (the judge must catch these)
  exemplar flagged 0/4   (false alarms)
  chapter flagged  0/4
  verdict: PASS
```

**Notes:**
- **03r2:** not counted, because house style (chapter words, Oxford comma) leaked into the packet.
- **03r3** and **03r4:** both PASS with valid runs and the chapter flagged 0/4. 03r4 used the corrected normaliser.
