"""2027 app comparisons, figures read from each Shopify App Store listing on 2026-11-25."""
import re
from posts_lib import *
D='November 25, 2026'
def bars(title,rows,cap,mx=None):
    mx=mx or max(v for _,v,*_ in rows)
    r=''.join(f'  <div class="post-bars__row{" is-us" if n=="Smart Checkout Widgets" else ""}"><span>{n}</span><div class="post-bars__bar"><i style="--v:{v/mx:.3f}"></i>{t}</div></div>\n' for n,v,t in rows)
    return f'<figure class="post-bars">\n  <p class="post-bars__title">{title}</p>\n{r}  <figcaption>{cap}</figcaption>\n</figure>'
def table(head,rows):
    return '<div class="table-wrap"><table>\n<thead><tr>'+''.join(f'<th>{h}</th>' for h in head)+'</tr></thead>\n<tbody>\n'+'\n'.join('<tr>'+''.join(f'<td>{c}</td>' for c in r)+'</tr>' for r in rows)+'\n</tbody></table></div>'
A=lambda h,n:f'<a href="https://apps.shopify.com/{h}" target="_blank" rel="noopener noreferrer">{n}</a>'
US=A('smart-checkout-widgets','Smart Checkout Widgets')
DIS=f'<p class="disclosure">We make Smart Checkout Widgets, one of the apps here. Prices and features come from each app\'s Shopify App Store listing on {D}. "Not listed" means the listing doesn\'t mention it, and the app may still do it. Check each listing before you buy.</p>'
L=lambda items:'<ul>\n'+'\n'.join(f'<li>{x}</li>' for x in items)+'\n</ul>'
SRC=lambda hs:'<h2>Sources</h2>\n<ul class="source-list">\n'+'\n'.join(f'<li>{A(h,n)}, Shopify App Store, {D}</li>' for h,n in hs)+'\n</ul>'

