import subprocess
import time

cmd = 'cmd /k azcopy cp "https://ueprd28file01.file.core.windows.net/prd/NewCo/logs?sv=2021-06-08&ss=bfqt&srt=sco&sp=rwlacupitfx&se=2024-02-27T23:16:48Z&st=2023-02-27T15:16:48Z&spr=https&sig=nS46%2FwdUg%2B%2F6kprU%2BJiIRuOiSH7menDH8R5VyTuWlA4%3D" "C:\\Users\\DG04170\\BillingPaymentArchives\\logs" --recursive=true  --overwrite=false &'

proc = subprocess.Popen(cmd, shell=True)  
print('returned value:', proc)
time.sleep(25) # <-- sleep for 15''
proc.terminate() # <-- terminate the process



cmd = 'cmd /k azcopy cp "https://ueprd28file01.file.core.windows.net/prd/NewCo/BillingPayments/Archives?sv=2022-11-02&ss=bfqt&srt=sco&sp=rwdlacupitfx&se=2024-07-01T18:09:50Z&st=2023-07-18T03:09:50Z&spr=https&sig=9SPCThduZpl91yEi5WKNV6rGSVYQw6O1dMnyDt5fNSA%3D" "C:\\Users\\DG04170\\BillingPaymentArchives\\ongoing" --recursive=true  --overwrite=false &'

#azcopy cp "https://ueprd28file01.file.core.windows.net/prd/NewCo/BillingPayments/Archives?sv=2022-11-02&ss=bfqt&srt=sco&sp=rwdlacupitfx&se=2024-07-01T18:09:50Z&st=2023-07-18T03:09:50Z&spr=https&sig=9SPCThduZpl91yEi5WKNV6rGSVYQw6O1dMnyDt5fNSA%3D" "C:\Users\DG04170\BillingPaymentArchives\ongoing" --recursive=true  --overwrite=false
