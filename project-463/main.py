from merge_sort import merge_sort
from max_subarray import max_subarray
from closest_pair import closest_pair
from data_handler import load_data, preprocess_data

import yfinance as yf

def main():
    # get our dataset
    data = load_data('financial_data.csv')

    # Preprocess the data
    sorted_data = preprocess_data(data, 'Date')

    # Apply merge sort
    sorted_prices = merge_sort(sorted_data['Close'].to_list())

    # Find the period of maximum gain or loss
    gains, start_idx, end_idx = max_subarray(sorted_prices)
    print(f"Maximum gain: {gains} from {start_idx} to {end_idx}")

    # anominies detection
    anomalies = closest_pair(list(zip(sorted_data['Close'], sorted_data['Volume'])))
    print(f"Anomalies detected between: {anomalies[0]} and {anomalies[1]}")


main()
