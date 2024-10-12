# Logistics Company Multi-Agent System
## Overview
This project implements a multi-agent system for a logistics company using the Swarm framework. The system is designed to handle customer inquiries about order tracking and parcel price estimation. It consists of three main agents that work together to provide a seamless customer service experience.
Agents

`Order Status Agent`: Handles all inquiries related to tracking orders. It can provide the current status and location of an order based on the order ID.

`Price Estimator Agent`: Calculates shipping costs based on parcel dimensions (length, width, height) and weight. It provides estimated prices for shipping parcels.

`Triage Agent`: Acts as the first point of contact for all user inquiries. It analyzes the user's request and directs it to the appropriate specialized agent (either Order Status or Price Estimator).

## Features

`Order Tracking`: Users can inquire about the status of their orders using order IDs.

`Price Estimation`: Users can get shipping cost estimates by providing parcel dimensions and weight.

`Intelligent Triaging`: The system automatically directs user queries to the most appropriate agent.
