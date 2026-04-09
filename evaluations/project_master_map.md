# Bolão CazéTV — Project Master Map
### Status: April 7, 2026 | Go-live: May 11, 2026 | 34 days remaining

---

## The Critical Dependency Chain

Before anything else, the single biggest risk to May 11 is this chain:

```
Sponsor deal closes?
       ↓
→ YES: Use sponsor's SSO → integrate with LiveLike (Workstream B)
→ NO by April 14: Proceed immediately with own SSO or LiveLike's SSO partner

SSO decision unblocked
       ↓
LiveLike Workstream B starts (SSO integration)
       ↓
QA + UAT (Week 8)
       ↓
May 11 Go-Live
```

**The sponsor decision must have a hard deadline: April 14.** If there's no answer by then, you cannot wait — SSO build takes time and it's on the critical path. Every day of indecision here compresses the integration window.

---

## Items You Listed — Assessed

| # | Your Item | Status | Priority |
|---|---|---|---|
| 1 | Sponsor proposal | Waiting — **set hard deadline April 14** | 🔴 CRITICAL |
| 2 | Caixa Econômica Federal registration | Active — see legal note below | 🟠 HIGH |
| 3 | SSO partner deal | Blocked on sponsor — unblock by April 14 | 🔴 CRITICAL |
| 4 | Social media team (Brandwatch / Respond.io) | In progress — good, but incomplete (see below) | 🟡 MEDIUM |

---

## What's Missing From Your List

### 🔴 CRITICAL — Could kill May 11

**A. Is the LiveLike contract signed?**
The LOI exists. But the final contract has never been mentioned as closed. If it isn't signed, nothing else matters. Confirm this immediately. Also: the P1 SLA is currently "2 hours during business hours only" — this must be renegotiated to 24/7 *before* signing, since World Cup matches happen on weekends and evenings.

**B. Has the LiveLike kick-off meeting happened?**
Their proposal defines Week 1 as a kick-off workshop to align on prediction mechanics, SSO flow, OPTA feed integration, and RACI. If this hasn't happened, the implementation clock hasn't started. May 11 is only achievable if the project is already in Weeks 3–4. You need to know exactly where you are on their 8-week timeline right now.

**C. OPTA feed → LiveLike connection**
CazéTV has access to the OPTA feed — that's confirmed. But has anyone planned the actual technical integration of that feed into LiveLike's system? This is a discrete technical task that must be scoped and executed. It powers real-time scoring, prediction locking, and automatic resolution. Without it, the game doesn't work automatically.

---

### 🟠 HIGH — Must start this week

**D. L1 Support team (separate from social media)**
Brandwatch and Respond.io handle social mentions and community. That is not the same as L1 support. L1 support is: a user whose points didn't count, a prediction that didn't save, a league invite that isn't working. This team needs to:
- Be trained on LiveLike's Producer Suite (CMS/dashboard)
- Have a direct Slack channel to LiveLike's L2 team
- Have a defined escalation script

This is a separate function from social media. If you don't structure it before go-live, your social media team will be flooded with technical complaints they can't resolve, and LiveLike will receive a wave of L2 tickets that are actually L1.

**E. CRM / Push Notifications provider**
Not on your list at all. LiveLike provides webhooks and triggers — but it doesn't send emails or push notifications. CazéTV must pick, integrate, and operate its own provider. This is needed for: pre-match reminders, "predictions are open," leaderboard updates, re-engagement mid-tournament. Options: OneSignal (push, simple), Braze (full CRM, complex), Klaviyo (email-first). If this isn't decided soon, users register once and you have no way to bring them back.

**F. Brand assets → LiveLike Professional Services**
LiveLike's PS team is doing the UI customization. They need CazéTV's brand guidelines: colors, fonts, logos, tone, any UI references or Lovable prototype. If these haven't been sent, the design phase is stalled and PS credits are burning.

---

### 🟡 MEDIUM — Start by April 21

