# BidBell service availability

Independent public-service monitoring for [BidBell](https://getbidbell.com/), powered by [Upptime](https://github.com/upptime/upptime).

Checks are scheduled every five minutes on GitHub, including while the owner's computer is off. GitHub can delay scheduled jobs. Actions records each execution time; history files record the latest status change. History begins November 6, 2026; no historical uptime is implied.

## Recorded status

<!--start: status pages-->
| Service | Recorded status | History |
| --- | --- | --- |
| BidBell website | Up | [View record](history/bid-bell-website.yml) |
| Trial signup | Up | [View record](history/trial-signup.yml) |
| Cleaning opportunities | Up | [View record](history/cleaning-opportunities.yml) |
| Workspace sign-in | Up | [View record](history/workspace-sign-in.yml) |
| Application health | Up | [View record](history/application-health.yml) |
<!--end: status pages-->

## Incidents

An endpoint failure opens an issue assigned to the owner; recovery closes it. GitHub notification delivery depends on the owner's existing GitHub notification settings. No SMTP secrets are stored in this repository.

## What is checked

- Website, trial signup, cleaning opportunities and workspace sign-in: HTTPS, successful status and expected BidBell content.
- Application health: HTTPS, successful status and the expected healthy response.
- A separate local Uptime Kuma dashboard also checks the reported AI and billing availability flags.

These checks do not create accounts, generate AI answers, send mail, complete payments or submit bids. Availability does not establish that those customer journeys work.

## Configuration and recovery

Configuration: [.upptimerc.yml](.upptimerc.yml). Schedule and pinned Upptime action: [.github/workflows/uptime.yml](.github/workflows/uptime.yml).

The public repository contains public endpoint URLs and monitoring results only. Changes are recoverable in Git history. No customer information or production credentials belong here.

Scheduled workflows in public repositories may be disabled by GitHub after 60 days without repository activity. Normal monitoring commits provide activity; check Actions if history stops advancing. Monitoring has no paid host and uses standard public GitHub Actions runners.

Upstream template automation is replaced by this narrowly scoped, pinned monitor. Review upstream releases before updating the action. The original template remains recoverable in the initial commit.
