# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    marketing.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mmago <mmago@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/09/18 23:11:54 by mmago             #+#    #+#              #
#    Updated: 2022/09/18 23:11:56 by mmago            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/Library/Frameworks/Python.framework/Versions/3.7/Resources/Python.app/Contents/MacOS/Python
import sys

def get_subjects_data() -> list:
	clients = [
		'andrew@gmail.com', 'jessica@gmail.com',
		'ted@mosby.com', 'john@snow.is',
		'bill_gates@live.com', 'mark@facebook.com',
		'elon@paypal.com', 'jessica@gmail.com'
		]

	participants = [
		'walter@heisenberg.com', 'vasily@mail.ru',
		'pinkman@yo.org', 'jessica@gmail.com',
		'elon@paypal.com', 'pinkman@yo.org',
		'mr@robot.gov', 'eleven@yahoo.com'
		]

	recipients = [
		'andrew@gmail.com', 'jessica@gmail.com',
		'john@snow.is'
		]
	
	return set(clients), set(participants), set(recipients)

def call_center_list(clients: set, recipients: set) -> list:
	return (list(clients - recipients))

def potential_clients_list(participants: set, clients: set) -> list:
	return (list(participants - clients))

def loyalty_program_list(clients: set, participants: set) -> list:
	return (list(clients - participants))

def	ft_send(send_task: str) -> None:
	clients, participants, recipients = get_subjects_data()
	# call_center, potential_clients, loyalty_program
	if send_task == "call_center":
		print(call_center_list(clients, recipients))
	elif send_task == "potential_clients":
		print(potential_clients_list(participants, clients))
	elif send_task == "loyalty_program":
		print(loyalty_program_list(clients, participants))
	else:
		raise ValueError('Invalid argument')

def	main():
	if (len(sys.argv) == 2):
		ft_send(sys.argv[1])

if __name__ == '__main__':
	main()