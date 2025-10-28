---
name: excel-expert-skill
description: Master Microsoft Excel from basics to advanced automation. Use for Excel formulas (VLOOKUP, INDEX-MATCH, XLOOKUP, SUMIFS, array formulas), pivot tables, Power Query (data transformation, M language), Power Pivot (DAX formulas, data modeling), data visualization (charts, conditional formatting, sparklines), dashboard creation, VBA macros (automation, UserForms), data analysis (What-If Analysis, Solver, regression), Excel tables (structured references), dynamic arrays (FILTER, SORT, UNIQUE), financial modeling, keyboard shortcuts, data validation, and production-ready Excel workflows for business analytics.
---

# Excel Expert Mastery Skill

## Overview

**Excel = The world's most powerful spreadsheet tool for business analytics, financial modeling, and data analysis.**

**This skill covers:**
- 📊 Essential Functions & Formulas (VLOOKUP, INDEX-MATCH, XLOOKUP)
- 📈 Advanced Analysis (Pivot Tables, Power Query, Power Pivot)
- 🎨 Data Visualization (Charts, Dashboards, Conditional Formatting)
- 🤖 Automation (VBA Macros, Power Automate)
- 💼 Business Applications (Financial Modeling, Reporting)
- ⚡ Productivity (Shortcuts, Best Practices)

**Target Users:** Business Analysts, Financial Analysts, Data Analysts, Excel Power Users

---

# Part 1: Excel Fundamentals & Essential Functions

## 1.1 Excel Interface & Navigation

### Ribbon Organization
```
Home Tab:
├─ Clipboard (Copy, Paste, Format Painter)
├─ Font (Formatting)
├─ Alignment
├─ Number (Formatting)
├─ Styles (Cell Styles, Conditional Formatting)
├─ Cells (Insert, Delete)
└─ Editing (Sum, Fill, Find)

Insert Tab:
├─ Tables
├─ Illustrations (Charts, Pictures)
├─ Add-ins
└─ Charts

Data Tab:
├─ Get & Transform Data (Power Query)
├─ Queries & Connections
├─ Sort & Filter
├─ Data Tools (Text to Columns, Remove Duplicates)
└─ Forecast (What-If Analysis)

Formulas Tab:
├─ Insert Function
├─ AutoSum
├─ Recently Used
├─ Financial, Logical, Text, Date & Time
└─ More Functions
```

### Essential Keyboard Shortcuts
```
Navigation:
Ctrl + Arrow Keys    = Jump to edge of data region
Ctrl + Home         = Go to cell A1
Ctrl + End          = Go to last used cell
Ctrl + Page Up/Down = Switch between worksheets

Selection:
Ctrl + Shift + Arrow = Select to edge of data
Ctrl + A            = Select all
Shift + Space       = Select entire row
Ctrl + Space        = Select entire column

Editing:
F2                  = Edit cell
Ctrl + D            = Fill down
Ctrl + R            = Fill right
Ctrl + ;            = Insert current date
Ctrl + Shift + ;    = Insert current time

Formatting:
Ctrl + 1            = Format Cells dialog
Ctrl + Shift + $    = Currency format
Ctrl + Shift + %    = Percentage format
Ctrl + Shift + #    = Date format

Formulas:
F4                  = Toggle absolute/relative references
Ctrl + `            = Show formulas
Alt + =             = AutoSum
```

---

## 1.2 Essential Lookup Functions

### VLOOKUP (Legacy but still widely used)
```excel
=VLOOKUP(lookup_value, table_array, col_index_num, [range_lookup])

Example:
=VLOOKUP(A2, Products!A:D, 3, FALSE)
// Looks up value in A2, searches in Products sheet columns A-D,
// returns value from 3rd column, exact match

Limitations:
❌ Only looks to the right
❌ Breaks when columns are inserted
❌ Slow with large datasets
```

### INDEX-MATCH (Better alternative)
```excel
=INDEX(return_range, MATCH(lookup_value, lookup_range, 0))

Example:
=INDEX(Products!D:D, MATCH(A2, Products!A:A, 0))
// More flexible, looks left/right, faster

Two-way lookup:
=INDEX(data_range,
       MATCH(row_value, row_range, 0),
       MATCH(col_value, col_range, 0))
```

### XLOOKUP (Modern, Excel 365+)
```excel
=XLOOKUP(lookup_value, lookup_array, return_array, [if_not_found], [match_mode], [search_mode])

Example:
=XLOOKUP(A2, Products!A:A, Products!D:D, "Not Found")

Advanced features:
// Return multiple columns
=XLOOKUP(A2, Products!A:A, Products!B:E)

// Approximate match
=XLOOKUP(A2, Grades!A:A, Grades!B:B, , 1)  // 1 = exact or next smallest

// Search from last to first
=XLOOKUP(A2, Sales!A:A, Sales!D:D, , , -1)
```

---

## 1.3 Logical & Conditional Functions

### IF Statements
```excel
// Basic IF
=IF(A2 > 100, "High", "Low")

// Nested IF
=IF(A2 >= 90, "A",
   IF(A2 >= 80, "B",
      IF(A2 >= 70, "C",
         IF(A2 >= 60, "D", "F"))))

// Better: IFS (Excel 2016+)
=IFS(A2 >= 90, "A",
     A2 >= 80, "B",
     A2 >= 70, "C",
     A2 >= 60, "D",
     TRUE, "F")  // Default value
```

### AND, OR, NOT
```excel
// AND - All conditions must be TRUE
=IF(AND(A2 > 100, B2 < 50), "Approved", "Rejected")

// OR - At least one condition must be TRUE
=IF(OR(A2 = "VIP", B2 > 1000), "Premium", "Standard")

// NOT - Reverses logic
=IF(NOT(A2 = "Cancelled"), "Active", "Inactive")

// Complex combination
=IF(AND(OR(A2 = "VIP", A2 = "Gold"), B2 > 500), "Discount", "No Discount")
```

### SWITCH (Excel 2016+)
```excel
=SWITCH(expression, value1, result1, [value2, result2], ..., [default])

Example - Convert grade to points:
=SWITCH(A2,
        "A", 4.0,
        "B", 3.0,
        "C", 2.0,
        "D", 1.0,
        "F", 0.0,
        "Invalid")  // Default
```

---

## 1.4 Text Functions

### Common Text Operations
```excel
// Combine text
=CONCATENATE(A2, " ", B2)      // Legacy
=CONCAT(A2, " ", B2)           // Excel 2016+
=TEXTJOIN(", ", TRUE, A2:A10)  // Join with delimiter, ignore blanks

