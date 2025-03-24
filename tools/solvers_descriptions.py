solvers_descriptions = {
    1: {
        "type": "function",
        "function": {
            "name": "solver_1",
            "description": "Gives output of a specific command in VS code",
            "parameters": {
                "type": "object",
                "properties": {
                    "command": {
                        "type": "string",
                        "description": "the command whose output is required"
                    },
                    

                },
                "required": ["command"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    2: {
        "type": "function",
        "function": {
            "name": "solver_2",
            "description": "Sends a HTTPS request to {url} with the URL encoded parameter {param} set to {email}",
            "parameters": {
                "type": "object",
                "properties": {
                    "url": {
                        "type": "string",
                        "description": "the URL to send the request to"
                    },
                    "param": {
                        "type": "string",
                        "description": "the URL encoded parameter"
                    },
                    "value": {
                        "type": "string",
                        "description": "the value set to the parameter"
                    }
                    

                },
                "required": ["url", "param", "value"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    3: {
        "type": "function",
        "function": {
            "name": "solver_3",
            "description": "Download the attached file . In the directory where you downloaded it, make sure it is called {req_filename}, and run {command} . Use npx and prettier.",
            "parameters": {
                "type": "object",
                "properties": {
                    "req_filename": {
                        "type": "string",
                        "description": "the name that the file should be renamed to"
                    },
                    "command": {
                        "type": "string",
                        "description": "the command whose output is required"
                    },
                    

                },
                "required": ["req_filename", "command"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    4: {
        "type": "function",
        "function": {
            "name": "solver_4",
            "description": "Converts a Google Sheets formula to a Python code and returns the result",
            "parameters": {
                "type": "object",
                "properties": {
                    "formula": {
                        "type": "string",
                        "description": "the Google Sheets formula"
                    },
                    

                },
                "required": ["formula"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    5: {
        "type": "function",
        "function": {
            "name": "solver_5",
            "description": "Converts a Microsoft excel_formula to a Python code and returns the result",
            "parameters": {
                "type": "object",
                "properties": {
                    "excel_formula": {
                        "type": "string",
                        "description": "the Microsoft Excel formula"
                    },
                    

                },
                "required": ["excel_formula"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    6: {
        "type": "function",
        "function": {
            "name": "solver_6",
            "description": "Extracts the value from a hidden input",
            "parameters": {
                "type": "object",
                "properties": {
                    "html_element": {
                        "type": "string",
                        "description": "the HTML element"
                    },
                    

                },
                "required": ["html_element"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    7: {
        "type": "function",
        "function": {
            "name": "solver_7",
            "description": "Counts the number of {day_name} between {start_date} and {end_date}",
            "parameters": {
                "type": "object",
                "properties": {
                    "day_name": {
                        "type": "string",
                        "description": "the day name"
                    },
                    "start_date": {
                        "type": "string",
                        "description": "the start date"
                    },
                    "end_date": {
                        "type": "string",
                        "description": "the end date"
                    }
                    

                },
                "required": ["day_name", "start_date", "end_date"],
                "additionalProperties": False
            },
            "strict": True
    }
    },

    8: {
        "type": "function",
        "function": {
            "name": "solver_8",
            "description": "Unzip and extracts the value in a given column from a CSV file",
            "parameters": {
                "type": "object",
                "properties": {
                    "csv_file": {
                        "type": "string",
                        "description": "the name of the CSV file"
                    },

                    "column_name": {
                        "type": "string",
                        "description": "the name of the column"
                    }             

                },
                "required": ["csv_file", "column_name"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    9: {
        "type": "function",
        "function": {
            "name": "solver_9",
            "description": "Sorts a {json_array} of objects by the value of the {first_field} field. In case of a tie, sort by the {second_field} field.",
            "parameters": {
                "type": "object",
                "properties": {
                    "json_array": {
                        "type": "string",
                        "description": "the JSON array of objects"
                    },
                    "first_field": {
                        "type": "string",
                        "description": "the first field for sorting"
                    },
                    "second_field": {
                        "type": "string",
                        "description": "the second field for sorting"
                    }
                    

                },
                "required": ["json_array", "first_field", "second_field"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    10: {
        "type": "function",
        "function": {
            "name": "solver_10",
            "description": "Converts a multi-cursor text into a single JSON object",
            "parameters": {
                "type": "object",
                "properties": {
                    

                },
                "required": [],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    11: {
        "type": "function",
        "function": {
            "name": "solver_11",
            "description": "Finds all {html_element}'s having a {given_class} class in the {hidden_html}. Returns the sum of their {given_attribute} attributes",
            "parameters": {
                "type": "object",
                "properties": {
                    "html_element": {
                        "type": "string",
                        "description": "the HTML element"
                    },
                    "given_class": {
                        "type": "string",
                        "description": "the class name"
                    },
                    "given_attribute": {
                        "type": "string",
                        "description": "the attribute name"
                    },
                    "hidden_html": {
                        "type": "string",
                        "description": "it is termed as the hidden HTML but this is the html that is passed along with the prompt"
                    }
                    

                },
                "required": ["html_element", "given_class", "given_attribute", "hidden_html"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    12: {
        "type": "function",
        "function": {
            "name": "solver_12",
            "description": "Sum up all the values where the symbol matches {symbol_1} OR {symbol_2} OR {symbol_3} across all three files. The symbols are separated by OR in the format - {symbol_1} OR {symbol_2} OR {symbol_3}. Symbols would not include the 'OR' word",
            "parameters": {
                "type": "object",
                "properties": {
                    "symbol_1": {
                        "type": "string",
                        "description": "It is the first symbol to match. It would be between the word matches and the first OR like matches {symbol_1} OR. Make sure not to include the 'OR' word"
                    },
                    "symbol_2": {
                        "type": "string",
                        "description": "the second symbol to match, it will be after the first OR and before the second OR. It would not include the 'OR' word"
                    },
                    "symbol_3": {
                        "type": "string",
                        "description": "the third symbol to match, it will be just after the second OR. It would not include the 'OR' word"
                    },
                    "file_1": {
                        "type": "string",
                        "description": "the name of the first file"
                    },
                    "encoding_1": {
                        "type": "string",
                        "description": "the encoding of the first file"
                    },
                    "file_2": {
                        "type": "string",
                        "description": "the name of the second file"
                    },
                    "encoding_2": {
                        "type": "string",
                        "description": "the encoding of the second file"
                    },
                    "file_3": {
                        "type": "string",
                        "description": "the name of the third file"
                    },
                    "encoding_3": {
                        "type": "string",
                        "description": "the encoding of the third file"
                    }
                    

                },
                "required": ["symbol_1", "symbol_2", "symbol_3", "file_1", "encoding_1", "file_2", "encoding_2", "file_3", "encoding_3"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    13: {
        "type": "function",
        "function": {
            "name": "solver_13",
            "description": "Commit a single JSON file called {file_name} with the value {value} and push it. Enter the raw Github URL of email.json so we can verify it.",
            "parameters": {
                "type": "object",
                "properties": {
                    "file_name": {
                        "type": "string",
                        "description": "the name of the file"
                    },
                    "value": {
                        "type": "string",
                        "description": "the value to be committed"
                    }
                    

                },
                "required": ["file_name", "value"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    14: {
        "type": "function",
        "function": {
            "name": "solver_14",
            "description": "This function replaces all {existing_word} with {new_word} in all files and Leave everything as-is, then run the command {command} T",
            "parameters": {
                "type": "object",
                "properties": {
                    "existing_word": {
                        "type": "string",
                        "description": "the word to be replaced"
                    },
                    "new_word": {
                        "type": "string",
                        "description": "the word to be replaced with"
                    },
                    "command": {
                        "type": "string",
                        "description": "the command to be run"
                    }
                    

                },
                "required": ["existing_word", "new_word", "command"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    15: {
        "type": "function",
        "function": {
            "name": "solver_15",
            "description": "Lists all files in the folder along with their date and file size. Returns the total size of all files at least {file_size_number} bytes large and modified on or after {date_string}",
            "parameters": {
                "type": "object",
                "properties": {
                    "file_size_number": {
                        "type": "string",
                        "description": "the minimum file size"
                    },
                    "date_string": {
                        "type": "string",
                        "description": "the date string in the format %a, %d %b, %Y, %I:%M %p %Z"
                    }
                    

                },
                "required": ["file_size_number", "date_string"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    16: {
        "type": "function",
        "function": {
            "name": "solver_16",
            "description": "Moves all files under folders into an empty folder. Then renames all files replacing each digit with the next. 1 becomes 2, 9 becomes 0, a1b9c.txt becomes a2b0c.txt. Then execute the given command {command}",
            "parameters": {
                "type": "object",
                "properties": {
                    "command": {
                        "type": "string",
                        "description": "the command to be run"
                    }
                    

                },
                "required": ["command"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    17: {
        "type": "function",
        "function": {
            "name": "solver_17",
            "description": "Counts the number of lines that are different between {file_1} and {file_2}",
            "parameters": {
                "type": "object",
                "properties": {
                    "file_1": {
                        "type": "string",
                        "description": "the name of the first file"
                    },
                    "file_2": {
                        "type": "string",
                        "description": "the name of the second file"
                    }
                    

                },
                "required": ["file_1", "file_2"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    18: {
        "type": "function",
        "function": {
            "name": "solver_18",
            "description": "Calculates total sales of all the items in the {ticket_type} ticket type. For that the ticket_type parameter is required.",
            "parameters": {
                "type": "object",
                "properties": {
                    "ticket_type": {
                        "type": "string",
                        "description": "the string containing the type of ticket"
                    }
                    

                },
                "required": ["ticket_type"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    19: {
        "type": "function",
        "function": {
            "name": "solver_19",
            "description": "Writes documentation in Markdown for an imaginary analysis of the number of steps you walked each day for a week, comparing over time and with friends.",
            "parameters": {
                "type": "object",
                "properties": {
            
                },
                "required": [],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    20: {
        "type": "function",
        "function": {
            "name": "solver_20",
            "description": "Compresses the image losslessly to an image that is less than 1,500 bytes",
            "parameters": {
                "type": "object",
                "properties": {
            
                },
                "required": [],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    21: {
        "type": "function",
        "function": {
            "name": "solver_21",
            "description": "Publishes a page using GitHub Pages that showcases your work. Ensures that your email address {email_id} is in the page's HTML.",
            "parameters": {
                "type": "object",
                "properties": {
                    "email_id": {
                        "type": "string",
                        "description": "the email ID"
                    }
                    

                },
                "required": ["email_id"],
                "additionalProperties": False
            },
            "strict": True
        }
    },


    22: {
        "type": "function",
        "function": {
            "name": "solver_22",
            "description": "Runs the given program on Google Colab, allowing all required access to your email ID: {email_id}",
            "parameters": {
                "type": "object",
                "properties": {
                    "email_id": {
                        "type": "string",
                        "description": "the email ID"
                    },

                },
                "required": ["email_id"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    23: {
        "type": "function",
        "function": {
            "name": "solver_23",
            "description": "Runs the given code on Google Colab to calculate the number of pixels with a certain minimum brightness",
            "parameters": {
                "type": "object",
                "properties": {
                    "lightness_threshold": {
                        "type": "number",
                        "description": "the minimum brightness as described in the python code snippet"
                    }
            
                },
                "required": ["lightness_threshold"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    24: {
        "type": "function",
        "function": {
            "name": "solver_24",
            "description": "Calculates the average marks of all students in the class and deploy in vercel",
            "parameters": {
                "type": "object",
                "properties": {
            
                },
                "required": [],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    25: {
        "type": "function",
        "function": {
            "name": "solver_25",
            "description": "Create a GitHub action on one of your GitHub repositories. Make sure one of the steps in the action has a name that contains your email address {email}.",
            "parameters": {
                "type": "object",
                "properties": {
                    "email": {
                        "type": "string",
                        "description": "the email ID"
                    }
                    

                },
                "required": ["email"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    26: {
        "type": "function",
        "function": {
            "name": "solver_26",
            "description": "Create and push an image to Docker Hub. Add a tag named {tag} to the image.",
            "parameters": {
                "type": "object",
                "properties": {
                    "tag": {
                        "type": "string",
                        "description": "the tag to be added"
                    }
                    

                },
                "required": ["tag"],
                "additionalProperties": False
            },
            "strict": True
        }
    },

    27: {},
    28: {},

    29: {
        "type": "function",
        "function": {
            "name": "solver_29",
            "description": "Analyze the sentiment of the given {meaningless_text} into GOOD, BAD or NEUTRAL using OpenAI's {model_name}",
            "parameters": {
                "type": "object",
                "properties": {
                    "model_name": {
                        "type": "string",
                        "description": "the model name"
                    },
                    "meaningless_text": {
                        "type": "string",
                        "description": "the meaningless text"
                    }
                    

                },
                "required": ["model_name", "meaningless_text"],
                "additionalProperties": False
            },
            "strict": True
        }
    },






}