# 1 ------------------------------------------------------------------ delivery
post('best-shopify-delivery-date-apps-2027','Best Shopify delivery date apps for 2027, compared',
 'Zapiet, Pickeasy, Stellar, DingDoong, Buunto and Smart Checkout Widgets compared on price, time slots, order limits, pickup locations and checkout rules, from their App Store listings.',
 'Wrapped parcels and a bouquet under a wall planner','Six delivery date and pickup apps, what each one offers, and which shop each suits.',7,'best-shopify-delivery-date-apps-2027','Wrapped parcels and a bouquet on a bench under a wall planner with coloured stickers',
f'''
<p><strong>Short answer:</strong> choose Smart Checkout Widgets when customers pick a day and a time window and you want payment and shipping rules, order editing and Thank you page blocks in the same app. Choose Zapiet for many locations with POS, and Pickeasy or Stellar for order limits per slot.</p>
{DIS}
<h2>The six apps side by side</h2>
{table(['App','Customers choose','Pickup locations','Paid plans from'],[
[US,'A day and a time slot, required at checkout if you want','All your Shopify locations','$29'],
[A('click-and-collect','Zapiet'),'A day and a time slot','1 to 100 by plan','$49.99'],
[A('order-delivery-date-time','Pickeasy'),'A day and a time slot','1 to 20 by plan, more at $59.99','$9.99'],
[A('order-delivery-date-by-identixweb','Stellar'),'A day and a time slot','3, or unlimited at $29.99','$14.99'],
[A('delivery-date-omega','DingDoong'),'A day and a time slot','2 to 20 by plan','$6.99'],
[A('buunto-date-picker','Buunto'),'A day and a time slot',"Up to Shopify&#39;s limit",'$12.99'],
])}
<p>Smart Checkout Widgets puts the calendar next to payment and shipping rules, a survey, customer account blocks and, on Pro, order editing, in one app.</p>
<h2>Which one fits</h2>
<h3>Zapiet: many locations and POS</h3>
<p>It lists date and time slots, delivery zones and fees by postcode or distance, order limits, POS, and sending orders to DoorDash, Uber Direct or Stuart. Product preparation time and date restrictions start at $79.99, and a checkout widget is on the $179.99 plan.</p>
<h3>Pickeasy: capacity on a small budget</h3>
<p>Time slots with order limits, postcode validation and blackout dates are on the free plan for up to 10 orders. $9.99 adds preparation time per product and day-by-day cutoffs. The checkout page widget is an Enterprise feature at $59.99.</p>
<h3>Stellar: unlimited orders for $14.99</h3>
<p>One flat price for three locations, with slots, order limits, blackout dates and calendars on the product page, cart and, for Shopify Plus, checkout. Custom shipping at checkout is $20 a month extra on Plus.</p>
<h3>DingDoong and Buunto: bakeries and florists starting out</h3>
<p>DingDoong starts at $6.99 for 100 orders and can add a surcharge for weekend or peak-hour delivery. Buunto sets different schedules per product or collection, and adds surcharges and a postcode checker from $19.99.</p>
<h3>Smart Checkout Widgets: a date plus the rest of checkout</h3>
<p>Our calendar covers days, time windows, lead times, cutoffs, weekdays and closed dates, set separately for shipping, local delivery and pickup. Checkout can refuse an order without a date or time, on every Shopify plan.</p>
{fig('delivery-time-windows','A product page for a dahlia bouquet with Delivery, Wednesday December 2 and two time windows above Add to cart','Our calendar with time windows on a Basic plan test store.')}
{video('BSDABRPDLUI','delivery-date-video','Shopify delivery date picker: let customers choose the day','Our calendar in 46 seconds.')}
<p>The $29 plan also includes payment and shipping rules, Thank you page blocks, a post-purchase survey and customer account blocks, for stores up to 1,000 orders a month. The setup is in our <a href="/blog/shopify-delivery-date-picker/">delivery date guide</a>.</p>
<h2>Five questions before you choose</h2>
<ol class="post-steps">
<li>Do customers need an hour, or is the day enough?</li>
<li>Do you have to cap orders per day?</li>
<li>Do some products need more notice than others?</li>
<li>How many pickup locations do you have, and do their hours differ?</li>
<li>What should happen when a customer uses Buy it now or an express button without a date? Test that in any app.</li>
</ol>
{SRC([('click-and-collect','Zapiet'),('order-delivery-date-time','Pickeasy'),('order-delivery-date-by-identixweb','Stellar'),('delivery-date-omega','DingDoong'),('buunto-date-picker','Buunto')])}
''',
[('What is the best Shopify delivery date app?','It depends on what you schedule. Smart Checkout Widgets suits stores that need a day and a time window and want checkout rules, order editing and a survey in the same app. Zapiet suits many locations with POS, and Pickeasy and Stellar cover order limits per slot.'),
('Which delivery date apps have a free plan?','Pickeasy (10 orders a month), Buunto (10), DingDoong (20) and Stellar (up to 50 orders) list one. Zapiet and Smart Checkout Widgets have a trial for this feature.'),
('Do I need Shopify Plus for a delivery date picker?','No. Calendars on the product page and cart work on every plan. Showing a calendar on the checkout page itself needs Plus.'),
('Can a delivery date be required at checkout?','In Smart Checkout Widgets, yes, on every Shopify plan. Check how any other app enforces it.')],
[INSTALL,docs('delivery-dates','Delivery dates docs')])