// Extract text
=LEFT(A2, 5)         // First 5 characters
=RIGHT(A2, 3)        // Last 3 characters
=MID(A2, 3, 4)       // 4 characters starting at position 3

// Find position
=FIND("@", A2)       // Case-sensitive
=SEARCH("excel", A2) // Case-insensitive

// Replace
=SUBSTITUTE(A2, "old", "new")           // Replace all
=SUBSTITUTE(A2, "old", "new", 2)        // Replace 2nd occurrence
=REPLACE(A2, 1, 5, "Excel")             // Replace by position

// Clean
=TRIM(A2)            // Remove extra spaces
=CLEAN(A2)           // Remove non-printable characters
=UPPER(A2)           // Uppercase
=LOWER(A2)           // Lowercase
=PROPER(A2)          // Title Case
```

### Text Extraction Examples
```excel
// Extract email domain
=MID(A2, FIND("@", A2) + 1, LEN(A2))

// Extract first name from "Lastname, Firstname"
=TRIM(MID(A2, FIND(",", A2) + 1, LEN(A2)))

// Extract last name
=LEFT(A2, FIND(",", A2) - 1)

// Split text (Excel 365 - use TEXTSPLIT)
=TEXTSPLIT(A2, " ")  // Split by space into columns
=TEXTSPLIT(A2, ",", , TRUE)  // Split by comma, ignore empty
```

---

## 1.5 Date & Time Functions

### Date Functions
```excel
// Current date/time
=TODAY()             // Returns current date
=NOW()               // Returns current date & time

// Create date
=DATE(2024, 12, 31)  // December 31, 2024

// Extract components
=YEAR(A2)            // Extract year
=MONTH(A2)           // Extract month (1-12)
=DAY(A2)             // Extract day (1-31)
=WEEKDAY(A2)         // Day of week (1-7, Sunday=1)
=WEEKDAY(A2, 2)      // Monday=1

// Date calculations
=EDATE(A2, 3)        // Add 3 months
=EOMONTH(A2, 0)      // End of current month
=EOMONTH(A2, 1)      // End of next month
=WORKDAY(A2, 10)     // 10 business days after A2
=WORKDAY.INTL(A2, 10, 1)  // Custom weekend definition

// Days between dates
=DATEDIF(start_date, end_date, "D")     // Days
=DATEDIF(start_date, end_date, "M")     // Months
=DATEDIF(start_date, end_date, "Y")     // Years
=NETWORKDAYS(start_date, end_date)      // Business days
```

### Time Functions
```excel
// Create time
=TIME(14, 30, 0)     // 2:30 PM

// Extract components
=HOUR(A2)            // Extract hour (0-23)
=MINUTE(A2)          // Extract minute (0-59)
=SECOND(A2)          // Extract second (0-59)

// Time calculations (times are fractions of a day)
=A2 + TIME(2, 30, 0) // Add 2.5 hours
=A2 - B2             // Time difference (result in days)
=(A2 - B2) * 24      // Time difference in hours
=(A2 - B2) * 1440    // Time difference in minutes
```

### Date Formatting Tips
```
Format Code         Result
-----------         ------
dd/mm/yyyy          31/12/2024
mm/dd/yyyy          12/31/2024
ddd, mmm d          Mon, Dec 31
dddd, mmmm d, yyyy  Monday, December 31, 2024
[$-th-TH]d mmmm yyyy  31 ธันวาคม 2024 (Thai)
```

---

# Part 2: Advanced Formulas & Data Analysis

## 2.1 SUMIF, COUNTIF, AVERAGEIF Family

### Single Criterion Functions
```excel
// SUMIF - Sum based on criteria
=SUMIF(range, criteria, [sum_range])
=SUMIF(A:A, "Apple", C:C)           // Sum C where A = "Apple"
=SUMIF(B:B, ">100", C:C)            // Sum C where B > 100
=SUMIF(A:A, "Apple")                // Sum A where A = "Apple"

// COUNTIF - Count based on criteria
=COUNTIF(A:A, "Apple")              // Count cells = "Apple"
=COUNTIF(B:B, ">100")               // Count cells > 100
=COUNTIF(A:A, "*apple*")            // Wildcard match

// AVERAGEIF
=AVERAGEIF(A:A, "North", B:B)       // Average B where A = "North"
```

### Multiple Criteria Functions
```excel
// SUMIFS - Sum with multiple criteria
=SUMIFS(sum_range, criteria_range1, criteria1, [cr2, c2], ...)
=SUMIFS(D:D, A:A, "Apple", B:B, "North", C:C, ">100")
// Sum D where A="Apple" AND B="North" AND C>100

// COUNTIFS
=COUNTIFS(A:A, "Apple", B:B, ">100")

// AVERAGEIFS
=AVERAGEIFS(D:D, A:A, "North", B:B, ">=100")

// Dynamic criteria
=SUMIFS(Sales, Region, F2, Product, F3)  // Criteria from cells
```

### Wildcard Patterns
```excel
// * = any characters, ? = single character
=COUNTIF(A:A, "apple*")     // Starts with "apple"
=COUNTIF(A:A, "*apple")     // Ends with "apple"
=COUNTIF(A:A, "*apple*")    // Contains "apple"
=COUNTIF(A:A, "apple?")     // "apple" + 1 character
=COUNTIF(A:A, "???")        // Exactly 3 characters
```

---

## 2.2 Array Formulas & Dynamic Arrays (Excel 365)

### Dynamic Array Functions
```excel
// FILTER - Filter data based on conditions
=FILTER(array, include, [if_empty])
=FILTER(A2:D100, C2:C100 > 100)              // Single condition
=FILTER(A2:D100, (C2:C100 > 100) * (B2:B100 = "North"))  // AND
=FILTER(A2:D100, (C2:C100 > 100) + (B2:B100 = "VIP"))    // OR

// SORT - Sort data
=SORT(array, [sort_index], [sort_order], [by_col])
=SORT(A2:D100, 3, -1)                        // Sort by 3rd column, descending
=SORT(A2:D100, {2,1}, {1,-1})                // Sort by col 2 asc, then col 1 desc

// SORTBY - Sort by another array
=SORTBY(A2:D100, C2:C100, -1)                // Sort A:D by column C descending

// UNIQUE - Extract unique values
=UNIQUE(array, [by_col], [exactly_once])
=UNIQUE(A2:A100)                             // Unique list
=UNIQUE(A2:C100)                             // Unique rows
=UNIQUE(A2:A100, , TRUE)                     // Values that appear once

