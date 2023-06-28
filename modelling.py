from tabular_data import load_airbnb,read_df

    def __train_and_predict__(self):
        # Creates and trains the model
        model = linear_model.SGDRegressor()
        model.fit(X_train, y_train)
        
        #Makes predictions
        y_predictions_train = model.predict(X_train)
        y_predictions_test = model.predict(X_test)
        y_predictions_validation = model.predict(X_validation)

        return y_predictions_train, y_predictions_test, y_predictions_validation

if __name__ == '__main__':
     # folder to read from or save to
    listing_directory = 'tabular_data'
    # Read data
    df = read_df(listing_directory,'listing.csv')
    # print the features-label tuple
    feature_columns = ['guests', 'beds', 'bathrooms', 'Cleanliness_rating', 
                        'Accuracy_rating', 'Communication_rating', 'Location_rating', 
                        'Check-in_rating', 'Value_rating', 'amenities_count', 'bedrooms']
    label_column = 'Price_Night'
    features_labels_tuple = tabular_data.load_airbnb(clean_df,feature_columns,label_column)