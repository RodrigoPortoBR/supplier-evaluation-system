# Live Broadcast Stress Test — World Cup Simulation
### CazéTV x LiveLike | Sunday Match (~3M Concurrent Viewers)

---

## 1. Why This Test Matters More Than a Synthetic Stress Test

A synthetic load test (e.g., Artillery, k6, Locust) generates predictable, linear traffic from controlled machines. It does not replicate:

| Factor | Synthetic Test | Real Broadcast Test |
|---|---|---|
| Traffic shape | Artificial ramp | Instant vertical spike (CTA moment) |
| Geographic distribution | Simulated IPs | Real Brazilian users from real ISPs |
| SSO load pattern | Mocked / scripted | Real concurrent JWT auth requests |
| CDN edge behavior | Not tested | Real edge nodes under real load |
| User concurrency model | Scripted sessions | Humans with real latency, retries, timeouts |
| Emotional "retry behavior" | None | Users re-tap when it's slow (amplifies load) |

The Sunday match is the closest approximation of a World Cup CTA moment CazéTV will have before go-live. **It is irreplaceable.**

---

## 2. Test Design

### 2.1 Prediction Widget Configuration

**Widget type:** Single match result predictor — "Who wins + exact score?"

**Why this widget:**
- Lowest possible payload (2 fields: team selection + score)
- Prediction lock at kickoff is native to LiveLike (no custom logic needed)
- Resolves automatically via OPTA feed (zero manual effort post-match)
- Replicates the exact core mechanic of the Bolão

**Configuration checklist (align with LiveLike before Sunday):**
- [ ] Widget configured and published in staging environment by Friday EOD
- [ ] Prediction lock timestamp set to exact kickoff time
- [ ] Scoring rule configured (e.g., 10pts correct team, 25pts exact score)
- [ ] Widget tested on mobile web (primary traffic channel for broadcast CTAs)
- [ ] No league enrollment required at this stage — global leaderboard only
- [ ] Social sharing enabled post-submission (amplifies organic traffic)

### 2.2 Authentication Flow — Critical Decision

Two options, with different risk profiles:

#### Option A: Pre-Authenticated (Recommended)
Users are already logged in to CazéTV's platform before the CTA moment.

- SSO handshake happens before the spike
- At CTA moment, the LiveLike API receives only prediction submissions (not auth requests)
- Peak RPS is clean prediction traffic — most representative of World Cup conditions
- **Requires:** CTA designed to drive users into the platform 5–10 min before the key moment

#### Option B: CTA triggers login + prediction in sequence
Users click → authenticate → submit prediction in one flow.

- Stress-tests SSO and LiveLike simultaneously
- Risk: if CazéTV's SSO becomes a bottleneck, it may obscure LiveLike's performance data
- Useful for exposing SSO weakness, but noisy for measuring LiveLike RPS ceiling

**Recommendation:** Run Option A for a clean LiveLike signal. Plan for Option B in a second test or World Cup rehearsal.

### 2.3 Entry Point Design (Broadcast CTA)

The CTA should be:
1. **Single action** — "Submit your prediction at [URL]" — no intermediate steps
2. **URL must be pre-warmed** — the prediction page should already be loaded in the user's browser if possible (embed via webview or pre-open in app)
3. **Deep link or QR code** — directs user straight to the prediction widget, not the homepage
4. **CTA window defined** — pick a moment in the broadcast that creates a sharp, single spike:
   - Best: 10–15 minutes before kickoff ("submit your score prediction now")
   - Avoid halftime (too dispersed, traffic is gradual)

---

## 3. Metrics to Capture

### 3.1 LiveLike Side (request from LiveLike explicitly)

| Metric | Why It Matters |
|---|---|
| **Peak RPS to prediction API endpoint** | Core measurement — how many submissions/sec at CTA peak |
| **p50 / p95 / p99 response latency** | p99 tells you the worst experience for real users |
| **Error rate (4xx / 5xx) at peak** | Any errors during spike = failures that matter |
| **Auto-scaling trigger timestamp** | When did AWS scale out? How long did it take? |
| **Queue depth (if any)** | Were requests queued or dropped? |
| **Leaderboard update latency** | Did rankings update near-real-time even at peak? |

### 3.2 CazéTV Side (internal monitoring)

| Metric | Why It Matters |
|---|---|
| **SSO auth requests per second** | Validates SSO won't bottleneck World Cup |
| **JWT issuance time under load** | If JWT is slow, LiveLike never sees the request |
| **CDN hit rate on prediction page** | Is the static front-end served from edge? |
| **Error rate on CazéTV's own endpoints** | Isolate: is any failure ours or LiveLike's? |

### 3.3 Timestamp Synchronization

Define the **T=0 moment** (exact second the CTA is delivered on air). All metrics must be timestamped relative to T=0 to produce a traffic spike shape curve.

