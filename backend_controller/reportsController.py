from backend_model.reportsModel import *


def getReport(timeframe, start_date, end_date, product):
    if timeframe == 'Day':
        query = "SELECT orders.order_id, s_name, s_brand, day, cont.price, quantity," \
                "cost, image_link FROM orders JOIN cont JOIN stickers WHERE orders.order_id = cont.order_id AND " \
                "cont.sticker_id = stickers.sticker_id AND day = %s AND s_name = %s"
    else:
        query = "SELECT orders.order_id, s_name, s_brand, day, cont.price, quantity, cost, image_link " \
                "FROM orders JOIN cont JOIN stickers WHERE orders.order_id = cont.order_id AND cont.sticker_id = stickers.sticker_id " \
                "AND day BETWEEN %s AND %s AND s_name = %s"
    return getReportModel(timeframe, query, start_date, end_date, product)


def getNames():
    return getNamesModel()


def getDatedReport(start_date, end_date, frame):
    if frame == "day":
        query = """
        SELECT orders.order_id, orders.tracking_number, s_name, s_brand, day, cont.price, quantity, cost
        FROM orders
        JOIN cont ON orders.order_id = cont.order_id
        JOIN stickers ON cont.sticker_id = stickers.sticker_id
        WHERE day = %s ORDER BY order_id ASC;
        """
    else:
        query = "SELECT orders.order_id, orders.tracking_number, s_name, s_brand, day, cont.price, quantity, cost " \
                "FROM orders JOIN cont JOIN stickers WHERE orders.order_id = cont.order_id AND cont.sticker_id = stickers.sticker_id " \
                "AND day BETWEEN %s AND %s ORDER BY order_id ASC"

    return getDatedReportModel(start_date, end_date, frame, query)


def getStockReport():
    return getStockReportModel()

def getimagecontroller(product):
    query = """
        SELECT image_link
        FROM stickers
        WHERE s_name = %s;
        """
    return getimagemodel(query, product)