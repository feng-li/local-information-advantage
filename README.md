# Local Information Advantage and Stock Returns: Evidence from Social Media

This repository provides the code implementation for the paper


Yuqin Huang, Feng Li, Tong Li and Tse-Chun Lin (2024). “Local Information Advantage and Stock Returns: Evidence from Social Media”. Contemporary Accounting Research, Vol. 41(2), pp. 1089-1119. DOI: https://doi.org/10.1111/1911-3846.12935

## Disclaimer

This code is provided **AS IS**, with no further updates or maintenance. If you have any questions, please contact [Feng Li](https://feng.li/) via email `feng.li@gsm.pku.edu.cn`.

## Overview

We examine the information asymmetry between local and nonlocal investors with a large dataset of stock message board postings. We document that abnormal relative postings of a firm, i.e., unusual changes in the volume of postings from local versus nonlocal investors, capture locals’ information advantage. This measure positively predicts firms’ short-term stock returns as well as those of peer firms in the same city. Sentiment analysis shows that posting activities primarily reflect good news, potentially due to social transmission bias and short-sales constraints. We identify the information driving return predictability through content-based analysis. Abnormal relative postings also lead analysts’ forecast revisions. Overall, investors’ interactions on social media contain valuable geography-based private information.

This repository contains the code used to replicate the key results from the paper. 


## Features

- Code to estimate the local information advantage using various machine learning models and statistical techniques.
- Scripts to preprocess financial data, including stock price movements and geographic information.
- Visualization tools to interpret the findings and display the local information advantage across different regions.

## Requirements

Before running the code, you need to install the following Python libraries:

- `pandas`
- `numpy`
- `matplotlib`
- `scikit-learn`
- `statsmodels`

You can install these dependencies using `pip`:

```bash
pip install pandas numpy matplotlib scikit-learn statsmodels
```

## Code Structure

- **data/**: Contains the raw data files used for analysis.
- **scripts/**: Holds the Python scripts for data preprocessing, model training, and evaluation.
- **notebooks/**: Jupyter notebooks that explain the analysis step by step.
- **results/**: Generated outputs and plots from the analysis.

## How to Use

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/feng-li/local-information-advantage.git
   cd local-information-advantage
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the analysis script to replicate the main results:

   ```bash
   python scripts/main_analysis.py
   ```

## License

This code is made available under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Citation

If you use this code in your own research, please cite the following paper:

```
@article{HuangY2024LocalInformation,
	title = {Local {Information} {Advantage} and {Stock} {Returns}: {Evidence} from {Social} {Media}},
	volume = {41},
	shorttitle = {Local {Information} {Advantage} and {Stock} {Returns}},
	url = {http://doi.org/10.2139/ssrn.2501937},
	doi = {10.1111/1911-3846.12935},
	language = {en},
	number = {2},
	urldate = {2023-11-30},
	journal = {Contemporary Accounting Research},
	author = {Huang, Yuqin and Li, Feng and Li, Tong and Lin, Tse-Chun},
	month = jul,
	year = {2024},
	note = {(alphabetical order, FT50)},
	keywords = {Local Information Advantage, Return Predictability, Sentiment Analysis, Social Media, Topical Analysis},
	pages = {1089--1119},
}

```
