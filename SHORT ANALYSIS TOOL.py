#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 13:36:07 2024

@author: DAE-CYBER/GRC
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 12:34:38 2024

@author: DAE-CYBER/GRC
"""

import pandas as pd

# Define the data
data = [
    {"Date": "2024-08-16", "Short Volume": 7649560, "Total Volume": 18981916, "Short Volume Ratio": 40.75},
    {"Date": "2024-08-15", "Short Volume": 11462294, "Total Volume": 30876820, "Short Volume Ratio": 37.53},
    # Add more data points here
]

# Create a Pandas DataFrame from the data
df = pd.DataFrame(data)

# Calculate the short squeeze ratio
df["Short Squeeze Ratio"] = df["Short Volume"] / df["Total Volume"]

# Print the resulting DataFrame
print(df)