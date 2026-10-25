<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0:0f2027,50:203a43,100:2c5364&amp;height=190&amp;section=header&amp;text=Uthman%20Ayodeji%20Dabiri&amp;fontSize=50&amp;fontColor=ffffff&amp;fontAlignY=36&amp;desc=Senior%20Backend%20Engineer%20%C2%B7%20.NET%2C%20Distributed%20Systems%20and%20Fintech&amp;descSize=18&amp;descAlignY=58" alt="Uthman Ayodeji Dabiri - Senior Backend Engineer, .NET, Distributed Systems and Fintech" width="100%" />
</p>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&amp;weight=500&amp;size=20&amp;duration=3200&amp;pause=900&amp;color=2C9CDB&amp;center=true&amp;vCenter=true&amp;width=660&amp;lines=Backend+systems+that+move+real+money;Kafka+%C2%B7+gRPC+%C2%B7+Temporal+%C2%B7+Kubernetes+%C2%B7+Azure;10%2B+bank+and+payment+integrations;Building+AI+agents+with+Claude+Code+%2B+MCP" alt="Backend systems that move real money - Kafka, gRPC, Temporal, Kubernetes, Azure - 10+ bank and payment integrations - building AI agents with Claude Code and MCP" />
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/uthman-dabiri-576339288"><img src="https://img.shields.io/badge/LinkedIn-Uthman%20Dabiri-0A66C2?style=for-the-badge&amp;logo=linkedin&amp;logoColor=white" alt="LinkedIn" /></a>
  <a href="mailto:dabirideji@gmail.com"><img src="https://img.shields.io/badge/Email-dabirideji%40gmail.com-D14836?style=for-the-badge&amp;logo=gmail&amp;logoColor=white" alt="Email" /></a>
  <a href="https://wa.me/2348142546500"><img src="https://img.shields.io/badge/WhatsApp-Chat-25D366?style=for-the-badge&amp;logo=whatsapp&amp;logoColor=white" alt="WhatsApp" /></a>
  <a href="http://dabirideji-portfolio.great-site.net/"><img src="https://img.shields.io/badge/Portfolio-Visit-111111?style=for-the-badge&amp;logo=googlechrome&amp;logoColor=white" alt="Portfolio" /></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Microsoft%20Certified-Azure%20Developer%20Associate%20(AZ--204)-0078D4?style=flat-square&amp;logo=microsoftazure&amp;logoColor=white" alt="Microsoft Certified: Azure Developer Associate (AZ-204)" />
  <img src="https://img.shields.io/badge/Status-Open%20to%20work-2ea44f?style=flat-square" alt="Open to work" />
  <img src="https://img.shields.io/badge/Based%20in-Lagos%2C%20Nigeria-008751?style=flat-square" alt="Based in Lagos, Nigeria" />
  <img src="https://img.shields.io/badge/Remote%20%2B%20relocation-Open-0e75b6?style=flat-square" alt="Open to remote and relocation" />
  <img src="https://komarev.com/ghpvc/?username=dabirideji&amp;label=Profile%20views&amp;color=0e75b6&amp;style=flat-square" alt="Profile views" />
</p>

---

## About me

I build the backend systems that move money: **payment processing, interbank lending, KYC and bank integrations**, in
**C#/.NET**, for regulated fintech. I have **10+ years** of it, and I design event-driven microservices on **Kafka, gRPC
and Temporal**.

| 10,000+ | < 20 ms | 10+ | 99.9% |
|:---:|:---:|:---:|:---:|
| transactions per minute, load-tested Kafka payment processing | API responses with gRPC and event sourcing | bank and payment integrations (NIBSS/BVN, Paystack, Flutterwave, Stripe, VFD...) | uptime on the platform I build for today |

What sets my work apart: I verify distributed systems end to end against real infrastructure (Kafka, Postgres, live
HTTP), not only green test suites, and I find the bug everyone else's mocks missed.

