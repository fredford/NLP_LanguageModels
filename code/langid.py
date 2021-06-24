# This program should loop over the files listed in the input file directory,
# assign perplexity with each language model,
# and produce the output as described in the assignment description.

import pandas as pd
import os
from unsmoothed import Unsmoothed
from laplace import Laplace
from interpolation import Interpolation

import sys

def get_filenames(filepath):
    """
    Function used to get all of the file names in the specified directory.

    Arguments:
        filepath -- String specifying the root directory

    Return:
        dataFiles -- Dictionary with keys as file name and value as file path
    """

    dataFiles = {}

    for root, dirs, filenames in os.walk(filepath):

        #filenames = sorted(filenames, key=lambda x: int(x.split(".")[0]))
        for filename in filenames:
            dataFiles[filename] = os.path.join(root, filename)

    return dataFiles

# Directory storing data files to be processed
def main ():

    # Directory storing data files to be processed
    train_path = "data/train"
    test_path = "data/dev"

    # Call function to receive dictionary of filenames in the specified directory
    trainFiles = get_filenames(train_path)
    testFiles = get_filenames(test_path)


    # Initialize Pandas DataFrames
    dfs = {
        "--unsmoothed"    : pd.DataFrame(columns=["Training_file", "Testing_file", "Perplexity", "N"]),
        "--laplace"       : pd.DataFrame(columns=["Training_file", "Testing_file", "Perplexity", "N"]),
        "--interpolation" : pd.DataFrame(columns=["Training_file", "Testing_file", "Perplexity", "N"])
        }

    # Initialize default n values
    n_dict = {
        "--unsmoothed"    : 2,
        "--laplace"       : 2,
        "--interpolation" : 1
        }

    # Initialize model dictionary
    models = {
        "--unsmoothed"    : None,
        "--laplace"       : None,
        "--interpolation" : None
        }

    # Initialize output paths
    outputPaths = {
        "--unsmoothed"    : "output/results_dev_unsmoothed.csv",
        "--laplace"       : "output/results_dev_add-one.csv",
        "--interpolation" : "output/results_dev_interploation.csv"
    } 

    # Initialize n
    n = None

    # Iterate through command line arguments
    for arg in sys.argv[1:]:

        # If an input value is an integer store it as n
        if arg not in models.keys():
            try:
                n = int(arg)
            except:
                continue

        # If an argument is declared as unsmoothed
        elif arg == "--unsmoothed":
            if n == None:
                unsm = Unsmoothed(n_dict[arg])
            else:
                unsm = Unsmoothed(n)

            models[arg] = unsm

        # If an argument is declared as laplace
        elif arg == "--laplace":
            if n == None:
                lapl = Laplace(n_dict[arg])
            else:
                lapl = Laplace(n)

            models[arg] = lapl

        # If an argument is declared as interpolation
        elif arg == "--interpolation":
            if n == None:
                intp = Interpolation(n_dict[arg])
            else:
                intp = Interpolation(n)

            models[arg] = intp

        else:
            print("Error")

    i = 0

    # Iterate through the models specified by command line
    for key, model in models.items():

        # Set the dataframe counter to zero
        counter  = 0

        # If no model was specified continue to the next model
        if model == None:
            continue

        # Iterate through every file in the directory
        for filename, filepath in trainFiles.items():

            # Open the current file
            dataFile = open(filepath, "r")

            # Process data file
            model.process_train(dataFile, filename)

            # Close the current file
            dataFile.close()

        # If the interpolation model is specified
        if key == "--interpolation":

            #count = 0

            #for testfilename, filepath in testFiles.items():

                #if count < 10:

                    # Open the current file
                    #testFile = open(filepath, "r")

                    #for i in range(10):
                        # Process data file
                        #model.process_interpolate(testFile, testfilename)

                    # Output the data returned from the extraction
                    #data = model.get_data()

                    # Add all output data to the DataFrame
                    #dfs[arg].loc[counter] = [data[0], data[1], data[2], data[3]]
                    #counter+=1

                #else:

                    # Open the current file
                    #testFile = open(filepath, "r")

                    # Process data file
                    #model.process_test(testFile, testfilename)

                    # Output the data returned from the extraction
                    #data = model.get_data()

                    # Add all output data to the DataFrame
                    #dfs[arg].loc[counter] = [data[0], data[1], data[2], data[3]]
                    #counter+=1


                #if data[0].split(".")[0] == data[1].split(".")[0]:
                #    i += 1

                #count +=1
                # Close the current file
                #dataFile.close()

            continue

        # Iterate through every file in the directory
        for testfilename, filepath in testFiles.items():

            # Open the current file
            testFile = open(filepath, "r")

            # Process data file
            model.process_test(testFile, testfilename)

            # Output the data returned from the extraction
            data = model.get_data()

            # Add all output data to the DataFrame
            dfs[arg].loc[counter] = [data[0], data[1], data[2], data[3]]
            counter+=1

            # Close the current file
            dataFile.close()

        # Write the data to a CSV file
        dfs[arg].to_csv(outputPaths[key], index=False)

main()

