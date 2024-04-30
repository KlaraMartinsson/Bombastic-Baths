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

## Testing User Stories

Testing of the User stories for the project.
All User Stories can be found [Here](https://github.com/users/KlaraMartinsson/projects/5)
