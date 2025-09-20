from pyscript import document

def click(event):
    output_div = document.getElementById("output")
    output_div.innerText = ""

    name = document.getElementById("name").value
    age = document.getElementById("age").value
    school = document.getElementById("school").value

    message = f"""
    \nStudent Profile:
    
    Name: {name}
    Age: {age}
    School: {school}

    \nNotes:
    
   Hello {name}!
   You're currently {age} years old.
   You study at {school}.
   This website was made with HTML and Python Script.
    """

    output_div.innerText = message