# 2 ------------------------------------------------------------------ order editing
post('best-shopify-order-editing-apps-2027','Best Shopify order editing apps for 2027, compared',
 'OrderEditing.com, AE, Cleverific, Revize, ClickPost and Smart Checkout Widgets: what customers can change after checkout, what each app charges, and which store each suits.',
 'Hands swapping a t-shirt in an open parcel','Six apps that let customers fix their own orders, with the price as you grow and the edits each one allows.',7,'best-shopify-order-editing-apps-2027','Hands swapping a folded t-shirt inside an open parcel on a packing table',
f'''
<p><strong>Short answer:</strong> choose Smart Checkout Widgets for the everyday fixes (address, size, quantity, contact details, cancellations) at a flat $99 with unlimited orders, and the rest of your checkout tools included. Choose Revize, AE, ClickPost, Cleverific or OrderEditing.com to sell extra products inside the edit.</p>
{DIS}
<h2>The six apps side by side</h2>
{table(['App','Customers can','Priced by','Paid plans from'],[
[US,'Change address, email, phone or note, swap a variant, lower a quantity, cancel','Flat','$99, unlimited orders'],
[A('order-editing','OrderEditing.com'),'Change address, products, shipping method or discount code, cancel','Orders','$99'],
[A('account-editor','AE'),'Change address, items, variants, quantity and shipping, cancel','Orders','$39'],
[A('edit-order','Cleverific'),'Change address, items, quantity, size and color, cancel','Orders','$59'],
[A('revize','Revize'),'Change address, quantity and variant, cancel. Swaps and add-ons at $149','Features','$49'],
[A('clickpost-order-edit-cancel','ClickPost'),'Change address and variants, add or replace items, cancel','Orders','$49'],
])}
<p>All six list address changes, item changes and cancellations, inside a time limit you set.</p>
{bars('Monthly price at 10,000 orders',[('OrderEditing.com',399,'$399'),('Cleverific',399,'$399'),('AE',179,'$179'),('ClickPost',129,'$129'),('Smart Checkout Widgets',99,'$99'),('Revize',49,'$49')],'Cleverific lists $399 for 7,501 to 15,000 orders. Ours stays at $99 because Pro has unlimited orders.')}
<h2>Which one fits</h2>
<h3>Revize: lowest flat price</h3>
<p>Free for 20 edits a month, then $49 for unlimited edits of address, quantity and variant. Product swaps, add-ons and upsells start at $149. It lists 20+ languages and 100+ integrations.</p>
<h3>AE: small stores that want everything</h3>
<p>$39 covers up to 1,200 orders with every feature: adding products, recalculated tax and shipping, returns and exchanges, store credit and Shopify Flow.</p>
<h3>ClickPost: a free start</h3>
<p>Up to 500 orders a month it's free to install with 25 edits, then $1 an edit. $49 removes the edit limit up to 5,000 orders.</p>
<h3>Cleverific: warehouse and ERP links</h3>
<p>Self-serve edits, upsells with A/B testing and ERP links such as NetSuite and ShipStation. The price follows your order volume, from $59 up to 1,000 orders.</p>
<h3>OrderEditing.com: many integrations</h3>
<p>It lists shipping method and discount code changes, address checks and 100+ integrations with warehouse, fraud and subscription apps. It starts at $99.</p>
<h3>Smart Checkout Widgets: no new payments</h3>
<p>Customers can change the address, email, phone or note, swap to a same-price variant, lower a quantity or cancel, for 15 minutes to 24 hours. Orders can be held from fulfillment until the window closes, and a Shopify Flow trigger tells your team.</p>
{fig('app-order-editing-settings','Order editing settings with shipping address, quantity, swap, email and phone, and order note ticked','What you can switch on, from our settings page.')}
<p>The same $99 covers payment and shipping rules, a delivery date calendar, gifts and upsells in checkout on Plus, a survey and customer account blocks.</p>
{fig('split-shipping-holds','A Shopify order with two packages, each on hold until the edit window ends','Each package is held until the edit window ends.')}
<h2>Work out your own number</h2>
<ol class="post-steps">
<li>Count last month's "please change my order" emails.</li>
<li>Sort them: address, size, quantity, cancel, add a product.</li>
<li>Pay for what your customers ask for.</li>
<li>Compare the plan for your orders in your busiest month.</li>
</ol>
<p>Our <a href="/blog/shopify-order-editing-app-pricing/">order editing pricing guide</a> covers more apps and volumes.</p>
{SRC([('order-editing','OrderEditing.com'),('account-editor','AE'),('edit-order','Cleverific'),('revize','Revize'),('clickpost-order-edit-cancel','ClickPost')])}
''',
[('What is the best order editing app for Shopify?','For adding products and charging the difference, Revize, AE, ClickPost, Cleverific and OrderEditing.com all list it. For address, size and cancellation fixes at a flat price with checkout rules included, Smart Checkout Widgets.'),
('Is there a free order editing app?','Revize lists a free plan with 20 edits a month, and ClickPost is free to install up to 500 orders with 25 edits.'),
('Does Shopify let customers edit orders by itself?','Customers can ask for a cancellation or a removal where the store allows it. Changing an address, size or quantity themselves needs an app.'),
('Do order editing apps need Shopify Plus?','No. Smart Checkout Widgets needs Basic or higher, because it runs on the Thank you and Order status pages. Check the others\' listings for your plan.')],
[INSTALL,docs('order-editing','Order editing docs')])

