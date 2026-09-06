# EXECUTIVE DECISION BRIEF: CAREEM FOOD (DOWNTOWN DUBAI)
**Incident Window:** 2026-09-04 19:00 - 22:00 (Peak Dinner Rush)
**Owner:** Growth & Product Lead, Careem Food UAE

---

### 1. Executive Summary
During the Friday dinner peak in Downtown Dubai, completed orders dropped 93.3% below baseline despite healthy user traffic (Sessions: 25,136.0, +-80.2%). The end-to-end conversion rate collapsed from 13.7% to 4.62%, representing an estimated lost GMV of AED 1,342,177.92. This underperformance was triggered by a compound failure: merchant kitchen prep delays cascaded into inflated customer ETAs (64.9 mins), triggering acute cart abandonment, while aggressive promo discounts cannibalized margin without defending conversion.

---

### 2. Root Cause Attribution
The conversion breakdown isolates across three interconnected friction points:

1. **Merchant Kitchen Congestion Triggered Cart Abandonment:**
   Average kitchen prep time spiked from 20.9 mins to 40.5 mins (+19.6 mins, +93.8%). As delivery ETAs crossed the psychological 60-minute threshold to 64.9 mins, menu-to-cart conversion fell from 40.66% to 25.51% (-15.15 pts) and cart-to-checkout plummeted by 20.2 pts.
2. **Captain Shortage Exacerbated Batch Inefficiencies:**
   The driver supply gap widened to 25.2% (+18.8 pts). Captains spent excessive idle time waiting at high-density merchant clusters in Downtown, reducing effective fleet throughput and inflating order-to-dispatch latency.
3. **Voucher Cannibalization Collapsed Net Unit Economics:**
   Promo spend surged to 36.15% of GMV (vs 9.64% baseline), while Average Basket Size fell 36.8% from AED 82.56 to AED 52.19. Unrestricted flat vouchers incentivized small, low-margin orders that choked kitchen queues while compressing net take rate from 17.56% to 10.84%.

---

### 3. Prioritized Business Actions

#### Action 1: Operational Dispatch & Kitchen Throttling (Immediate: 24-48h)
- **Mechanism:** Implement dynamic delivery radius throttling for merchants whose rolling 30-minute prep time exceeds 30 minutes. Compress discovery radius from 7 km to 3.5 km during peak congestion.
- **Captain Re-allocation:** Reposition standby Captains from peripheral Business Bay zones into Downtown pickup hubs via targeted AED 4 surge incentives per completed drop-off.
- **Accountable:** City Operations & Logistics Lead.

#### Action 2: Commercial Voucher Guardrail Recalibration (Commercial: Next Cycle)
- **Mechanism:** Restructure peak-hour promo vouchers from flat AED discounts to tiered minimum spend requirements (Minimum Order Value raised from AED 40 to AED 75).
- **Margin Defense:** Cap platform co-funded discounts during 19:00 - 22:00 peak to prevent unprofitable basket dilution, restoring net take rate above 16.0%.
- **Accountable:** Commercial Growth Lead.

#### Action 3: In-App ETA Transparency & Scheduled Orders Experiment (Product: Sprint 1)
- **A/B Experiment:** Deploy a 'Fastest Delivery' smart filter badge and a Kitchen Congestion Banner on restaurant cards showing real-time prep times.
- **Demand Smoothing:** Introduce an inline nudge offering 50 Careem Plus reward points for users opting to schedule delivery +30 minutes post-peak, shifting 12-15% of demand off the 20:00 spike.
- **Accountable:** Product Manager (Careem Food Experience).

---

### 4. Guardrail Metrics & Target Recovery
- **Target Funnel Recovery:** Restore Menu-to-Cart conversion to >= 38.0% and End-to-End CVR to >= 13.7%.
- **Operational SLA:** Compress Downtown peak kitchen prep time below 25.0 mins; limit Captain wait time to < 7.0 mins.
- **Financial Guardrail:** Maintain Net Take Rate >= 16.5% and Contribution Margin positive across all voucher-driven orders.
