from pdfminer.high_level import extract_text


def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)


if __name__ == '__main__':
    print(extract_text_from_pdf(r'C:\Users\faiza\Resume_Recommendation_System\app\static\uploads'))