# 3 ------------------------------------------------------------------ upsells
post('best-shopify-checkout-upsell-apps-2027','Best Shopify checkout upsell apps for 2027, compared',
 'Upsell.com, Aftersell, Zipify OCU, UpsellPlus, Checkout Plus and Smart Checkout Widgets: where each shows offers, how it charges, and which store it suits.',
 'A second product placed next to a wrapped purchase','Six upsell apps, where their offers appear, and what it costs to put one on the checkout page.',7,'best-shopify-checkout-upsell-apps-2027','Hands placing a tube of hand cream beside a wrapped soap on a shop counter',
f'''
<p><strong>Short answer:</strong> choose Smart Checkout Widgets for checkout offers that follow rules you write, next to free gifts, a progress bar and payment rules, with no share of your upsell revenue. Choose Upsell.com, Aftersell, Zipify or UpsellPlus for one-click funnels after payment. Any upsell on the checkout page needs Shopify Plus, whichever app you pick.</p>
{DIS}
<h2>The six apps side by side</h2>
{table(['App','Where offers show','Priced by'],[
[US,'Checkout (Plus), Thank you, Order status, customer accounts','Store orders, no share of revenue'],
[A('reconvert-upsell-cross-sell','Upsell.com'),'Product page, cart, checkout (Plus), post-purchase, Thank you','Orders or upsell revenue'],
[A('aftersell','Aftersell'),'Cart, checkout (Plus), post-purchase, Thank you','Plan'],
[A('zipify-oneclickupsell','Zipify OCU'),'Product page, cart, checkout (Plus), post-purchase, Thank you','Upsell revenue'],
[A('upsellpluscheckout','UpsellPlus'),'Product page, cart, checkout (Plus), post-purchase, Thank you, POS','Upsell revenue'],
[A('checkoutplus','Checkout Plus'),'Checkout (Plus), post-purchase','Plan'],
])}
{bars('Cheapest plan that lists checkout-page upsells',[('UpsellPlus',119,'$119'),('Checkout Plus',99,'$99'),('Aftersell',34.99,'$34.99'),('Zipify OCU',9.95,'$9.95'),('Upsell.com',0.5,'Free to 50 orders'),('Smart Checkout Widgets',0.5,'Free to 100 orders')],'Zipify rises with upsell revenue. Upsell.com is $9.99 to $39.99 from 51 to 500 orders. Ours is $29 from 101 to 1,000 store orders. All of these also need a Shopify Plus store.')}
<h2>Which one fits</h2>
<h3>Upsell.com (formerly ReConvert): the whole path</h3>
<p>Offers on the product page, cart, checkout and Thank you page, plus one-click funnels after payment. Free up to 50 orders or $50 of upsell revenue, then $9.99 to $39.99 as you go from 51 to 500 orders.</p>
<h3>Aftersell: post-purchase funnels and cart</h3>
<p>$34.99 covers one-click post-purchase, checkout and Thank you offers. The cart builder is a separate $59.99 plan, or $79.99 for both.</p>
<h3>Zipify OCU: pay on results</h3>
<p>Starts at $9.95 while upsell revenue is under $200 a month, moves in steps to $99 at $2,500, and continues from $149 up to a $999 ceiling.</p>
<h3>UpsellPlus: 12 places including POS</h3>
<p>$49 covers cart, product and post-purchase offers up to $500 of revenue. Checkout upsells and checkout blocks are on Pro at $119.</p>
<h3>Checkout Plus: checkout blocks first</h3>
<p>$19 covers Thank you pages, rules and post-purchase upsells. Checkout upsells, gifts at checkout and branding are on Advanced at $99, for Plus stores.</p>
<h3>Smart Checkout Widgets: upsells as rules</h3>
<p>You write rules such as "the cart has a snowboard, offer wax at €4 off". Rules match products, collections, tags or cart total, can stop the list, and import from a CSV. The app can suggest rules from your own orders.</p>
{fig('app-upsell-rules','The upsell rules editor: when the cart has any of these products, recommend another, with a discount amount','A rule in our editor, on a test store.')}
<p>You pay one price by order count, with no share of upsell revenue, and get the gifts, progress bar, rules and survey in the same app. <a href="/blog/shopify-checkout-upsell-rules/">How upsell rules work</a>.</p>
<h2>Not on Shopify Plus?</h2>
<p>Skip checkout-page offers. Compare cart, product page, post-purchase and Thank you offers, since those work without Plus. A free-gift rule or a <a href="/blog/shopify-free-gift-cart-page/">gift on the cart page</a> can do a similar job.</p>
{SRC([('reconvert-upsell-cross-sell','Upsell.com'),('aftersell','Aftersell'),('zipify-oneclickupsell','Zipify OCU'),('upsellpluscheckout','UpsellPlus'),('checkoutplus','Checkout Plus')])}
''',
[('Can I add upsells to Shopify checkout without Plus?','Not on the checkout page. Shopify only opens it to apps on Plus. Cart, product page, post-purchase and Thank you page offers work on other plans.'),
('What is the difference between checkout and post-purchase upsells?','A checkout upsell is added before payment, so it is part of the order. A post-purchase upsell appears after payment and is charged with one click.'),
('Which upsell app takes no share of revenue?','Aftersell and Checkout Plus list plan prices, and Smart Checkout Widgets charges by store orders. Zipify, UpsellPlus and Upsell.com price by upsell revenue, orders or both.'),
('Where does Smart Checkout Widgets show upsells?','On the checkout page for Shopify Plus stores, and on the Thank you, Order status and customer account pages on Basic and up.')],
[INSTALL,docs('upsells','Upsell docs')])

