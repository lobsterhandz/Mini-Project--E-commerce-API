# validation.py
import re

# Function to validate email format
def validate_email(email):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        raise ValueError('Invalid email format')

# Function to validate phone number format
def validate_phone_number(phone_number):
    if not re.match(r"^\+?[1-9]\d{1,14}$", phone_number):  # E.164 format
        raise ValueError('Invalid phone number format')

# Function to validate required fields are present in the data
def validate_required_fields(data, fields):
    missing_fields = [field for field in fields if field not in data]
    if missing_fields:
        raise ValueError(f"Missing required fields: {', '.join(missing_fields)}")

# Function to validate that a value is a positive float
def validate_positive_float(value, field_name):
    if not isinstance(value, (int, float)) or value < 0:
        raise ValueError(f"{field_name} must be a positive number")

# Function to validate non-negative integer for fields like stock level
def validate_non_negative_integer(value, field_name):
    if not isinstance(value, int) or value < 0:
        raise ValueError(f"{field_name} must be a non-negative integer")