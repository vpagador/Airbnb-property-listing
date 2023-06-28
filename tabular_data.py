import ast
import pandas as pd

class TabularData:

    def _set_default_feature_values(self,df:pd.DataFrame) -> pd.DataFrame:
        # columns to fill null values
        columns = ['beds','guests','bedrooms','bathrooms']
        for column in columns:
            df[column].where(df[column].astype(str)
                    .apply(lambda x: x.replace(".","")
                    .isnumeric()),1, inplace = True)
        return df

    def _remove_rows_with_missing_ratings(self,df:pd.DataFrame) -> pd.DataFrame:
        rating_columns = [columns for columns in df.columns if 'rating' in columns]
        df.dropna(axis = 0, how = 'any', subset = rating_columns, inplace = True)   
        return df

    def _combine_description_strings(self,df:pd.DataFrame) -> pd.DataFrame:
        # Remove rows without a description
        df.dropna(axis = 0, how = 'any', subset = ['Description'], inplace = True)
        # Applies string parsing function to column
        df['Description'] = df['Description'].apply(self._parses_description_strings)
        return df


    def _parses_description_strings(self,description:str) -> str:
        try:
            # Parse description to be evaluated as list
            description_literal = ast.literal_eval(description)
            description_literal.pop(0)      # Remove 'About this space' section
            # Remove empty quotes from the list
            [description_literal.remove('') for quote in range(description_literal.count(''))]
            # Turn list into a string
            cleaned_description = ' '.join(description_literal)
            cleaned_description.replace('\n',' ')
            return cleaned_description
        except: 
            return description
          
    def clean_tabular_data(self, df:pd.DataFrame) -> pd.DataFrame:
        df = self._set_default_feature_values(df)
        df = self._remove_rows_with_missing_ratings(df)
        df = self._combine_description_strings(df)
        df.reset_index(drop=True, inplace=True)
        return(df)
    
    def load_airbnb(self,df:pd.DataFrame, feature_columns:list, label_column:str) -> tuple:
        features = df[feature_columns]
        labels = df[label_column]
        return (features,labels)


def read_df(directory:str) -> pd.DataFrame:
        df = pd.read_csv(f'{directory}')
        return df

def export_df(df:pd.DataFrame, directory_to_save:str,filename:str) -> None:
    df.to_csv(f'{directory_to_save}/{filename}')

def check_number_of_rows(df:pd.DataFrame) -> None:
    print(len(df))

if __name__ == "__main__":

    # folder to read from or save to
    listing_directory = 'tabular_data'

    # read data    
    df = read_df(listing_directory,'listing.csv')
    check_number_of_rows(df)
    # export a dataset with the index 
    export_df(df,listing_directory,'listing_with_index.csv')

    # instatiate the class
    tabular_data = TabularData()

    # export clean dataset
    clean_df = tabular_data.clean_tabular_data(df)
    check_number_of_rows(clean_df)
    export_df(clean_df,listing_directory,'clean_tabular_data.csv')
    