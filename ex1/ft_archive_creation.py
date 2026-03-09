#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_archive_creation.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/09 13:59:07 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/09 14:19:22 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def main():
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print("\nInitializing new storage unit: new_discovery.txt")

    try:
        with open("new_discovery.txt", 'w') as f:
            
    except FileNotFoundError:
        print("error when opening the file")
        return
    print("Connection established...")
    print("RECOVERED DATA:")
    content = f.write()
    print(content)

    f.close()
    print("Data recovery complete. Storage unit disconnected")



if __name__ == "__main__":
    main()
