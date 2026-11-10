from flask import Flask, render_template, request
import webbrowser

app = Flask(__name__, static_folder="statics")


lending_items = []
student_requests = []


@app.route("/")
def home():
    return render_template("index.html")


# LEND ITEM
@app.route("/lend", methods=["GET", "POST"])
def lend():

    if request.method == "POST":

        item_name = request.form.get("item_name")
        quantity = request.form.get("quantity")
        location = request.form.get("location")
        availability = request.form.get("availability")
        owner = request.form.get("owner")

        values = {
            "item_name": item_name,
            "quantity": int(quantity),
            "location": location,
            "availability": availability,
            "owner": owner
        }

        lending_items.append(values)

        print("Lending Items:", lending_items)

        return "Item received successfully!"

    return render_template("lend.html")


# NEED ITEM

@app.route("/need", methods=["GET", "POST"])
def need():

    if request.method == "POST":

        item_name = request.form.get("item_name")
        quantity = request.form.get("quantity")
        location = request.form.get("location")
        duration = request.form.get("duration")
        priority = request.form.get("priority")

        request_values = {
            "item_name": item_name,
            "quantity": int(quantity),
            "location": location,
            "duration": duration,
            "priority": priority
        }
        print("Lending items:", lending_items)
        print("Requested item:", item_name)
        matches=[]

        student_requests.append(request_values)

        print("Student Requests:", student_requests)
        for i in lending_items:
            if i["item_name"].lower() == item_name.lower() and i["quantity"] >= int(quantity) and i["availability"] == "Available":
                print(f"Match found for {item_name}!, Quantity: {quantity}, Location: {location}")
                matches.append(i)
        
        return render_template("matches.html", matches=matches)

    return render_template("need.html")

@app.route("/borrow", methods=["POST"])
def borrow():

    owner = request.form.get("owner")
    borrow_quantity = int(request.form.get("borrow_quantity"))

    if borrow_quantity <= 0:
        return "Please enter a valid quantity!"

    for item in lending_items:

        if item["owner"] == owner:

            if borrow_quantity <= item["quantity"]:

                item["quantity"] -= borrow_quantity

                if item["quantity"] == 0:
                    item["availability"] = "Unavailable"

                print("Updated Lending Items:", lending_items)

                return "Borrowing confirmed!"

            else:
                return "Not enough quantity available!"

    return "Item not found!"

if __name__ == "__main__":
    webbrowser.open("http://127.0.0.1:3000")
    app.run(host="127.0.0.1", port=3000)