import subprocess
process=subprocess.popen(["powershell","-Command","Start-Process powershell -Verb RunAs -ArgumentList 'set-MpPreference -DisableRealtimrMonitoring $true'"],stdout=subprocess.PIPE)
output,error=process.communicate()
print(output.decode())
