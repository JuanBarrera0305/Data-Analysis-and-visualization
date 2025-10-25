import pandas as pd

# -----------------------------
# 1. Load datasets
# -----------------------------
try:
    post_survey = pd.read_csv("post_survey_data_25rows.csv")
    trackeo = pd.read_csv("trackeo_survey.csv")
except FileNotFoundError as e:
    print(" CSV file not found:", e)
    exit()

# Clean up weird spaces in headers and values
post_survey.columns = post_survey.columns.str.strip()
trackeo.columns = trackeo.columns.str.strip()
post_survey = post_survey.apply(lambda col: col.str.strip() if col.dtype == "object" else col)

print(" Data loaded successfully\n")

# -----------------------------
# 2. Helper functions
# -----------------------------
def convert_to_score(value):
    """Convert Yes/Somewhat/No to numeric score (1.0, 0.5, 0.0)."""
    if isinstance(value, str):
        v = value.strip().lower()
        if v == "yes":
            return 1.0
        elif v == "somewhat":
            return 0.5
    return 0.0


def method_to_org_score(method):
    """Return 0, 0.25, 0.5, 0.6, 0.75, or 1 depending on how organized the tracking method is."""
    if not isinstance(method, str):
        return 0
    m = method.strip().lower()
    
    if "trackeo" in m:
        return 1        
    elif "excel" in m or "spreadsheet" in m or "notion" in m:
        return 0.75     
    elif "pdf" in m:
        return 0.6     
    elif "whatsapp" in m or "youtube" in m:
        return 0.5     
    elif "notebook" in m or "phone notes" in m:
        return 0.25     
    else:  
        return 0        



print(" Validating Graph 1: Improvement in Athlete Experience (Visibility & Organization)\n")

# Ensure correct column names exist
required_cols = [
    "Visibility for Recruitment (Now)",
    "Visibility for Recruitment (After)",
    "Current Tracking Method",
    "Tracking Method (After)"
]
for col in required_cols:
    if col not in post_survey.columns:
        raise KeyError(f"Missing expected column: '{col}' in post_survey_data_25rows.csv")

# --- Visibility ---
post_survey["Visibility_Now_Score"] = post_survey["Visibility for Recruitment (Now)"].apply(convert_to_score)
post_survey["Visibility_After_Score"] = post_survey["Visibility for Recruitment (After)"].apply(convert_to_score)

visibility_before = post_survey["Visibility_Now_Score"].mean() * 100
visibility_after = post_survey["Visibility_After_Score"].mean() * 100

# --- Organization ---
post_survey["Organization_Before"] = post_survey["Current Tracking Method"].apply(method_to_org_score)
post_survey["Organization_After"] = post_survey["Tracking Method (After)"].apply(method_to_org_score)

organization_before = post_survey["Organization_Before"].mean() * 100
organization_after = post_survey["Organization_After"].mean() * 100

# --- Output results ---
print("Improvement in Athlete Experience (Visibility & Organization):")
print(f"Visibility: Before Trackeo = {visibility_before:.1f} %, After Trackeo = {visibility_after:.1f} %")
print(f"Organization: Before Trackeo = {organization_before:.1f} %, After Trackeo = {organization_after:.1f} %")
print(f"\nChange in Visibility = {visibility_after - visibility_before:.1f} percentage points")
print(f"Change in Organization = {organization_after - organization_before:.1f} percentage points\n")


# -----------------------------
# 4. Market Interest (Graph 2)
# -----------------------------
print(" Validating Graph 2: Market Interest in Trackeo\n")

interest_col = "Do You Believe This Could Change Visibility for South American Athletes"
feature_col = "Feature That Excites You the Most"

# Check column existence
for col in [interest_col, feature_col]:
    if col not in trackeo.columns:
        raise KeyError(f"Missing expected column: '{col}' in trackeo_survey.csv")

interest_counts = trackeo[interest_col].value_counts()
total_responses = len(trackeo)
interest_summary = (interest_counts / total_responses * 100).round(1)

print("Interest levels based on responses:")
print(interest_summary.to_string())
print()

feature_counts = trackeo[feature_col].value_counts(normalize=True) * 100
feature_counts_rounded = feature_counts.round(1)
print("💡 Most valuable feature (by % of respondents):")
print(feature_counts_rounded.to_string())
print()


# -----------------------------
# 5. Data-driven Summary
# -----------------------------
print("\n VALIDATION SUMMARY (data-driven):\n")

visibility_change = visibility_after - visibility_before
organization_change = organization_after - organization_before

# --- Visibility ---
if visibility_change >= 40:
    print(f"-  Strong visibility improvement: {visibility_change:.1f} points — supports Graph 1.")
elif visibility_change >= 10:
    print(f"- ⚠️ Moderate visibility improvement: {visibility_change:.1f} points — partially supports Graph 1.")
else:
    print(f"-  Low visibility improvement: {visibility_change:.1f} points — does NOT support Graph 1.")

# --- Organization ---
if organization_change >= 40:
    print(f"-  Strong organization improvement: {organization_change:.1f} points — supports Graph 1.")
elif organization_change >= 10:
    print(f"- ⚠️ Moderate organization improvement: {organization_change:.1f} points — partially supports Graph 1.")
else:
    print(f"-  Low organization improvement: {organization_change:.1f} points — does NOT support Graph 1.")

# --- Market interest ---
# --- Market interest ---
yes_pct = interest_summary.get("Yes", 0.0)
somewhat_pct = interest_summary.get("Somewhat", 0.0)
no_pct = interest_summary.get("No", 0.0)

expected = {"Yes": 76.0, "Somewhat": 24.0, "No": 0.0}
tolerance = 12.0

differences = {
    "Yes": abs(yes_pct - expected["Yes"]),
    "Somewhat": abs(somewhat_pct - expected["Somewhat"]),
    "No": abs(no_pct - expected["No"])
}

if all(diff <= tolerance for diff in differences.values()):
    print(f"-  Market interest distribution is close to expected (Yes = {yes_pct} %, Somewhat = {somewhat_pct} %, No = {no_pct} %). Supports Graph 2.")
else:
    print(f"- ⚠️ Market interest distribution differs from expected. Observed: Yes = {yes_pct} %, Somewhat = {somewhat_pct} %, No = {no_pct} %.")

# --- Feature preference ---
top_features = feature_counts_rounded.sort_values(ascending=False).head(3)
top_features_list = [f.lower() for f in top_features.index.tolist()]

has_verified = any("verified" in f for f in top_features_list)
has_recruiting = any("recruit" in f for f in top_features_list)

if has_verified and has_recruiting:
    print("-  Top features include Verified Results and Recruiting Tools — matches product narrative.")
elif has_verified or has_recruiting:
    print("- ⚠️ One expected top feature appears, but not both.")
else:
    print("-  Top features differ from expected; review slide narrative or data.")

# --- Final metrics summary ---
print("\nRaw metrics used:")
print(f"- visibility_before = {visibility_before:.1f} %, visibility_after = {visibility_after:.1f} %")
print(f"- organization_before = {organization_before:.1f} %, organization_after = {organization_after:.1f} %")
print(f"- interest breakdown: {interest_summary.to_dict()}")
print(f"- top features (%): {feature_counts_rounded.to_dict()}")