## Experience

### Senior Backend Engineer · [PeerPay Digital Assets](https://www.peerpaynetwork.com/) &nbsp;<sub>01/2025 - present</sub>
Automated financial commitment settlement (AFCS): interbank lending, co-signed credit and loan recovery across Nigerian banks.
- Own four services of the AFCS backend (onboarding, unified bank integration, notifications, credit disbursement) on **.NET 8, Docker and Kubernetes (AKS)**
- Built real-time **NIBSS** integration for BVN verification, KYC automation and credit history, with retries and circuit breakers
- Designed the loan-mandate lifecycle as a **state machine** (draft → dual-signer OTP consent → institution attestation → active), advanced by **Kafka** events
- Fixed five latent defects in one pass, including a package skew that broke every JWT validation; an unbounded auth call that hung requests for 20+ s now returns in ~0.4 s

### CTO & Solutions Architect (Contract) · [SwissPay](https://swisspay.africa/) &nbsp;<sub>2025 - 2026 · ended</sub>
Tap-to-pay platform that turns a smartphone into a payment terminal (NFC, QR, BLE, offline payments).
- Owned the architecture of a platform serving 1,000-10,000 merchants and users: a 7-project **Clean Architecture / DDD** solution on .NET 9
- **Kafka** payment processing load-tested at **10,000+ transactions per minute**, sub-second latency; API responses **under 20 ms** with gRPC and event sourcing
- Unified six payment and banking providers (Paystack, Flutterwave, Stripe, SageCloud, ErcasPay, Reloadly) behind one API, with bank-code reconciliation that prevents misrouted transfers
- Zero-downtime encryption-key rotation (key ring + dry-run re-encryption job); cut CI/CD from 4-6 hours to 20-30 minutes (~10x)

### Contract & earlier roles

