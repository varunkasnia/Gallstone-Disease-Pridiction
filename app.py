import streamlit as st
import pandas as pd
import joblib

st.title("GalStone Project")

st.header("Patient Basic Details")
age = st.number_input("Age", min_value=0, max_value=120, value=30)
height = st.number_input("Height (cm)", min_value=50, max_value=250, value=170)
weight = st.number_input("Weight (kg)", min_value=1.0, max_value=250.0, value=65.0)

st.header("Body Composition Metrics")
bmi = st.number_input("Body Mass Index (BMI)", min_value=0.0, max_value=100.0, value=22.0)
tbw = st.number_input("Total Body Water (TBW)", min_value=0.0, max_value=100.0, value=40.0)
ecw = st.number_input("Extracellular Water (ECW)", min_value=0.0, max_value=100.0, value=20.0)
icw = st.number_input("Intracellular Water (ICW)", min_value=0.0, max_value=100.0, value=20.0)
ecf_tbw = st.number_input("Extracellular Fluid/Total Body Water (ECF/TBW)", min_value=0.0, max_value=100.0, value=50.0)
tbfr = st.number_input("Total Body Fat Ratio (TBFR) (%)", min_value=0.0, max_value=100.0, value=20.0)
lm = st.number_input("Lean Mass (LM) (%)", min_value=0.0, max_value=100.0, value=80.0)
protein = st.number_input("Body Protein Content (Protein) (%)", min_value=0.0, max_value=100.0, value=20.0)
vfr = st.number_input("Visceral Fat Rating (VFR)", min_value=0, max_value=100, value=10)
bm = st.number_input("Bone Mass (BM)", min_value=0.0, max_value=10.0, value=2.5)
mm = st.number_input("Muscle Mass (MM)", min_value=0.0, max_value=200.0, value=50.0)
obesity = st.number_input("Obesity (%)", min_value=0.0, max_value=5000.0, value=20.0)
tfc = st.number_input("Total Fat Content (TFC)", min_value=0.0, max_value=100.0, value=20.0)
vfa = st.number_input("Visceral Fat Area (VFA)", min_value=0.0, max_value=200.0, value=10.0)
vma = st.number_input("Visceral Muscle Area (VMA) (Kg)", min_value=0.0, max_value=200.0, value=20.0)

st.header("Biochemical Parameters")
glucose = st.number_input("Glucose", min_value=0.0, max_value=1000.0, value=90.0)
tc = st.number_input("Total Cholesterol (TC)", min_value=0.0, max_value=1000.0, value=180.0)
ldl = st.number_input("Low Density Lipoprotein (LDL)", min_value=0.0, max_value=1000.0, value=100.0)
hdl = st.number_input("High Density Lipoprotein (HDL)", min_value=0.0, max_value=1000.0, value=50.0)
triglyceride = st.number_input("Triglyceride", min_value=0.0, max_value=1000.0, value=150.0)
ast = st.number_input("Aspartat Aminotransferaz (AST)", min_value=0.0, max_value=1000.0, value=20.0)
alt = st.number_input("Alanin Aminotransferaz (ALT)", min_value=0.0, max_value=1000.0, value=20.0)
alp = st.number_input("Alkaline Phosphatase (ALP)", min_value=0.0, max_value=1000.0, value=100.0)
creatinine = st.number_input("Creatinine", min_value=0.0, max_value=10.0, value=1.0)
gfr = st.number_input("Glomerular Filtration Rate (GFR)", min_value=0.0, max_value=500.0, value=90.0)
crp = st.number_input("C-Reactive Protein (CRP)", min_value=0.0, max_value=500.0, value=0.0)
hgb = st.number_input("Hemoglobin (HGB)", min_value=0.0, max_value=25.0, value=14.0)
vit_d = st.number_input("Vitamin D", min_value=0.0, max_value=200.0, value=30.0)

st.header("Categorical Inputs")
gender = st.selectbox("Gender (0=Male, 1=Female)", options=[0, 1])
comorbidity = st.selectbox("Comorbidity (0=None, 1=Single, 2=Double, 3=Triple)", options=[0, 1, 2, 3])
cad = st.selectbox("Coronary Artery Disease (CAD)", options=[0, 1])
hypothyroidism = st.selectbox("Hypothyroidism", options=[0, 1])
hyperlipidemia = st.selectbox("Hyperlipidemia", options=[0, 1])
dm = st.selectbox("Diabetes Mellitus (DM)", options=[0, 1])
hfa = st.selectbox("Hepatic Fat Accumulation (HFA)", options=[0, 1, 2, 3, 4])

pipeline = joblib.load('pipeline.pkl')

if st.button("Submit"):
    
    user_data = {
    "Age": age,
    "Gender": gender,
    "Comorbidity": comorbidity,
    "Coronary Artery Disease (CAD)": cad,
    "Hypothyroidism": hypothyroidism,
    "Hyperlipidemia": hyperlipidemia,
    "Diabetes Mellitus (DM)": dm,
    "Height": height,
    "Weight": weight,
    "Body Mass Index (BMI)": bmi,
    "Total Body Water (TBW)": tbw,
    "Extracellular Water (ECW)": ecw,
    "Intracellular Water (ICW)": icw,
    "Extracellular Fluid/Total Body Water (ECF/TBW)": ecf_tbw,
    "Total Body Fat Ratio (TBFR) (%)": tbfr,
    "Lean Mass (LM) (%)": lm,
    "Body Protein Content (Protein) (%)": protein,
    "Visceral Fat Rating (VFR)": vfr,
    "Bone Mass (BM)": bm,
    "Muscle Mass (MM)": mm,
    "Obesity (%)": obesity,
    "Total Fat Content (TFC)": tfc,
    "Visceral Fat Area (VFA)": vfa,
    "Visceral Muscle Area (VMA) (Kg)": vma,
    "Hepatic Fat Accumulation (HFA)": hfa,
    "Glucose": glucose,
    "Total Cholesterol (TC)": tc,
    "Low Density Lipoprotein (LDL)": ldl,
    "High Density Lipoprotein (HDL)": hdl,
    "Triglyceride": triglyceride,
    "Aspartat Aminotransferaz (AST)": ast,
    "Alanin Aminotransferaz (ALT)": alt,
    "Alkaline Phosphatase (ALP)": alp,
    "Creatinine": creatinine,
    "Glomerular Filtration Rate (GFR)": gfr,
    "C-Reactive Protein (CRP)": crp,
    "Hemoglobin (HGB)": hgb,
    "Vitamin D": vit_d
    }

    data=pd.DataFrame([user_data])
    pred=pipeline.predict(data)[0]
    
    if pred==1:
        st.success(f'Positive {pred}')
    else:
        st.success(f'Negative {pred}')

    st.success("Done")


