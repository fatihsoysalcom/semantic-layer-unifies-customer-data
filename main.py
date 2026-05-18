# Simulate data silos from different departments
sales_data = [
    {"customer_id": "C001", "product": "Laptop", "amount": 1200},
    {"customer_id": "C002", "product": "Mouse", "amount": 25},
    {"customer_id": "C001", "product": "Keyboard", "amount": 75},
    {"customer_id": "C003", "product": "Monitor", "amount": 300}
]

marketing_data = [
    {"email": "john.doe@example.com", "segment": "Tech Enthusiast", "customer_id_ref": "C001"},
    {"email": "jane.smith@example.com", "segment": "Casual User", "customer_id_ref": "C002"},
    {"email": "bob.johnson@example.com", "segment": "New Prospect", "customer_id_ref": "C003"}
]

# --- Problem: Without a semantic layer, AI models struggle with inconsistent data ---
# An AI model trying to understand 'customer value' would find it hard to link
# sales data (by customer_id) with marketing data (by email, with a ref to customer_id)
# and get a consistent view of a single customer.

# --- Semantic Layer Simulation ---
def build_semantic_customer_profile(sales_records, marketing_records):
    """
    Simulates a semantic layer by unifying customer data from different silos.
    It resolves different identifiers (customer_id, email) and creates a
    consistent 'customer profile' schema, providing meaning and context.
    """
    customer_profiles = {}

    # Process sales data: establish base customer profiles from sales
    for sale in sales_records:
        customer_id = sale["customer_id"]
        if customer_id not in customer_profiles:
            customer_profiles[customer_id] = {
                "unified_id": customer_id, # Consistent identifier across systems
                "sales_total": 0,
                "products_purchased": [],
                "email": None, # Placeholder for marketing info
                "marketing_segment": None,
            }
        customer_profiles[customer_id]["sales_total"] += sale["amount"]
        customer_profiles[customer_id]["products_purchased"].append(sale["product"])

    # Process marketing data: enrich existing profiles or create new ones
    for marketing_rec in marketing_records:
        customer_id_ref = marketing_rec["customer_id_ref"]
        if customer_id_ref in customer_profiles:
            # Link marketing data to an existing sales-based customer profile
            customer_profiles[customer_id_ref]["email"] = marketing_rec["email"]
            customer_profiles[customer_id_ref]["marketing_segment"] = marketing_rec["segment"]
        else:
            # If marketing data exists for a customer not in sales (e.g., new lead),
            # create a basic profile for them. This ensures comprehensive coverage.
            customer_profiles[customer_id_ref] = {
                "unified_id": customer_id_ref,
                "sales_total": 0,
                "products_purchased": [],
                "email": marketing_rec["email"],
                "marketing_segment": marketing_rec["segment"],
            }

    return list(customer_profiles.values())

# --- AI-like Function (now able to use the semantically unified data) ---
def analyze_customer_value(unified_customer_profiles):
    """
    An AI-like function that can now easily process unified customer data.
    It calculates a simple 'value score' based on sales and marketing segment,
    demonstrating how a semantic layer enables richer AI analysis.
    """
    print("--- AI-like Customer Value Analysis (using unified data) ---")
    for customer in unified_customer_profiles:
        score = customer["sales_total"] / 100 # Base score on sales amount
        if customer["marketing_segment"] == "Tech Enthusiast":
            score *= 1.5 # Tech enthusiasts might be more valuable
        elif customer["marketing_segment"] == "Casual User":
            score *= 0.8 # Casual users might be less valuable

        print(f"Customer {customer['unified_id']} (Email: {customer['email']}):")
        print(f"  Sales Total: ${customer['sales_total']}")
        print(f"  Segment: {customer['marketing_segment']}")
        print(f"  Calculated Value Score: {score:.2f}\n")

# --- Execution Flow ---
print("--- Raw Sales Data (Silo 1) ---")
for s in sales_data:
    print(s)
print("\n--- Raw Marketing Data (Silo 2) ---")
for m in marketing_data:
    print(m)
print("\n" + "="*60 + "\n")

# Apply the semantic layer to unify the data
unified_data = build_semantic_customer_profile(sales_data, marketing_data)
print("--- Unified Customer Profiles (Output of Semantic Layer) ---")
for customer in unified_data:
    print(customer)
print("\n" + "="*60 + "\n")

# Now the AI-like function can work effectively with consistent, meaningful data
analyze_customer_value(unified_data)
