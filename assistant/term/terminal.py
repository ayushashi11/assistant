from assistant.ai_m2 import reply
resp = ""
while "bye" not in resp.lower() and "see ya" not in resp.lower():
	resp = reply(input("\x1b[38;2;0;0;125myou>\x1b[0m "))
	print("\x1b[38;2;0;125;0mbot>\x1b[0m ",resp)
