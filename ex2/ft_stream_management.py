#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_stream_management.py                           :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cehenrot <cehenrot@student.42lyon.fr>     +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/09 17:26:40 by cehenrot        #+#    #+#               #
#  Updated: 2026/03/09 18:53:37 by cehenrot        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys


def main():

    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
    print()
    arch_id = input("Input Stream active. Enter archivist ID: ")
    report = input("Input Stream active. Enter status report: ")
    print()
    print(f"[STANDARD] Archive status from {arch_id}: {report}")
    print("[ALERT] System diagnostic: Communication channels "
          "verified", file=sys.stderr)
    print("[STANDARD] Data transmission complete")
    print("\nThree-channel communication test successful")


if __name__ == "__main__":
    main()