Request from LiveLike: export raw event log with timestamps for the T=0 ± 10-minute window.

---

## 4. Success Criteria

| Criteria | Pass Threshold |
|---|---|
| Peak RPS absorbed without errors | 0% error rate at peak |
| p99 response time at peak | < 2,000ms |
| Auto-scaling response | Scale-out completes within 60s of spike start |
| Leaderboard update post-prediction | < 5s visible to user |
| System stability post-spike | No degradation 5 minutes after peak |

If the test with 3M viewers passes cleanly, the projected World Cup peak (10M) represents a ~3.3x multiplier. LiveLike's AWS auto-scaling should handle this linearly — but this must be explicitly confirmed with their engineering team.

---

## 5. What to Ask LiveLike — Pre-Test Briefing

This is the message to align with LiveLike before Sunday. The goal is to ensure they treat this as a **World Cup dress rehearsal**, not a routine event.

---

### Draft Message to LiveLike (Alex / Engineering Team)

> **Subject: Sunday Match — World Cup Stress Simulation — Engineering Standby Request**
>
> Hi Alex,
>
> We want to use Sunday's match (~3M expected concurrent viewers) as a live World Cup simulation. We're planning a broadcast CTA that will direct all viewers to submit a score prediction simultaneously — a sharp, real-world traffic spike.
>
> This is **more strategically valuable to us than a synthetic stress test** because it replicates the actual broadcast trigger behavior we'll face during the World Cup. We'd like to treat it as an official infrastructure readiness test.
>
> **What we need from LiveLike for Sunday:**
>
> 1. **Engineering on standby** during the match window (please confirm the timezone coverage — we need someone monitoring live, not on async response)
> 2. **Real-time telemetry access** — can you share a live view of RPS and error rates during the event, or give us a post-event export within 1 hour of the spike?
> 3. **Metrics to be exported:** peak RPS on the prediction endpoint, p50/p95/p99 latency, error rate, auto-scaling trigger timestamps, leaderboard update latency
> 4. **Pre-event infra check** — can your engineering team confirm the widget environment is pre-warmed and AWS scaling policies are active before the match?
> 5. **T=0 sync** — we'll share the exact broadcast CTA timestamp so you can align your telemetry window
>
> **Our internal setup:**
> - Prediction widget: single match result + score (lowest-payload mechanic)
> - Auth flow: users pre-authenticated before CTA (clean LiveLike RPS signal)
> - CTA window: ~10–15 min before kickoff
> - Expected spike duration: 3–5 minutes
>
> **Why this matters to us:** If Sunday's test at 3M viewers validates the infrastructure, we have a ~3.3x headroom before reaching World Cup peak (10M). That data point is critical for our stakeholder sign-off and for contract conversations around usage tiers.
>
> Can we schedule a 30-min call this Friday to align on the technical setup and confirm your engineering team's availability on Sunday?
>
> Thanks,
> Rodrigo

---

## 6. Post-Test Analysis Framework

Immediately after the match, run this analysis:

### Traffic Spike Shape
Plot RPS over the T=0 ± 10 minute window. Look for:
- **Instant wall** (good: CTA was effective, spike is clean and measurable)
- **Gradual ramp** (indicates users came from social, not direct broadcast — less peak-like)

### Scalability Projection
```
World Cup projected peak = Sunday peak RPS × (10M / actual Sunday peak users)
```
Use this to model whether 10M users will stay within the $325k usage tier or breach it.

### Error Attribution
Any errors during the spike must be attributed:
- **LiveLike API errors** → LiveLike's responsibility; must be resolved before May
- **SSO/JWT errors** → CazéTV's responsibility; accelerates SSO build priority
- **CDN / frontend errors** → CazéTV's responsibility

### Go/No-Go Signal for World Cup
| Outcome | Signal |
|---|---|
| 0% errors, p99 < 2s | Strong green light — scale linearly to 10M |
| < 1% errors, p99 < 3s | Yellow — identify root cause; fix before go-live |
| > 1% errors OR p99 > 5s | Red — escalate immediately; World Cup readiness at risk |

---

## 7. Timeline (This Week)

| Day | Action | Owner |
|---|---|---|
| **Monday** | Share this plan with LiveLike; request Friday call | Rodrigo |
| **Wednesday** | Widget configured and tested in staging | LiveLike + CazéTV |
| **Thursday** | Auth flow tested end-to-end (SSO → LiveLike JWT → prediction submit) | CazéTV + LiveLike |
| **Friday** | 30-min alignment call — confirm metrics, standby coverage, T=0 protocol | Both |
| **Saturday** | Pre-warm widget environment; confirm AWS scaling policies active | LiveLike |
| **Sunday (match day)** | CTA at T=0; monitor live; LiveLike engineering on standby | Both |
| **Sunday (post-match)** | Export telemetry; run post-test analysis | Both |
| **Monday** | Debrief + stakeholder report | Rodrigo |
