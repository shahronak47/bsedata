from bsetools import bsetools
import pandas as pd
from email_file import email_main
import pdb

#path of the csv file
CSV_FILE_PATH = "C:\\Users\\Ronak Shah\\Google Drive\\Documents\\Shares.csv"

def get_current_stock_prices(share_list, bse) :
    current_data_list = []
    for share in share_list :
        current_data = bse.get_quote(share)
        #If the code is valid and we have the data take the 1st index, 2nd is change from yesterday
        if current_data is not None :
            current_data_list.append(current_data[0])
        else :
            #If we do not have the data we append 0
            current_data_list.append(0)

    return current_data_list

if __name__ == '__main__' :
    # Read the csv file which has data
    df = pd.read_csv(CSV_FILE_PATH)
    #Initialise the bsetools object
    bse = bsetools.bsetools()
    current_data_list = get_current_stock_prices(df['Shares'].tolist(), bse)
    # Add new columns to dataframe coverting string to float value
    df['Current_price'] = [float(x) for x in current_data_list]
    df['Profit'] = (df.Current_price * df.Quantity) - df.Amount

    #Get BSE index
    obj = bse.get_BSE_index()
    #pdb.set_trace()
    email_main(df, obj)