from patient import  printPatientDetails

def test_patient():
    op=(
        f"Patient id:1001\n"
        f"Patient name:Queen\n"
        f"Patient age:16\n"
        f"Patient diagnosis:Cold\n"
    )

    assert printPatientDetails(1001,"Queen",16,"Cold") == op