# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    data_types.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mmago <mmago@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/09/18 23:12:16 by mmago             #+#    #+#              #
#    Updated: 2022/09/18 23:12:18 by mmago            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/Library/Frameworks/Python.framework/Versions/3.7/Resources/Python.app/Contents/MacOS/Python

def data_types():
	var = (
		1,
		"text",
		4.2,
		True,
		["aloha", 3],
		{'dict': '1', 'moobs': "2"},
		(7.7, "three"),
		{2, "two", 4.3},
	)
	output = '['
	for v in var:
		output += type(v).__name__ + ', '
	print (output[0:-2] + ']')

if __name__ == '__main__':
	data_types()