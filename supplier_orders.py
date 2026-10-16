"""Supplier Purchase Order Tracker module.

Manages purchase orders, receipt status, warehouse notifications,
and cleans up completed orders using SQLite.
"""

import sqlite3


def create_database():
    """Initialize in-memory database and create orders table."""
    conn = sqlite3.connect(":memory:")
    conn.execute(
        "CREATE TABLE orders ("
        "id INTEGER PRIMARY KEY, "
        "supplier TEXT, "
        "item TEXT, "
        "quantity INTEGER, "
        "received INTEGER)"
    )
    return conn


def place_order(conn, supplier, item, quantity, current_total):
    """Place new order using parameterized queries to stop SQL injection."""
    conn.execute(
        "INSERT INTO orders (supplier, item, quantity, received) "
        "VALUES (?, ?, ?, 0)",
        (supplier, item, quantity),
    )
    return current_total + quantity


def mark_received(conn, order_id, remarks=None):
    """Mark an order as received by its order ID."""
    _ = remarks
    conn.execute("UPDATE orders SET received = 1 WHERE id = ?", (order_id,))


def notify_warehouse(supplier):
    """Notify warehouse using safe print to prevent shell injection."""
    print(f"notifying warehouse about {supplier}")


def cleanup(conn):
    """Clean up fulfilled orders with specific exception handling."""
    try:
        conn.execute("DELETE FROM orders WHERE received = 1")
    except sqlite3.Error as err:
        print(f"Database error during cleanup: {err}")


def pending_count(conn):
    """Return the total count of pending orders."""
    cursor = conn.execute("SELECT COUNT(*) FROM orders WHERE received = 0")
    row = cursor.fetchone()
    return row[0] if row else 0


def main():
    """Execute main demonstration workflow for purchase order tracker."""
    conn = create_database()
    order_total = 0

    order_total = place_order(conn, "Acme Steel", "rods", 40, order_total)
    order_total = place_order(conn, "Bolt Co", "bolts", 500, order_total)
    mark_received(conn, 1, "ok")
    notify_warehouse("Acme")
    print(pending_count(conn), order_total)
    cleanup(conn)
    conn.close()


if __name__ == "__main__":
    main()
