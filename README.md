# AI-Driven Document Layout Analysis & Information Extraction

Midterm Requirement in the subject, Intelligent Systems

A comprehensive web application that leverages artificial intelligence and machine learning techniques to automatically analyze document layouts and extract structured information from complex documents such as invoices, forms, and reports.

## Table of Contents
- [Overview](#overview)
- [Purpose and Objectives](#purpose-and-objectives)
- [Core Concepts and Technologies](#core-concepts-and-technologies)
- [Methodology](#methodology)
- [Features](#features)
- [Installation and Setup](#installation-and-setup)
- [Usage](#usage)
- [Architecture](#architecture)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)

## Overview

This application represents a modern approach to document processing, combining traditional computer vision techniques with cutting-edge generative AI to create an intelligent document analysis system. The application can process both PDF documents and images, automatically extracting relevant information based on user-specified fields.

## Purpose and Objectives

### Primary Purpose
To automate the traditionally manual and time-consuming process of extracting structured information from unstructured or semi-structured documents, reducing human error and increasing processing efficiency.

### Key Objectives

1. **Automated Document Processing**: Eliminate manual data entry by automatically extracting key information from documents
2. **Layout Analysis**: Understand document structure and layout to improve extraction accuracy
3. **Flexible Field Extraction**: Allow users to specify custom fields for extraction based on their specific needs
4. **Data Quality Assurance**: Provide mechanisms for users to review and correct extracted data
5. **Multiple Format Support**: Handle various document formats including PDFs and images
6. **User-Friendly Interface**: Provide an intuitive web-based interface for non-technical users
7. **Structured Output**: Generate machine-readable outputs in standard formats (JSON, CSV)

## Core Concepts and Technologies

### 1. Optical Character Recognition (OCR)
- **Technology**: Tesseract OCR engine via `pytesseract`
- **Purpose**: Converts images and scanned documents into machine-readable text
- **Application**: Extracts text from image-based documents and PDF pages

### 2. PDF Processing
- **Technology**: `pdfplumber` library
- **Purpose**: Native text extraction from PDF documents without OCR when possible
- **Advantages**: More accurate than OCR for text-based PDFs, maintains formatting

### 3. Computer Vision
- **Technology**: OpenCV (`cv2`) and PIL (Python Imaging Library)
- **Purpose**: Image preprocessing and enhancement before OCR
- **Applications**: 
  - Image noise reduction
  - Contrast enhancement
  - Document orientation correction

### 4. Natural Language Processing (NLP)
- **Technology**: Google's Gemini AI (Generative AI)
- **Purpose**: Intelligent understanding and extraction of specific fields from unstructured text
- **Advantages**: Context-aware extraction that understands semantic relationships

### 5. Web Application Framework
- **Technology**: Streamlit
- **Purpose**: Rapid development of interactive web applications
- **Benefits**: Real-time updates, easy deployment, built-in widgets

## Methodology

### Phase 1: Document Input and Preprocessing

```
Document Upload → Format Detection → Preprocessing
```

1. **File Upload**: Users upload PDF or image files through the web interface
2. **Format Detection**: Application automatically detects file type and applies appropriate processing
3. **Image Preprocessing**: For images, apply noise reduction and enhancement techniques

### Phase 2: Text Extraction

```
PDF Path: PDF → pdfplumber → Raw Text
Image Path: Image → Tesseract OCR → Raw Text
```

#### PDF Processing:
- Use `pdfplumber` for direct text extraction
- Maintain text structure and formatting
- Extract tables separately for structured data

#### Image Processing:
- Apply image preprocessing using OpenCV
- Use Tesseract for OCR conversion
- Post-process text to clean artifacts

### Phase 3: AI-Powered Information Extraction

```
Raw Text + User Fields → Gemini AI → Structured JSON
```

1. **Prompt Engineering**: Construct intelligent prompts for the AI model
2. **Context Provision**: Send document text and field specifications to Gemini
3. **Structured Response**: Receive JSON-formatted extracted data
4. **Error Handling**: Manage API failures and malformed responses

### Phase 4: User Review and Validation

```
AI Output → User Interface → Manual Corrections → Final Output
```

1. **Data Presentation**: Display extracted fields in editable form
2. **Manual Correction**: Allow users to modify incorrect extractions
3. **Quality Assurance**: Enable users to verify accuracy before export

### Phase 5: Data Export

```
Validated Data → Format Selection → Download (CSV/JSON)
```

## Features

### Current Features

- **Multi-format Support**: PDF and image (PNG, JPG, JPEG) processing
- **Custom Field Extraction**: User-defined fields for flexible data extraction
- **AI-Powered Analysis**: Leverages Google's Gemini for intelligent extraction
- **Interactive Review**: Real-time editing of extracted data
- **Multiple Export Formats**: CSV and JSON download options
- **User Feedback System**: Built-in rating and feedback collection
- **Responsive Design**: Works across different screen sizes

### Technical Features

- **Modular Architecture**: Separate functions for different processing stages
- **Error Handling**: Comprehensive error management throughout the pipeline
- **API Integration**: RESTful integration with Google's Gemini API
- **Session Management**: Streamlit's built-in session state management

## Installation and Setup

### Prerequisites

```bash
Python 3.8+
Tesseract OCR engine
Google Cloud account (for Gemini API)
```

### Installation Steps

1. **Clone the repository**:
```bash
git clone [repository-url]
cd ai-document-analysis
```

2. **Install dependencies**:
```bash
pip install streamlit google-generativeai pdfplumber pytesseract opencv-python pillow pandas requests numpy
```

3. **Install Tesseract OCR**:
   - Windows: Download from [GitHub releases](https://github.com/UB-Mannheim/tesseract/wiki)
   - Linux: `sudo apt-get install tesseract-ocr`
   - macOS: `brew install tesseract`

4. **Configure API Key**:
   - Obtain a Gemini API key from Google Cloud Console
   - Replace the API key in `app.py` (line 8)

5. **Run the application**:
```bash
streamlit run app.py
```

## Usage

### Basic Workflow

1. **Navigate to Demo Page**: Use the sidebar navigation
2. **Upload Document**: Select a PDF or image file
3. **Specify Fields**: Enter comma-separated field names to extract
4. **Extract Data**: Click the "Extract Data" button
5. **Review Results**: Examine and edit the extracted information
6. **Download**: Export results in CSV or JSON format

### Example Field Specifications

- **Invoices**: `invoice number, customer name, total amount, date, vendor`
- **Forms**: `name, address, phone number, email, date of birth`
- **Reports**: `report title, author, date, summary, recommendations`

## Architecture

### System Architecture

```
Frontend (Streamlit) ←→ Backend (Python) ←→ External APIs (Gemini)
                    ↓
              File Processing Layer
                    ↓
           Text Extraction (OCR/PDF)
                    ↓
              AI Processing Layer
                    ↓
              Data Export Layer
```

### Data Flow

1. **Input Layer**: File upload and validation
2. **Processing Layer**: Text extraction and preprocessing
3. **AI Layer**: Intelligent field extraction
4. **Presentation Layer**: User interface for review
5. **Output Layer**: Data export and download

## Future Improvements

### Short-term Enhancements (3-6 months)

1. **Enhanced Document Types**:
   - Support for Word documents (.docx)
   - Excel spreadsheet processing
   - PowerPoint presentation analysis

2. **Improved OCR Accuracy**:
   - Integration with more advanced OCR engines (Azure Cognitive Services, AWS Textract)
   - Document orientation detection and correction
   - Table structure recognition

3. **Batch Processing**:
   - Multiple file upload capability
   - Bulk extraction operations
   - Progress tracking for large batches

4. **Template System**:
   - Pre-defined templates for common document types
   - Custom template creation and saving
   - Template sharing across users

### Medium-term Developments (6-12 months)

5. **Advanced AI Features**:
   - Integration with multiple AI models (OpenAI GPT, Claude)
   - Model ensemble for improved accuracy
   - Confidence scoring for extracted fields

6. **Database Integration**:
   - SQL database support for storing extracted data
   - Search and filtering capabilities
   - Historical data analysis

7. **API Development**:
   - RESTful API for programmatic access
   - Webhook support for automated workflows
   - Third-party integrations

8. **Enhanced User Experience**:
   - Real-time collaboration features
   - User authentication and role management
   - Customizable dashboards

### Long-term Vision (1-2 years)

9. **Machine Learning Pipeline**:
   - Custom model training on user data
   - Continuous learning from user corrections
   - Domain-specific model fine-tuning

10. **Advanced Document Understanding**:
    - Document classification and routing
    - Relationship extraction between entities
    - Multi-language support

11. **Enterprise Features**:
    - Single Sign-On (SSO) integration
    - Audit trails and compliance features
    - Enterprise-grade security

12. **Analytics and Insights**:
    - Processing analytics and metrics
    - Data quality reports
    - Extraction accuracy tracking

### Technical Improvements

13. **Performance Optimization**:
    - Asynchronous processing for large files
    - Caching mechanisms for repeated operations
    - GPU acceleration for OCR tasks

14. **Security Enhancements**:
    - End-to-end encryption for sensitive documents
    - Data anonymization features
    - Secure file storage options

15. **Deployment Options**:
    - Docker containerization
    - Cloud deployment guides (AWS, GCP, Azure)
    - On-premises installation packages

## Contributing

We welcome contributions to improve this project! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch
3. Make your changes with appropriate tests
4. Submit a pull request with a clear description

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

**Note**: This application is designed for educational and research purposes. For production use, please ensure proper security measures and API key management are implemented.



