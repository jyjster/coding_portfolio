""" This is a utility module for Homework #5 
    For this homework, use the read_deaths function to read the deaths related data 
    for a county as follows:

    import hw5_util
    cdata = hw5_util.read_deaths('US') ##for county='US'


"""
    
def read_deaths(county):
    dates, counties = read_deaths_all()
    for county_data in counties:
        if county_data[0].lower() == county.lower():
            return county_data[1:]
    return []

def read_deaths_all():
    i = 0
    header = []
    counties = []
    dates = []
    for line in open('nys_deaths.csv').read().split("\n"):
        m = line.strip().split(",")
        i += 1
        if i == 1:
            for val in m[1:]:
                counties.append( [val] )
        else:
            dates.append(m[0])
            for i in range(1,len(m)):
                val = float(m[i])
                counties[i-1].append(val)
    return dates, counties


if __name__ == "__main__":
    ## Example use
    data = read_deaths('Allegany')
    print(data)