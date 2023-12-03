fetch("/config/")
  .then((result) => {
    return result.json();
  })
  .then((data) => {
    // Initialize Stripe.js
    const stripe = Stripe(data.publicKey);
    const el = document.querySelector("#js")
    id = el.dataset.itemId

    document.querySelector("#submitBtn").addEventListener("click", () => {
      // Get Checkout Session ID

      fetch(`/buy/${id}`, {method: 'GET'})
        .then((result) => {
          return result.json();
        })
        .then((data) => {
          console.log("data: ", data);
          // Redirect to Stripe Checkout
          return stripe.redirectToCheckout({ sessionId: data.sessionId });
        })
        .catch((res) => {
          console.log("res", res);
        });
    });
  });