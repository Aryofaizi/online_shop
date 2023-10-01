# Django Online Shop with Cart
<i class="fas fa-docker"></i> Docker
<i class="fab fa-python"></i> Python
<img src="https://user-images.githubusercontent.com/25181517/192158954-f88b5814-d510-4564-b285-dff7d6400dad.png">
<i class="fab fa-css3"></i> CSS
<i class="fab fa-markdown"></i> Markdown



Welcome to the Django Online Shop with Cart project! This project is designed to provide a simple and functional online shopping experience with a primary emphasis on the shopping cart feature.

<h2 style="font-size: 36px; font-weight: bold; color: #fff;">Overview</h2>
This Django-based online shop allows users to browse a catalog of products, add them to a cart, and proceed to checkout. While it's a work in progress, the core functionality for managing a shopping cart is fully implemented.

<h4 style="font-size: 36px; font-weight: bold; color: #fff;">Features</h4>
Browse products in the catalog.
Add and remove items from the shopping cart.
Adjust item quantities in the cart.
Calculate and display the total price in the cart.
Basic checkout functionality.

<h5 style="font-size: 36px; font-weight: bold; color: #fff;">Installation and Setup</h5>
To run this project locally, follow these steps:

Clone the repository: 
```
git clone https://github.com/Aryofaizi/online_shop.git

```
Navigate to the project directory:
```
cd your-online-shop
```
Create a virtual environment:
```
python -m venv venv
```
Activate the virtual environment:
On Windows:
```
venv\Scripts\activate
```
On macOS and Linux:
```
source venv/bin/activate
```
Install dependencies:
```
pip install -r requirements.txt
```
Apply database migrations:
```
python manage.py migrate
```
Create a superuser for admin access:
```
python manage.py createsuperuser
```
Start the development server:
```
python manage.py runserver
```
For Docker users, you can also run this project in a Docker container:

bash
Copy code

```
docker-compose up 
```
For more detailed instructions and documentation, please refer to our documentation.

<h5 style="font-size: 36px; font-weight: bold; color: #fff;">Usage</h5>
Once you have set up the project, you can:

Browse the catalog and add products to the cart.
Adjust product quantities in the cart.
Proceed to checkout (note that this is a basic implementation).
<h5 style="font-size: 36px; font-weight: bold; color: #fff;">Contributing</h5>
We welcome contributions! If you'd like to contribute to this project, please follow our contribution guidelines.

<h5 style="font-size: 36px; font-weight: bold; color: #fff;">License</h5>
This project is licensed under the MIT License.

<h5 style="font-size: 36px; font-weight: bold; color: #fff;">Contact</h5>
If you have any questions, feedback, or suggestions, feel free to reach out to us at **aryofaizi@gmail.com**