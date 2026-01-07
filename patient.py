def printPatientDetails(i,n,a,d):
    return(
        f"Patient id:{i}\n"
        f"Patient name:{n}\n"
        f"Patient age:{a}\n"
        f"Patient diagnosis:{d}\n"
    )

if __name__== "__main__":
    id=101
    name="king"
    age=90
    diagnosis="cancer"

    res= printPatientDetails(id,name,age,diagnosis)
    print(res)