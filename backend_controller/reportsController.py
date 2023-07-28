from backend_model.reportsModel import *


def getReport(timeframe, start_date, end_date, product):
    if timeframe == 'Day':
        query = "SELECT orders.order_id, s_name, s_brand, day, cont.price, quantity," \
                "cost FROM orders JOIN cont JOIN stickers WHERE orders.order_id = cont.order_id AND " \
                "cont.sticker_id = stickers.sticker_id AND day = %s AND s_name = %s"
    else:
        query = "SELECT orders.order_id, s_name, s_brand, day, cont.price, quantity, cost " \
                "FROM orders JOIN cont JOIN stickers WHERE orders.order_id = cont.order_id AND cont.sticker_id = stickers.sticker_id " \
                "AND day BETWEEN %s AND %s AND s_name = %s"
    return getReportModel(timeframe, query, start_date, end_date, product)


def getNames():
    return getNamesModel()


def getDatedReport():
    return getDatedReportModel()


def getStockReport():
    return getStockReportModel()
