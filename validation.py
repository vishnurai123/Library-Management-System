"""Input validation utilities."""
import re

def required(value, field):
    value = str(value).strip()
    if not value:
        raise ValueError(f"{field} cannot be empty.")
    return value

def positive_int(value, field):
    try:
        n = int(value)
    except (TypeError, ValueError):
        raise ValueError(f"{field} must be a positive integer.")
    if n <= 0:
        raise ValueError(f"{field} must be a positive integer.")
    return n

def email(value):
    value = required(value, "Email")
    if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", value):
        raise ValueError("Enter a valid email address.")
    return value
