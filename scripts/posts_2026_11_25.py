"""The three guides published 2026-11-25: delivery dates (two) and split shipping."""
from post_from_template import make

INSTALL = '<a class="btn btn-primary" href="https://apps.shopify.com/smart-checkout-widgets" target="_blank" rel="noopener noreferrer">Install on Shopify</a>'
def docs(anchor, label): return f'<a class="btn btn-secondary" href="/docs/#{anchor}">{label}</a>'
def fig(name, w, h, alt, cap): return f'<figure class="post-figure">\n  <img src="/images/blog/{name}.webp" width="{w}" height="{h}" alt="{alt}" loading="lazy" decoding="async">\n  <figcaption>{cap}</figcaption>\n</figure>'

make('shopify-delivery-date-picker',
 'Shopify delivery date picker: let customers choose a date on the product page or in the cart',
 'Shopify shows delivery estimates but has no calendar for customers. Here is how to add one on any Shopify plan, set lead times and cutoffs, and decide whether checkout should require a date.',
 'delivery dates', 'shopify-delivery-date-picker', 'Guide: adding a delivery date picker to Shopify', '2026-11-25', 'Published November 25, 2026',
f'''
<p>Shopify can show a customer when an order might arrive. It has no calendar where the customer picks the day. If you sell flowers, cakes, furniture or anything that needs someone at home, that choice usually ends up in the order note or in an email the next morning.</p>
<p>Smart Checkout Widgets now has a delivery date calendar. It works on every Shopify plan, because it lives in your theme and the checkout part uses Shopify's validation rules, which are open to all plans. The calendar itself is part of the app's paid plans.</p>
{fig('delivery-date-calendar', 1600, 1125, 'A product page with a delivery date calendar above the Add to cart button, with closed days crossed out', 'The calendar on an example product page. Crossed-out days are closed or too soon.')}
<h2>What the customer does</h2>
<p>They choose how they want the order (shipping, local delivery or pickup, whichever you offer) and then a day. The choice shows on the product page, on the cart page and in the cart drawer, and it stays the same in all of them. After they buy, the date can show on the Thank you and Order status pages.</p>
<p>You see the method and the date on the order in Shopify admin, under Additional details. With Buy it now, they are on the product line instead, because that button skips the cart.</p>
<h2>What you decide</h2>
<div class="table-wrap"><table>
    <thead><tr><th>Setting</th><th>What it does</th></tr></thead>
    <tbody>
      <tr><td>Lead days</td><td>How many days ahead the first date is. 0 allows the same day.</td></tr>
      <tr><td>Cutoff time</td><td>After this time, one more day is added. It uses your store's time zone, wherever the customer is.</td></tr>
      <tr><td>Days of the week</td><td>Which days you deliver or open for pickup.</td></tr>
      <tr><td>Closed dates</td><td>Holidays and days you are fully booked.</td></tr>
      <tr><td>How far ahead</td><td>The last day a customer can book.</td></tr>
    </tbody>
</table></div>
<p>Lead days, the cutoff and the days of the week are set separately for each way to receive an order. A shop can offer pickup tomorrow and delivery in three days.</p>
<h2>Adding it to your theme</h2>
<ol>
  <li>Open Delivery Dates in the app, switch the calendar on and save.</li>
  <li>Click Switch on in theme, then save the theme.</li>
  <li>Add the Delivery date block to the Thank you and Order status pages in the checkout editor.</li>
</ol>
<p>The calendar looks for your Check out and Add to cart buttons and goes above them. We tried it on 22 theme demo stores on desktop and phone, including Dawn, Horizon, Prestige, Impulse, Warehouse, Turbo and Empire.</p>
<p>If it lands in the wrong place, enter a class name or ID from your theme in the app embed settings and choose before it, after it, or inside it. That also helps with older themes. Headless storefronts won't work, since they have no theme to put it in.</p>
<h2>Should checkout require a date?</h2>
<p>You can leave the date optional or let checkout refuse an order without one. With the check on, checkout also refuses a date that has passed, and a mismatch such as a delivery date on an order the customer switches to pickup.</p>
<p>Think about these before you turn it on:</p>
<ul>
  <li>Every order with a physical product will need a date, including ones from draft orders, checkout links and other online sales channels. Point of sale is not checked.</li>
  <li>Keep the calendar on your product pages, because Buy it now skips the cart.</li>
  <li>If you offer Shop Pay, Apple Pay, Google Pay or PayPal, try each button once. Shopify says the check covers express checkouts, and we have not tested those buttons ourselves yet.</li>
</ul>
<p>If your paid plan ends, the calendar and the check switch off together, so a missing calendar can't leave customers stuck at checkout.</p>
<h2>Watch out for Shopify's own estimates</h2>
<p>Shopify's delivery estimates don't know which date the customer chose. In our test the customer picked 27 November while the rate at checkout said 1 to 3 December. To hide those dates, go to Settings, then Shipping and delivery, and set Delivery estimates to Off. Your rates may still show a transit time.</p>
<h2>What it doesn't do yet</h2>
<p>There are no time slots, daily order limits or extra charges for a date. One date covers the whole cart.</p>
''',
[('Does Shopify have a built-in delivery date picker?', "No. Shopify can show estimated delivery dates, but customers can't choose a day without an app."),
 ('Does a delivery date picker work without Shopify Plus?', "Yes. The calendar runs in your theme and the checkout check is a Shopify validation rule, so both work on every Shopify plan. The feature is part of the app's Growth, Advanced and Pro plans."),
 ('Where do I see the date?', 'On the order in Shopify admin, under Additional details. For Buy it now orders it is on the product line.'),
 ('Can I require a date before checkout?', 'Yes. It is off by default. When you switch it on, checkout refuses orders with a physical product that have no valid date.'),
 ('Which themes does it work with?', 'We tried 22 theme demo stores, including Dawn and Horizon. If it lands in the wrong place, you can point it at a class name or ID in your theme. Headless storefronts are not supported.')],
 [INSTALL, docs('delivery-dates', 'Delivery dates docs')])