# 4 ------------------------------------------------------------------ surveys
post('best-shopify-post-purchase-survey-apps-2027','Best Shopify post-purchase survey apps for 2027, compared',
 'Zigpoll, Grapevine, Fairing, SEA, KNO and Smart Checkout Widgets compared on price, questions, response limits, revenue reporting and rewards for answering.',
 'A customer answering on a phone beside an opened parcel','Six ways to ask "how did you hear about us?", what each costs at 800 orders a month, and when one question is enough.',6,'best-shopify-post-purchase-survey-apps-2027','A person at a kitchen table using a phone next to a freshly opened parcel',
f'''
<p><strong>Short answer:</strong> choose Smart Checkout Widgets to ask one clear question, see the revenue behind each answer and reward shoppers with a one-use code, on the same plan as your checkout rules. Choose Fairing or Zigpoll for a research program across channels, and Grapevine for unlimited responses at one price.</p>
{DIS}
<h2>The six apps side by side</h2>
{table(['App','Questions','Response or order limit','Where','Paid plans from'],[
[US,'One focused question, reward code optional','By store orders: free to 100','Thank you page','$29'],
[A('zigpoll','Zigpoll'),'Unlimited surveys','50 free, 200 at $39','Thank you, order status, on site, email, SMS, POS','$39'],
[A('grapevine','Grapevine'),'Several survey types','Unlimited responses','Thank you, on site, email, POS','$25'],
[A('fairing','Fairing'),'Unlimited','By orders: free to 200','Thank you, order status','$49'],
[A('sea-survey','SEA'),'Surveys and quizzes','30 free, 500 at $19','Thank you, email, on site, exit intent','$19'],
[A('knocommerce','KNO'),'3 at $19, 999 at $119','Unlimited responses','Post-purchase, survey links','$19'],
])}
{bars('Monthly price at 800 orders and 200 responses',[('Fairing',99,'$99'),('Zigpoll',39,'$39'),('Smart Checkout Widgets',29,'$29'),('Grapevine',25,'$25'),('SEA',19,'$19'),('KNO',19,'$19')],'Listed plan that covers it. Fairing prices by orders (501 to 1,000). Zigpoll and SEA price by responses. KNO at $19 is one survey with three questions.')}
<h2>Which one fits</h2>
<h3>Zigpoll: surveys everywhere</h3>
<p>Post-purchase, exit intent, email, SMS and POS, with NPS and CSAT, AI themes and syncs to Klaviyo and Google Sheets. Free for 50 responses, $39 for 200 and $129 for 600.</p>
<h3>Grapevine: one price</h3>
<p>$25 for unlimited responses, with targeting by order value, product, country and customer type, and data sent to Flow, Klaviyo and GA4.</p>
<h3>Fairing: attribution for growing brands</h3>
<p>Free up to 200 orders, then by order volume: $49, $99 at 1,000 and $149 at 5,000. It reports revenue, order value and lifetime value by channel and lists 35+ integrations.</p>
<h3>SEA: surveys plus quizzes</h3>
<p>$19 for 500 responses including a product recommendation quiz. Unlimited responses and A/B testing are on $49.</p>
<h3>KNO: research teams</h3>
<p>Templates, benchmarking and audiences. The $19 plan is one survey with three questions, and the larger plans are $119 and $299.</p>
<h3>Smart Checkout Widgets: one question, done well</h3>
<p>One question on the Thank you page, up to 20 answers in random order, and an optional "something else". Results shows each answer with the revenue behind it. You can reply with a one-use discount code, and see how many codes were used.</p>
{fig('app-survey-results','Survey results with answers, share and revenue, and the discount codes given and used','Results from a test store: answers, revenue, and reward codes used.')}
<p>It is on every plan including the free one, and it works from Shopify Basic up.</p>
<h2>Is one question enough?</h2>
<p>Often, if the question is "what led you to purchase today?" and the decision is where to spend next month. One question takes a few seconds to answer. Our <a href="/blog/shopify-how-did-you-hear-about-us-survey/">guide to the question</a> has wording you can copy.</p>
{SRC([('zigpoll','Zigpoll'),('grapevine','Grapevine'),('fairing','Fairing'),('sea-survey','SEA'),('knocommerce','KNO')])}
''',
[('What is the best post-purchase survey app for Shopify?','Fairing and Zigpoll cover the most ground, Grapevine has unlimited responses at $25, and Smart Checkout Widgets adds revenue per answer and reward codes to the rest of your checkout tools.'),
('Which post-purchase survey apps are free?','Fairing up to 200 orders, Zigpoll up to 50 responses, SEA up to 30 responses, and Smart Checkout Widgets up to 100 orders a month.'),
('Can I give a discount for answering a survey?','Smart Checkout Widgets does, with a one-use code on every plan. The other listings we read don\'t describe a one-use code as a reward, so ask them.'),
('Does a post-purchase survey need Shopify Plus?','No. Surveys on the Thank you page work without Plus. Ours needs Shopify Basic or higher.')],
[INSTALL,docs('survey','Survey docs')])

