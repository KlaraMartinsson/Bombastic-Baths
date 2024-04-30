## Code Validation
The Bombastic Baths website have been through a lot of manual testing by myself, friends, mentors and family. This includes code validation, performance testing, cross-device testing, testing if user stories are completed and feedback messages for users.

### HTML Validation
All HTML code has passed through validation using W3 Markup Validator and shows no errors:

| **Tested** | **Result** | **View Result** | **Pass** |
--- | --- | --- | :---:
| **Home App** |
|index.html| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](/documentation/validation/index-validation.jpg)</details>| ✅
|about.html| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](/documentation/validation/about-validation.jpg)</details>| ✅
|faq.html| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](/documentation/validation/faq-validation.jpg)</details>| ✅
|privacypolicy.html| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](/documentation/validation/privacypolicy-validation.jpg)</details>| ✅
| **Products App** |
|products.html| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](/documentation/validation/products-validation.jpg)</details>| ✅
|product_details.html| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](/documentation/validation/productdetails-validation.jpg)</details>| ✅
| **Cart App** |
|cart.html| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](/documentation/validation/cart-validation.jpg)</details>| ✅
| **Checkout App** |
|checkout.html| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](/documentation/validation/checkout-validation.jpg)</details>| ✅
|checkout_success.html| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](/documentation/validation/checkout-success-validation.jpg)</details>| ✅
| **Profile App** |
|profile.html| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](/documentation/validation/profile-validation.jpg)</details>| ✅
| **Wishlist App** |
|wishlist.html| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](/documentation/validation/wishlist-validation.jpg)</details>| ✅
| **Signup HTML** |
|signup.html| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](/documentation/validation/signup-validation.jpg)</details>| ✅
| **Login HTML** |
|login.html| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](/documentation/validation/login-validation.jpg)</details>| ✅
| **Logout HTML** |
|logout.html| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](/documentation/validation/logout-validation.jpg)</details>| ✅

### CSS Validation
All CSS files has passed through validation using [W3C Jigsaw](https://jigsaw.w3.org/css-validator/) and shows no errors:
| **Tested** | **Result** | **View Result** | **Pass** |
--- | --- | --- | :---:
| **Style.css** |
|style.css| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](/documentation/validation/style.css-validation.jpg)</details>| ✅
| **Profile.css** |
|profile.css| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](/documentation/validation/profile.css-validation.jpg)</details>| ✅
| **Checkout.css** |
|checkout.css| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](/documentation/validation/checkout.css-validation.jpg)</details>| ✅
| **Whole page** |
|Whole page| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](/documentation/validation/wholepage.css-validation.jpg)</details>| ✅

### Python Validation
All Python files has passed through validation using [PEP 8](https://pep8ci.herokuapp.com/) and shows no errors:
| **Tested** | **Result** | **View Result** | **Pass** |
--- | --- | --- | :---:
| **Home App** |
|views.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](/documentation/validation/home-views.py-validation.jpg)</details>| ✅
|urls.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](/documentation/validation/home-urls.py-validation.jpg)</details>| ✅
|apps.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](/documentation/validation/home-apps.py-validation.jpg)</details>| ✅
| **Products App** |
|models.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](/documentation/validation/products-models.py-validation.jpg)</details>| ✅
|views.py| 1 django import line to long | <details><summary>Screenshot of result</summary>![Result](/documentation/validation/products-views.py-validation.jpg)</details>| ✅
|urls.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](/documentation/validation/products-urls.py-validation.jpg)</details>| ✅
|apps.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](/documentation/validation/products-apps.py-validation.jpg)</details>| ✅
|forms.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](/documentation/validation/products-forms.py-validation.jpg)</details>| ✅
|admin.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](/documentation/validation/products-admin.py-validation.jpg)</details>| ✅
| **Cart App** |
|views.py| All clear, no errors found  | <details><summary>Screenshot of result</summary>![Result](/documentation/validation/cart-views.py-validation.jpg)</details>| ✅
|urls.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](/documentation/validation/cart-urls.py-validation.jpg)</details>| ✅
|apps.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](/documentation/validation/cart-apps.py-validation.jpg)</details>| ✅
|contexts.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](/documentation/validation/cart-contexts.py-validation.jpg)</details>| ✅
| **Checkout App** |
|models.py| All clear, no errors found  | <details><summary>Screenshot of result</summary>![Result](/documentation/validation/checkout-models.py-validation.jpg)</details>| ✅
|views.py| All clear, no errors found  | <details><summary>Screenshot of result</summary>![Result](/documentation/validation/checkout-views.py-validation.jpg)</details>| ✅
|urls.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](/documentation/validation/checkout-urls.py-validation.jpg)</details>| ✅
|apps.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](/documentation/validation/checkout-apps.py-validation.jpg)</details>| ✅
|signals.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](/documentation/validation/checkout-signals.py-validation.jpg)</details>| ✅
|admin.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](/documentation/validation/checkout-admin.py-validation.jpg)</details>| ✅
|forms.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](/documentation/validation/checkout-forms.py-validation.jpg)</details>| ✅
|webhook_handler.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](/documentation/validation/checkout-webhookshandler.py-validation.jpg)</details>| ✅
|webhooks.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](/documentation/validation/checkout-webhooks.py-validation.jpg)</details>| ✅
| **Profiles App** |
|models.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](/documentation/validation/profiles-models.py-validation.jpg)</details>| ✅
|views.py| All clear, no errors found  | <details><summary>Screenshot of result</summary>![Result](/documentation/validation/profiles-views.py-validation.jpg)</details>| ✅
|urls.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](/documentation/validation/profiles-urls.py-validation.jpg)</details>| ✅
|apps.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](/documentation/validation/profiles-apps.py-validation.jpg)</details>| ✅
|admin.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](/documentation/validation/profiles-admin.py-validation.jpg)</details>| ✅
|forms.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](/documentation/validation/profiles-forms.py-validation.jpg)</details>| ✅
| **Wishlist App** |
|models.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](/documentation/validation/wishlist-models.py-validation.jpg)</details>| ✅
|views.py| All clear, no errors found  | <details><summary>Screenshot of result</summary>![Result](/documentation/validation/wishlist-views.py-validation.jpg)</details>| ✅
|urls.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](/documentation/validation/wishlist-urls.py-validation.jpg)</details>| ✅
|admin.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](/documentation/validation/wishlist-admin.py-validation.jpg)</details>| ✅
|apps.py| All clear, no errors found | <details><summary>Screenshot of result</summary>![Result](/documentation/validation/wishlist-apps.py-validation.jpg)</details>| ✅

