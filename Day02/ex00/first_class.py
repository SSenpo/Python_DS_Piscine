# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    first_class.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mmago <mmago@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/09/19 11:09:13 by mmago             #+#    #+#              #
#    Updated: 2022/09/19 11:28:45 by mmago            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

##!/Library/Frameworks/Python.framework/Versions/3.7/Resources/Python.app/Contents/MacOS/Python

class Must_read:
    with open('data.csv', 'r', encoding='utf-8') as file:
        print(file.read())
