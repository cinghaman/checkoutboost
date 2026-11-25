"""The three guides published 2026-11-25 (rebuilt the same day on the wide article template)."""
from posts_lib import *

post('shopify-delivery-date-picker',
 'Shopify delivery date picker: let customers choose a date on the product page or in the cart',
 'Shopify shows delivery estimates but has no calendar for customers. Here is how to add one on any Shopify plan, set lead times and cutoffs, and decide whether checkout should require a date.',
 'A florist hands over a bouquet at the front door',
 'Shopify can estimate when an order will arrive. If your customers need to pick the day themselves, you need a calendar, and it works on any plan.',
 5, 'delivery-date-cover', 'A florist hands a wrapped bouquet of peonies to a customer at the front door',
f'''
<p>Flowers, cakes and sofas all need someone at home on the right day. Shopify has no calendar for that, so the day usually ends up in the order note or in an email the next morning.</p>
<p>Smart Checkout Widgets adds one to your product pages, cart page and cart drawer. The calendar lives in your theme, and the part that runs in checkout uses Shopify's validation rules, which are open to every plan.</p>
{video('BSDABRPDLUI', 'delivery-date-video', 'Shopify delivery date picker: let customers choose the day', 'The whole flow in 46 seconds, from product page to checkout.')}
{fig('delivery-date-calendar-2', 'A product page for a peony bouquet with a delivery date calendar above Add to cart. Mondays and Sundays are crossed out', 'A florist on a Basic plan test store. Mondays and Sundays are closed for delivery.')}
{note('Plans', 'It works on every Shopify plan, Basic included. In the app it is part of Growth, Advanced and Pro.')}
<h2>What the customer does</h2>
<p>They choose how they want the order (shipping, local delivery or pickup, whichever you offer) and then a day. The choice follows them from the product page to the cart drawer and the cart page, and they can change it in any of them.</p>
{fig('delivery-date-steps', 'Three screens: choosing Delivery, picking a day in December, and the same date shown in the cart drawer', 'Delivery, then a day, then the same date above Check out.')}
<p>You see the method and the date on the order in Shopify admin, under Additional details. Orders placed with Buy it now carry them on the product line instead, because that button skips the cart. After the purchase, the date can show on the Thank you and Order status pages.</p>
<h2>What you decide</h2>
<div class="table-wrap"><table>
    <thead><tr><th>Setting</th><th>What it does</th></tr></thead>
    <tbody>
      <tr><td>Lead time</td><td>How many days ahead the first date is. 0 allows the same day.</td></tr>
      <tr><td>Cutoff time</td><td>After this time, one more day is added. It uses your store's time zone, wherever the customer is.</td></tr>
      <tr><td>Days of the week</td><td>Which days you deliver or open for pickup.</td></tr>
      <tr><td>Closed dates</td><td>Holidays and days you are fully booked.</td></tr>
      <tr><td>How far ahead</td><td>The last day a customer can book.</td></tr>
    </tbody>
</table></div>
<p>Lead time, cutoff and days of the week are set separately for shipping, local delivery and pickup, so a shop can offer pickup tomorrow and delivery in two days.</p>
{fig('delivery-date-ship-pickup', 'App settings side by side. Delivery has a lead time of 2 days, a 14:00 cutoff and Tuesday to Saturday. Pickup has 1 day, 16:00 and Monday to Saturday', 'The settings behind the calendar above.')}
<h2>Add it to your theme</h2>
<ol class="post-steps">
  <li>Open Delivery Dates in the app, switch the calendar on and save.</li>
  <li>Click Switch on in theme, then save the theme.</li>
  <li>Add the Delivery date block to the Thank you and Order status pages in the checkout editor.</li>
</ol>
<p>The calendar finds your Check out and Add to cart buttons and goes above them. We tried it on 22 theme demo stores on desktop and phone, including Dawn, Horizon, Prestige, Impulse, Warehouse, Turbo and Empire.</p>
<p>If it lands in the wrong place, enter a class name or ID from your theme in the app embed settings and choose before, after or inside it. Headless storefronts won't work, since they have no theme to put it in.</p>
<h2>Should checkout require a date?</h2>
<p>You can leave the date optional or let checkout refuse an order without one. With the check on, checkout also refuses a date that has passed, and a delivery date on an order the customer switches to pickup.</p>
{fig('delivery-date-checkout', 'Shopify checkout with the message: Please choose a delivery date on the product or cart page before checking out', 'Checkout on the Basic plan test store, with the check on and no date chosen.')}
<p>Before you turn it on:</p>
<ul>
  <li>Every order with a physical product will need a date, including draft orders, checkout links and other online sales channels. Point of sale is not checked.</li>
  <li>Keep the calendar on your product pages, because Buy it now skips the cart.</li>
  <li>If you offer Shop Pay, Apple Pay, Google Pay or PayPal, try each button once after you switch it on. Shopify's validation rules apply to express checkouts as well.</li>
</ul>
<p>If your paid plan ends, the calendar and the check switch off together, so a missing calendar can't leave customers stuck at checkout.</p>
{note("Shopify's own estimates", "Delivery estimates don't know which date the customer chose. In our test the customer picked 27 November while the rate at checkout said 1 to 3 December. To hide those dates, go to Settings, then Shipping and delivery, and set Delivery estimates to Off. Your rates may still show a transit time.")}
<h2>More than one pickup location</h2>
<p>The calendar asks for pickup and a day. Customers choose the location itself at checkout, where Shopify lists the ones you have switched on for pickup. Set pickup days that suit all of them.</p>
<h2>For florists and bakeries</h2>
<p>One date covers the whole cart. If you sell flowers or cakes, the <a href="/blog/shopify-delivery-pickup-dates-florists-bakeries/">florist and bakery guide</a> has worked examples.</p>
''',
[('Does Shopify have a built-in delivery date picker?', "No. Shopify can show estimated delivery dates, but customers can't choose a day without an app."),
 ('Does a delivery date picker work without Shopify Plus?', "Yes. The calendar runs in your theme and the checkout check is a Shopify validation rule, so both work on every Shopify plan. The feature is part of the app's Growth, Advanced and Pro plans."),
 ('Where do I see the date?', 'On the order in Shopify admin, under Additional details. For Buy it now orders it is on the product line.'),
 ('Can I require a date before checkout?', 'Yes. It is off by default. When you switch it on, checkout refuses orders with a physical product that have no valid date.'),
 ('Can customers choose a pickup location?', 'Yes, at checkout, from the locations you have switched on for pickup in Shopify.'),
 ('Which themes does it work with?', 'We tried 22 theme demo stores, including Dawn and Horizon. If it lands in the wrong place, you can point it at a class name or ID in your theme. Headless storefronts are not supported.')],
 [INSTALL, docs('delivery-dates', 'Delivery dates docs')])

