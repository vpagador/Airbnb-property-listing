from tabular_data import CleanTabularData, read_df


if __name__ == "__main__":
    # instatiate the class
    tabular_data_cleaner = CleanTabularData()

    # read data
    df = read_df('tabular_data/listing.csv')
    # clean data
    clean_df = tabular_data_cleaner.clean_tabular_data(df)

    # print the features-label tuple
    feature_columns = ['guests', 'beds', 'bathrooms', 'Cleanliness_rating', 
                       'Accuracy_rating', 'Communication_rating', 'Location_rating', 
                       'Check-in_rating', 'Value_rating', 'amenities_count', 'Price_Night']
    label_column = 'bedrooms'
    features_label_tuple = tabular_data_cleaner.load_airbnb(clean_df,feature_columns,label_column)
    
    # print the shape of the tuple
    [print(x.shape) for x in features_label_tuple]

