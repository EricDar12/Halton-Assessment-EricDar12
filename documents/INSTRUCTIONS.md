# Setup Instructions

Use the steps below to set up the project locally.

---

## 1) Install components

- Install Python 3.10+ (includes `pip` in most installs)
- Install VS Code (optional)

---

## 2) Install project requirements

- Create a virtual environment in the project folder
- Install the project requirements from `requirements.txt`

---

## 3) Download and import the dataset

- Download the “Contracts over $10,000” dataset  
- Dataset page: [https://open.canada.ca/data/en/dataset/d8f85d91-7dec-4fd1-8055-483b77225d8b/resource/fac950c0-00d5-4ec1-a4d3-9cbebf98a305](https://open.canada.ca/data/en/dataset/d8f85d91-7dec-4fd1-8055-483b77225d8b/resource/fac950c0-00d5-4ec1-a4d3-9cbebf98a305)
- Save the file to: `data/contracts.csv`

---

## 4) Configure environment variables

- Copy `.env.example` to `.env`
- Ensure `LOCAL_DATASET_PATH` points to your local data file

---

## 5) Test connection

- Open `notebooks/research.ipynb`
- Run all cells to confirm the dataset loads successfully

---

## 6) Complete the assignment

- Follow the instructions in the [Take-Home Assignment](TAKE-HOME.md)