post('shopify-delivery-pickup-dates-florists-bakeries',
 'Delivery and pickup dates for florists and bakeries on Shopify: cutoffs, lead times and closed days',
 'How to set up a delivery and pickup calendar for a flower shop or bakery on Shopify, with cutoff times, lead days per method, closed dates and the questions to answer first.',
 'Wrapped bouquets and cake boxes on a workroom bench',
 'A bouquet for Friday is worth nothing on Saturday. Here are two shops, one with flowers and one with cakes, and the settings that fit each.',
 5, 'florist-bakery-cover', 'Five wrapped bouquets in buckets next to two white cake boxes on a workroom bench',
f'''
<p>For a florist or a bakery the date is part of the product, and a Shopify checkout doesn't ask for it. This guide sets up a calendar with the <a href="/blog/shopify-delivery-date-picker/">delivery date picker</a> in Smart Checkout Widgets. It works on every Shopify plan and is part of the app's paid plans.</p>
{video('BSDABRPDLUI', 'delivery-date-video', 'Shopify delivery date picker: let customers choose the day', 'The whole flow in 46 seconds, from product page to checkout.')}
<h2>Answer these first</h2>
<ul>
  <li>How long does an order take to make? That is your lead time, and it may differ for pickup and delivery.</li>
  <li>When do you stop taking orders for the next day?</li>
  <li>Which days do you deliver, and which days can people collect?</li>
  <li>Which dates are you closed or already full?</li>
</ul>
<h2>A flower shop</h2>
<p>Say a shop makes bouquets the day before, delivers Tuesday to Saturday and is open for pickup Monday to Saturday.</p>
{pair(fig('florist-delivery-van', 'Wrapped bouquets in buckets in the back of a delivery van', 'Delivery: two days ahead, order by 14:00.'), fig('bakery-cake-box', 'A baker lowers a raspberry cake into a white box', 'Cakes need more notice than bread.'))}
<div class="table-wrap"><table>
    <thead><tr><th>Setting</th><th>Delivery</th><th>Pickup</th></tr></thead>
    <tbody>
      <tr><td>Lead time</td><td>2 days</td><td>1 day</td></tr>
      <tr><td>Cutoff time</td><td>14:00</td><td>16:00</td></tr>
      <tr><td>Days of the week</td><td>Tue to Sat</td><td>Mon to Sat</td></tr>
    </tbody>
</table></div>
{fig('delivery-date-ship-pickup', 'The same settings in the app, with Delivery on the left and Pickup on the right', 'The same numbers in the app.')}
<p>A customer ordering on Wednesday at 13:00 can have delivery on Friday. At 15:00 the cutoff has passed, so the first delivery day becomes Saturday. Pickup on Thursday is still open until 16:00. The times are the shop's, so a customer abroad sees the same days.</p>
{fig('delivery-date-steps', 'The customer picks Delivery, then Friday December 11, and sees the same date in the cart drawer', 'What the customer sees. Closed days and days that are too soon are crossed out.')}
<h2>A bakery</h2>
<p>Bread can be ready tomorrow and a celebration cake needs four days. The lead time applies to the whole store, so there are two ways to handle that:</p>
<ul>
  <li>Set the lead time for the slowest product. Simple, and bread customers wait longer than they need to.</li>
  <li>Set it for the fastest product and say on the cake's page that it needs four days. You then check cake orders by hand.</li>
</ul>
<p>The first way is safer if cakes are most of what you sell.</p>
<h2>Two or more shops</h2>
<p>Customers choose pickup and a day in the calendar, then pick the shop at checkout from the locations you have switched on for pickup in Shopify. Set pickup days that suit all your shops.</p>
<h2>Holidays and busy days</h2>
<p>Add closed dates for public holidays and for days you can't take any more orders. A range works too, so one entry covers a week off. Close a day as soon as it is full.</p>
<p>For Valentine's Day or Mother's Day, close the days before and after if you only deliver on the day itself.</p>
<h2>Require the date</h2>
<p>Switch on Require a date before checkout if an order without a date is useless to you. Checkout then also stops a customer who picks a delivery date and later chooses pickup. Leave it off if you take orders through draft orders or checkout links, since those are checked as well. Try your express buttons, such as Shop Pay, once after you switch it on.</p>
{fig('delivery-date-checkout', 'Checkout asking the customer to choose a delivery date first', 'An order without a date, refused at checkout.')}
<p>The calendar doesn't change your shipping setup. Local delivery areas, pickup locations and their prices still come from Shopify. If some postcodes can't have delivery, a <a href="/blog/shopify-shipping-rates-by-postcode/">shipping rule by postcode</a> handles that.</p>
<h2>In the workroom</h2>
<p>Each order shows its method and date under Additional details in Shopify admin. Add the Delivery date block to the Thank you and Order status pages too, so customers can check the day themselves.</p>
''',
[('Can I set different cutoff times for delivery and pickup?', 'Yes. Lead time, the cutoff and the days of the week are set separately for shipping, local delivery and pickup.'),
 ('Can I close days when I am fully booked?', 'Yes. Add a date or a range to your closed dates.'),
 ('Can customers collect from different shops?', 'Yes. They choose the shop at checkout, from the locations you have switched on for pickup.'),
 ('Which time zone is the cutoff in?', "Your store's time zone, for every customer.")],
 [INSTALL, docs('delivery-dates', 'Delivery dates docs')])

