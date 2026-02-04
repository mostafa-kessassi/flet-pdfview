# 📄 flet-pdfview

**A lightweight and efficient PDF viewer component for Flet applications.**

`flet-pdfview` provides a simple way to render PDF files inside your UI while keeping performance, stability, and user experience in mind.

---

### ✨ Features

* 🧩 **Native PDF rendering** inside Flet layouts.
* 🔍 **Interactive Zoom**: Support for zooming in and out with configurable limits.
* 📐 **High-resolution** rendering with custom DPI.
* 🖼️ **Flexible image fitting** using `BoxFit`.
* 📱 **Fully responsive** (via `expand=True`).
* 🚫 **Silent failure** for invalid paths (no crashes, no UI freezes).
* ⚡ **Optimized** for performance and UI stability.

---

### 📦 Installation

Install the package directly from PyPI:

```bash
pip install flet-pdfview
```
### 🚀 Basic UsagePython
```
from flet_pdfview import PdfColumn
from flet import Page, run, BoxFit

def main(page: Page):
    page.add(
        PdfColumn(
            src="path/to/your/file.pdf",
            expand=True,
            dpi=300,
            fitImage=BoxFit.FILL,
            enable_zoom=True
        )
    )

run(main)
```
### 🔍 Zoom Control
You can now fully control the viewing experience with the following properties:

min_zoom: Sets the minimum scale allowed (Default : 0.8).

max_zoom: Sets the maximum scale allowed to ensure quality and performance (Default : 2.5).
### ⚠️ Important Behavior & Performance
**1. Silent Failure**

PdfColumn will not render anything if the provided path does not exist or does not end with .pdf.

No exceptions ❌

No error dialogs ❌

No UI interruption ❌

**2. Technical Performance Warning**

[!WARNING] Resource Management: Be cautious when performing intensive property updates on the PdfColumn object after its initial call. If changes involve high values or frequent updates, it may cause a brief delay when closing the application as the component finishes processing tasks to ensure a stable exit.

> [!IMPORTANT]
> **This behavior is intentional:**
> * **No exceptions** ❌
> * **No error dialogs** ❌
> * **No UI interruption** ❌
> 
> The component simply stays silent and allows the application to continue running normally.

---

### 🎯 Why Silent Failure?

This design choice ensures:

* 🛡️ **Application stability**: Prevents crashes due to missing files.
* 🧠 **Clean Experience**: A distraction-free UI for the end-user.
* 🚀 **Production Ready**: Predictable behavior in live environments.

**In short:** *No valid PDF → No rendering → App remains stable.*
