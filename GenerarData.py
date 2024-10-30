import pandas as pd
import numpy as np
import json

cantidad = 15

# Definir los rangos para cada campo
age_range = (18, 59)
gender_range = (0, 1)
years_at_company_range = (1, 51)
job_role_range = (0, 4)
monthly_income_range = (1226, 16149)
work_life_balance_range = (0, 3)
job_satisfaction_range = (0, 3)
performance_rating_range = (0, 3)
number_of_promotions_range = (0, 4)
overtime_range = (0, 1)
distance_from_home_range = (1, 99)
education_level_range = (0, 4)
marital_status_range = (0, 2)
number_of_dependents_range = (0, 6)
job_level_range = (0, 2)
company_size_range = (0, 2)
company_tenure_range = (2, 128)
remote_work_range = (0, 1)
leadership_opportunities_range = (0, 1)
innovation_opportunities_range = (0, 1)
company_reputation_range = (0, 3)
employee_recognition_range = (0, 3)

# Generar los datos aleatorios con validación de las reglas
data = []

while len(data) < cantidad:
    age = np.random.randint(age_range[0], age_range[1] + 1)
    years_at_company = np.random.randint(years_at_company_range[0], years_at_company_range[1] + 1)
    company_tenure = np.random.randint(company_tenure_range[0], company_tenure_range[1] + 1)
    
    # Validar que la diferencia entre Age y Years_at_Company, y Age y Company_Tenure no sea menor a 15 años
    if age - years_at_company >= 15 and age - company_tenure >= 15 and years_at_company - company_tenure >= 0:
        data.append({
            "Age": age,
            "Gender": np.random.randint(gender_range[0], gender_range[1] + 1),
            "Years_at_Company": company_tenure,
            "Job_Role": np.random.randint(job_role_range[0], job_role_range[1] + 1),
            "Monthly_Income": np.random.randint(monthly_income_range[0], monthly_income_range[1] + 1),
            "Work_Life_Balance": np.random.randint(work_life_balance_range[0], work_life_balance_range[1] + 1),
            "Job_Satisfaction": np.random.randint(job_satisfaction_range[0], job_satisfaction_range[1] + 1),
            "Performance_Rating": np.random.randint(performance_rating_range[0], performance_rating_range[1] + 1),
            "Number_of_Promotions": np.random.randint(number_of_promotions_range[0], number_of_promotions_range[1] + 1),
            "Overtime": np.random.randint(overtime_range[0], overtime_range[1] + 1),
            "Distance_from_Home": np.random.randint(distance_from_home_range[0], distance_from_home_range[1] + 1),
            "Education_Level": np.random.randint(education_level_range[0], education_level_range[1] + 1),
            "Marital_Status": np.random.randint(marital_status_range[0], marital_status_range[1] + 1),
            "Number_of_Dependents": np.random.randint(number_of_dependents_range[0], number_of_dependents_range[1] + 1),
            "Job_Level": np.random.randint(job_level_range[0], job_level_range[1] + 1),
            "Company_Size": np.random.randint(company_size_range[0], company_size_range[1] + 1),
            "Company_Tenure": company_tenure,
            "Remote_Work": np.random.randint(remote_work_range[0], remote_work_range[1] + 1),
            "Leadership_Opportunities": np.random.randint(leadership_opportunities_range[0], leadership_opportunities_range[1] + 1),
            "Innovation_Opportunities": np.random.randint(innovation_opportunities_range[0], innovation_opportunities_range[1] + 1),
            "Company_Reputation": np.random.randint(company_reputation_range[0], company_reputation_range[1] + 1),
            "Employee_Recognition": np.random.randint(employee_recognition_range[0], employee_recognition_range[1] + 1),
        })

# Convertir a DataFrame
df = pd.DataFrame(data)

# Convertir DataFrame a diccionario
data_dict = df.to_dict(orient='records')

# Guardar en un archivo JSON
with open('./data/entrada.json', 'w') as f:
    json.dump(data_dict, f, indent=4)

print("Datos guardados en entrada.json")