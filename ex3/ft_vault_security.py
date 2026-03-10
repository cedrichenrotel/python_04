#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_vault_security.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/09 18:59:32 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/10 14:52:36 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

NAME_FILE = "security_protocols.txt"
NEW_FILE = "classified_data.txt"


def create_file(name: str, content: str) -> None:

    with open(name, 'a+') as f:
        f.write(content)


def read_file(name: str) -> str:

    with open(name, 'r+') as f:
        content = f.read()
    return content


def main():

    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print("\nInitiating secure vault access...")
    print("Vault connection established with failsafe protocols")

    print("\nSECURE EXTRACTION:")
    try:

        content = read_file(NAME_FILE)
    except (PermissionError, FileNotFoundError, OSError,
            FileExistsError) as e:
        print(f"error {NAME_FILE}: {e} [KO]")

    print("\nSECURE PRESERVATION:")
    try:
        create_file(NEW_FILE, content)
        print(read_file(NEW_FILE))
    except (PermissionError, FileNotFoundError, OSError,
            FileExistsError) as e:
        print(f"error {NEW_FILE}: {e} [KO]")

    print("\nAll vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
