#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_crisis_response.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/10 12:48:30 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/10 14:12:02 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def read_file(name: str) -> str:

    with open(name, 'r') as f:
        content = f.read()
    return content


def main():

    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

    print("\nCRISIS ALERT: Attempting access to 'lost_archive.txt'...")
    try:
        read_file('lost_archive.txt')
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")

    print("\nCRISIS ALERT: Attempting access to 'classified_vault.txt'...")
    try:
        read_file('classified_vault.txt')
    except (PermissionError):
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")

    print("\nROUTINE ACCESS: Attempting access to "
          "'standard_archive.txt'...")
    try:
        read_file('standard_archive.txt')
        print("SUCCESS: Archive recovered - "
              "``Knowledge preserved for humanity''")
        print("STATUS: Normal operations resumed")
    except (OSError, PermissionError, FileNotFoundError):
        print("Error")

    print("\nAll crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
