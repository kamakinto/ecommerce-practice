#Checkout Process

1. Cart --> Checkout View :: Prepares the Order
        -Login or Enter an Email (as Guest)
        - User enters Shipping Address
        - User enters Billing info
                - Billing Address
                - Credit Cart / Payment

2. Billing App/Component
        - Billing Profile - A profile that is associated to a user or an email address
                - User or Email (guest Email)
                - generate payment processor token (Stripe or Braintree)

3. Orders / Invoices App/component :: How we are going to handle the ordering on the Backend.
        - Connecting the Billing Profile
        - Shipping / Billing Address
        - Cart
        - Status -- Shipped? Cancelled?
