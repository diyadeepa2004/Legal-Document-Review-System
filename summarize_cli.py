from extract_text import extract_text_from_pdf
from preprocess import clean_text
from summarizer import summarize_contract
from risk_detector import keyword_risk_detection
from clause_classifier import predict_clause_risk
import os

def main():
    print("\n=== Legal Document Review CLI Tool ===")
    file_path = input("Enter path to PDF file (or press Enter for 'data/sample_contract.pdf'): ").strip()

    if not file_path:
        file_path = "data/sample_contract.pdf"

    if not os.path.exists(file_path):
        print(f" File not found: {file_path}")
        return

    print("\n Extracting text...")
    text = extract_text_from_pdf(file_path)

    print(" Cleaning text...")
    cleaned = clean_text(text)

    print(" Summarizing document...")
    summary = summarize_contract(cleaned)

    print("\n--- SUMMARY ---\n")
    print(summary)

    print("\n--- RISK ANALYSIS ---")
    keyword_risk = keyword_risk_detection(cleaned)
    print(keyword_risk)

    try:
        model_risk = predict_clause_risk(cleaned)
        print("ML-based Risk Prediction:", model_risk)
    except:
        print(" No trained ML model found. Using keyword-based risk detection only.")

if __name__ == "__main__":
    main()
