WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
BOYAGAIN = ";"
class TIMESTAMP:
    weekday = ""
    hour = ""
    consumption = 0.0
    price = 0.0
class DAY_USAGE:
    weekday = ""
    usage = 0.0
    cost = 0.0
def readTimestamps(filename, timestamps):
    print('Reading file "' + filename + '".')
    timestamps.clear()
    filehandle = open(filename, "r", encoding="utf-8")
    skip_header = filehandle.readline()
    while True:
        line = filehandle.readline()
        if len(line) == 0:
            break
        clean_line = line.strip()
        if len(clean_line) > 0:
            cols = clean_line.split(BOYAGAIN)
            stamp = TIMESTAMP()
            stamp.weekday = cols[0]
            stamp.hour = cols[1]
            stamp.consumption = float(cols[2])
            stamp.price = float(cols[3])
            timestamps.append(stamp)
            cols.clear()
    filehandle.close()
    return None
def analyseUsage(timestamps, results):
    print("Analysing timestamps.")
    results.clear()
    daily_stuff = []
    for i in range(len(WEEKDAYS)):
        day_obj = DAY_USAGE()
        day_obj.weekday = WEEKDAYS[i]
        day_obj.usage = 0.0
        day_obj.cost = 0.0
        daily_stuff.append(day_obj)
    for i in range(len(timestamps)):
        stamp = timestamps[i]
        for j in range(len(daily_stuff)):
            if stamp.weekday == daily_stuff[j].weekday:
                daily_stuff[j].usage += stamp.consumption
                daily_stuff[j].cost += stamp.consumption * stamp.price
    results.append("### Electricity consumption summary ###")
    for i in range(len(daily_stuff)):
        day_obj = daily_stuff[i]
        usage_str = "{0:.2f}".format(day_obj.usage)
        cost_str = "{0:.2f}".format(day_obj.cost)
        results.append(" - " + day_obj.weekday + " usage " + usage_str + " kWh, cost " + cost_str + " €")
    results.append("### Electricity consumption summary ###")
    daily_stuff.clear()
    return None
def displayResults(results):
    print("Displaying results.")
    for i in range(len(results)):
        print(results[i])
    return None
def main():
    print("Program starting.")
    timestamps = []
    results = []
    filename = input("Insert filename: ")
    readTimestamps(filename, timestamps)
    analyseUsage(timestamps, results)
    displayResults(results)
    timestamps.clear()
    results.clear()
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()
