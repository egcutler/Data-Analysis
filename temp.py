def prioritize_us(item):
    # Assign highest priority to 'US'
    return (item != 'US', item)

# Example list
country_list = ['USA', 'UK', 'CAN', 'AUS', 'GER', 'FRA', 'JPN', 'CHN', 'RUS', 'BRA', 'IND', 'US']

# Sorting the list with 'US' as the first element if it exists
country_list.sort(key=prioritize_us)

print(country_list)
