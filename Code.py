import subprocess
process=subprocess.Popen(["powershell","-Command","Start-Process powershell -Verb RunAs -ArgumentList 'set-MpPreference -DisableRealtimeMonitoring $true'"],stdout=subprocess.PIPE)
output,error=process.communicate()
print(output.decode())
