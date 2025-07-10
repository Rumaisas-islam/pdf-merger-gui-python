import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QFileDialog, QLabel, QMessageBox
)
from PyPDF2 import PdfMerger

class PDFMergerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PDF Merger - by Rumaisa")
        self.setGeometry(100, 100, 400, 200)

        self.pdf_files = []

        layout = QVBoxLayout()

        self.label = QLabel("No PDFs selected yet.")
        layout.addWidget(self.label)

        self.browse_button = QPushButton("📂 Select PDFs to Merge")
        self.browse_button.clicked.connect(self.select_pdfs)
        layout.addWidget(self.browse_button)

        self.merge_button = QPushButton("🛠️ Merge PDFs and Save")
        self.merge_button.clicked.connect(self.merge_pdfs)
        layout.addWidget(self.merge_button)

        self.setLayout(layout)

    def select_pdfs(self):
        files, _ = QFileDialog.getOpenFileNames(
            self,
            "Select PDF files",
            "",
            "PDF Files (*.pdf)"
        )
        if files:
            self.pdf_files = files
            self.label.setText(f"{len(files)} file(s) selected.")
        else:
            self.label.setText("No PDFs selected.")

    def merge_pdfs(self):
        if not self.pdf_files:
            QMessageBox.warning(self, "No PDFs", "Please select PDFs first.")
            return

        save_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save Merged PDF As",
            "merged.pdf",
            "PDF Files (*.pdf)"
        )

        if save_path:
            merger = PdfMerger()
            try:
                for pdf in self.pdf_files:
                    merger.append(pdf)
                merger.write(save_path)
                merger.close()
                QMessageBox.information(self, "Success", f"Merged PDF saved to:\n{save_path}")
            except Exception as e:
                QMessageBox.critical(self, "Error", str(e))
        else:
            QMessageBox.information(self, "Cancelled", "Save operation cancelled.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PDFMergerApp()
    window.show()
    sys.exit(app.exec_())