SPLIT = 'https://help.shopify.com/en/manual/checkout-settings/split-shipping'
MIXED = 'https://help.shopify.com/en/manual/checkout-settings/ship-and-pickup'
OPEN = 'https://changelog.shopify.com/posts/split-shipping-in-checkout-is-available-to-all-merchants'
post('shopify-split-shipping-rate-rules',
 'Shopify split shipping: make your shipping rules work in every shipment',
 'Split shipping is on every Shopify plan; ship and pickup in one order is Plus only. Here is the difference, and how to set shipping rules that leave a rate in every shipment.',
 'Two parcels being packed on a bench, one with a mug and one with coffee filters',
 'When one cart ships in two packages, each package has its own rates. A rule that empties one of them stops the whole order.',
 5, 'split-shipping-cover', 'Two parcels on a packing bench, one with a stoneware mug and one with paper coffee filters',
f'''
<p>A customer buys a mug and a box of coffee filters. The mug ships by Freight or White glove, the filters by Economy or Standard, and checkout shows two shipments with a choice for each. If your shipping rule removes every option from one of them, the customer can't check out.</p>
{video('KqUg7xFt4Hw', 'split-shipping-video', 'Shopify split shipping and ship and pickup: make your rate rules work', 'One minute: show-only, reorder, ship and pickup, holds and the return window.')}
<h2>Split shipping or ship and pickup?</h2>
<p>Shopify has two features that put several deliveries in one order, and they are on different plans.</p>
<div class="table-wrap"><table>
    <thead><tr><th></th><th>Split shipping</th><th>Ship and pickup in one order</th></tr></thead>
    <tbody>
      <tr><td>What it does</td><td>Shows several shipments, each with its own rates</td><td>Ships some items while the customer collects others</td></tr>
      <tr><td>Shopify plan</td><td>Every plan, Basic included</td><td>Plus and Enterprise</td></tr>
      <tr><td>Where to find it</td><td>Settings, Shipping and delivery, if you have more than one shipping profile or location</td><td>Settings, Feature test drives. Shopify turns it on for all eligible Plus stores on July 1, 2027</td></tr>
      <tr><td>Our shipping rules</td><td>Work inside each shipment</td><td>Limit the shipped items, leave the pickup alone</td></tr>
    </tbody>
</table></div>
<p>Shopify opened split shipping <a href="{OPEN}" target="_blank" rel="noopener">to all merchants in August 2024</a>. Its help pages cover <a href="{SPLIT}" target="_blank" rel="noopener">split shipping</a> and <a href="{MIXED}" target="_blank" rel="noopener">ship and pickup</a>. Stores that have moved to shipping options by market have split shipping on already, and the setting no longer applies to them.</p>
{note('Not seeing two shipments?', "With local delivery switched on, Shopify doesn't show several shipments at checkout. It also won't split a single line: five of the same shirt have to ship from one location.")}
<h2>Show only one rate</h2>
<p>Back to the mug and the filters, with a rule that says show only Standard.</p>
{fig('split-shipping-show-only-2', 'Shopify checkout before and after a show-only rule. Shipment 1 keeps Freight and White glove, shipment 2 shows only Standard', 'Recorded on a test store.')}
<p>Shipment 2 keeps Standard and drops Economy. Shipment 1 has no Standard rate, so it keeps its own two and the customer can finish.</p>
<h2>Reorder</h2>
<p>Positions are counted from 1 inside each shipment. Move Freight and Standard to position 1, and each leads the shipment it belongs to.</p>
{fig('split-shipping-reorder-2', 'Shopify checkout before and after a reorder rule. Standard moves above Economy in shipment 2', 'Shipment 1 already had Freight first. In shipment 2, Standard moves above Economy.')}
<h2>Hide and rename</h2>
<p>These match by name in every shipment. Take care with hide rules: if a shipment has one rate and your rule hides it, that shipment has nothing left. To offer only one rate, use a show-only rule, which never empties a shipment.</p>
<h2>Ship and pickup in one order</h2>
<p>On Plus stores with the feature on, each part of the order has its own options. A show-only rule for a shipping rate limits the shipped items and leaves the pickup alone. To be sure a rule can never touch pickup, set its Apply to scope to shipping rates.</p>
{fig('split-shipping-pickup', 'Checkout with one item for pickup in store and another shipped to an address', 'A Plus test store: one snowboard collected in store, the other shipped.')}
<h2>After checkout</h2>
<p>If customers can <a href="/blog/shopify-customer-order-editing/">edit their own orders</a>, every package is held until the edit window ends, and then they are all released.</p>
{fig('split-shipping-holds', 'A Shopify order with two fulfillments, each on hold until the edit window ends', 'Two packages, two holds, one release time.')}
<p>The return window on the customer's order page waits for the last package. With one package sent, it says the window starts once the order arrives.</p>
{fig('split-shipping-returns', 'Order page with the message: You will have 30 days to return items once your order arrives', 'One package sent, one to go.')}
<h2>Test yours</h2>
<ol class="post-steps">
  <li>Find two products that ship from different shipping profiles or locations.</li>
  <li>Put both in a cart and open the shipping step.</li>
  <li>Check that each shipment has at least one rate, with your rules on.</li>
</ol>
<p>In the app, order editing is part of the Pro plan and the return window block is part of the paid plans.</p>
''',
[('Is split shipping available on Shopify Basic?', "Yes. Shopify made split shipping in checkout available to all merchants in August 2024. You need more than one shipping profile or location to use it."),
 ('Is ship and pickup in one order available on Shopify Basic?', 'No. Shopify offers it on the Plus and Enterprise plans, as a feature test drive until July 1, 2027.'),
 ('Why can a shipping rule block checkout?', 'If a rule removes every rate from one shipment, the customer has nothing to choose there and cannot finish. A show-only rule in Smart Checkout Widgets keeps a shipment\'s own rates when none of the named ones is offered.'),
 ('Do shipping rules apply to each shipment separately?', 'Show-only and reorder rules work inside each shipment. Hide and rename rules match by name in all of them.'),
 ('Can a shipping rule hide store pickup by mistake?', 'Set the rule\'s Apply to scope to shipping rates and it never touches pickup.'),
 ('Do I need Shopify Plus for the rules?', 'No. Shipping method rules work on every Shopify plan.')],
 [INSTALL, docs('split-shipping', 'Split shipment docs')])