| Role | Where | When | Live |
|---|---|---|---|
| Solutions Architect & Project Lead | LetsMeet Technologies - real-time social backend: SignalR chat, PostgreSQL spatial matchmaking with Azure Maps, Stripe | 03/2025 - 11/2025 | [letsmeet.chat](http://letsmeet.chat/) |
| Backend Developer | DeCloud23 Tech - ZHEETA social platform API: age and event verification, multi-currency payouts, OpenTelemetry | 05/2024 - 12/2025 | [zheeta.com](https://www.zheeta.com/) |
| Backend Engineer | Coronation Registrars (via Gapplus) - registrar API gateway, ShareholderLive, IssuerLive, virtual AGM with secure voting, an ESOP edition for Access Bank | 2023 - 2025 | [ShareholderLive](https://shareholderlive.coronationregistrars.com/) · [IssuerLive](https://issuerlive.coronationregistrars.com/) · [AGM](https://coronation.ng/institutional/products-solutions/registrars-and-data-Management-services/company-registrar-services/meeting-administration/) |
| Backend & Mobile Engineer (Contract) | Useri - agrotech platform: .NET backend, admin portal, Flutter app (BLoC, on-device OCR, Gemini, Shorebird OTA), Paystack | 2026 | - |
| Lead Developer | Virtual360 MevTech - modular .NET 8 e-learning platform, Stripe subscriptions, Azure + CDN delivery | - | [mev-tech-web](https://mev-tech-web.onrender.com/) |
| Instructor & Mentor | Codeweb Coding Academy - taught the backend .NET curriculum | 12/2021 - 04/2024 | - |
| Software Developer | Nigerian Communications Commission | 2022 | - |
| Software Engineer | CompuClick Software - logistics and POS/ERP apps | 2018 - 2020 | [MarchXpress](https://play.google.com/store/apps/details?id=com.compuclick.march_xpress) · [Flex+ PDA](https://play.google.com/store/apps/details?id=com.pos.compuclick.pdaflex) |
| Developer & Consultant | Codeweb Project Solutions | 2015 - 2018 | - |

## AI & platform engineering

| Project | What it does | Built with |
|---|---|---|
| **Autonomous job-application agent** | Sources roles from hundreds of job boards, tailors a resume per posting, and fills and submits real ATS forms unattended on a VPS. Reads a live mailbox to clear email-OTP challenges, and a rule-based honesty audit checks every LLM-drafted answer before anything is sent. | Python, Playwright/CDP, LLM APIs, IMAP, Docker |
| **MASTER AI** - multi-agent dev toolkit | Compiles one set of rules, agents and skills into Claude Code, Cursor, Gemini and Codex configs, with model-tier routing, code-graph MCP integration, multi-session coordination and evidence-gated review. 490+ commits. | Node.js, Claude Code, MCP |
| **Shared .NET service template + observability stack** | Multi-tenant SaaS template with OpenTelemetry tracing and metrics built in, reused across 6+ production APIs, plus a self-hosted Kubernetes observability stack. | ASP.NET Core, OpenTelemetry, SigNoz, Prometheus, Grafana, Loki, Seq |

<sub>Most of my code is private client work. Happy to walk through any of it in an interview.</sub>

## Tech stack

**Languages & frameworks**<br/>
<img src="https://skillicons.dev/icons?i=cs,dotnet,python,ts,nodejs,flutter,dart,php,laravel,django&amp;perline=10" alt="C#, .NET, Python, TypeScript, Node.js, Flutter, Dart, PHP, Laravel, Django" />

**Distributed systems & data**<br/>
<img src="https://skillicons.dev/icons?i=kafka,rabbitmq,postgres,redis,cassandra,mysql,mongodb,elasticsearch&amp;perline=10" alt="Kafka, RabbitMQ, PostgreSQL, Redis, Cassandra, MySQL, MongoDB, Elasticsearch" /><br/>
<img src="https://img.shields.io/badge/Temporal-000000?style=flat-square&amp;logo=temporal&amp;logoColor=white" alt="Temporal" /> <img src="https://img.shields.io/badge/TigerBeetle-1a1a1a?style=flat-square" alt="TigerBeetle" /> <img src="https://img.shields.io/badge/gRPC-244c5a?style=flat-square&amp;logo=grpc&amp;logoColor=white" alt="gRPC" /> <img src="https://img.shields.io/badge/SignalR-512BD4?style=flat-square&amp;logo=dotnet&amp;logoColor=white" alt="SignalR" /> <img src="https://img.shields.io/badge/SQL%20Server-CC2927?style=flat-square&amp;logo=microsoftsqlserver&amp;logoColor=white" alt="SQL Server" /> <img src="https://img.shields.io/badge/EF%20Core-512BD4?style=flat-square&amp;logo=dotnet&amp;logoColor=white" alt="Entity Framework Core" /> <img src="https://img.shields.io/badge/Hangfire-2E3A59?style=flat-square" alt="Hangfire" />

**Cloud & DevOps**<br/>
<img src="https://skillicons.dev/icons?i=azure,aws,kubernetes,docker,terraform,githubactions,linux,git&amp;perline=10" alt="Azure, AWS, Kubernetes, Docker, Terraform, GitHub Actions, Linux, Git" /><br/>
<img src="https://img.shields.io/badge/Azure%20DevOps-0078D7?style=flat-square&amp;logo=azuredevops&amp;logoColor=white" alt="Azure DevOps" /> <img src="https://img.shields.io/badge/AKS-326CE5?style=flat-square&amp;logo=kubernetes&amp;logoColor=white" alt="Azure Kubernetes Service" />

**Observability**<br/>
<img src="https://skillicons.dev/icons?i=prometheus,grafana,sentry&amp;perline=10" alt="Prometheus, Grafana, Sentry" /><br/>
<img src="https://img.shields.io/badge/OpenTelemetry-425CC7?style=flat-square&amp;logo=opentelemetry&amp;logoColor=white" alt="OpenTelemetry" /> <img src="https://img.shields.io/badge/SigNoz-E75536?style=flat-square" alt="SigNoz" /> <img src="https://img.shields.io/badge/Grafana%20Loki-F46800?style=flat-square&amp;logo=grafana&amp;logoColor=white" alt="Loki" /> <img src="https://img.shields.io/badge/Seq-2C3E50?style=flat-square" alt="Seq" /> <img src="https://img.shields.io/badge/Serilog-1C1C1C?style=flat-square" alt="Serilog" />

**AI tooling**<br/>
<img src="https://img.shields.io/badge/Claude%20Code-D97757?style=flat-square&amp;logo=claude&amp;logoColor=white" alt="Claude Code" /> <img src="https://img.shields.io/badge/MCP-111111?style=flat-square&amp;logo=modelcontextprotocol&amp;logoColor=white" alt="Model Context Protocol" /> <img src="https://img.shields.io/badge/LLM%20APIs-Anthropic%20%C2%B7%20Gemini-6E56CF?style=flat-square" alt="LLM APIs: Anthropic, Gemini" /> <img src="https://img.shields.io/badge/RAG-pgvector-336791?style=flat-square&amp;logo=postgresql&amp;logoColor=white" alt="RAG with pgvector" /> <img src="https://img.shields.io/badge/Ollama-000000?style=flat-square&amp;logo=ollama&amp;logoColor=white" alt="Ollama" /> <img src="https://img.shields.io/badge/Playwright-2EAD33?style=flat-square&amp;logo=playwright&amp;logoColor=white" alt="Playwright" />

**Frontend (when the job needs it)**<br/>
<img src="https://skillicons.dev/icons?i=react,angular,js,tailwind&amp;perline=10" alt="React, Angular, JavaScript, Tailwind" />

<sub>Architecture: microservices, Clean Architecture, DDD / CQRS, event sourcing, sagas, idempotent APIs, multi-tenant SaaS · Payments &amp; security: NIBSS / BVN, Paystack, Flutterwave, Stripe, VFD, KYC/AML, OAuth2 / JWT, encryption at rest and key rotation</sub>

## Certifications & education

- **Microsoft Certified: Azure Developer Associate (AZ-204)**
- **B.Sc. Computer Science** - University of Lagos
- Courses: Microsoft .NET Development · IBM Software Development · Duke University (Coursera) Full-Stack Software Development · Codeweb Coding Academy Full-Stack Web Development

## GitHub activity

Most of my work lives in private client repositories, so these numbers come from the full contribution calendar.

<!-- STATS:START -->
| Contributions since 2022 | Last 12 months | Active days (12 mo) | Longest streak |
|:---:|:---:|:---:|:---:|
| **12,074** | **7,265** | **340** | **94 days** |

<sub>Auto-refreshed 2026-10-25 (UTC) by a GitHub Action in this repo.</sub>
<!-- STATS:END -->

<p align="center">
  <img src="https://streak-stats.demolab.com/?user=dabirideji&amp;theme=github-dark-blue&amp;hide_border=true&amp;border_radius=10" alt="GitHub contribution streak" />
</p>

---

<p align="center">
  <b>Hiring for backend, platform or fintech engineering?</b> I'd love to talk -
  <a href="mailto:dabirideji@gmail.com">dabirideji@gmail.com</a> ·
  <a href="https://www.linkedin.com/in/uthman-dabiri-576339288">LinkedIn</a>
</p>

<p align="center">
  <a href="https://www.buymeacoffee.com/dabirideji"><img src="https://img.shields.io/badge/Buy%20me%20a%20coffee-FFDD00?style=flat-square&amp;logo=buymeacoffee&amp;logoColor=black" alt="Buy me a coffee" /></a>
</p>

<img src="https://capsule-render.vercel.app/api?type=waving&amp;color=0:2c5364,50:203a43,100:0f2027&amp;height=100&amp;section=footer" alt="" width="100%" />
