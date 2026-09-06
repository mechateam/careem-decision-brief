"""
Generate synthetic operational and funnel telemetry for Careem Food in Dubai.
Simulates multi-zone performance across peak dinner hours with realistic bottlenecks.
"""

import csv
import random
from datetime import datetime, timedelta

def generate_careem_food_data():
    zones = ["Downtown Dubai", "Dubai Marina", "Business Bay", "JLT", "Deira"]
    cuisines = ["Burgers & Fast Food", "Middle Eastern / Shawarma", "Healthy & Bowls", "Asian / Sushi", "Coffee & Desserts"]
    
    start_time = datetime(2026, 9, 4, 12, 0) # Friday lunch start (UAE weekend peak)
    hours = 36 # Friday 12:00 to Saturday 23:00
    
    rows = []
    
    for h in range(hours):
        current_dt = start_time + timedelta(hours=h)
        hour_of_day = current_dt.hour
        is_dinner_peak = 19 <= hour_of_day <= 22
        is_lunch_peak = 12 <= hour_of_day <= 14
        
        for zone in zones:
            for cuisine in cuisines:
                # Base session volume
                base_sessions = 1200 if is_dinner_peak else (750 if is_lunch_peak else 350)
                zone_mult = 1.4 if zone in ["Downtown Dubai", "Dubai Marina"] else (1.1 if zone == "Business Bay" else 0.85)
                
                sessions = int(base_sessions * zone_mult * random.uniform(0.92, 1.08))
                listing_views = int(sessions * random.uniform(0.88, 0.94))
                menu_views = int(listing_views * random.uniform(0.55, 0.65))
                
                # Baseline funnel conversion
                cart_add_rate = random.uniform(0.38, 0.44)
                checkout_rate = random.uniform(0.68, 0.76)
                order_complete_rate = random.uniform(0.82, 0.90)
                
                # Operational baseline
                kitchen_prep_min = random.uniform(18.0, 24.0)
                driver_gap_pct = random.uniform(4.0, 9.0)
                delivery_time_min = kitchen_prep_min + random.uniform(14.0, 18.0)
                
                # Commercial baseline
                avg_basket_aed = random.uniform(72.0, 94.0)
                promo_spend_per_order = random.uniform(6.0, 10.0)
                take_rate = random.uniform(16.5, 18.5)
                
                # INJECT CRITICAL ANOMALY: Friday Dinner Rush in Downtown Dubai (2026-09-04 19:00 - 21:00)
                # Severe kitchen bottleneck in Downtown fast food/shawarma + voucher code saturation
                if current_dt.strftime("%Y-%m-%d") == "2026-09-04" and zone == "Downtown Dubai" and 19 <= hour_of_day <= 21:
                    kitchen_prep_min = random.uniform(37.5, 43.0) # >37 min bottleneck
                    delivery_time_min = kitchen_prep_min + random.uniform(22.0, 28.0) # ETA jumps to 65+ min
                    driver_gap_pct = random.uniform(21.0, 29.0) # captain shortage
                    
                    # Cart abandonment triggers as ETA jumps to 60+ min
                    cart_add_rate = random.uniform(0.24, 0.28) # severe drop
                    checkout_rate = random.uniform(0.48, 0.54) # drop at checkout review
                    order_complete_rate = random.uniform(0.62, 0.68)
                    
                    # Heavy voucher burn on small orders
                    promo_spend_per_order = random.uniform(16.0, 22.0)
                    avg_basket_aed = random.uniform(48.0, 58.0) # lower basket value
                    take_rate = random.uniform(9.5, 12.0) # net margin collapse
                
                cart_adds = int(menu_views * cart_add_rate)
                checkout_starts = int(cart_adds * checkout_rate)
                orders_completed = int(checkout_starts * order_complete_rate)
                
                gmv_aed = round(orders_completed * avg_basket_aed, 2)
                promo_spend_aed = round(orders_completed * promo_spend_per_order, 2)
                
                rows.append({
                    "timestamp": current_dt.strftime("%Y-%m-%d %H:00"),
                    "zone": zone,
                    "cuisine_category": cuisine,
                    "sessions": sessions,
                    "listing_views": listing_views,
                    "menu_views": menu_views,
                    "cart_adds": cart_adds,
                    "checkout_starts": checkout_starts,
                    "orders_completed": orders_completed,
                    "gmv_aed": gmv_aed,
                    "avg_basket_size_aed": round(avg_basket_aed, 2),
                    "promo_spend_aed": promo_spend_aed,
                    "net_take_rate_pct": round(take_rate, 2),
                    "kitchen_prep_time_min": round(kitchen_prep_min, 1),
                    "avg_delivery_time_min": round(delivery_time_min, 1),
                    "driver_supply_gap_pct": round(driver_gap_pct, 1)
                })
                
    output_path = "documents/job-search/careem_ai_challenge/careem_food_dubai_hourly.csv"
    with open(output_path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
        
    print(f"Generated {len(rows)} records saved to {output_path}")

if __name__ == "__main__":
    generate_careem_food_data()
