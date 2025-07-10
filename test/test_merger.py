import os
from PyPDF2 import PdfMerger

def test_pdf_merge():
    merger = PdfMerger()

    # Create dummy PDFs for test
    from PyPDF2 import PdfWriter

    filenames = []
    for i in range(2):
        writer = PdfWriter()
        writer.add_blank_page(width=72, height=72)
        fname = f"test_file_{i}.pdf"
        with open(fname, "wb") as f:
            writer.write(f)
        filenames.append(fname)

    # Merge PDFs
    output = "merged_test.pdf"
    try:
        for file in filenames:
            merger.append(file)
        merger.write(output)
        merger.close()

        # Check if output file exists
        assert os.path.exists(output)
        assert os.path.getsize(output) > 0

        print("✅ Test Passed: PDF merged successfully.")

    finally:
        # Clean up
        for f in filenames + [output]:
            if os.path.exists(f):
                os.remove(f)

if __name__ == "__main__":
    test_pdf_merge()