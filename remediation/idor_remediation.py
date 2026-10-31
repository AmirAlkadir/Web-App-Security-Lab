
# IDOR Remediation Demonstration

# Simulated database of shopping baskets
baskets = {
    6: {"owner": 25, "items": ["Banana Juice"]},
    7: {"owner": 26, "items": ["Apple Juice"]}
}

# Account 1 is currently authenticated
current_user = 25


# Vulnerable: checks basket ID but not ownership
def vulnerable_basket_access(basket_id):
    return baskets.get(basket_id, "Basket not found")


# Secure: verifies the user owns the basket
def secure_basket_access(basket_id, user_id):
    basket = baskets.get(basket_id)

    if basket is None:
        return "Basket not found"

    if basket["owner"] != user_id:
        return "403 Forbidden: Access denied"

    return basket


# Account 1 attempts to access Account 2's basket
target_basket = 7

print("=== IDOR Remediation Test ===")

print("\nVulnerable implementation:")
print(vulnerable_basket_access(target_basket))

print("\nSecure implementation:")
print(secure_basket_access(target_basket, current_user))


# Verify legitimate access still works
print("\nAuthorized access test:")
print(secure_basket_access(6, current_user))