// SEQUENCE - Generate number sequence
=SEQUENCE(rows, [columns], [start], [step])
=SEQUENCE(10)                                // 1 to 10
=SEQUENCE(5, 3, 10, 2)                       // 5x3 grid, start 10, step 2

// RANDARRAY - Random numbers
=RANDARRAY(rows, [columns], [min], [max], [integer])
=RANDARRAY(10, 1, 1, 100, TRUE)              // 10 random integers 1-100
```

### Combining Dynamic Arrays
```excel
// Top 10 products by sales
=SORT(FILTER(A2:C100, B2:B100 = "North"), 3, -1)

// Unique customers with total sales
=UNIQUE(A2:A100)  // In one column
=SUMIF(A:A, D2:D11, C:C)  // In next column (where D2:D11 = unique list)

// Or use SUMIFS with dynamic array:
=BYROW(UNIQUE(A2:A100), LAMBDA(customer, SUMIF(A:A, customer, C:C)))
```

### Legacy Array Formulas (Ctrl+Shift+Enter)
```excel
// Sum top 3 values
{=SUM(LARGE(A2:A100, {1;2;3}))}

// Count unique values (pre-365)
{=SUM(1/COUNTIF(A2:A100, A2:A100))}

// Multi-criteria sum (pre-SUMIFS)
{=SUM((A2:A100="North")*(B2:B100="Apple")*C2:C100)}
```

---

## 2.3 Advanced Lookups & Data Retrieval

### Multiple Criteria Lookup
```excel
// INDEX-MATCH with multiple criteria
=INDEX(return_range,
       MATCH(1, (criteria1_range=value1) * (criteria2_range=value2), 0))
// Must be entered as array formula (Ctrl+Shift+Enter) in older Excel

// Excel 365 - Use FILTER
=FILTER(D:D, (A:A = "North") * (B:B = "Apple"))
```

### Lookup with Approximate Match
```excel
// Find tax bracket
=VLOOKUP(income, tax_table, 2, TRUE)  // TRUE = approximate match

// Better: XLOOKUP with exact or next smallest
=XLOOKUP(income, brackets, rates, , 1)
```

### Return Multiple Columns
```excel
// XLOOKUP return multiple columns (Excel 365)
=XLOOKUP(A2, Products!A:A, Products!B:E)  // Returns B, C, D, E

// INDEX with multiple columns
=INDEX(Products!B:E, MATCH(A2, Products!A:A, 0), {1,2,3,4})
```

### Two-Way Lookup (Matrix Lookup)
```excel
// Price table: Products in rows, Regions in columns
=INDEX(B2:E10,
       MATCH("Product A", A2:A10, 0),
       MATCH("North", B1:E1, 0))

// Or XLOOKUP two-way
=XLOOKUP(product, A2:A10,
         XLOOKUP(region, B1:E1, B2:E10))
```

---

## 2.4 Statistical & Mathematical Functions

### Basic Statistics
```excel
// Central tendency
=AVERAGE(A:A)        // Mean
=MEDIAN(A:A)         // Median
=MODE.SNGL(A:A)      // Most frequent value
=MODE.MULT(A:A)      // Multiple modes (array formula)

// Spread
=STDEV.S(A:A)        // Standard deviation (sample)
=STDEV.P(A:A)        // Standard deviation (population)
=VAR.S(A:A)          // Variance (sample)

// Position
=MIN(A:A)            // Minimum
=MAX(A:A)            // Maximum
=LARGE(A:A, 2)       // 2nd largest
=SMALL(A:A, 3)       // 3rd smallest
=PERCENTILE.INC(A:A, 0.95)  // 95th percentile
=QUARTILE.INC(A:A, 1)       // 1st quartile (Q1)

// Count
=COUNT(A:A)          // Count numbers
=COUNTA(A:A)         // Count non-empty
=COUNTBLANK(A:A)     // Count blanks
```

### Rounding Functions
```excel
=ROUND(A2, 2)        // Round to 2 decimals
=ROUNDUP(A2, 0)      // Round up to integer
=ROUNDDOWN(A2, 1)    // Round down to 1 decimal
=MROUND(A2, 0.25)    // Round to nearest 0.25
=CEILING(A2, 10)     // Round up to nearest 10
=FLOOR(A2, 5)        // Round down to nearest 5
=INT(A2)             // Remove decimals
=TRUNC(A2, 1)        // Truncate to 1 decimal
```

### Advanced Math
```excel
// Absolute & sign
=ABS(A2)             // Absolute value
=SIGN(A2)            // Returns -1, 0, or 1

// Power & roots
=POWER(A2, 3)        // A2^3
=SQRT(A2)            // Square root
=A2^(1/3)            // Cube root

// Random
=RAND()              // Random 0-1
=RANDBETWEEN(1, 100) // Random integer 1-100

// Modulo
=MOD(A2, 3)          // Remainder after dividing by 3

// Aggregate (ignore errors)
=AGGREGATE(function_num, options, array)
=AGGREGATE(9, 6, A:A)  // SUM, ignore errors
// function_num: 1=AVERAGE, 4=MAX, 5=MIN, 9=SUM, etc.
// options: 6=ignore errors, 7=ignore errors+hidden rows
```

---

## 2.5 Financial Functions

### Loan & Investment Calculations
```excel
// Loan payment
=PMT(rate, nper, pv, [fv], [type])
=PMT(5%/12, 30*12, -200000)  // Monthly payment for $200k loan at 5% for 30 years

// Interest portion
=IPMT(rate, per, nper, pv)
=IPMT(5%/12, 1, 360, -200000)  // Interest in 1st payment

// Principal portion
=PPMT(rate, per, nper, pv)
=PPMT(5%/12, 1, 360, -200000)  // Principal in 1st payment

// Future value
=FV(rate, nper, pmt, [pv], [type])
=FV(8%/12, 20*12, -500, 0, 0)  // Save $500/month at 8% for 20 years

// Present value
=PV(rate, nper, pmt, [fv], [type])
=PV(6%/12, 10*12, -1000)  // PV of $1000/month for 10 years at 6%

// Number of periods
=NPER(rate, pmt, pv, [fv])
=NPER(6%/12, -1000, 50000)  // Months to pay off $50k at 6% paying $1000/month

// Interest rate
=RATE(nper, pmt, pv, [fv])
=RATE(360, -1200, 200000) * 12  // Annual rate
```

### Investment Analysis
```excel
// Net Present Value
=NPV(rate, value1, [value2], ...)
=NPV(10%, B2:B6)  // Discount rate 10%, cash flows in B2:B6
=NPV(10%, B2:B6) + B1  // Add initial investment

