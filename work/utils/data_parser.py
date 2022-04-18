from utils.custom_time import Time

def TimeBlockCleaner(raw_data):
    # Clean Raw Data
    
    # Check if start and end time are in dict form or Time obj form
    # actually its given that its a dict because we are loading from json
    cleaned_start = Time(**raw_data["start_time"])
    cleaned_end = Time(**raw_data["end_time"])

    raw_data["start_time"] = cleaned_start
    raw_data["end_time"] = cleaned_end

    # Make a copy
    # parsed_data = {
    #     **raw_data,
    #     "start_time": cleaned_start,
    #     "end_time": cleaned_end
    # }
    
    return raw_data

