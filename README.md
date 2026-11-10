# NeedIt – Smart Campus Item-Matching System

**Find what you need. Lend what you have.**

NeedIt is a smart campus item-matching system designed to make resource sharing easier among college students. It connects students who need items with students who are willing to lend them.

Instead of spending time asking multiple people for everyday academic essentials, students can list available items or submit requests. NeedIt uses a Python-based matching algorithm to identify suitable listings based on item name, available quantity, and availability status.

The system also supports partial borrowing and automatically updates the remaining quantity after a borrowing request is confirmed.

---

## HOW TO USE

### Installation

1. Clone or download this repository.
2. Open the project folder in VS Code or another code editor.
3. Make sure Python is installed on your system.
4. Open the terminal in the project directory.
5. Install Flask using:

   ```bash
   py -m pip install flask
   ```

6. Run the application:

   ```bash
   py main.py
   ```

7. The website will automatically open in your default browser at:

   `http://127.0.0.1:3000`

8. Keep the terminal running while using the website. Press `Ctrl + C` in the terminal to stop the server.

### Using NeedIt

1. **Lend an Item:** Select the option to lend an item and enter its name, quantity, location, availability, and owner details.
2. **Request an Item:** Select the option to find an item and enter the required item name, quantity, location, duration, and priority.
3. **View Matches:** NeedIt displays listings that satisfy the matching conditions.
4. **Borrow an Item:** Select the quantity you wish to borrow and confirm the borrowing.
5. **Automatic Quantity Update:** The available quantity is reduced automatically after successful borrowing. Listings with zero remaining quantity become unavailable.

---

## TECH STACK

- **Python:** Core programming language used for the matching algorithm and quantity management.
- **Flask:** Python web framework used to connect the frontend with the backend.
- **HTML:** Used to structure the web pages and forms.
- **CSS:** Used to design and style the user interface.

---

## LIMITATIONS

- The current prototype uses in-memory Python lists to store lending listings and student requests instead of a persistent database.
- Item quantities are updated during the active Flask session, but the data is not retained after the server is restarted.
- The current implementation is designed as a prototype for a single-college environment and does not yet handle simultaneous borrowing requests with database-level transaction management.

---

## CONTRIBUTOR

- **Avani M Nair**