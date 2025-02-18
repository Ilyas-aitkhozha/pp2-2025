import datetime
time1 = datetime.datetime.now()
graduate = datetime.datetime(2028, 5, 25, 0, 0, 0)
diff = graduate - time1
print(diff.total_seconds())
print("without microsec: ", round(diff.total_seconds()))