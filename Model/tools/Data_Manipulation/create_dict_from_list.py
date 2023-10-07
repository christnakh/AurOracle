def create_dict_from_list(features_list):
    feature_names = [
        "feature1", "feature2", "feature3", "feature4", "feature5",
        "feature6", "feature7", "feature8", "feature9", "feature10",
        "feature11", "feature12", "feature13"
    ]

    if len(features_list) != len(feature_names):
        raise ValueError("Input list length does not match the expected number of features.")

    feature_dict = {feature_names[i]: features_list[i] for i in range(len(features_list))}
    return feature_dict


input_list = [5.12,5.07,-0.49,0.33,1.96,0.75,2.51,0.32,0.26,0.4,466.6,4.51,156265.0]
result_dict = create_dict_from_list(input_list)
print(result_dict)

