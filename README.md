# QSAR-Based pIC50 Prediction Dashboard

**Computational Biology Final Project**

A machine learning-powered web application for predicting compound potency (pIC50) from molecular structures using Quantitative Structure-Activity Relationship (QSAR) modeling. This project demonstrates how computational tools can accelerate early-stage drug discovery by predicting biological activity without expensive laboratory experiments.

## 👥 Team Members

- Albertus Santoso
- Gabriel Anderson
- Rafael Anderson

## 📋 Table of Contents

- [Overview](#overview)
- [Why This Project Matters](#why-this-project-matters)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Data](#data)
- [Machine Learning Models](#machine-learning-models)
- [Project Workflow](#project-workflow)
- [Results](#results)
- [License](#license)

## 🎯 Overview

This project focuses on predicting **pIC50**, a logarithmic measure of compound potency derived from IC50 values. Using a combination of molecular descriptors, SMILES-based features, and machine learning models, we build a QSAR system capable of estimating biological activity for acetylcholinesterase inhibitors from the ChEMBL2599 dataset.

**pIC50 = -log₁₀(IC50 in M)**

## 💡 Why This Project Matters

Modern drug discovery faces a fundamental challenge: **how do we identify promising compounds quickly, accurately, and at scale?** Traditional wet-lab experiments, while essential, are slow, costly, and resource-intensive. As chemical libraries grow into the millions, computational tools become indispensable.

This dashboard demonstrates how **machine learning and cheminformatics** can accelerate early-stage drug discovery by predicting compound potency directly from molecular structure.

### Problem Statement

- Experimental IC50 measurements are expensive and slow
- IC50 values span several orders of magnitude and are non-linear
- Manual screening of thousands of compounds is impractical
- Early-stage filtering requires fast, scalable computational tools

### Real-World Applications

QSAR-based pIC50 prediction is widely used in:

- **Virtual screening** of large chemical libraries
- **Lead optimization** in medicinal chemistry
- **Toxicity and ADMET prediction**
- **Reducing experimental workload** in early drug discovery

## ✨ Features

- **Interactive Streamlit Dashboard**: User-friendly web interface for exploring the QSAR pipeline
- **Multiple ML Models**: Implementation of ANN, CatBoost, RandomForest, and XGBoost
- **Molecular Descriptor Generation**: Automated feature extraction from SMILES using RDKit
- **Data Visualization**: Comprehensive EDA and model evaluation visualizations
- **Feature Selection**: RFECV-based feature selection for optimal model performance
- **Model Comparison**: Side-by-side evaluation of different machine learning approaches

## 📁 Project Structure

```
Computational-Biology-FP/
│
├── data/                                    # Dataset files
│   ├── ChemBL2599_combined_data.csv.gz
│   ├── ChemBL2599_converted_smiles.csv.gz
│   └── compressed_data.csv.gz
│
├── EDA/                                     # Exploratory Data Analysis
│   └── EDA.ipynb
│
├── GUI/                                     # Streamlit dashboard application
│   ├── streamlit_app.py                    # Main Streamlit app entry point
│   ├── home_page.py                        # Home page with project overview
│   ├── data_preparation_page.py            # Data preprocessing documentation
│   ├── model_training_and_testing_page.py  # Model training pipeline
│   └── model_evaluation_page.py            # Model evaluation and metrics
│
├── machine_learning/                        # ML model implementations
│   ├── ChemBL2599_ANN.ipynb                # Artificial Neural Network
│   ├── ChemBL2599_CatBoost.ipynb           # CatBoost Regressor
│   ├── ChemBL2599_RandomForest.ipynb       # Random Forest Regressor
│   └── ChemBL2599_XGBoost.ipynb           # XGBoost Regressor
│
├── gui.py                                   # Alternative Tkinter GUI (optional)
└── README.md                                # This file
```

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd Computational-Biology-FP
```

### Step 2: Install Dependencies

```bash
pip install streamlit pandas numpy scikit-learn xgboost catboost rdkit-pypi matplotlib seaborn
```

**Note**: RDKit installation may require additional steps. For Windows, you can use:
```bash
pip install rdkit-pypi
```

For other platforms, refer to the [RDKit installation guide](https://www.rdkit.org/docs/Install.html).

### Step 3: Verify Installation

```bash
python -c "import streamlit; import rdkit; print('Installation successful!')"
```

## 💻 Usage

### Running the Streamlit Dashboard

1. Navigate to the project directory:
   ```bash
   cd Computational-Biology-FP
   ```

2. Run the Streamlit application:
   ```bash
   streamlit run GUI/streamlit_app.py
   ```

3. The dashboard will open in your default web browser at `http://localhost:8501`

### Dashboard Navigation

The dashboard consists of four main pages:

- **Home Page**: Overview of the project, its importance, and real-world applications
- **Data Preparation Page**: Step-by-step documentation of data preprocessing pipeline
- **Model Training and Testing Page**: Detailed explanation of model training process
- **Model Evaluation Page**: Performance metrics, visualizations, and model comparisons

### Running Individual ML Models

You can also run the Jupyter notebooks individually:

```bash
jupyter notebook machine_learning/ChemBL2599_XGBoost.ipynb
```

### Alternative Tkinter GUI

For a desktop application interface:

```bash
python gui.py
```

## 🛠️ Technologies Used

### Core Libraries
- **Streamlit**: Web application framework for the interactive dashboard
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **RDKit**: Cheminformatics toolkit for molecular descriptor generation

### Machine Learning
- **scikit-learn**: Machine learning utilities, feature selection, and model evaluation
- **XGBoost**: Gradient boosting framework
- **CatBoost**: Gradient boosting with categorical features support
- **TensorFlow/Keras**: Deep learning for ANN implementation

### Visualization
- **Matplotlib**: Plotting and visualization
- **Seaborn**: Statistical data visualization

### GUI Frameworks
- **Streamlit**: Primary web-based interface
- **Tkinter**: Alternative desktop GUI (optional)

## 📊 Data

### Dataset: ChEMBL2599

The project uses acetylcholinesterase inhibitor data from the ChEMBL database (ChEMBL ID: 2599). The dataset includes:

- **SMILES strings**: Molecular structure representations
- **IC50 values**: Half-maximal inhibitory concentration (in nM)
- **Molecular descriptors**: Pre-computed molecular properties (Molecular Weight, AlogP, etc.)
- **pIC50 values**: Target variable (calculated as -log₁₀(IC50 in M))

### Data Preprocessing Pipeline

1. **Data Loading**: Read compressed CSV files
2. **Missing Value Removal**: Drop rows with missing critical attributes
3. **Filtering**: Select IC50 standard type with nM units
4. **pIC50 Calculation**: Convert IC50 (nM) to pIC50 (M)
5. **Molecular Descriptor Generation**: Extract 200+ descriptors from SMILES using RDKit
6. **Feature Engineering**: Convert descriptor arrays into individual columns
7. **Data Cleaning**: Remove non-numerical and unused attributes

## 🤖 Machine Learning Models

The project implements and compares four different machine learning approaches:

### 1. Artificial Neural Network (ANN)
- Deep learning model for non-linear relationships
- Multi-layer perceptron architecture

### 2. CatBoost Regressor
- Gradient boosting with categorical feature support
- Robust to overfitting

### 3. Random Forest Regressor
- Ensemble of decision trees
- Feature importance analysis

### 4. XGBoost Regressor
- Optimized gradient boosting
- High performance on structured data

### Model Training Process

1. **Data Splitting**: 80% training, 20% testing
2. **Feature Selection**: RFECV (Recursive Feature Elimination with Cross-Validation)
   - Step size: 5 features per iteration
   - Cross-validation: 3-fold KFold
   - Minimum features: 20
   - Scoring metric: R²
3. **Hyperparameter Tuning**: Grid search or random search optimization
4. **Model Evaluation**: R² score, MAE, RMSE, and visualization metrics

## 🔄 Project Workflow

```
Raw Data (ChEMBL2599)
    ↓
Data Preprocessing
    ├── Missing value removal
    ├── IC50 filtering
    ├── pIC50 calculation
    └── SMILES to descriptors conversion
    ↓
Feature Engineering
    ├── RDKit descriptor extraction
    ├── Feature expansion
    └── Non-numerical attribute removal
    ↓
Model Training
    ├── Train/test split (80/20)
    ├── Feature selection (RFECV)
    ├── Hyperparameter tuning
    └── Model training
    ↓
Model Evaluation
    ├── Performance metrics (R², MAE, RMSE)
    ├── Visualization (scatter plots, residuals)
    └── Model comparison
```

## 📈 Results

Model performance metrics are displayed in the **Model Evaluation Page** of the dashboard. The evaluation includes:

- **R² Score**: Coefficient of determination (train and test)
- **MAE**: Mean Absolute Error
- **RMSE**: Root Mean Squared Error
- **Visualizations**: 
  - Predicted vs. Actual scatter plots
  - Residual plots
  - Model comparison charts

## 📝 Notes

- The dataset files are compressed (`.gz` format) to save space
- All molecular descriptors are generated using RDKit's `MolecularDescriptorCalculator`
- The project uses a comprehensive set of 200+ molecular descriptors
- Feature selection is performed to optimize model performance and reduce overfitting

## 🤝 Contributing

This is a final project for a Computational Biology course. For questions or suggestions, please contact the team members.

## 📄 License

This project is created for educational purposes as part of a Computational Biology course final project.

## 🙏 Acknowledgments

- **ChEMBL Database**: For providing the acetylcholinesterase inhibitor dataset
- **RDKit Community**: For the cheminformatics toolkit
- **Streamlit Team**: For the excellent web application framework

---

**Note**: This project is for educational and research purposes. The models and predictions should not be used for actual drug discovery decisions without proper validation and expert consultation.
