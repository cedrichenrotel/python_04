#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_crisis_response.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42lyon.fr>     +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/10 12:48:30 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/10 19:00:40 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def read_file(name: str) -> str:

    with open(name, 'r') as f:
        content = f.read()
    return content


def crisis_handler(name: str) -> None:

    try:
        read_file(name)
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")

    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")

    except OSError:
        print("RESPONSE: Unexpected system anomaly detected")
        print("STATUS: Crisis handled, system stable")

    else:
        print("SUCCESS: Archive recovered - "
              "``Knowledge preserved for humanity''")
        print("STATUS: Normal operations resumed")


def main():

    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

    print("\nCRISIS ALERT: Attempting access to 'lost_archive.txt'...")
    crisis_handler('lost_archive.txt')

    print("\nCRISIS ALERT: Attempting access to 'classified_vault.txt'...")
    crisis_handler('classified_vault.txt')

    print("\nROUTINE ACCESS: Attempting access to "
          "'standard_archive.txt'...")
    crisis_handler('standard_archive.txt')

    print("\nROUTINE ACCESS: Attempting access to 'corrupted_archive.txt'...")
    crisis_handler('corrupted_archive.txt')

    print("\nAll crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
