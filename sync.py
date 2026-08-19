import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('160.202.238.40', port=32050, username='root', password='qgllCAPR4085', timeout=10)

sftp = client.open_sftp()
sftp.get('/opt/qq_bot/bot.py', r'C:\Users\Administrator\Desktop\智简魔方\qq_bot\bot.py')
sftp.close()

print("Downloaded latest bot.py")

client.close()
