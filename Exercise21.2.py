guests = ["Dipika", "Sanchita", "Ankita", "Anushka", "Bhakti"]
rsvp_status = {}
def collect_rsvp():
    print("=== EVENT REGISTRATION MANAGER ===")
    for guest in guests:
        while True:
            response = input(
                f"Will {guest} attend the event? (Yes/No): "
            ).strip().lower()
            if response in ["yes", "no"]:
                rsvp_status[guest] = response.capitalize()
                break
            else:
                print("Invalid input! Enter Yes or No.")
def display_summary():
    expected = 0
    print("\n--- RSVP SUMMARY ---")
    for guest, status in rsvp_status.items():
        print(f"{guest}: {status}")
        if status == "Yes":
            expected += 1
    print("\nTotal invited guests:", len(guests))
    print("Expected attendees:", expected)
    print("Not attending:", len(guests) - expected)
def main():
    collect_rsvp()
    display_summary()
main()
