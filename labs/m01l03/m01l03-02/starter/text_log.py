"""Logging as prose. Readable by one person, useless to a machine."""

ORDERS = [(1071, 31.86, "u4"), (1072, 74.63, "u1"), (1073, 8.5, "u4")]

for order, total, user in ORDERS:
    print(f"09:41:02 checkout: order {order} for user {user} "
          f"totalling {total} pounds was accepted")
