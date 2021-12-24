PREDICTION_SCHEMA = {
    'type': "object",
    'properties': {
        'MSSubClass': {
            'type': 'number',
        },
        'MSZoning': {
            'type': 'string',
        },
        'LotFrontage': {
            'type': 'number',
        },
        'LotArea': {
            'type': 'number',
        },
        'Street': {
            'type': 'string',
        },
        'LotShape': {
            'type': 'string',
        },
        'LandContour': {
            'type': 'string',
        },
        'Utilities': {
            'type': 'string',
        },
        'LotConfig': {
            'type': 'string',
        },
        'LandSlope': {
            'type': 'string',
        },
        'Neighborhood': {
            'type': 'string',
        },
        'Condition1': {
            'type': 'string',
        },
        'Condition2': {
            'type': 'string',
        },
        'BldgType': {
            'type': 'string',
        },
        'HouseStyle': {
            'type': 'string',
        },
        'RoofStyle': {
            'type': 'string',
        },
        'RoofMatl': {
            'type': 'string',
        },
        'Exterior1st': {
            'type': 'string',
        },
        'Exterior2nd': {
            'type': 'string',
        },
        'ExterQual': {
            'type': 'string',
        },
        'ExterCond': {
            'type': 'string',
        },
        'Foundation': {
            'type': 'string',
        },
        'BsmtQual': {
            'type': 'string',
        },
        'BsmtCond': {
            'type': 'string',
        },
        'BsmtExposure': {
            'type': 'string',
        },
        'BsmtFinType1': {
            'type': 'string',
        },
        'BsmtFinType2': {
            'type': 'string',
        },
        'Heating': {
            'type': 'string',
        },
        'HeatingQC': {
            'type': 'string',
        },
        'CentralAir': {
            'type': 'string',
        },
        'Electrical': {
            'type': 'string',
        },
        '1stFlrSF': {
            'type': 'number',
        },
        '2ndFlrSF': {
            'type': 'number',
        },
        'LowQualFinSF': {
            'type': 'number',
        },
        'GrLivArea': {
            'type': 'number',
        },
        'BedroomAbvGr': {
            'type': 'number',
        },
        'KitchenAbvGr': {
            'type': 'number',
        },
        'KitchenQual': {
            'type': 'string',
        },
        'TotRmsAbvGrd': {
            'type': 'number',
        },
        'Functional': {
            'type': 'string',
        },
        'Fireplaces': {
            'type': 'number',
        },
        'FireplaceQu': {
            'type': 'string',
        },
        'GarageType': {
            'type': 'string',
        },
        'GarageYrBlt': {
            'type': 'number',
        },
        'GarageFinish': {
            'type': 'string',
        },
        'GarageCars': {
            'type': 'number',
        },
        'GarageArea': {
            'type': 'number',
        },
        'GarageQual': {
            'type': 'string',
        },
        'GarageCond': {
            'type': 'string',
        },
        'PavedDrive': {
            'type': 'string',
        },
        'WoodDeckSF': {
            'type': 'number',
        },
        'OpenPorchSF': {
            'type': 'number',
        },
        'EnclosedPorch': {
            'type': 'number',
        },
        '3SsnPorch': {
            'type': 'number',
        },
        'ScreenPorch': {
            'type': 'number',
        },
        'PoolArea': {
            'type': 'number',
        },
        'MiscVal': {
            'type': 'number',
        },
        'MoSold': {
            'type': 'number',
        },
        'SaleType': {
            'type': 'string',
        },
        'SaleCondition': {
            'type': 'string',
        },
        'cond*qual': {
            'type': 'number',
        },
        'home_age_when_sold': {
            'type': 'number',
        },
        'after_remodel_home_age_when_sold': {
            'type': 'number',
        },
        'BsmtFinSF1+BsmtFinSF2': {
            'type': 'number',
        },
        'TotalSF': {
            'type': 'number',
        },
        'Total_Bathrooms': {
            'type': 'number',
        },
    },
    'required': [
        'MSSubClass', 'MSZoning', 'LotFrontage', 'LotArea', 'Street',
        'LotShape', 'LandContour', 'Utilities', 'LotConfig', 'LandSlope',
        'Neighborhood', 'Condition1', 'Condition2', 'BldgType', 'HouseStyle',
        'RoofStyle', 'RoofMatl', 'Exterior1st', 'Exterior2nd', 'ExterQual',
        'ExterCond', 'Foundation', 'BsmtQual', 'BsmtCond', 'BsmtExposure',
        'BsmtFinType1', 'BsmtFinType2', 'Heating', 'HeatingQC', 'CentralAir',
        'Electrical', '1stFlrSF', '2ndFlrSF', 'LowQualFinSF', 'GrLivArea',
        'BedroomAbvGr', 'KitchenAbvGr', 'KitchenQual', 'TotRmsAbvGrd',
        'Functional', 'Fireplaces', 'FireplaceQu', 'GarageType', 'GarageYrBlt',
        'GarageFinish', 'GarageCars', 'GarageArea', 'GarageQual', 'GarageCond',
        'PavedDrive', 'WoodDeckSF', 'OpenPorchSF', 'EnclosedPorch',
        '3SsnPorch', 'ScreenPorch', 'PoolArea', 'MiscVal', 'MoSold',
        'SaleType', 'SaleCondition', 'cond*qual', 'home_age_when_sold',
        'after_remodel_home_age_when_sold', 'BsmtFinSF1+BsmtFinSF2', 'TotalSF',
        'Total_Bathrooms']
}


def get_json_data(obj):
    """Gets all values of a Dict

    Args:
        obj (Dict): To extract values of json

    Returns:
        [list of string]: Values of a given dict without keys
    """
    temp_list = []
    obj_keys = obj.keys()

    for key in obj_keys:
        temp_list.append(obj[key])

    return temp_list