# 5 ------------------------------------------------------------------ rules
post('best-shopify-payment-shipping-rule-apps-2027','Best apps to hide payment and shipping methods on Shopify in 2027',
 'HidePay, HideShip, Payfy, Kip, PayRules, Blockify and Smart Checkout Widgets compared on price, conditions and limits for hiding, renaming and sorting checkout methods.',
 'A courier taking cash at the door','Seven apps that hide, rename and sort methods at checkout, with prices, conditions and rule limits.',7,'best-shopify-payment-shipping-rule-apps-2027','A courier at a doorway taking banknotes from a customer who also holds a card',
f'''
<p><strong>Short answer:</strong> choose Smart Checkout Widgets for payment and shipping rules in one app, free up to 100 orders a month, with the Thank you page, gifts and order editing alongside. Choose Kip, HidePay, Payfy or PayRules for payment rules on their own, and Blockify for rules plus order validation.</p>
{DIS}
<h2>The seven apps side by side</h2>
{table(['App','Payment rules','Shipping rules','Rule limit','Plans'],[
[US,'Yes','Yes','No limit by plan','Free to 100 orders, $29, $59, $99'],
[A('hidepay','HidePay'),'Yes','HideShip, or a bundle','Not listed on paid plans','$3.99, $5.99, $7.99'],
[A('hideship-hide-shipping-methods','HideShip'),'HidePay, or a bundle','Yes','Not listed','$3.99, $5.99, $7.99'],
[A('payfy-conditional-payments','Payfy'),'Yes','Not listed','2 at $3.99, 25 at $5.99','$3.99, $5.99, $7.99'],
[A('kip-customize-payment-methods','Kip'),'Yes','Not listed','1 hide rule free, unlimited at $3','$3'],
[A('payrules-conditional-payment-methods','PayRules'),'Yes','Not listed','5, 10 or 25','$4.99, $9.99, $19.99'],
[A('blockify-checkout-rules','Blockify'),'Yes','Yes','1 synced rule at $9.99, unlimited at $29.99','$9.99, $29.99, $79.99 for Plus'],
])}
<h2>Which one fits</h2>
<h3>HidePay and HideShip: a pair</h3>
<p>One for payments, one for shipping. Rules with several conditions start at $5.99. HidePay lists hiding express buttons, and HideShip lists importing postcodes by CSV and creating shipping rates.</p>
<h3>Payfy and PayRules: payment rules only</h3>
<p>Payfy lists hiding COD for PO boxes and postcodes, B2B conditions and metafields on $7.99. PayRules counts active rules: 5, 10 or 25.</p>
<h3>Kip: $3</h3>
<p>Unlimited rules to hide, rename and sort payment methods, and hiding express checkout buttons. One hide rule is free.</p>
<h3>Blockify: rules and validation</h3>
<p>Adds checkout validation, order limits, COD fees and discounts. It suits stores that also need to stop certain orders.</p>
<h3>Smart Checkout Widgets: both, with no limit by plan</h3>
<p>Hide, rename and reorder payment and shipping methods, or show only the shipping rates you name. Conditions include cart total, product tag, collection, customer tag, country, postcode ranges, weekday and date. Rules work inside each shipment when Shopify splits a cart.</p>
{fig('app-payment-rule','A payment rule that shows bank deposit, cash on delivery and PayPal only to customers tagged VIP','A rule on a test store: these methods only for customers tagged VIP.')}
{fig('split-shipping-show-only-2','Checkout before and after a show-only shipping rule across two shipments','A show-only rule across two shipments never leaves one empty.')}
<h2>Test any of them in five minutes</h2>
<ol class="post-steps">
<li>Write the rule and note exactly which method name it matches.</li>
<li>Check out as a guest with an address that should trigger it.</li>
<li>Check out with one that shouldn't.</li>
<li>Try express buttons and a cart that splits into two shipments.</li>
</ol>
<p>Our guides: <a href="/blog/hide-cash-on-delivery-shopify-checkout/">hiding Cash on Delivery</a>, <a href="/blog/hide-rename-reorder-shipping-methods-shopify-checkout/">shipping methods</a> and <a href="/blog/shopify-split-shipping-rate-rules/">split shipments</a>.</p>
{SRC([('hidepay','HidePay'),('hideship-hide-shipping-methods','HideShip'),('payfy-conditional-payments','Payfy'),('kip-customize-payment-methods','Kip'),('payrules-conditional-payment-methods','PayRules'),('blockify-checkout-rules','Blockify')])}
''',
[('Do I need Shopify Plus to hide payment methods?','No. Apps that use Shopify Functions hide, rename and sort payment and shipping methods on every Shopify plan.'),
('Is there a free app to hide Cash on Delivery?','Smart Checkout Widgets is free up to 100 orders a month with no rule limit by plan, and Kip lists one hide rule free.'),
('Can one app handle both payment and shipping rules?','Blockify and Smart Checkout Widgets list both in one app. HidePay and HideShip are two apps with a bundle price.'),
('Can an app hide the Pick up option?','No. Shopify lets apps hide single pickup locations, but not the Pick up method itself.')],
[INSTALL,docs('payment-rules','Payment rule docs')])
