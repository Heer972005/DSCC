import wikipedia
from domain_detector import detect_domain, get_source_for_domain
from claim_extractor import extract_claims

def check_fact_with_wikipedia(claim):
    try:
        summary = wikipedia.summary(claim, sentences=2)
        return True, summary
    except:
        return False, "No reliable information found"

def dynamic_fact_check(ai_response):
    print("\n🔍 Analyzing:", ai_response)

    claims = extract_claims(ai_response)

    for claim in claims:
        domain = detect_domain(claim)
        source = get_source_for_domain(domain)

        print(f"\n➡️ Claim: {claim}")
        print("Detected Domain:", domain)
        print("Source Selected:", source)

        # For now, we only auto-check Wikipedia domains
        if source.startswith("Wikipedia"):
            is_valid, info = check_fact_with_wikipedia(claim)
            if is_valid:
                print("✔ Possibly Correct (based on Wikipedia)")
                print("Info:", info)
            else:
                print("❌ Potential Hallucination")
                print("Reason:", info)
        else:
            print("⚠ Domain-specific source selected. Manual/API integration required.")

# Test
test_inputs = [
    "Sydney is the capital of Australia.",
    "Vaccines cause infertility in women.",
    "Python does not support object oriented programming.",
    "India got independence in 1950."
]

for text in test_inputs:
    dynamic_fact_check(text)