**G. Legal: Competition Rules + T&Cs + LGPD addendum**
The Caixa ECF registration is on your list, but it's one piece of a larger legal workstream:
- **Competition rules document** (regras do bolão) — required for Caixa and for publication
- **Terms & Conditions** for the prediction game itself — distinct from CazéTV's general T&Cs
- **LGPD addendum** — the Bolão collects behavioral data; the privacy policy needs to reflect this

One note on Caixa ECF: if the prediction game is purely **skill-based** (best predictor wins, no randomness), it may not require Caixa authorization — that's typically for chance-based draws (sorteios). If there's any lottery or random draw element (e.g., "predict correctly and enter a draw for a prize"), then yes, authorization is mandatory. Clarify this with your legal team — it changes the registration path.

**H. Internal team training on LiveLike CMS**
LiveLike trains the CazéTV team on their Producer Suite. This should be scheduled for the last two weeks before go-live (late April / early May). The people who will operate the game day-to-day — publishing predictions, monitoring scores, adjusting missions — need to know how to use the platform before it's live.

**I. User acquisition plan for go-live**
How do you drive the first wave of users to register for the Bolão? The broadcast CTA on Sunday is a test, but the World Cup go-live needs a coordinated launch: social campaign, influencer activation, CazéTV editorial integration, email to existing users. This is a marketing workstream that needs to start now in parallel with the technical track.

---

### 🔵 POST-SUNDAY — Immediate actions after the test

**J. Sunday test debrief → stakeholder sign-off**
After Sunday's match, compile: peak RPS, error rate, p99 latency, auto-scaling behavior. This becomes the stakeholder report that validates "the infrastructure is ready." Without this report, internal sign-off for the full rollout is based on trust, not evidence.

**K. Usage tier stress model**
After Sunday, you'll have a real RPS number. Use it to model: at what user volume does the $325k tier breach? At what point does it become $425k? This is a CFO conversation that needs to happen before go-live, not during the tournament.

---

## Prioritized Timeline

```
WEEK OF APRIL 7 (NOW)
├── 🔴 Hard deadline: Sponsor decision by April 14
├── 🔴 Confirm: Is the LiveLike contract signed?
├── 🔴 Confirm: Where are we on the 8-week LiveLike implementation timeline?
├── 🔴 Negotiate 24/7 SLA into contract before signing
├── 🟠 Send brand assets / UI guidelines to LiveLike PS team
└── 🟠 Sunday test setup (already in motion with Alex)

WEEK OF APRIL 14
├── 🔴 SSO decision locked (sponsor or own or LiveLike partner)
├── 🔴 LiveLike Workstream B starts (SSO integration)
├── 🟠 OPTA feed → LiveLike integration scoped and started
├── 🟠 CRM / Push provider selected
├── 🟠 Define L1 support team structure and Slack escalation channel
└── 🔵 Sunday test debrief + stakeholder report delivered

WEEK OF APRIL 21
├── 🟠 CRM / Push provider integration started
├── 🟡 Competition legal rules document drafted
├── 🟡 T&Cs for the Bolão drafted
├── 🟡 Caixa ECF / SPA registration filed (if applicable)
└── 🟡 User acquisition plan for go-live defined

WEEK OF APRIL 28
├── 🟡 LiveLike CMS training for CazéTV ops team
├── 🟡 Full UAT with CazéTV stakeholders
├── 🟡 Brandwatch / Respond.io setup finalized
└── 🟡 Social media team briefed on product and escalation flow

WEEK OF MAY 5
├── QA + load testing (Week 8 of LiveLike timeline)
├── L1 support team dry run
├── CRM / push notification flow tested end-to-end
└── Go/No-Go decision

MAY 11 — GO LIVE
```

---

## Open Questions for You to Answer This Week

1. **Is the LiveLike contract signed?** If not, what's blocking it?
2. **What week of the LiveLike 8-week implementation are you currently in?**
3. **Has the kick-off meeting with LiveLike happened?**
4. **Have brand assets been sent to LiveLike's Professional Services team?**
5. **Is the prize structure defined?** (skill-based ranking vs. random draw?) — this determines the Caixa/SPA path
6. **If the sponsor deal doesn't close by April 14, do you have a budget approved for an independent SSO?**
