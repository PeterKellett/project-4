/* Core logic/payment for this comes from here:
    https://stripe.com/docs/accept-a-payment

   CSS
   https://stripe.com/docs/stripe-js
*/
console.log("stripe_elements js")
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();

// Custom styling can be passed to options when creating an Element.
// (Note that this demo uses a wider set of styles than the guide below.)
var style = {
  base: {
    color: '#000',
    fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
    fontSmoothing: 'antialiased',
    fontSize: '16px',
    '::placeholder': {
      color: '#000'
    }
  },
  invalid: {
    color: '#fa755a',
    iconColor: '#fa755a'
  }
};
var card = elements.create('card', {style: style});

card.mount('#card-element');

//Handle realtime validation errors on the card element
card.addEventListener('change', function(event) {
    console.log("event listener")
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
        <span class="icon" role="alert">
            <i class="fas fa-times"></i>
        </span>
        <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    }
    else {
        errorDiv.textContent = '';
    }
});

// Handle the payment form submit to @Stripe
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
  ev.preventDefault();
  card.update({'disabled': true})
  $('#submit-button').attr('disabled', true);
  stripe.confirmCardPayment(clientSecret, {
    payment_method: {
      card: card,
    }
  }).then(function(result) {
    if (result.error) {
      // Show error to your customer (e.g., insufficient funds)
      console.log(result.error.message);
      var errorDiv = document.getElementById('card-errors');
      var html = `
        <span class="icon" role="alert">
            <i class="fas fa-times"></i>
        </span>
        <span>${result.error.message}</span>
        `;
        $(errorDiv).html(html);
        card.update({'disabled': false})
        $('#submit-button').attr('disabled', false)
    } else {
      // The payment has been processed!
      if (result.paymentIntent.status === 'succeeded') {
          console.log("payment succeeded")
          form.submit();
        // Show a success message to your customer
        // There's a risk of the customer closing the window before callback
        // execution. Set up a webhook or plugin to listen for the
        // payment_intent.succeeded event that handles any business critical
        // post-payment actions.
      }
    }
  });
});