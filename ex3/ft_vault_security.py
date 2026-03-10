#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_vault_security.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42lyon.fr>     +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/09 18:59:32 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/10 18:28:03 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

CLASSIFIELD = "classified_data.txt"
SECURITY = "security_protocols.txt"


def append_arg_file(name: str, content: str) -> None:

    with open(name, 'a') as f:
        f.write("\n" + content)


def read_file(name: str) -> str:

    with open(name, 'r') as f:
        content = f.read()
    return content


def main():

    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print("\nInitiating secure vault access...")
    print("Vault connection established with failsafe protocols")

    print("\nSECURE EXTRACTION:")
    try:

        content = read_file(CLASSIFIELD)
        print(content)
    except (PermissionError, FileNotFoundError, OSError,
            FileExistsError) as e:
        print(f"error {CLASSIFIELD}: {e} [KO]")

    print("\nSECURE PRESERVATION:")
    try:
        append_arg_file(SECURITY, "[CLASSIFIED] New security protocols "
                        "archived")
        print(read_file(SECURITY))
    except (PermissionError, FileNotFoundError, OSError,
            FileExistsError) as e:
        print(f"error {SECURITY}: {e} [KO]")

    print("Vault automatically sealed upon completion")
    print("\nAll vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
