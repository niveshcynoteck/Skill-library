#!/bin/bash

links=(
    "https://www.groovyweb.co/blog/in-house-vs-outsource-ai-development-2026"
    "https://colaninfotech.com/blog/in-house-vs-outsourcing-ai-development-in-2026/"
    "https://alphacorp.ai/blog/in-house-vs-outsourced-ai-development-2026-guide"
    "https://stealthagents.com/research/cost-of-hiring-a-machine-learning-engineer-2026"
    "https://motionrecruitment.com/it-salary/machine-learning"
    "https://www.isometrik.ai/blog/ai-development-agency-vs-in-house-cost/"
    "https://www.secondtalent.com/resources/global-ai-talent-shortage-statistics/"
    "https://www.bu.edu/online/2026/06/27/ai_skills_gap_2026/"
    "https://qubit-labs.com/ai-talent-shortage/"
    "https://www.valuecoders.com/blog/software-engineering/guide-to-safeguarding-your-intellectual-property-when-outsourcing/"
    "https://www.ability.ai/blog/ai-vendor-lock-in-risks"
    "https://www.futureproofing.dev/resources/build-vs-outsource/outsource-ai-development-guide"
    "https://www.techaheadcorp.com/blog/enterprise-ai-build-vs-buy-vs-partner/"
    "https://helium42.com/blog/build-vs-buy-ai"
    "https://www.mckinsey.com/~/media/mckinsey/business%20functions/people%20and%20organizational%20performance/our%20insights/the%20state%20of%20organizations/2026/the-state-of-organizations-2026.pdf"
    "https://www.ibm.com/think/insights/whats-new-2024-cost-of-a-data-breach-report"
    "https://www.verizon.com/about/news/2025-data-breach-investigations-report"
    "https://www.helpnetsecurity.com/2025/04/23/verizon-2025-data-breach-investigations-report-dbir/"
    "https://www.deloitte.com/us/en/services/consulting/articles/global-outsourcing-survey.html"
    "https://innowise.com/blog/in-house-vs-outsourcing-software-development/"
    "https://www.leanware.co/insights/outsource-ai-mvp-development-a-complete-guide-for-startups"
    "https://www.premai.io/blog/ai-data-residency-requirements-by-region-the-complete-enterprise-compliance-guide/"
    "https://truto.one/blog/how-to-handle-eu-data-residency-and-gdpr-compliance-for-mcp-servers/"
)

for link in "${links[@]}"; do
    status=$(curl -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64)" -Ls -o /dev/null -w "%{http_code}" --max-time 15 "$link")

    if [[ "$status" == "200" || "$status" == "301" || "$status" == "302" ]]; then
        valid=true
    else
        valid=false
    fi

    echo "$link,$status,$valid"
done
