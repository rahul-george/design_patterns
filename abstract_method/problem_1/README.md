# 🧠 Factory Method Pattern Practice Problem

## 📝 Problem Statement: Report Exporter with Pluggable Formats

You’re building the export module for a SaaS analytics platform. Users can export dashboards to different formats: **PDF**, **CSV**, and **HTML** today, with more like **XLSX** and **Markdown** coming soon. While the core export workflow—pagination, metadata handling, and data streaming—remains the same, the file writing logic differs for each format.

## 🎯 Goals

- Design a single export workflow that is format-agnostic.
- Enable adding new formats without changing core logic.
- Separate responsibilities clearly:
  - The export workflow orchestrates.
  - Format-specific writers handle file mechanics.

## ⚙️ Functional Requirements

- **Input:**
  - Data rows (streaming or large batch)
  - Dashboard metadata (e.g., title, author, createdAt)
  - Export options (e.g., page size for PDF, delimiter for CSV)

- **Output:**  
  - A file in the selected format (saved to disk or returned as byte stream)

- **Export Flow Must:**
  - Initialize a writer for the selected format
  - Write header/metadata
  - Stream and write data rows
  - Write footer (e.g. summary stats)
  - Finalize and close output

- **Writer Interface Must Support:**
  - `open(target)`
  - `writeHeader(metadata)`
  - `writeRow(row)`
  - `writeFooter(stats)`
  - `close()`

- **Error Handling:**
  - On failure during writing, ensure cleanup of resources and remove partial files.
  - Emit export summary with row count, duration, and file size.

## 📐 Non-Functional Requirements

- Handle large datasets without memory overload.
- No format-specific conditionals in core export logic.
- Adding new formats should require changes limited to their own writer classes.

## 🧪 Acceptance Criteria

- Core exporter must call a **factory method** to obtain the writer.
- Exporter should be unaware of concrete writer classes.
- Demo should show exporting the same dataset to multiple formats using identical workflow.
- Logs or output summary must confirm headers, rows, and footer written via correct writer.
