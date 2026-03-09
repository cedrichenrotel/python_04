#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_archive_creation.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42lyon.fr>     +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/09 13:59:07 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/09 17:17:58 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def main():

    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")

    print("\nInitializing new storage unit: new_discovery.txt")
    try:
        with open("new_discovery.txt", 'w') as f:
            content = f.write("[ENTRY 001] New quantum algorithm discovered\n"
                              "[ENTRY 002] Efficiency increased by 347%\n"
                              "[ENTRY 003] Archived by Data Archivist trainee")
    except PermissionError:
        print("problem encountered when creating the file [KO]")
        return

    print("Storage unit created successfully...")
    try:
        with open("new_discovery.txt") as f:
            content = f.read()
    except PermissionError:
        print("problem encountered when reading the file [KO]")
        return

    print("\nInscribing preservation data...")
    print(content)
    print("\nData inscription complete. Storage unit sealed")
    print("Archive 'new_discovery.txt' ready for long-term preservation")


if __name__ == "__main__":
    main()