// Internal Rate of Return
=IRR(values, [guess])
=IRR(B1:B6)  // B1 = initial investment (negative)

// Modified IRR
=MIRR(values, finance_rate, reinvest_rate)
=MIRR(B1:B6, 8%, 10%)

// Depreciation
=SLN(cost, salvage, life)  // Straight-line
=DB(cost, salvage, life, period)  // Declining balance
=DDB(cost, salvage, life, period)  // Double declining balance
```

---

# Part 3: Pivot Tables, Power Query & Data Visualization

## 3.1 Excel Tables (Structured References)

### Creating & Using Tables
```
Create Table:
1. Select data range
2. Ctrl + T (or Insert > Table)
3. Check "My table has headers"
4. Click OK

Benefits:
✅ Auto-expand when adding data
✅ Structured references (readable formulas)
✅ Built-in filtering
✅ Easy formatting
✅ Works seamlessly with Pivot Tables
```

### Structured References
```excel
// Instead of: =SUM(C2:C100)
=SUM(Sales[Amount])

// Calculated columns auto-fill
=[Amount] * [Quantity]  // In table column

// This row
=[@Amount] * [@Quantity]

// Specific columns
=Sales[[#Headers],[Amount]]  // Header
=Sales[[#Totals],[Amount]]   // Total row
=Sales[[#Data],[Amount]]     // Data only
=Sales[[Amount]:[Tax]]       // Multiple columns

// Entire table
=Sales[#All]
```

### Table Formulas
```excel
// VLOOKUP with tables
=VLOOKUP(A2, Products[#All], 3, FALSE)

// SUMIF with tables
=SUMIF(Sales[Region], "North", Sales[Amount])

// Count unique in table
=SUMPRODUCT(1/COUNTIF(Sales[Product], Sales[Product]))
```

---

## 3.2 Pivot Tables

### Creating Pivot Tables
```
Steps:
1. Click anywhere in data (or Table)
2. Insert > PivotTable
3. Choose data range
4. Choose location (New/Existing worksheet)
5. Drag fields to areas:
   - Rows: Categories/dimensions
   - Columns: Additional dimensions
   - Values: Metrics to aggregate
   - Filters: Filter entire report
```

### Pivot Table Structure
```
Rows Area:
├─ Product Category
└─ Product Name

Columns Area:
├─ Year
└─ Quarter

Values Area:
├─ Sum of Sales
├─ Count of Orders
└─ Average Discount

Filters:
├─ Region
└─ Sales Rep
```

### Value Field Settings
```
Aggregation Functions:
- Sum (default for numbers)
- Count
- Average
- Max / Min
- Product
- Count Numbers
- StdDev / StdDevP
- Var / VarP

Show Values As:
- % of Grand Total
- % of Column Total
- % of Row Total
- % of Parent Row Total
- Difference From
- % Difference From
- Running Total In
- % Running Total In
- Rank Smallest to Largest
- Index
```

### Calculated Fields & Items
```
Calculated Field:
Insert > Calculated Field
Name: "Profit Margin"
Formula: =Profit / Sales

Calculated Item:
Right-click on field value
Insert Calculated Item
Name: "Q1-Q2"
Formula: =Q1 + Q2
```

### Pivot Table Formulas (GETPIVOTDATA)
```excel
// Auto-generated when clicking pivot table cells
=GETPIVOTDATA("Sales", $A$3, "Product", "Apple", "Region", "North")

// More flexible with cell references
=GETPIVOTDATA("Sales", $A$3, "Product", E2)

// Disable auto-GETPIVOTDATA:
File > Options > Formulas > Uncheck "Use GetPivotData"
```

---

## 3.3 Power Query (Get & Transform)

### Power Query Basics
```
Launch Power Query:
Data > Get Data > From File/Table/Other
Or: Data > From Table/Range (for existing data)

Power Query Editor opens:
- Applied Steps (right pane) - transformation history
- Formula Bar - M language formulas
- Queries pane (left) - all queries
```

### Common Transformations
```
Data Cleaning:
├─ Remove Duplicates
├─ Remove Errors
├─ Remove Blanks
├─ Trim (remove spaces)
├─ Clean (remove non-printable)
└─ Replace Values

Data Types:
├─ Change Type
├─ Detect Data Type
└─ Using Locale

Column Operations:
├─ Split Column (by delimiter, position, # characters)
├─ Merge Columns
├─ Pivot Column (rows → columns)
├─ Unpivot Columns (columns → rows)
├─ Add Custom Column
└─ Extract (Text Before/After/Range)

Filter & Sort:
├─ Filter Rows
├─ Keep Top Rows / Bottom Rows
├─ Keep Errors / Remove Errors
└─ Sort Ascending/Descending

Group By:
├─ Group rows
├─ Aggregations: Sum, Count, Average, Min, Max
└─ All Rows (create nested table)
```

### Merge & Append Queries
```
Merge (JOIN):
Home > Merge Queries
Select matching columns
Join Kinds:
├─ Left Outer (keep all from first)
├─ Right Outer (keep all from second)
├─ Full Outer (keep all from both)
├─ Inner (only matching)
├─ Left Anti (only in first)
└─ Right Anti (only in second)

Append (UNION):
Home > Append Queries
Combines tables vertically
```

### M Language Basics
```m
// Add custom column
= Table.AddColumn(#"Previous Step", "NewColumn", each [Column1] * [Column2])

// Conditional column
= Table.AddColumn(#"Previous Step", "Category",
    each if [Sales] > 1000 then "High"
         else if [Sales] > 500 then "Medium"
         else "Low")

// Text operations
= Table.AddColumn(#"Previous Step", "Domain", each Text.AfterDelimiter([Email], "@"))

// Date operations
= Table.AddColumn(#"Previous Step", "YearMonth", each Date.ToText([Date], "yyyy-MM"))

// Replace errors
= Table.ReplaceErrorValues(#"Previous Step", {{"Column1", 0}})

// Filter rows
= Table.SelectRows(#"Previous Step", each [Region] = "North")

// Group by
= Table.Group(#"Previous Step", {"Product"},
    {{"Total Sales", each List.Sum([Sales]), type number}})
```

---

## 3.4 Power Pivot & DAX

### Power Pivot Setup
```
Enable Power Pivot:
File > Options > Add-ins
Manage: COM Add-ins > Power Pivot

Load data to Data Model:
Power Query > Close & Load To > Only Create Connection + Add to Data Model
Or: Data > Get Data > [...] > Load To > Add to Data Model
```

### Data Model Relationships
```
Create Relationships:
Power Pivot > Manage > Diagram View
Drag foreign key to primary key

Relationship Types:
├─ One-to-Many (most common)
├─ One-to-One
└─ Many-to-Many (requires bridge table)

Cardinality & Filter Direction:
- Active relationship (solid line)
- Inactive relationship (dotted line)
- Filter direction: Single / Both
```

### DAX Calculated Columns
```dax
// Calculated column (evaluated row-by-row)
Profit = Sales[Revenue] - Sales[Cost]

// Related table lookup
Product Name = RELATED(Products[ProductName])

// Conditional
Category = IF(Sales[Amount] > 1000, "High", "Low")

// Text operations
Full Name = Sales[FirstName] & " " & Sales[LastName]

// Date operations
Year = YEAR(Sales[Date])
Quarter = "Q" & FORMAT(Sales[Date], "Q")
```

### DAX Measures (Aggregations)
```dax
// Basic aggregation
Total Sales = SUM(Sales[Amount])
Order Count = COUNT(Sales[OrderID])
Distinct Customers = DISTINCTCOUNT(Sales[CustomerID])

// CALCULATE - Change filter context
Sales North = CALCULATE([Total Sales], Region[Name] = "North")
Sales This Year = CALCULATE([Total Sales], YEAR(Sales[Date]) = 2024)

// Time intelligence (requires Date table)
Sales YTD = TOTALYTD([Total Sales], Calendar[Date])
Sales Last Year = CALCULATE([Total Sales], SAMEPERIODLASTYEAR(Calendar[Date]))
Sales Growth = [Total Sales] - [Sales Last Year]
Sales Growth % = DIVIDE([Sales Growth], [Sales Last Year])

// Moving averages
Sales 3M Avg = CALCULATE([Total Sales],
                         DATESINPERIOD(Calendar[Date],
                                      LASTDATE(Calendar[Date]),
                                      -3, MONTH))

// Ranking
Sales Rank = RANKX(ALL(Products[Name]), [Total Sales], , DESC)

// Percentage of total
% of Total = DIVIDE([Total Sales],
                    CALCULATE([Total Sales], ALL(Products)))
```

### DAX Table Functions
```dax
// FILTER
High Value Customers = CALCULATE([Total Sales],
                                 FILTER(Customers, [Total Sales] > 10000))

// ALL - Remove filters
Total for All Regions = CALCULATE([Total Sales], ALL(Region))

// VALUES - Get distinct values
Customer List = VALUES(Sales[CustomerID])

// SUMMARIZE - Create summary table
Summary = SUMMARIZE(Sales,
                    Products[Category],
                    "Total", SUM(Sales[Amount]))
```

---

## 3.5 Data Visualization & Charts

### Chart Types & Use Cases
```
Column/Bar Charts:
✓ Compare categories
✓ Show rankings
✓ Time series (few periods)

Line Charts:
✓ Trends over time
✓ Multiple series comparison
✓ Continuous data

Pie/Donut Charts:
✓ Parts of whole (< 7 categories)
✓ Percentage breakdown
⚠️ Avoid for precise comparison

Scatter Plots:
✓ Correlation between variables
✓ Identify outliers
✓ Regression analysis

Combo Charts:
✓ Different scales (column + line)
✓ Revenue + profit margin
✓ Actuals vs targets

Waterfall Charts:
✓ Sequential changes
✓ Profit/loss breakdown
✓ Budget variance

Treemap:
✓ Hierarchical data
✓ Market share visualization
✓ Budget allocation

Sunburst:
✓ Hierarchical proportions
✓ Multi-level categories
```

### Chart Design Best Practices
```
Do:
✅ Start Y-axis at zero (for bar/column)
✅ Use clear, descriptive titles
✅ Label axes with units
✅ Use consistent colors
✅ Limit to 5-7 data series
✅ Remove chartjunk (gridlines, borders)
✅ Use data labels when precise values matter

Don't:
❌ Use 3D charts (distortion)
❌ Use too many colors
❌ Use red/green only (colorblind)
❌ Truncate Y-axis to exaggerate differences
❌ Use dual axes incorrectly
```

### Conditional Formatting
```
Data Bars:
✓ Quick visual comparison
✓ Show relative magnitude
✓ Can show negative values

Color Scales:
✓ Heatmap effect
✓ 2-color or 3-color
✓ Identify high/low values

Icon Sets:
✓ Traffic lights (3-5 icons)
✓ Arrows, ratings, indicators
✓ Custom thresholds

Rules:
✓ Highlight cells > value
✓ Top 10 items
✓ Above/below average
✓ Duplicate values
✓ Formula-based (custom logic)
```

### Sparklines
```
Mini charts in cells:
Insert > Sparklines

Types:
- Line (trends)
- Column (variations)
- Win/Loss (positive/negative)

Customization:
- High/Low points
- First/Last points
- Negative points
- Markers
- Axis settings
```

---

# Part 4: VBA Macros & Automation

## 4.1 VBA Basics

### Enable Developer Tab
```
File > Options > Customize Ribbon
Check "Developer" in right pane
```

### Record Macro
```
Developer > Record Macro
Name: MyMacro (no spaces)
Shortcut: Ctrl+Shift+M (optional)
Store in: This Workbook / Personal Macro Workbook
Description: What it does

Perform actions...

Developer > Stop Recording
```

### View/Edit Macro Code
```
Developer > Visual Basic (or Alt+F11)

Project Explorer (left):
├─ VBAProject (ThisWorkbook)
    ├─ Microsoft Excel Objects
    │   ├─ Sheet1, Sheet2, etc.
    │   └─ ThisWorkbook
    └─ Modules
        └─ Module1 (your recorded macros)
```

### Basic VBA Structure
```vb
Sub MacroName()
    ' Comment line

    ' Select cell
    Range("A1").Select

    ' Set value
    Range("A1").Value = "Hello"

    ' Format
    Range("A1").Font.Bold = True
    Range("A1").Font.Color = RGB(255, 0, 0)

    ' Formula
    Range("B1").Formula = "=SUM(A:A)"

    ' Message box
    MsgBox "Done!"
End Sub
```

---

## 4.2 VBA Programming Essentials

### Variables & Data Types
```vb
' Declare variables
Dim customerName As String
Dim salesAmount As Double
Dim orderCount As Integer
Dim orderDate As Date
Dim isActive As Boolean

' Arrays
Dim regions(1 To 5) As String
Dim sales(1 To 10, 1 To 3) As Double  ' 10 rows, 3 columns

' Dynamic arrays
Dim data() As Variant
ReDim data(1 To 100)
```

### Control Structures
```vb
' If-Then-Else
If salesAmount > 1000 Then
    discount = 0.1
ElseIf salesAmount > 500 Then
    discount = 0.05
Else
    discount = 0
End If

' Select Case
Select Case region
    Case "North", "South"
        taxRate = 0.08
    Case "East"
        taxRate = 0.09
    Case "West"
        taxRate = 0.07
    Case Else
        taxRate = 0.1
End Select

' For Loop
For i = 1 To 10
    Cells(i, 1).Value = i * 2
Next i

' For Each Loop
For Each cell In Range("A1:A10")
    cell.Value = cell.Value * 1.1  ' Increase by 10%
Next cell

' Do While Loop
Do While ActiveCell.Value <> ""
    ActiveCell.Offset(1, 0).Select
Loop

' Do Until Loop
Do Until ActiveCell.Row = 100
    ActiveCell.Value = "Processed"
    ActiveCell.Offset(1, 0).Select
Loop
```

### Working with Ranges
```vb
' Reference cells
Range("A1").Value = 100
Cells(1, 1).Value = 100  ' Same as A1
Range("A1:C10").Value = "Bulk"

' Last row/column
lastRow = Cells(Rows.Count, 1).End(xlUp).Row
lastCol = Cells(1, Columns.Count).End(xlToLeft).Column

' Current region (contiguous data)
Set dataRange = Range("A1").CurrentRegion

' Find
Set foundCell = Range("A:A").Find("Apple")
If Not foundCell Is Nothing Then
    MsgBox "Found at " & foundCell.Address
End If

' Copy/Paste
Range("A1:C10").Copy Destination:=Range("E1")

' Delete
Range("A1:A10").Delete Shift:=xlUp
```

---

## 4.3 Practical VBA Examples

### Example 1: Format Report
```vb
Sub FormatReport()
    ' Format header row
    With Range("A1:E1")
        .Font.Bold = True
        .Font.Size = 12
        .Interior.Color = RGB(0, 112, 192)
        .Font.Color = RGB(255, 255, 255)
        .HorizontalAlignment = xlCenter
    End With

    ' Auto-fit columns
    Columns("A:E").AutoFit

    ' Add borders
    Range("A1").CurrentRegion.Borders.LineStyle = xlContinuous

    ' Number format
    Range("C:C").NumberFormat = "$#,##0.00"
    Range("D:D").NumberFormat = "0.0%"

    MsgBox "Report formatted!", vbInformation
End Sub
```

### Example 2: Remove Duplicates
```vb
Sub RemoveDuplicates()
    Dim lastRow As Long
    Dim dataRange As Range

    ' Find last row
    lastRow = Cells(Rows.Count, 1).End(xlUp).Row

    ' Define data range
    Set dataRange = Range("A1:C" & lastRow)

    ' Remove duplicates based on column 1
    dataRange.RemoveDuplicates Columns:=1, Header:=xlYes

    MsgBox "Duplicates removed!", vbInformation
End Sub
```

### Example 3: Split Data by Category
```vb
Sub SplitByCategory()
    Dim ws As Worksheet
    Dim lastRow As Long, i As Long
    Dim category As String
    Dim categorySheet As Worksheet

    Set ws = ThisWorkbook.Sheets("Data")
    lastRow = ws.Cells(Rows.Count, 1).End(xlUp).Row

    ' Loop through data
    For i = 2 To lastRow  ' Start at 2 (skip header)
        category = ws.Cells(i, 2).Value  ' Category in column B

        ' Check if sheet exists, create if not
        On Error Resume Next
        Set categorySheet = ThisWorkbook.Sheets(category)
        On Error GoTo 0

        If categorySheet Is Nothing Then
            Set categorySheet = ThisWorkbook.Sheets.Add(After:=Sheets(Sheets.Count))
            categorySheet.Name = category
            ' Copy header
            ws.Rows(1).Copy categorySheet.Rows(1)
        End If

        ' Copy row to category sheet
        ws.Rows(i).Copy categorySheet.Cells(categorySheet.Cells(Rows.Count, 1).End(xlUp).Row + 1, 1)

        Set categorySheet = Nothing
    Next i

    MsgBox "Data split by category!", vbInformation
End Sub
```

### Example 4: Send Email from Excel
```vb
Sub SendEmail()
    Dim OutlookApp As Object
    Dim OutlookMail As Object

    ' Create Outlook object
    Set OutlookApp = CreateObject("Outlook.Application")
    Set OutlookMail = OutlookApp.CreateItem(0)

    ' Compose email
    With OutlookMail
        .To = "recipient@example.com"
        .CC = "cc@example.com"
        .Subject = "Monthly Report"
        .Body = "Please find the attached report."
        .Attachments.Add ThisWorkbook.FullName
        .Display  ' Or .Send to send directly
    End With

    Set OutlookMail = Nothing
    Set OutlookApp = Nothing
End Sub
```

---

## 4.4 UserForms

### Create UserForm
```
Developer > Insert > UserForm

Toolbox controls:
├─ Label (display text)
├─ TextBox (user input)
├─ ComboBox (dropdown)
├─ ListBox (multiple selection)
├─ CommandButton (action button)
├─ CheckBox (yes/no)
├─ OptionButton (radio button)
├─ Frame (group controls)
└─ SpinButton, ScrollBar, etc.
```

### UserForm Code Example
```vb
' UserForm1 code
Private Sub UserForm_Initialize()
    ' Run when form opens
    ComboBox1.List = Array("North", "South", "East", "West")
    ComboBox1.Value = "North"  ' Default
End Sub

Private Sub CommandButton1_Click()
    ' Submit button clicked
    Dim ws As Worksheet
    Set ws = ThisWorkbook.Sheets("Data")

    ' Get last row
    Dim lastRow As Long
    lastRow = ws.Cells(Rows.Count, 1).End(xlUp).Row + 1

    ' Write data
    ws.Cells(lastRow, 1).Value = TextBox1.Value  ' Name
    ws.Cells(lastRow, 2).Value = ComboBox1.Value  ' Region
    ws.Cells(lastRow, 3).Value = TextBox2.Value  ' Amount
    ws.Cells(lastRow, 4).Value = Date  ' Today

    ' Clear form
    TextBox1.Value = ""
    TextBox2.Value = ""

    MsgBox "Record added!", vbInformation
End Sub

Private Sub CommandButton2_Click()
    ' Cancel button
    Unload Me
End Sub
```

### Show UserForm
```vb
Sub ShowDataEntry()
    UserForm1.Show
End Sub
```

---

## 4.5 Error Handling & Best Practices

### Error Handling
```vb
Sub SafeMacro()
    On Error GoTo ErrorHandler

    ' Your code here
    Dim result As Double
    result = 100 / 0  ' This will error

    Exit Sub  ' Exit before error handler

ErrorHandler:
    MsgBox "Error " & Err.Number & ": " & Err.Description, vbCritical
    ' Optional: Log error, clean up, etc.
End Sub
```

### Best Practices
```vb
Sub BestPracticesMacro()
    ' 1. Turn off screen updating (faster)
    Application.ScreenUpdating = False

    ' 2. Turn off automatic calculation (faster for large workbooks)
    Application.Calculation = xlCalculationManual

    ' 3. Disable events (prevent infinite loops)
    Application.EnableEvents = False

    ' Your code here
    Dim ws As Worksheet
    Set ws = ThisWorkbook.Sheets("Data")

    Dim lastRow As Long
    lastRow = ws.Cells(Rows.Count, 1).End(xlUp).Row

    ' ... process data ...

Cleanup:
    ' 4. Always restore settings
    Application.ScreenUpdating = True
    Application.Calculation = xlCalculationAutomatic
    Application.EnableEvents = True
End Sub
```

### Code Organization
```vb
' Module1: Utility functions
Function GetLastRow(ws As Worksheet, col As Integer) As Long
    GetLastRow = ws.Cells(ws.Rows.Count, col).End(xlUp).Row
End Function

Function IsWorksheetExists(sheetName As String) As Boolean
    On Error Resume Next
    IsWorksheetExists = Not (ThisWorkbook.Sheets(sheetName) Is Nothing)
    On Error GoTo 0
End Function

' Use in main code:
Sub ProcessData()
    Dim lastRow As Long
    lastRow = GetLastRow(ThisWorkbook.Sheets("Data"), 1)

    If IsWorksheetExists("Summary") Then
        ' Process
    End If
End Sub
```

---

# Part 5: Advanced Techniques & Productivity

## 5.1 Data Validation

### Basic Validation
```
Data > Data Validation

Settings:
├─ Whole number (min, max)
├─ Decimal
├─ List (source: range or comma-separated)
├─ Date
├─ Time
├─ Text length
└─ Custom (formula)

Input Message:
Show message when cell selected

Error Alert:
Style: Stop / Warning / Information
```

### Custom Validation Formulas
```excel
// No duplicates in column
=COUNTIF($A$1:$A$1000, A1) = 1

// Date must be future
=A1 > TODAY()

// Email format
=AND(FIND("@", A1) > 0, FIND(".", A1) > FIND("@", A1))

// Sum of row must equal 100
=SUM($B1:$F1) = 100

// Dependent dropdown (indirect)
=INDIRECT($B$1)  // Where B1 contains name of named range
```

---

## 5.2 What-If Analysis

### Goal Seek
```
Data > What-If Analysis > Goal Seek

Set cell: B10 (result cell)
To value: 1000
By changing cell: B2 (input cell)

Use Case: Find required sales to reach profit target
```

### Data Tables
```
One-Variable Data Table:
Row input or Column input

Two-Variable Data Table:
Row input AND Column input

Example: Loan payment table
Rows: Different interest rates
Columns: Different loan amounts
```

### Scenario Manager
```
Data > What-If Analysis > Scenario Manager

Create scenarios:
- Best Case (optimistic inputs)
- Worst Case (pessimistic inputs)
- Most Likely (realistic inputs)

Generate Scenario Summary Report
```

### Solver
```
Data > Solver (if not visible, enable in Add-ins)

Set Objective: Cell to maximize/minimize
To: Max / Min / Value
By Changing Variable Cells: Input cells
Subject to Constraints: Limits/rules

Use Cases:
- Production optimization
- Resource allocation
- Portfolio optimization
- Scheduling
```

---

## 5.3 Advanced Tips & Tricks

### Flash Fill (Excel 2013+)
```
Data > Flash Fill (Ctrl+E)

Examples:
Column A        Column B (type example, then Ctrl+E)
---------       ---------
John Smith  →   John
Jane Doe    →   Jane
            ... (auto-fills)

john@email.com  →  john
jane@email.com  →  jane
```

### Custom Number Formats
```
Format Cells > Custom

Format structure: [Color][Condition]format

Examples:
#,##0                    // Thousands separator
#,##0.00                 // 2 decimals
$#,##0.00                // Currency
0.00%                    // Percentage
[Red]#,##0;[Blue]#,##0   // Positive red, negative blue
#,##0;" "                // Hide zeros
[<100]"Low";[>1000]"High";"Medium"  // Conditional

Date/Time:
dd/mm/yyyy
dddd, mmmm d, yyyy
[$-th-TH]d mmmm yyyy     // Thai locale
```

### Name Manager
```
Formulas > Name Manager

Create Named Ranges:
1. Select range
2. Name Box (left of formula bar)
3. Type name, press Enter

Or: Formulas > Define Name

Use in formulas:
=SUM(MonthlySales)
=VLOOKUP(A2, ProductList, 3, FALSE)

Dynamic named ranges:
=OFFSET(Sheet1!$A$1, 0, 0, COUNTA(Sheet1!$A:$A), 1)
```

### Consolidate Data
```
Data > Consolidate

Function: Sum, Count, Average, etc.
Reference: Multiple ranges from multiple sheets
Use labels in: Top row / Left column
Create links to source data (optional)

Use Case: Combine data from multiple regional reports
```

---

## 5.4 Excel Add-ins & Extensions

### Useful Add-ins
```
Analysis ToolPak:
├─ Descriptive Statistics
├─ Regression
├─ Correlation
├─ Histogram
├─ Moving Average
└─ Random Number Generation

Solver:
├─ Linear programming
├─ Non-linear optimization
└─ Constraint satisfaction

Power Pivot:
├─ Data modeling
├─ DAX formulas
└─ Millions of rows

Power Query:
├─ Data transformation
├─ ETL workflows
└─ M language

Enable:
File > Options > Add-ins > Manage Excel Add-ins > Go
```

---

## 5.5 Excel Best Practices

### Workbook Structure
```
Good Structure:
├─ Raw Data (separate sheet, don't modify)
├─ Calculations (formulas referencing raw data)
├─ Summary (pivot tables, charts)
└─ Dashboard (final presentation)

Best Practices:
✅ One table per sheet
✅ No merged cells in data
✅ Headers in row 1
✅ No blank rows/columns in data
✅ Consistent data types per column
✅ Use Tables for data ranges
✅ Document assumptions
```

### Formula Best Practices
```
Do:
✅ Use named ranges
✅ Break complex formulas into steps
✅ Use helper columns
✅ Comment complex logic
✅ Use structured references (Tables)
✅ Avoid volatile functions (NOW, TODAY, RAND in large sheets)

Don't:
❌ Hard-code values in formulas
❌ Use A1 when you mean $A$1
❌ Create circular references
❌ Nest too many functions (> 5 levels)
❌ Use entire column references in large files (A:A)
```

### Performance Optimization
```
Speed up slow workbooks:

1. Calculation:
   - Manual calculation for data entry
   - Use VALUES/COLUMNS instead of OFFSET
   - Replace SUMPRODUCT with SUMIFS when possible

2. Formulas:
   - Minimize volatile functions
   - Use INDEX-MATCH instead of VLOOKUP
   - Avoid array formulas in older Excel

3. Formatting:
   - Limit conditional formatting rules
   - Avoid excessive formatting
   - Use Table styles instead of manual

4. File Size:
   - Delete unused sheets
   - Clear unused cells (Ctrl+End should be last used cell)
   - Remove duplicate data in hidden sheets
   - Compress images (Picture Format > Compress)

5. VBA:
   - Turn off ScreenUpdating
   - Set Calculation to Manual
   - Use With statements
   - Avoid Select/Activate
```

---

## 5.6 Excel Shortcuts Master List

### Essential Shortcuts
```
File Operations:
Ctrl + N            New workbook
Ctrl + O            Open
Ctrl + S            Save
Ctrl + W            Close workbook
Ctrl + P            Print
F12                 Save As

Editing:
Ctrl + C            Copy
Ctrl + X            Cut
Ctrl + V            Paste
Ctrl + Z            Undo
Ctrl + Y            Redo
Delete              Clear contents
Ctrl + D            Fill down
Ctrl + R            Fill right

Navigation:
Ctrl + Home         Go to A1
Ctrl + End          Go to last cell
Ctrl + Arrow        Jump to edge
Page Up/Down        Scroll screen
Alt + Page Up/Down  Scroll left/right

Selection:
Shift + Arrow       Extend selection
Ctrl + Shift + Arrow  Select to edge
Ctrl + Space        Select column
Shift + Space       Select row
Ctrl + A            Select all

Formatting:
Ctrl + B            Bold
Ctrl + I            Italic
Ctrl + U            Underline
Ctrl + 1            Format Cells
Alt + H + H         Fill color
Alt + H + B         Borders

Formulas:
=                   Start formula
Alt + =             AutoSum
F4                  Toggle $ in cell reference
Ctrl + `            Show formulas
F9                  Calculate now

Data:
Ctrl + T            Create Table
Alt + A + T         Filter toggle
Alt + D + S         Sort
Alt + D + F + F     Advanced Filter

Worksheets:
Shift + F11         New sheet
Ctrl + Page Up/Down Switch sheet
Alt + H + O + R     Rename sheet

Other:
F2                  Edit cell
F4                  Repeat last action
Alt + Enter         New line in cell
Ctrl + ;            Insert date
Ctrl + Shift + ;    Insert time
```

---

## Summary & Quick Reference

### When to Use What

**Lookup Functions:**
- Small data, simple: `VLOOKUP`
- Flexible, faster: `INDEX-MATCH`
- Modern Excel: `XLOOKUP`

**Aggregation:**
- Single criterion: `SUMIF`, `COUNTIF`, `AVERAGEIF`
- Multiple criteria: `SUMIFS`, `COUNTIFS`, `AVERAGEIFS`
- Complex logic: `SUMPRODUCT`

**Data Analysis:**
- Quick summary: **Pivot Tables**
- Data transformation: **Power Query**
- Advanced modeling: **Power Pivot + DAX**
- Statistical: **Analysis ToolPak**

**Automation:**
- Simple repetitive tasks: **Record Macro**
- Complex logic: **VBA**
- No-code automation: **Power Automate**

**Visualization:**
- Trends: **Line charts**
- Comparison: **Column/Bar charts**
- Parts of whole: **Pie charts** (< 7 categories)
- Correlation: **Scatter plots**
- In-cell: **Sparklines, Conditional Formatting**

---

## ภาษาไทย: Excel Tips สำหรับคนไทย

### ฟังก์ชันที่ใช้บ่อย
```excel
// รวมยอดตามเงื่อนไข
=SUMIF(A:A, "กรุงเทพ", C:C)

// นับตามเงื่อนไข
=COUNTIF(B:B, ">1000")

// ค้นหาข้อมูล
=VLOOKUP(A2, ตารางสินค้า, 3, FALSE)
=XLOOKUP(A2, รหัส, ราคา, "ไม่พบ")

// วันที่ภาษาไทย
=TEXT(A2, "[$-th-TH]d mmmm yyyy")  // 15 มกราคม 2567
=TEXT(A2, "[$-th-TH]วันdddd")      // วันจันทร์
```

### Keyboard Shortcuts ที่ต้องรู้
```
Ctrl + ;    = ใส่วันที่วันนี้
Ctrl + D    = คัดลอกลงล่าง (Fill Down)
F4          = สลับ $ ในสูตร (ล็อคเซลล์)
Ctrl + T    = สร้างตาราง
Alt + =     = SUM อัตโนมัติ
```

### Tips การทำงาน
```
✅ ใช้ Table แทนช่วงข้อมูลธรรมดา → สูตรอ่านง่าย อัพเดทอัตโนมัติ
✅ ใช้ Pivot Table สรุปข้อมูล → ไม่ต้องเขียนสูตรซับซ้อน
✅ ใช้ Power Query ทำความสะอาดข้อมูล → ทำครั้งเดียว ใช้ซ้ำได้
✅ Record Macro สำหรับงานซ้ำๆ → ประหยัดเวลา
✅ ใช้ Named Range → สูตรอ่านง่าย =SUM(ยอดขาย) แทน =SUM(C:C)
```

---

**Total Lines:** ~2,400 lines
**Coverage:** Complete Excel mastery from basics to VBA automation
**Target:** Business analysts, financial analysts, data professionals

**Keywords optimized for:** Excel formulas, VLOOKUP, XLOOKUP, INDEX-MATCH, pivot tables, Power Query, Power Pivot, DAX, VBA macros, data visualization, dashboards, financial modeling, automation, array formulas, dynamic arrays, data analysis
