import re
import os
import PyPDF2

def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text

def extract_text_from_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def load_resume(file_path):
    if file_path.endswith('.pdf'):
        return extract_text_from_pdf(file_path)
    elif file_path.endswith('.txt'):
        return extract_text_from_txt(file_path)
    else:
        raise ValueError("Unsupported file format. Please use .txt or .pdf.")

def check_keywords(resume_text, keywords):
    resume_text_lower = resume_text.lower()
    found = []
    missing = []
    for kw in keywords:
        pattern = re.escape(kw.lower())
        if re.search(pattern, resume_text_lower):
            found.append(kw)
        else:
            missing.append(kw)
    return found, missing

def main():
    print("== Resume Keyword Checker ==")
    resume_path = input("Enter path to your resume (.pdf or .txt): ").strip()
    if not os.path.exists(resume_path):
        print("❌ File not found.")
        return

    # Example keyword input
    print("Paste job description keywords (comma-separated):")
    raw_keywords = input(">> ")
    keywords = [kw.strip() for kw in raw_keywords.split(',') if kw.strip()]

    print("\n📄 Reading resume...")
    try:
        resume_text = load_resume(resume_path)
    except Exception as e:
        print(f"Error: {e}")
        return

    found, missing = check_keywords(resume_text, keywords)

    print("\n=== ✅ Keywords Found ===")
    for word in found:
        print("✔️", word)

    print("\n=== ❌ Keywords Missing ===")
    for word in missing:
        print("❌", word)

    print("\n✅ Done! Make sure your resume speaks the job's language.")

if __name__ == "__main__":
    main()
