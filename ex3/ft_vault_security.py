#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_vault_security.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42lyon.fr>     +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/09 18:59:32 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/09 19:40:08 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


def main():

    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print("\nInitiating secure vault access...")
    print("\nSECURE EXTRACTION:")

    try:
        with open("module sans interet.txt", 'w') as f:
            f.write("Ce module est sans interet, bien que les sujets sur "
                    "lequelle il traite soit interressant, il comporte "
                    "trop de hardcoding qui empeche une bonne comprehention.")
    except PermissionError:
        print("An issue occurred while creating the file.")

    try:
        with open("module sans interet.txt", 'r') as f:
            content = f.read()
            print(content)
    except PermissionError:
        print("Problem occurred while reading the file.")

    print("\nSECURE PRESERVATION:")
    print(f"[CLASSIFIED] {content}")

    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