make('shopify-delivery-pickup-dates-florists-bakeries',
 'Delivery and pickup dates for florists and bakeries on Shopify: cutoffs, lead times and closed days',
 'How to set up a delivery and pickup calendar for a flower shop or bakery on Shopify, with cutoff times, lead days per method, closed dates and the questions to answer first.',
 'delivery dates', 'shopify-delivery-pickup-dates-florists-bakeries', 'Guide: delivery and pickup dates for florists and bakeries', '2026-11-25', 'Published November 25, 2026',
f'''
<p>A bouquet for Friday is worth nothing on Saturday. For a florist or a bakery the date is part of the product, and a Shopify checkout doesn't ask for it.</p>
<p>This guide sets up a calendar for that kind of shop with the <a href="/blog/shopify-delivery-date-picker/">delivery date picker</a> in Smart Checkout Widgets. It works on every Shopify plan and is part of the app's paid plans.</p>
<h2>Answer these first</h2>
<ul>
  <li>How long does an order take to make? That is your lead time, and it may differ for pickup and delivery.</li>
  <li>When do you stop taking orders for the next day?</li>
  <li>Which days do you deliver, and which days can people collect?</li>
  <li>Which dates are you closed or already full?</li>
</ul>
<h2>An example: a flower shop</h2>
<p>Say a shop makes bouquets the day before, delivers Tuesday to Saturday and is open for pickup Monday to Saturday.</p>
<div class="table-wrap"><table>
    <thead><tr><th>Setting</th><th>Local delivery</th><th>Pickup</th></tr></thead>
    <tbody>
      <tr><td>Lead days</td><td>2</td><td>1</td></tr>
      <tr><td>Cutoff time</td><td>14:00</td><td>16:00</td></tr>
      <tr><td>Days of the week</td><td>Tue to Sat</td><td>Mon to Sat</td></tr>
    </tbody>
</table></div>
<p>A customer ordering on Wednesday at 13:00 can have delivery on Friday. At 15:00 the cutoff has passed, so the first delivery day becomes Saturday. Pickup on Thursday is still open until 16:00. The times are the shop's, so a customer abroad sees the same days.</p>
{fig('delivery-date-chosen', 1600, 1125, 'A product page with Local delivery and Friday, December 11 chosen above the Add to cart button', 'After the customer chooses, the calendar closes and shows the day.')}
<h2>An example: a bakery</h2>
<p>A bakery that sells bread and celebration cakes has a harder question, because bread can be ready tomorrow and a cake needs four days. The lead time applies to the whole store, so there are two ways to handle it:</p>
<ul>
  <li>Set the lead time for the slowest product. Simple, and bread customers wait longer than they need to.</li>
  <li>Set it for the fastest product and say on the cake's page that it needs four days. You then check cake orders by hand.</li>
</ul>
<p>Lead times per product are not available yet, so the first way is safer if cakes are most of what you sell.</p>
<h2>Holidays and busy days</h2>
<p>Add closed dates for public holidays and for days you can't take any more orders. A range works too, so one entry covers a week off. There is no automatic limit on orders per day, so close a busy day yourself when it is full.</p>
<p>For Valentine's Day or Mother's Day, close the days before and after if you only deliver on the day itself.</p>
<h2>Make the date count</h2>
<p>Switch on <strong>Require a date before checkout</strong> if an order without a date is useless to you. Checkout then also stops a customer who picks a delivery date and later chooses pickup. Leave it off if you take orders through draft orders or checkout links, since those are checked as well. Try your express buttons, such as Shop Pay, once after you switch it on.</p>
<p>The calendar doesn't change your shipping setup. Local delivery areas, pickup locations and their prices still come from Shopify. If some postcodes can't have delivery, a <a href="/blog/shopify-shipping-rates-by-postcode/">shipping rule by postcode</a> handles that.</p>
<h2>In the workshop</h2>
<p>Each order shows its method and date under Additional details in Shopify admin. Add the Delivery date block to the Thank you and Order status pages too, so customers can check the day themselves.</p>
''',
[('Can I set different cutoff times for delivery and pickup?', 'Yes. Lead days, the cutoff time and the days of the week are set separately for shipping, local delivery and pickup.'),
 ('Can I set a lead time per product?', 'Not yet. The lead time applies to the whole store for each way to receive an order.'),
 ('Can customers choose a time slot?', 'Not yet. They choose a day.'),
 ('Can I limit how many orders I take per day?', 'There is no automatic limit. Add the day to your closed dates when it is full.'),
 ('Which time zone is the cutoff in?', "Your store's time zone, for every customer.")],
 [INSTALL, docs('delivery-dates', 'Delivery dates docs')])