## Accessibility


## Performance
All pages where tested on [Googles lighthouse](https://developer.chrome.com/docs/lighthouse/).
I received a low score for the index.html file due to the large carousel header. Because of its contribution to the design, I've chosen to retain it. However, I'll explore ways to enhance its performance for better optimization in the future. 
 The performance scores were assessed for both desktop and mobile devices. Below are the summarized results:

### Desktop Performance
| **Tested** | **Performance score** | **View Result** | **Pass** |
--- | --- | --- | :---:
| **Home App** |
|index.html| 80/100 | <details><summary>Screenshot of result</summary>![Result](/documentation/validation/index-lighthouse-desktop.jpg)</details>| ✅

### Mobile Performance
| **Tested** | **Performance score** | **View Result** | **Pass** |
--- | --- | --- | :---:
| **Home App** |
|index.html| 47/100 | <details><summary>Screenshot of result</summary>![Result](/documentation/index-lighthouse-mobile/.jpg)</details>| ✅



<details>
<summary>Desktop</summary>
<img src="placeholder">
</details>

<details>
<summary>Mobile</summary>
<img src="placeholder">
</details>


## Performing tests on various devices

## Manual Testing
| Functionality | What's being tested | Result |
|------|-------------|--------|
| Registration | A new user can create an account successfully. | Pass |
|  | The website displays an appropriate error message with hint when validation fails. | Pass |
|  | The website displays an appropriate success message if registration worked | Pass |
|  | User is signed in automatically when click confirm button | Pass |
|Login | A registered user can log in successfully. | Pass |
|  | The website displays an appropriate error message when a user enters an incorrect email or password. | Pass |
|  | The website displays an appropriate success message if registration worked | Pass |
|  | A logged-in user can sign out successfully. | Pass |
|Profile | A logged-in user can access their profile | Pass |
|  | User can view their order history in their profile | Pass |
|  | User can change their delivery details in profile | Pass |
|  | User can delete their account | Pass |
|  | A user cannot edit or delete another user's profile | Pass |
| Admin Panel | Admin can login to admin panel. | Pass |
|  | Admin can add, edit and delete products. | Pass |
|  | Admin can add, edit and delete users. | Pass |
|  | Admin can add, edit and delete users reviews. | Pass |
|Products CRUD | Verify that a user can add products, edit and delete products from the shopping cart | Pass |
|  | Confirmation message is displayed when a product is added, updated or deleted | Pass |
|Reviews CRUD | Verify that a user can add, edit and delete their reviews| Pass |
|  | Confirmation message is displayed when a review is added, updated or deleted | Pass |
|Ratings | Verify that a user can add a rating to a product. | Pass |
|Wishlist | Verify that a user can add to their wishlist. | Pass |
|  | Verify that a user can remove an item in their wishlist. | Pass |
|Sort functionality | Verify that sort functionality works. | Pass |
|Search functionality | Verify that search functionality works. | Pass |
|Confirmation messages | Verify that user gets success/error messages after an action. | Pass |
|Checkout | Verify that form is valid, have to be an email address, have to have a name, number, address, country. | Pass |
|  | Verify that a user can put in their credit cards | Pass |
|  | Verify that a user get an error message if card info is wrong | Pass |
|  | Verify that a user redirects to confirmation page after an order been made | Pass |
|  | Verify that the order is on users profile order history | Pass |









## Testing User Stories

Testing of the User stories for the project.
All User Stories can be found [Here](https://github.com/users/KlaraMartinsson/projects/5)
