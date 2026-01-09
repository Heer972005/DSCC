import pandas as pd
from claim_extractor import extract_claim
from bias_detector import detect_bias
from retriever import retrieve_evidence
from verifier import verify_claim
from corrector import generate_correction

# Load dataset
df = pd.read_excel(r"G:\vs\DSCC\dynamic\data\ffff_final.xlsx")

results = []

for idx, row in df.iterrows():
    ai_text = row["ai_response"]

    claim = extract_claim(ai_text)
    bias_flag, bias_type = detect_bias(ai_text)

    entry = {
        "thread_id": row["thread_id"],
        "ai_response": ai_text,
        "extracted_claim": claim,
        "bias_flag": bias_flag,
        "bias_type": bias_type,
        "verification_result": None,
        "correction": None
    }

    if bias_flag == 1:
        entry["verification_result"] = "Bias"
        entry["correction"] = "This statement contains bias and should be rephrased in a neutral manner."
    else:
        evidence = retrieve_evidence(claim)
        verification_result = verify_claim(claim, evidence)
        entry["verification_result"] = verification_result

        if verification_result == "False":
            entry["correction"] = generate_correction(claim, evidence, ai_text)
        else:
            entry["correction"] = "Not required"

    results.append(entry)

result_df = pd.DataFrame(results)
result_df.to_excel("output_results.xlsx", index=False)

print("Batch processing complete. Results saved to output_results.xlsx")
