#!/usr/bin/env python3.10
import pandas as pd

# Create a sample series of 10 timestamps (10-second intervals)
# Adjust the start time and frequency as needed
timestamps = pd.date_range(start='2025-02-20 00:00:00', periods=10, freq='10S')

# Create a pandas Series named 'start' to hold these timestamps
invocation_series = pd.Series(timestamps, name='start')

# Save the series to a pickle file.
# According to your InvocationRate class, it looks for files starting with "invocationRates"
# We'll use the name "invocationRates,1.pkl"
invocation_series.to_pickle('invocationRates,1.pkl')

print("Sample invocation rates file for DNAVisualizationWorkflow created as 'invocationRates,1.pkl'")
