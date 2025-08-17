TOOL_REGISTRY = {}

def tool(name):
    def deco(fn):
        TOOL_REGISTRY[name] = fn
        return fn
    return deco

@tool("get_merchant_status")
def get_merchant_status(merchant_id: str):
    return {"merchant_id": merchant_id, "prep_time_min": 40, "status": "overloaded"}

@tool("notify_customer")
def notify_customer(order_id: str, message: str, voucher_inr: int = 0):
    return {"order_id": order_id, "notified": True, "voucher_inr": voucher_inr}

@tool("re_route_driver")
def re_route_driver(order_id: str, driver_id: str):
    return {"order_id": order_id, "driver_id": driver_id, "assigned_temp_job": True}

@tool("contact_recipient_via_chat")
def contact_recipient_via_chat(package_id: str):
    return {"package_id": package_id, "recipient_replied": False}
@tool("check_traffic")
def check_traffic(route_id: str):
    return {"route_id": route_id, "status": "blocked", "delay_min": 25}

@tool("calculate_alternative_route")
def calculate_alternative_route(route_id: str):
    return {"route_id": route_id, "alt_route": "R2", "eta_min": 40}

@tool("notify_passenger_and_driver")
def notify_passenger_and_driver(passenger_id: str, driver_id: str, eta_min: int):
    return {"passenger_id": passenger_id, "driver_id": driver_id, "eta_min": eta_min, "notified": True}
