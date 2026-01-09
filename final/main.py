import pandas as pd
from claimFromDataSet import extract_claim
from fact_verifier import verify_claim

pd.set_option("display.max_rows", None)
pd.set_option("display.max_colwidth", None)
pd.set_option("display.width", 200)

df = pd.read_excel(r"hallucination_bias_dataset11.xlsx")

df["extracted_claim"] = df["ai_response"].apply(extract_claim)
df["verification_result"] = df["extracted_claim"].apply(
    lambda x: verify_claim(x) if x is not None else "Not Applicable"
)

print(df[["thread_id", "ai_response", "extracted_claim", "verification_result"]].to_string(index=False))
