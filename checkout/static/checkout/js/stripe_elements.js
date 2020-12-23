/* Core logic/payment for this comes from here:
    https://stripe.com/docs/accept-a-payment

   CSS
   https://stripe.com/docs/stripe-js
*/
console.log("stripe_elements js")
var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();

// Custom styling can be passed to options when creating an Element.
// (Note that this demo uses a wider set of styles than the guide below.)
var style = {
  base: {
    color: '#32325d',
    fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
    fontSmoothing: 'antialiased',
    fontSize: '16px',
    '::placeholder': {
      color: '#aab7c4'
    }
  },
  invalid: {
    color: '#fa755a',
    iconColor: '#fa755a'
  }
};
var card = elements.create('card', {style: style});

card.mount('#card-element');