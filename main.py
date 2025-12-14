from pyscript import document

# Get dropdown element
dropdown = document.getElementById("club")

# Function to show the selected club info
def show_club(evt=None):
    selected = dropdown.value
    # Hide all club info divs
    infos = document.getElementsByClassName("club-info")
    for i in range(len(infos)):
        infos[i].style.display = "none"
    # Show the selected club
    if selected:
        div = document.getElementById(selected)
        if div:
            div.style.display = "block"

# Attach event listener
dropdown.addEventListener("change", show_club)
    