make('shopify-split-shipping-rate-rules',
 'Shopify split shipping: make your shipping rules work in every shipment',
 'When Shopify splits a cart into several shipments, one hide or show-only rule can leave a package with no rate and block checkout. Here is how to set rules that work in each shipment, including ship and pickup in one order.',
 'shipping rules', 'shopify-split-shipping-rate-rules', 'Guide: shipping rules for split shipments', '2026-11-25', 'Published November 25, 2026',
f'''
<p>Some Shopify carts now split into several shipments at checkout, each with its own list of rates. Some carts mix shipping with store pickup in one order. Rules that were written for a single list of rates can go wrong there. If a rule removes every rate from one shipment, the customer can't check out.</p>
<p>The <a href="https://youtu.be/KqUg7xFt4Hw" target="_blank" rel="noopener">one-minute video</a> shows the checkout. The rest of this page explains what happens and how to set your rules.</p>
<h2>Show only one rate</h2>
<p>Take a cart with a heavy mug that ships by Freight or White glove, and a box of filters that ships by Standard or Economy. A rule says "show only Standard".</p>
{fig('split-shipping-show-only', 1600, 900, 'A Shopify checkout with two shipments. Shipment one keeps Freight and White glove, shipment two shows only Standard', 'Recorded on a test store.')}
<p>Shipment two keeps Standard and drops Economy. Shipment one has no Standard rate, so it keeps its own rates and the customer can finish. Before November 2026 the app compared the rule with all the rates at once, and shipment one could have ended up with none.</p>
<h2>Reorder</h2>
<p>Positions are counted from 1 inside each shipment. Move Freight and Standard to position 1, and each leads the shipment it belongs to.</p>
{fig('split-shipping-reorder', 1600, 900, 'The same checkout with Freight first in shipment one and Standard first in shipment two', 'Freight leads one shipment and Standard leads the other.')}
<h2>Hide and rename</h2>
<p>These match by name in every shipment, as they always did. Take care with hide rules: if a shipment has one rate and your rule hides it, that shipment has nothing left. When you mean "only offer this one", use a show-only rule, which never empties a shipment.</p>
<h2>Ship and pickup in one order</h2>
<p>Where Shopify lets customers ship some items and collect others, each part has its own options. A show-only rule for a shipping rate limits the shipped items and leaves the pickup alone. To be sure a rule can never touch pickup, set its Apply to scope to shipping rates.</p>
<h2>After checkout</h2>
<p>If customers can <a href="/blog/shopify-customer-order-editing/">edit their own orders</a>, every package is held until the edit window ends, and then they are all released. The return window on the customer's order page waits for the last package. With one package sent, it tells the customer the window starts once the order arrives.</p>
<h2>Test yours</h2>
<ol>
  <li>Find two products that ship from different shipping profiles or locations.</li>
  <li>Put both in a cart and open the shipping step.</li>
  <li>Check that each shipment has at least one rate, with your rules on.</li>
</ol>
<p>Splitting carts and mixing shipping with pickup are Shopify features, and Shopify decides which stores have them. The rules work on every Shopify plan. Order editing is part of the Pro plan, and the return window block is part of the paid plans.</p>
''',
[('Why can a shipping rule block checkout?', 'If a rule removes every rate from one shipment, the customer has nothing to choose there and cannot finish. A show-only rule in Smart Checkout Widgets keeps a shipment\'s own rates when none of the named ones is offered.'),
 ('Do shipping rules apply to each shipment separately?', 'Show-only and reorder rules work inside each shipment. Hide and rename rules match by name in all of them.'),
 ('Can a shipping rule hide store pickup by mistake?', 'Set the rule\'s Apply to scope to shipping rates and it never touches pickup.'),
 ('Do I need Shopify Plus for this?', 'No. Shipping method rules work on every Shopify plan.')],
 [INSTALL, docs('split-shipping', 'Split shipment docs')])
