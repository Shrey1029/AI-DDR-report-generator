import os
import fitz

def extract_data(pdf_path):
    doc = fitz.open(pdf_path)
    full_text = ""
    images = []

    os.makedirs("outputs/images", exist_ok=True)

    for page_num, page in enumerate(doc):
        text = page.get_text()
        full_text += text if text else ""

        for img_index, img in enumerate(page.get_images(full=True)):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]

            img_path = f"outputs/images/img_{page_num}_{img_index}.png"
            with open(img_path, "wb") as f:
                f.write(image_bytes)

            images.append(img_path)

    return full_text, images


def detect_conflicts(text1, text2):
    conflicts = []

    t1 = text1.lower()
    t2 = text2.lower()

    if "crack" in t1 and "no issue" in t2:
        conflicts.append("Inspection shows cracks but thermal report shows no issue.")

    if "leak" in t1 and "normal temperature" in t2:
        conflicts.append("Possible leakage not supported by thermal data.")

    return conflicts


# -----------------------------
# STEP 3: Generate DDR (NO AI)
# -----------------------------
def generate_ddr(inspection_text, thermal_text, conflicts):

    report = {
        "Property Issue Summary":
            "Issues identified from inspection and thermal reports.",

        "Area-wise Observations":
            inspection_text[:500] if inspection_text else "Not Available",

        "Probable Root Cause":
            "Possible structural stress, moisture, or leakage issues.",

        "Severity Assessment":
            "Medium – requires attention but not immediately critical.",

        "Recommended Actions":
            "Repair cracks, fix leakage sources, and conduct further inspection.",

        "Additional Notes":
            "Conflicts: " + ", ".join(conflicts) if conflicts else "No conflicts detected.",

        "Missing or Unclear Information":
            "Not Available"
    }

    return report



def generate_html(report, images):
    html = f"""
    <html>
    <head>
        <title>DDR Report</title>
        <style>
            body {{
                font-family: Arial;
                padding: 30px;
                background-color: #f4f6f7;
            }}
            h1 {{
                text-align: center;
                color: #2c3e50;
            }}
            .section {{
                background: white;
                padding: 15px;
                margin-bottom: 20px;
                border-radius: 10px;
                box-shadow: 0px 2px 8px rgba(0,0,0,0.1);
            }}
            h2 {{
                color: #34495e;
                border-bottom: 2px solid #ddd;
                padding-bottom: 5px;
            }}
            p {{
                color: #555;
            }}
            img {{
                width: 250px;
                margin: 10px;
                border-radius: 8px;
            }}
        </style>
    </head>
    <body>

    <h1>Detailed Diagnostic Report (DDR)</h1>
    """

    for key, value in report.items():
        html += f"""
        <div class="section">
            <h2>{key}</h2>
            <p>{value}</p>
        </div>
        """

    html += "<div class='section'><h2>Supporting Images</h2>"

    if images:
        for img in images:
            img_path = img.replace("outputs/", "")
            html += f'<img src="{img_path}">'
    else:
        html += "<p>Image Not Available</p>"

    html += "</div></body></html>"

    with open("outputs/report.html", "w", encoding="utf-8") as f:
        f.write(html)


def main():
    os.makedirs("outputs", exist_ok=True)

    print("Extracting data...")
    inspection_text, img1 = extract_data("input/inspection.pdf")
    thermal_text, img2 = extract_data("input/thermal.pdf")

    all_images = img1 + img2

    print("Detecting conflicts...")
    conflicts = detect_conflicts(inspection_text, thermal_text)

    print("Generating report...")
    report = generate_ddr(inspection_text, thermal_text, conflicts)

    print("Creating HTML report...")
    generate_html(report, all_images)

    print("DDR Report Generated: outputs/report.html")


if __name__ == "__main__":
    main()