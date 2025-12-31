from medical import fetch_medical_issues  

def test_real_medicle_file():
  
    result = fetch_medical_issues("medical_data.xml")
    
  
    expected = ['Allergy', 'Asthma', 'Cardiac Arrest', 
                'Diabetes', 'Hypertension']
    
    assert len(result) >= 5 
    assert result == sorted(set(result))  
    print(" Your  file works!")
    print("Found issues:", result)