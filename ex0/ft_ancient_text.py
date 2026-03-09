#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_ancient_text.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/09 13:01:34 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/09 13:54:27 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def main():
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print("\nAccessing Storage Vault: ancient_fragment.txt")
    try:
        f = open("ancient_fragment.txt", 'r')
    except FileNotFoundError:
        print("error when opening the file")
        return
    print("Connection established...")
    print("RECOVERED DATA:")
    content = f.read()
    print(content)

    f.close()
    print("Data recovery complete. Storage unit disconnected")


if __name__ == "__main__":
    main()
