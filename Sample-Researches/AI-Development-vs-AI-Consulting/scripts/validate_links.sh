#!/bin/bash
# Validates reference links for the AI Development vs AI Consulting research.
# Usage: bash validate_links.sh > /tmp/opencode/link_report.txt

urls=(
"https://www.bls.gov/ooh/computer-and-information-technology/computer-and-information-research-scientists.htm"
"https://www.bls.gov/opub/ted/2026/artificial-intelligence-information-technology-and-employment-2024-34.htm"
"https://www.pwc.com/gx/en/services/ai/ai-jobs-barometer.html"
"https://www.comptia.org/en/resources/research/state-of-the-tech-workforce-2026/"
"https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/upgrading-software-business-models-to-thrive-in-the-ai-era"
"https://cset.georgetown.edu/publication/identifying-the-ai-development-workforce/"
"https://www.dice.com/hiring/recruitment/reports/dice-tech-job-report"
"https://www.simon-kucher.com/en/insights/services-software-why-ai-rewriting-commercial-logic-business-services"
"https://dancumberlandlabs.com/blog/ai-consultant-vs-developer/"
"https://dancumberlandlabs.com/blog/ai-consulting-vs-development/"
"https://aimindshift.consulting/guides/ai-consultant-vs-ai-engineer/"
"https://vladbrakalo.com/blog/ai-consultant-vs-ai-engineer/"
"https://xonique.dev/blog/ai-consultant-vs-ai-developer-differences/"
"https://aatvi.ai/en/insights/ai-consulting-vs-ai-software-development"
"https://aidevlab.com/blog/ai-consulting-vs-ai-dev-shop/"
"https://azumo.com/artificial-intelligence/ai-insights/ai-consulting-vs-ai-development-vs-staff-augmentation"
"https://phosailabs.com/blog/ai-consulting-firm-vs-ai-software-vendor"
"https://www.agenticaipricing.com/the-service-to-software-transition-playbook-for-ai-consultancies/"
"https://www.agenticaipricing.com/pricing-ai-consulting-vs-ai-products-finding-your-model/"
"https://sfailabs.com/guides/why-the-ai-agency-model-is-colliding-with-the-ai-product-studio-model"
"https://nexaconsultancy.com/resources/compare/consulting-vs-saas"
"https://blog.magmalabs.io/2026/07/09/staff-augmentation-vs-product-dev-vs-consulting-2026.html"
"https://c0nsl.com/t/scaling-solo-ai-consulting-tradeoffs"
"https://www.consultkit.ai/blog/how-to-productize-ai-consulting-services"
"https://alicelabs.ai/en/insights/ai-consulting-vs-in-house-ai"
"https://eidel.io/posts/build-a-consulting-business-before-you-build-a-product-business"
"https://www.kore1.com/ai-engineer-career-path-2026/"
"https://www.codecademy.com/resources/blog/how-much-does-an-ai-engineer-make"
"https://cloudaqube.com/blog/ai-engineer-career-path-2026"
"https://www.acceler8talent.com/resources/blog/what-is-an-ai-engineer--career-guide-for-2026/"
"https://www.herohunt.ai/blog/ai-engineer-salary-2026-real-comp-bands-by-level/"
"https://myengineeringpath.dev/genai-engineer/day-in-the-life/"
"https://agenticcareers.co/blog/day-in-life-ai-agent-engineer"
"https://futureskillsacademy.com/blog/ai-analyst-vs-ai-engineer-vs-ai-consultant-roles/"
"https://mentorcruise.com/blog/how-to-become-an-ai-consultant/"
"https://www.advisori.de/en/blog/how-to-become-ai-consultant-career-path-skills-certifications"
"https://justinmckelvey.com/blog/ai-consultant"
"https://zalt.me/blog/2026/05/what-does-ai-consultant-do"
"https://careers.qoollege.com/compare/artificial-intelligence-consultant-vs-artificial-intelligence-engineer"
"https://www.glassdoor.com/Salaries/ai-consultant-salary-SRCH_KO0,13.htm"
"https://betonai.net/ai-consulting-rate-card-2026-what-to-charge-for-strategy-implementation-and-fractional-ai-leadership-real-rates-from-68-consultants/"
"https://pharallax.ai/guides/consulting-revenue-benchmarks-2026/"
"https://theaimarketpulse.com/insights/ai-consulting-rates-2026/"
"https://aiessentials.us/blog/what-is-an-ai-consultants-salary"
"https://alicelabs.ai/en/insights/ai-consulting-pricing-2026"
"https://axialsearch.com/insights/ai-engineering-jobs"
"https://aidevboard.com/research/ai-jobs-report-2026"
"https://www.articsledge.com/post/ai-business-models"
"https://iternal.ai/ai-consulting"
"https://www.clarista.io/platform/ai-consulting-services"
"https://www.airdev.co/services/ai-enablement"
"https://gxb.vc/"
)

for url in "${urls[@]}"; do
    code=$(curl -sL -o /dev/null -w "%{http_code}" --max-time 25 -A "Mozilla/5.0 (X11; Linux x86_64)" "$url" 2>/dev/null)
    if [[ "$code" =~ ^[23] ]]; then
        echo "$url,TRUE"
    else
        echo "$url,FALSE ($code)"
    fi
done
