import os
import cv2
from text_extraction import extract_text_with_confidence
from image_cleaning import clean_image
from validation import validate_document
from report_generation import generate_report

input_path = "input_documents/sample.jpg"
print(f"Input: {input_path}")

if not os.path.exists(input_path):
    print(f"File not found at {input_path}")
    exit()

image = cv2.imread(input_path)
cleaned = clean_image(image)

# Save cleaned image
cv2.imwrite("processed_images/sample_cleaned.jpg", cleaned)
print("Cleaned image saved")

full_text, df_conf, avg_conf = extract_text_with_confidence(cleaned)
print(f"Extracted Text: {full_text[:200]}")
print(f"Avg Confidence: {avg_conf:.2f}")

results = validate_document(full_text, avg_conf)
print(f"Validation: {results}")

generate_report(input_path, full_text, avg_conf, results)
print("DONE! Check output_reports/report.csv and processed_images folder")