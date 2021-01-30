## Testing  
### Code validation  
The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.
- [W3C Markup Validator](https://validator.w3.org/)
- [W3C CSS Validator](http://www.css-validator.org/)  
- Lighthouse browser test gave the following results  
    - Performance: 98  
    - Accessibility: 97  
    - Best Practices: 100  
    - SEO: 90  

### Testing the user stories  
- As a user:  
As a user upon entering the site I can see an illustration of the products, the company slogan with an obvious button to lead into the site proper. There is a navbar which is positioned sticky top so is always visible to the user with site navigation links provided.  
On entering the site proper, the products are clearly displayed in an organised manner with a neat sidebar available to be able to filter the products accordingly. All relevant details of each product are clearly displayed on each product card with an obvious button to view the product in more detail.  
The product details page has the form to add it to the shopping bag with a toast shown which provides feedback to the user on whether this action was carried out or not and also the shopping bag value in the navbar is updated to reflect this action.  
The shopping basket neatly lists each item in the shopping basket with the ability to add or remove quantities without the need to go back to the products page.  
The checkout page is neatly arranged with the field inputs clearly defined and labelled with only the necessary information required.  
Upon registering with the site I have the ability to be able to save my delivery details to prevent having to resubmit my details on subsequent purchases.   
  
- As an owner:  
As an owner I can see all the products are showcased in an organised tidy format. I can see there is a contrasting banner displayed beneath the navbar inviting users to register to avail of a discount.  
I can view all orders submitted with all the necessary order information  through the site admin which can only be accessed with my password.  
I can add, edit and delete products easily through the site admin with all changes being immediately made without delay.  

### Testing the templates  
Go to each page in turn and verify the page and contents display correctly.
1. / - Verify the home page is displayed  
2. /products - Verify the products page is displayed  
3. /product/product_id - Verify the product details page is displayed  
4. /bag - Verify the Shopping bag page is displayed  
5. /profile - Verify the profile page is displayed  
6. /checkout - Verify the checkout page is displayed. 
7. /login - Verify the login page is displayed  
8. /Register - Verify the register page is displayed  

### Testing functionality  
#### allAuth Registration test 
1. Go to registration page and submit login form.
2. Verify email verification page is displayed.
3. Verify verification email is received.
4. Verify visiting the link in the email completes the registration process.  

#### allAuth Login/logout test
1. Go to login in page and submit the form.
2. Verify user is logged in correctly.  
3. Click logout link in navbar and verify user is logged out correctly.

#### Sidebar filter tests
1. Go to products page and verify sidebar triggers correctly.  
2. Verify all checkboxes are ticked by default and all products are displayed.
3. Uncheck some of the checkboxes and verify the products are filtered out correctly.  
4. Verify the All checkbox checks and unchecks all other checkboxes in the sidebar menu.  

#### Product details test  
1. Go to product details of a product.  
2. Verify a user can select quantities and size of a particular product.  
3. Verify a user can submit the form to the shopping bag.  

#### Reviews  
1. Verify the reviews modal on a product with reviews opens and closes.
2. Verify all reviews for that product are listed on the modal.  

#### Add/Edit/Delete reviews test  
1. Verify a user must be logged in to be able to add a review.
2. Log in and add a review to a product.  
3. Go to profile page, edit and verify the review can be edited and deleted.  
4. Add another review and log out.
5. Verify the review added cannot be edited by entering /edit_review/<review_id> in the url.  
6. Verify the review added cannot be deleted by entering /delete_review/<review_id> in the url.  

#### Shopping bag test
1. Add several items of various sizes and quantities of each.
2. Click on the shopping bag icon in the navbar to go to the shopping bag page.  
3. Verify size, quantities and subtotals are correct for each item added.
4. Verify total, delivery, and grand totals are correct.  
5. Verify a user can edit and delete any item in their shopping bag. 

#### Checkout test  
1. Go to checkout page and submit the form using a Stripe test card number.  
    - [Stripe docs - Testing](https://stripe.com/docs/testing)
2. Verify the user is brought to the checkout success page with the order details displayed.  
3. Go to Stripe dashboard > Developers > logs and verify a payment intent was created, the payment was charged, and the payment was successful.  

#### Checkout Stripe webhook test  
In case there is a problem with the connection between the server and the user and a Stripe callback cannot be made at the time of payment execution a Stripe webhook is used to complete the payment and safely store the order to the database.  
The Stripe webhook endpoint can be tested in 2 ways:  
1. By ommitting the form.send() command on the checkout page. This will force the server to initiate the callback using the webhook endpoint.  
2. Webhook endpoints can be manually triggered from the Stripe dashboard > webhooks. This will trigger a generic callback response to the endpoint provided.  

#### Securing the views test (Restricting certain functionality to registered users only)  
@login_required from django.contrib.auth.decorators  
Restricted content and functionality includes:  
- Functionality of adding, editing, or deleting a review.  
- Access to the Profile page.  
- Access to order_history content.  
- Access to Product Management pages. 
1. Log out and manually force a url to restricted content.  
2. Verify access to requested url is denied and the user is brought to the home page with an error message displayed. 
3. Verify that only the superuser has access to the Product Management page. 

### Other tests  
#### Testing the discount banner and discount calculation.  
- With user logged out  
1. Verify the discount banner is displayed on all pages.    
2. Add some products to the shopping bag and verify that no discount value is being applied on the checkout page.  
  
- With user logged in  
1. Verify the discount banner is hidden on all pages.  
2. Add some products to the shopping bag and verify that a discount percentage of 15% is being applied to the total less delivery charge on the checkout page.  

#### Testing the delivery threshold and delivery cost calculation  
1. Add a product to the shopping bag and verify that a delivery charge of 10% is applied to the order total.  
2. Verify the delivery charge is free once the order total exceeds €50.  

