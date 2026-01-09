from claim_extractor import extract_claim
from bias_detector import detect_bias
from retriever import retrieve_evidence
from verifier import verify_claim
from corrector import generate_correction

test_inputs = [
    "Yes, honey can cure diabetes permanently.",
    "Women are naturally poor drivers.",
    "The Earth revolves around the Sun.",
    "Sydney is the capital of Australia.",
    "There are 5 union territories of India."
]

for text in test_inputs:
    print("\n==============================")
    print("AI Response:", text)

    claim = extract_claim(text)
    print("Extracted Claim:", claim)

    bias_flag, bias_type = detect_bias(text)
    print("Bias Detected:", bias_flag, bias_type)

    # If bias detected → do NOT send to verifier
    if bias_flag == 1:
        print("Verification Result: Bias Detected")
        print("Correction: This statement contains bias and unfairly generalizes a group. It should be rephrased in a neutral and respectful manner.")
        continue

    evidence = retrieve_evidence(claim)
    print("Retrieved Evidence:", evidence)

    verification_result = verify_claim(claim, evidence)
    print("Verification Result:", verification_result)

    if verification_result == "False":
        correction = generate_correction(claim, evidence, text)
        print("Correction:", correction)
    else:
        print("Correction: Not required.")
