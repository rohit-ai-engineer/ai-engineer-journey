# Flexible EPG Validator - Week 1 Advanced Project
# Handles different XML structures with configurable rules

import xml.etree.ElementTree as ET
from datetime import datetime

print("=== Flexible EPG Validator ===")
print()

filename = "Exchange listings & Highlights, Virgin Media Four week 11.xml"

# Parse XML
tree = ET.parse(filename)
root = tree.getroot()

print(f"Validating {filename}...")
print(f"Root: {root.tag}")
print()

# Find all slots (programs)
slots = root.findall('.//slot')
print(f"Found {len(slots)} programs to validate")
print()

issues_found = 0
slot_num = 0

for slot in slots:
    slot_num += 1
    
    # Check 1: announcedTime (it's an ATTRIBUTE, not a tag)
    announced_time = slot.get('announcedTime')
    
    if not announced_time:
        print(f"❌ Slot {slot_num}: Missing announcedTime")
        issues_found += 1
    else:
        # Validate time format (HH:MM:SS.mmm)
        try:
            # Just check if it's parseable
            parts = announced_time.split(':')
            if len(parts) != 3:
                raise ValueError("Invalid format")
        except:
            print(f"❌ Slot {slot_num}: Invalid announcedTime format: {announced_time}")
            issues_found += 1
    
    # Check 2: Get date from the parent schedule element
    # We need to traverse UP to the schedule, not down
    parent_schedule = None
    for schedule in root.findall('.//schedule'):
        if slot in list(schedule):
            parent_schedule = schedule
            break

    if parent_schedule is not None:
        date = parent_schedule.get('date')
        if not date:
            print(f"⚠️  Slot {slot_num}: Missing date in schedule")
            issues_found += 1
    
    # Check 3: title (nested inside product, as an attribute)
    title_element = slot.find('.//title[@type="EPG Title"]')
    
    if title_element is None:
        print(f"❌ Slot {slot_num}: Missing EPG Title")
        issues_found += 1
    else:
        title_value = title_element.get('value')
        if not title_value or title_value.strip() == '':
            print(f"❌ Slot {slot_num}: Empty EPG Title")
            issues_found += 1

print()
print("--- Validation Complete ---")
print(f"Total programs checked: {slot_num}")
print(f"Total issues found: {issues_found}")

if issues_found == 0:
    print("✅ All EPG metadata looks good!")
else:
    print(f"🔍 Please fix {issues_found} issue(s)")