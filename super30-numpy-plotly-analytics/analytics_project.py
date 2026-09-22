"""NumPy + Plotly Data Analytics Project for an e-commerce company."""

from pathlib import Path

import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# ---------------------------------------------------------------------------
# DATA GENERATION
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).parent
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

months = np.array([
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
])

# Fictional monthly e-commerce data. All numeric series are NumPy arrays.
revenue = np.array([120000, 132000, 145000, 138000, 160000, 175000,
                    168000, 182000, 195000, 210000, 238000, 265000])
orders = np.array([1200, 1280, 1390, 1320, 1500, 1640,
                   1580, 1710, 1840, 1980, 2240, 2510])
customers = np.array([900, 950, 1010, 1080, 1160, 1240,
                      1320, 1410, 1510, 1630, 1790, 1980])
expenses = np.array([76000, 80000, 85000, 84000, 94000, 101000,
                     99000, 104000, 110000, 119000, 132000, 145000])


# ---------------------------------------------------------------------------
# NUMPY PROCESSING
# ---------------------------------------------------------------------------
profit = revenue - expenses
revenue_differences = np.diff(revenue)
customer_differences = np.diff(customers)
profit_margin = profit / revenue * 100

# ---------------------------------------------------------------------------
# ANALYSIS
# ---------------------------------------------------------------------------
total_annual_revenue = revenue.sum()
average_monthly_revenue = revenue.mean()
best_month_index = revenue.argmax()
lowest_month_index = revenue.argmin()
best_month = months[best_month_index]
lowest_month = months[lowest_month_index]
annual_expenses = expenses.sum()
annual_profit = profit.sum()
average_order_value = revenue / orders
customer_growth = customers[-1] - customers[0]
customer_growth_percent = customer_growth / customers[0] * 100

print("=" * 78)
print("NUMPY + PLOTLY E-COMMERCE ANALYTICS PROJECT")
print("=" * 78)
print("\nDATA GENERATION")
print(f"Months tracked: {len(months)}")
print(f"Revenue array: {revenue}")
print(f"Orders array: {orders}")
print(f"Customers array: {customers}")
print(f"Expenses array: {expenses}")

print("\nNUMPY PROCESSING")
print(f"Profit array: {profit}")
print(f"Month-to-month revenue differences: {revenue_differences}")
print(f"Profit margin (%): {np.round(profit_margin, 2)}")

print("\nANALYSIS")
print(f"Total annual revenue: Rs. {total_annual_revenue:,.2f}")
print(f"Average monthly revenue: Rs. {average_monthly_revenue:,.2f}")
print(f"Best-performing month: {best_month} (Rs. {revenue.max():,.2f})")
print(f"Lowest-performing month: {lowest_month} (Rs. {revenue.min():,.2f})")
print(f"Total annual expenses: Rs. {annual_expenses:,.2f}")
print(f"Total annual profit: Rs. {annual_profit:,.2f}")
print(f"Customer growth: {customer_growth:,} customers ({customer_growth_percent:.2f}%)")
print(f"Average order value in December: Rs. {average_order_value[-1]:,.2f}")

print("\nINSIGHTS")
insights = [
    f"Revenue grew from Rs. {revenue[0]:,.0f} in {months[0]} to Rs. {revenue[-1]:,.0f} in {months[-1]}, a {((revenue[-1] / revenue[0]) - 1) * 100:.1f}% increase.",
    f"{best_month} is the strongest month with Rs. {revenue.max():,.0f} revenue, while {lowest_month} is the weakest with Rs. {revenue.min():,.0f}.",
    f"The largest month-to-month revenue increase is Rs. {revenue_differences.max():,.0f}, occurring between {months[revenue_differences.argmax()]} and {months[revenue_differences.argmax() + 1]}.",
    f"Annual profit is Rs. {annual_profit:,.0f}, and December's profit margin is {profit_margin[-1]:.1f}%.",
    f"Customers increased by {customer_growth:,}, from {customers[0]:,} to {customers[-1]:,}, which is {customer_growth_percent:.1f}% growth.",
    f"December average order value is Rs. {average_order_value[-1]:,.0f}; revenue growth is therefore supported by both higher order volume and a larger customer base.",
]
for number, insight in enumerate(insights, start=1):
    print(f"{number}. {insight}")


# ---------------------------------------------------------------------------
# PLOTLY VISUALIZATION
# ---------------------------------------------------------------------------
def save_figure(figure, filename):
    path = OUTPUT_DIR / filename
    figure.write_html(path, include_plotlyjs="cdn")
    print(f"Created chart: {path.name}")


