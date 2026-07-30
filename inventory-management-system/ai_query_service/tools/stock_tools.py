import sqlite3

DATABASE = "../backend/inventory.db"


def get_total_stock():
    """
    Return total quantity of all products in stock.
    """

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT SUM(quantity)
        FROM stocks
        """
    )

    result = cursor.fetchone()

    connection.close()

    total = result[0] if result[0] else 0

    return {
        "total_stock": total
    }


def get_product_stock(product_id: int):
    """
    Return stock of a product across all branches.
    """

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            branches.name,
            stocks.quantity
        FROM stocks
        JOIN branches
        ON stocks.branch_id = branches.id
        WHERE stocks.product_id = ?
        """,
        (product_id,)
    )

    results = cursor.fetchall()

    connection.close()

    return [
        {
            "branch": row[0],
            "quantity": row[1]
        }
        for row in results
    ]


def get_branch_stock(branch_id: int):
    """
    Return all products available in a branch.
    """

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            product_id,
            quantity
        FROM stocks
        WHERE branch_id = ?
        """,
        (branch_id,)
    )

    results = cursor.fetchall()

    connection.close()

    return [
        {
            "product_id": row[0],
            "quantity": row[1]
        }
        for row in results
    ]