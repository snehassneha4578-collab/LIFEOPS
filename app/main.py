from app.orchestrator import orchestrate

if __name__ == "__main__":
    print("LIFEOPS is online.")
    print("=" * 60)

    request = input("What should LIFEOPS handle? ").strip()

    if not request:
        print("No request provided.")
        raise SystemExit(1)

    print("\nLIFEOPS is working...\n")

    state = orchestrate(request)

    print("\n" + "=" * 60)
    print("LIFEOPS WORKFLOW COMPLETE")
    print("=" * 60)

    print("\nREPORT:")
    print(state.report)

    if state.errors:
        print("\nERRORS:")
        for error in state.errors:
            print(f"- {error}")
