from pyscript import display, document

def calculate(evt=None):
    # STUDENT INFO
    fname = document.getElementById("fname").value
    lname = document.getElementById("lname").value

    # GRADES (collected as integers)
    math = int(document.getElementById("math").value)
    science = int(document.getElementById("science").value)
    english = int(document.getElementById("english").value)
    filipino = int(document.getElementById("filipino").value)
    pe = int(document.getElementById("pe").value)

    # SUBJECTS AND UNITS
    subjects = ("Math", "Science", "English", "Filipino", "PE")
    grades = (math, science, english, filipino, pe)
    units = (5, 5, 5, 3, 1)

    # DISPLAY STUDENT NAME
    display(f"Student: {fname} {lname}", target="output")

    # DISPLAY GRADES
    sub1, sub2, sub3, sub4, sub5 = subjects
    grade1, grade2, grade3, grade4, grade5 = grades
    unit1, unit2, unit3, unit4, unit5 = units

    display(f"{sub1} ({unit1} units): {grade1}", target="output")
    display(f"{sub2} ({unit2} units): {grade2}", target="output")
    display(f"{sub3} ({unit3} units): {grade3}", target="output")
    display(f"{sub4} ({unit4} units): {grade4}", target="output")
    display(f"{sub5} ({unit5} units): {grade5}", target="output")

    # CALCULATE GWA
    weighted_sum = grade1*unit1 + grade2*unit2 + grade3*unit3 + grade4*unit4 + grade5*unit5
    total_units = unit1 + unit2 + unit3 + unit4 + unit5
    gwa = weighted_sum // total_units  

    display(f"General Weighted Average (GWA): {gwa}", target="output")

#GWA REMARKS
def passing_failing(evt=None):
   
    math = int(document.getElementById("math").value)
    science = int(document.getElementById("science").value)
    english = int(document.getElementById("english").value)
    filipino = int(document.getElementById("filipino").value)
    pe = int(document.getElementById("pe").value)

    units = (5, 5, 5, 3, 1)
    grades = (math, science, english, filipino, pe)

    weighted_sum = math*5 + science*5 + english*5 + filipino*3 + pe*1
    total_units = 5 + 5 + 5 + 3 + 1
    gwa = weighted_sum // total_units

    document.getElementById('output').innerHTML = ''
    if gwa > 74:
        display(f'GWA {gwa} is passing✅', target='output')
    else:
        display(f'GWA {gwa} is failing❌', target='output')
