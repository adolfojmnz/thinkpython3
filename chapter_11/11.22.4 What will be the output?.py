this = ["I", "am", "not", "a", "crook"]
that = ["I", "am", "not", "a", "crook"]

print(f"Test 1: {that is this}")    # Return False.
# This return False. Dispite of what I'd thought, Python do not assing them the same object reference,
# even when their strings are the sames. Maybe because their are list and so mutable data.

print(that == this)     # Return True.
# If the is is replace for "==" the result is True, it may be because the equal operator evaluates if the objects
# has the same values.

that = this
# Both, values and objects are being assign to another object, 
# that makes them the same in all posible ways.

print(f"Test 2: {this is that}")    # Return True. 
