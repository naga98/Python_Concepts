"""Entry point - runs the full Retail Store Management & Analytics pipeline."""

import analysis
import data_generator

if __name__ == "__main__":
    data_generator.main()
    print("\n" + "#" * 70)
    print("PART 4 & 5 - PANDAS ANALYSIS AND REPORTS")
    print("#" * 70)
    analysis.main()
