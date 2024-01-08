### Diamonds Dataset Report

**Overview:**
The dataset comprises information about diamonds, including various attributes such as carat, cut, color, clarity, dimensions, price, and volume.

**Dataset Size:**
The dataset contains **53,920 entries** and **8 columns** after data cleaning and manipulation.

**Data Types:**
- **Numeric Attributes:**
  - Carat: Continuous (float)
  - Depth: Continuous (float)
  - Table: Continuous (float)
  - Price: Continuous (integer)
  - Volume: Continuous (float)

- **Categorical Attributes:**
  - Cut: Qualitative (object)
  - Color: Qualitative (object)
  - Clarity: Qualitative (object)

**Main Statistical Characteristics (Numeric Attributes):**
- Carat: Mean = 0.7979, Min = 0.2, Max = 5.01
- Depth: Mean = 61.7494, Min = 43.0, Max = 79.0
- Table: Mean = 57.4572, Min = 43.0, Max = 95.0
- Price: Mean = $3932.80, Min = $326, Max = $18823

**Data Preparation:**
- Created a new 'volume' column using dimensions (length, width, and depth).
- Removed entries with zero volume, ensuring a clean dataset for analysis.
- Filtered diamonds with 'Ideal' cut quality and a value above $18,700.
- Dropped columns related to dimensions after volume calculation.

**Analysis:**
- Identified the most common diamond color as 'G' based on frequency.
- Explored how diamond prices change concerning color. Found that color 'J' had a higher average price despite being perceived as less valuable in the assignment.
- Investigated diamonds with prices higher than the median price.
- Determined that 'Fair' quality diamonds had the highest median price.
- Discovered that 'Premium' quality diamonds with prices above the median and a volume of more than 500 were most common.
- Calculated the average price of diamonds with 'Premium' or 'Ideal' quality.

**Insights:**
- The dataset suggests that price is influenced more by the quality and size of the diamond.
- 'Premium' quality diamonds tend to be more expensive and voluminous compared to other qualities.

**Conclusion:**
The dataset provides valuable insights into the pricing and attributes of diamonds. The analysis reveals patterns related to diamond qualities, colors, and their respective prices.