# 1. Revenue trend line chart
revenue_line = go.Figure(
    go.Scatter(
        x=months,
        y=revenue,
        mode="lines+markers",
        name="Revenue",
        line={"color": "#2563eb", "width": 3},
        hovertemplate="%{x}<br>Revenue: Rs. %{y:,.0f}<extra></extra>",
    )
)
revenue_line.update_layout(
    title="Monthly Revenue Trend",
    xaxis_title="Month",
    yaxis_title="Revenue (Rs.)",
)
save_figure(revenue_line, "01_revenue_trend.html")

# 2. Monthly orders bar chart
orders_bar = go.Figure(
    go.Bar(
        x=months,
        y=orders,
        name="Orders",
        marker_color="#059669",
        hovertemplate="%{x}<br>Orders: %{y:,}<extra></extra>",
    )
)
orders_bar.update_layout(
    title="Monthly Orders",
    xaxis_title="Month",
    yaxis_title="Number of Orders",
)
save_figure(orders_bar, "02_monthly_orders.html")

# 3. Revenue and expenses comparison
comparison = go.Figure()
comparison.add_trace(go.Scatter(x=months, y=revenue, mode="lines+markers", name="Revenue"))
comparison.add_trace(go.Scatter(x=months, y=expenses, mode="lines+markers", name="Expenses"))
comparison.update_layout(
    title="Monthly Revenue versus Expenses",
    xaxis_title="Month",
    yaxis_title="Amount (Rs.)",
    hovermode="x unified",
)
save_figure(comparison, "03_revenue_expenses.html")

# 4. Customer growth visualization
customer_chart = go.Figure(
    go.Bar(
        x=months,
        y=customers,
        name="Customers",
        marker_color="#7c3aed",
        hovertemplate="%{x}<br>Customers: %{y:,}<extra></extra>",
    )
)
customer_chart.add_trace(
    go.Scatter(
        x=months,
        y=customers,
        mode="lines+markers",
        name="Growth trend",
        line={"color": "#f97316", "width": 3},
    )
)
customer_chart.update_layout(
    title="Monthly Customer Growth",
    xaxis_title="Month",
    yaxis_title="Customers",
)
save_figure(customer_chart, "04_customer_growth.html")

# 5. Monthly profit visualization
profit_chart = go.Figure(
    go.Bar(
        x=months,
        y=profit,
        name="Profit",
        marker_color=np.where(profit >= 0, "#16a34a", "#dc2626"),
        hovertemplate="%{x}<br>Profit: Rs. %{y:,.0f}<extra></extra>",
    )
)
profit_chart.update_layout(
    title="Monthly Profit",
    xaxis_title="Month",
    yaxis_title="Profit (Rs.)",
)
save_figure(profit_chart, "05_monthly_profit.html")

# 6. Final management dashboard: four views in one figure
management_dashboard = make_subplots(
    rows=2,
    cols=2,
    subplot_titles=("Revenue and Expenses", "Orders", "Customers", "Profit"),
)
management_dashboard.add_trace(go.Scatter(x=months, y=revenue, mode="lines+markers", name="Revenue"), row=1, col=1)
management_dashboard.add_trace(go.Scatter(x=months, y=expenses, mode="lines+markers", name="Expenses"), row=1, col=1)
management_dashboard.add_trace(go.Bar(x=months, y=orders, name="Orders"), row=1, col=2)
management_dashboard.add_trace(go.Scatter(x=months, y=customers, mode="lines+markers", name="Customers"), row=2, col=1)
management_dashboard.add_trace(go.Bar(x=months, y=profit, name="Profit", marker_color="#16a34a"), row=2, col=2)
management_dashboard.update_xaxes(title_text="Month", row=1, col=1)
management_dashboard.update_xaxes(title_text="Month", row=1, col=2)
management_dashboard.update_xaxes(title_text="Month", row=2, col=1)
management_dashboard.update_xaxes(title_text="Month", row=2, col=2)
management_dashboard.update_yaxes(title_text="Amount (Rs.)", row=1, col=1)
management_dashboard.update_yaxes(title_text="Orders", row=1, col=2)
management_dashboard.update_yaxes(title_text="Customers", row=2, col=1)
management_dashboard.update_yaxes(title_text="Profit (Rs.)", row=2, col=2)
management_dashboard.update_layout(
    title="E-Commerce Management Performance Dashboard",
    height=800,
    hovermode="x unified",
    showlegend=True,
)
save_figure(management_dashboard, "06_management_dashboard.html")

print(f"\nCreated {len(list(OUTPUT_DIR.glob('*.html')))} interactive charts in {OUTPUT_DIR}")
