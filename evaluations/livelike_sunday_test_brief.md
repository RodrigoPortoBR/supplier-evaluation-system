# Sunday Live Test — CazéTV x LiveLike
### World Cup Infrastructure Simulation | April 2026

---

## What We Want to Do

This Sunday, CazéTV will broadcast a match expected to reach ~3 million concurrent viewers. We want to use this as a **real-world World Cup simulation** by triggering a live call-to-action on air, directing viewers to submit a free score prediction in real time.

This is more valuable than any synthetic stress test because it replicates the exact behavior we'll face during the World Cup: a sharp, instant traffic spike triggered by a broadcast moment, with real users from real devices across Brazil.

---

## The Flow (Simple)

```
Viewer sees QR code / URL on screen
          ↓
Opens page on mobile browser
          ↓
Sees a single prediction widget: "What will the final score be?"
          ↓
Picks the result, submits
          ↓
Done — no account, no login, no friction
```

**No authentication required.** The page must be publicly accessible and work instantly — zero barriers between the QR code and the submitted prediction.

LiveLike's platform supports anonymous profiles natively (local profiles with a unique auto-generated ID). This is the mode we want to use for this test.

---

## What We Need From LiveLike

### Setup (must be ready by Saturday)
- A publicly accessible URL hosting a single prediction widget for Sunday's match
- Widget type: score predictor (final result + exact score)
- Anonymous access enabled — no login wall
- Mobile web optimized
- Prediction lock set to kickoff time
- No league enrollment, no onboarding — land and predict

### On Sunday (during the match)
- Engineering team on standby during the broadcast window
- Real-time monitoring active on the prediction endpoint

### After the match (within 2 hours)
- Export of peak metrics for the spike window (T=0 ± 15 minutes from CTA moment):
  - Peak requests per second on the prediction endpoint
  - p50 / p95 / p99 response latency
  - Error rate (4xx / 5xx)
  - Auto-scaling event log (when did AWS scale out, and how fast?)

---

## Why This Test Is Critical for Us

The World Cup expected peak is ~10 million concurrent users. Sunday's test at ~3 million gives us a **real baseline** to project from.

If Sunday's infrastructure handles the spike cleanly, we have strong evidence that the May 11 go-live is on solid ground. If there are issues — we need to find them now, not during the World Cup.

We need this test to happen. It directly informs our internal stakeholder sign-off for the full rollout.

---

## Timeline This Week

| Day | Action |
|---|---|
| Today/Tomorrow | LiveLike confirms feasibility and anonymous flow setup |
| Wednesday | Widget live in staging — CazéTV validates the page end-to-end |
| Friday | Final check — widget URL confirmed, monitoring active, engineering on standby confirmed |
| Sunday | Live test during broadcast |
| Sunday (post-match) | Metrics export from LiveLike |

---

## One Ask

Can we get on a quick call tomorrow to confirm the setup and make sure your engineering team is aligned for Sunday? We want to make sure this goes smoothly on both sides.
