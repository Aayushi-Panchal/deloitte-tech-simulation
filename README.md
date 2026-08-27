<div align="center">

# Deloitte Australia Tech Job Simulation

### Software Development · Data Transformation · Testing

A technical job simulation completed as part of the **Deloitte Australia Technology Job Simulation on Forage**, focused on solving practical software development and data-processing tasks.

<br>

<img src="https://img.shields.io/badge/Deloitte-Technology%20Simulation-86BC25?style=for-the-badge&logo=deloitte&logoColor=white"/>
<img src="https://img.shields.io/badge/Forage-Job%20Simulation-111827?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/JSON-000000?style=for-the-badge&logo=json&logoColor=white"/>

</div>

---

## Overview

This project was completed as part of **Deloitte Australia's virtual technology job simulation through Forage**.

The simulation involved working with existing code, transforming structured data, writing a development proposal, and analyzing manufacturing-related dashboards.

It provided practical exposure to how software development and data processing tasks can be approached in a professional technology environment.

---

## Tasks Completed

### Code Modification

Modified existing Python code to process and transform device data represented in different JSON formats.

### Data Transformation

The project handles two different input formats and converts them into a consistent structure.

```text
Format 1 ──────┐
               ├──→ Common Data Structure
Format 2 ──────┘
```

The transformation includes:

- Device information
- Device type
- Timestamp conversion
- Location details
- Operational data
- Temperature information

### Development Proposal

Prepared a **development proposal** as part of the simulation, outlining the proposed technical approach.

### Manufacturing Dashboard Analysis

Analyzed manufacturing-related dashboard information to understand operational data and identify relevant insights.

---

## Technical Implementation

The Python solution contains separate conversion functions for the two incoming JSON structures.

### Format 1

The first format contains location information as a single `/` separated string along with operational fields.

The implementation splits the location into:

```text
Country
   ↓
City
   ↓
Area
   ↓
Factory
   ↓
Section
```

and restructures the operational information into a standardized `data` object.

### Format 2

The second format contains nested device information and an ISO-formatted timestamp.

The implementation:

- Extracts nested device information
- Converts the ISO timestamp into milliseconds
- Structures location information
- Preserves the provided device data

---

## Main Router

A central `main()` function determines which conversion method should be used based on the structure of the incoming JSON object.

```text
Incoming JSON
      ↓
Check Device Structure
      ↓
 ┌───────────────┐
 │               │
Format 1       Format 2
 │               │
 ↓               ↓
Convert 1      Convert 2
 │               │
 └───────┬───────┘
         ↓
 Standardized Output
```

This allows both input formats to be processed through a common interface.

---

## Testing

Unit testing was implemented using Python's built-in **unittest** framework.

The test suite checks:

- Basic data consistency
- Conversion from Format 1
- Conversion from Format 2

```text
Input Data
    ↓
Conversion
    ↓
Expected Result
    ↓
Unit Test
    ↓
Pass / Fail
```

The solution includes separate test cases for each supported data format.

---

## Tech Stack

<div align="center">

<p>
<img src="https://skillicons.dev/icons?i=python" />
</p>

<img src="https://img.shields.io/badge/JSON-000000?style=for-the-badge&logo=json&logoColor=white"/>
<img src="https://img.shields.io/badge/unittest-Python%20Standard%20Library-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Data%20Transformation-86BC25?style=for-the-badge"/>

</div>

---

## Key Concepts

- Python programming
- JSON data processing
- Data transformation
- Nested data structures
- Timestamp conversion
- Conditional routing
- Unit testing
- Manufacturing data analysis
- Development proposal writing

---

## Project Structure

```text
deloitte-tech-simulation/
│
├── data-1.json
├── data-2.json
├── data-result.json
├── solution.py
├── Proposal.pdf
└── README.md
```

---

## Key Learnings

Through this simulation, I gained practical experience in:

- Modifying and extending existing code
- Working with different JSON data formats
- Converting inconsistent data into a standardized structure
- Handling timestamps and nested objects
- Writing unit tests for data-processing logic
- Understanding technology tasks in a manufacturing context
- Communicating technical solutions through a development proposal

---

<div align="center">

### Deloitte Australia · Technology Job Simulation

**Software Development • Data Transformation • Testing**

<br>

<img src="https://img.shields.io/badge/Python-Data%20Processing-3776AB?style=flat-square&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/JSON-Transformation-000000?style=flat-square&logo=json&logoColor=white"/>
<img src="https://img.shields.io/badge/Unit%20Testing-Completed-86BC25?style=flat-square"/>

</div>
