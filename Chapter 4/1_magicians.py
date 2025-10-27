# FOR LOOPS THRU THE ENTIRE LIST

magicians = ["alice", "david", "carolina"]

for magician in magicians:
    print(magician)

# DOING MORE WITH A FOR LOOP

for magician in magicians:
    print(f"{magician.title()}, that was a stunning trick you just pulled.")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

    print("\n")

    # AVOID INDENTATION ERRORS
    # NOTE: RESULTS IN INDENDATION ERROR
#     magicians = ["alice", "david", "carolina"]

# for magician in magicians:
#     print(magician)
    
# FORGETTING TO IDENT ADDITIONAL LINES
magicians = ["alice", "david", "carolina"]

for magician in magicians:
    print(f"{magician.title()}, that was a stunning trick you just pulled.")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

    # INDENTING UNNECESSARILY
    # RESULTS IN INDENTATION ERROR
    message = "Hello Python world!"
    print(message)

    # indenting unnecessarily afer loop

    magicians = ["alice", "david", "carolina"]

for magician in magicians:
    print(f"{magician.title()}, that was a stunning trick you just pulled.")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

    print("\nThank you everyone, that was a great show!")
