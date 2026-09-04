import csv


def read_tickets(filename):
    """Read tickets from a CSV file and return a list of dictionaries."""
    tickets = []
    with open(filename, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["resolution_time"] = int(row["resolution_time"])
            tickets.append(row)
    return tickets


def count_by_field(tickets, field):
    """Count how many tickets fall into each value of a given field."""
    counts = {}
    for ticket in tickets:
        value = ticket[field]
        counts[value] = counts.get(value, 0) + 1
    return counts


def filter_by_field(tickets, field, value):
    """Return tickets whose field equals the given value."""
    result = []
    for ticket in tickets:
        if ticket[field] == value:
            result.append(ticket)
    return result


def average_resolution_time(tickets):
    """Return the average resolution time across all tickets."""
    if not tickets:
        return 0
    total = 0
    for ticket in tickets:
        total += ticket["resolution_time"]
    return total / len(tickets)


def average_resolution_time_per_category(tickets):
    """Return a dict of category -> average resolution time."""
    totals = {}
    counts = {}
    for ticket in tickets:
        category = ticket["category"]
        totals[category] = totals.get(category, 0) + ticket["resolution_time"]
        counts[category] = counts.get(category, 0) + 1

    averages = {}
    for category in totals:
        averages[category] = totals[category] / counts[category]
    return averages


def tickets_per_agent(tickets):
    """Return a dict of agent -> number of tickets handled."""
    return count_by_field(tickets, "assigned_agent")


def sort_by_resolution_time(tickets):
    """Return tickets sorted by resolution_time (ascending)."""
    return sorted(tickets, key=lambda t: t["resolution_time"])


def tickets_with_max_resolution_time(tickets):
    """Return the ticket(s) with the highest resolution time."""
    max_time = 0
    for ticket in tickets:
        if ticket["resolution_time"] > max_time:
            max_time = ticket["resolution_time"]

    result = []
    for ticket in tickets:
        if ticket["resolution_time"] == max_time:
            result.append(ticket)
    return result


def print_counts(title, counts):
    print(f"\n{title}")
    for key, value in counts.items():
        print(f"  {key}: {value}")


def export_summary_report(filename, tickets):
    """Write a plain-text summary report covering all required stats."""
    total = len(tickets)
    by_category = count_by_field(tickets, "category")
    by_priority = count_by_field(tickets, "priority")
    by_status = count_by_field(tickets, "status")
    open_tickets = filter_by_field(tickets, "status", "Open")
    critical_tickets = filter_by_field(tickets, "priority", "Critical")
    resolved_tickets = filter_by_field(tickets, "status", "Resolved")
    avg_time = average_resolution_time(tickets)
    avg_time_per_category = average_resolution_time_per_category(tickets)
    by_agent = tickets_per_agent(tickets)
    max_time_tickets = tickets_with_max_resolution_time(tickets)

    with open(filename, "w", encoding="utf-8") as f:
        f.write("SUPPORT TICKET SUMMARY REPORT\n")
        f.write("=" * 40 + "\n\n")

        f.write(f"Total tickets: {total}\n\n")

        f.write("Tickets by category:\n")
        for key, value in by_category.items():
            f.write(f"  {key}: {value}\n")

        f.write("\nTickets by priority:\n")
        for key, value in by_priority.items():
            f.write(f"  {key}: {value}\n")

        f.write("\nTickets by status:\n")
        for key, value in by_status.items():
            f.write(f"  {key}: {value}\n")

        f.write(f"\nOpen tickets: {len(open_tickets)}\n")
        f.write(f"Critical tickets: {len(critical_tickets)}\n")
        f.write(f"Resolved tickets: {len(resolved_tickets)}\n")

        f.write(f"\nAverage resolution time (all tickets): {avg_time:.2f} hours\n")

        f.write("\nAverage resolution time per category:\n")
        for key, value in avg_time_per_category.items():
            f.write(f"  {key}: {value:.2f} hours\n")

        f.write("\nTickets handled per agent:\n")
        for key, value in by_agent.items():
            f.write(f"  {key}: {value}\n")

        f.write(f"\nMaximum resolution time: {max_time_tickets[0]['resolution_time']} hours\n")
        f.write("Ticket(s) with maximum resolution time:\n")
        for ticket in max_time_tickets:
            f.write(f"  {ticket['ticket_id']} - {ticket['customer_name']} "
                     f"({ticket['category']}, {ticket['resolution_time']} hours)\n")

    print(f"\nSummary report exported to {filename}")


def main():
    tickets = read_tickets("tickets.csv")

    total = len(tickets)
    print(f"Total tickets: {total}")

    print_counts("Tickets by category:", count_by_field(tickets, "category"))
    print_counts("Tickets by priority:", count_by_field(tickets, "priority"))
    print_counts("Tickets by status:", count_by_field(tickets, "status"))

    open_tickets = filter_by_field(tickets, "status", "Open")
    critical_tickets = filter_by_field(tickets, "priority", "Critical")
    resolved_tickets = filter_by_field(tickets, "status", "Resolved")

    print(f"\nOpen tickets: {len(open_tickets)}")
    print(f"Critical tickets: {len(critical_tickets)}")
    print(f"Resolved tickets: {len(resolved_tickets)}")

    avg_time = average_resolution_time(tickets)
    print(f"\nAverage resolution time (all tickets): {avg_time:.2f} hours")

    print_counts("Average resolution time per category (hours):",
                 {k: round(v, 2) for k, v in average_resolution_time_per_category(tickets).items()})

    print_counts("Tickets handled per agent:", tickets_per_agent(tickets))

    sorted_tickets = sort_by_resolution_time(tickets)
    print("\nTickets sorted by resolution time (first 5 shown):")
    for ticket in sorted_tickets[:5]:
        print(f"  {ticket['ticket_id']}: {ticket['resolution_time']} hours")

    max_time_tickets = tickets_with_max_resolution_time(tickets)
    print(f"\nMaximum resolution time: {max_time_tickets[0]['resolution_time']} hours")
    print("Ticket(s) with maximum resolution time:")
    for ticket in max_time_tickets:
        print(f"  {ticket['ticket_id']} - {ticket['customer_name']} "
              f"({ticket['category']}, {ticket['resolution_time']} hours)")

    export_summary_report("summary_report.txt", tickets)


if __name__ == "__main__":
    main()
