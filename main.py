from dotenv import load_dotenv
load_dotenv()

import datetime
import random
from typing import Dict, Any

from swarm import Agent
from swarm.repl import run_demo_loop


orders = {
    "ORD001": {"status": "In Transit", "location": "New York"},
    "ORD002": {"status": "Delivered", "location": "Los Angeles"},
    "ORD003": {"status": "Processing", "location": "Chicago"},
    "ORD004": {"status": "Out for Delivery", "location": "Houston"},
    "ORD005": {"status": "Delayed", "location": "Miami"},
}

def get_order_status(order_id: str) -> str:
    """Get the status of an order based on the order ID.
    Takes as input arguments in the format '{"order_id":"ORD001"}'
    """
    if order_id in orders:
        return f"Order {order_id} status: {orders[order_id]['status']} - Current location: {orders[order_id]['location']}"
    else:
        return f"Order {order_id} not found."

def estimate_parcel_price(length: float, width: float, height: float, weight: float) -> str:
    """Estimate the price of a parcel based on its dimensions and weight.
    Takes as input arguments in the format '{"length":10,"width":5,"height":3,"weight":2}'
    """
    volume = length * width * height
    base_price = 5.00
    volume_factor = 0.001
    weight_factor = 0.5
    
    price = base_price + (volume * volume_factor) + (weight * weight_factor)
    return f"Estimated parcel price: ${price:.2f}"


order_status_agent = Agent(
    name="Order Status Agent",
    description="""You are an order status agent that handles all inquiries related to tracking orders.
    You must ask for the order ID to provide status information. Ask for the order_id in your message.""",
    functions=[get_order_status],
)

price_estimator_agent = Agent(
    name="Price Estimator Agent",
    description="""You are a price estimator agent that calculates shipping costs based on parcel dimensions and weight.
    You must ask for the length, width, height (all in cm), and weight (in kg) of the parcel to estimate the price.
    Ask for all four parameters (length, width, height, weight) in one message.""",
    functions=[estimate_parcel_price],
)

triage_agent = Agent(
    name="Triage Agent",
    instructions="""You are to triage a user's request and transfer to the right agent.
    If the user request is about tracking an order or getting order status, transfer to the Order Status Agent.
    If the user request is about estimating shipping costs or parcel pricing, transfer to the Price Estimator Agent.
    When you need more information to triage the request to an agent, ask a direct question without explaining why you're asking it.
    Do not share your thought process with the user! Do not make unreasonable assumptions on behalf of the user.""",

)

def transfer_back_to_triage():
    """Call this function if a user is asking about a topic that is not handled by the current agent."""
    return triage_agent


def transfer_to_order():
    return order_status_agent


def transfer_to_price():
    return price_estimator_agent

triage_agent.functions = [transfer_to_order, transfer_to_price]
order_status_agent.functions.append(transfer_back_to_triage)
price_estimator_agent.functions.append(transfer_back_to_triage)



if __name__ == "__main__":
    run_demo_loop(triage_agent, debug=False)