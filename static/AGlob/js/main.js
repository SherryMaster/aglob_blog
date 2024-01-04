my_ajax = ({url, method = "POST", data = {}, csrf_token = "", success_funcs = [], error_funcs = [], complete_funcs = []}) => {
                    $.ajax({
                        url: url,
                        type: method,
                        data: {
                            csrfmiddlewaretoken: csrf_token,
                            ...data
                        },
                        success: function() {
                            // Code to be executed when the request is successful
                            success_funcs.forEach(func => {
                                func()
                            })
                        },
                        error: function(xhr, status, error) {
                            // Code to be executed when an error occurs
                            error_funcs.forEach(func => {
                                func(xhr, status, error)
                            })
                        },
                        complete: function() {
                            // Code to be executed when the request is complete
                            complete_funcs.forEach(func => {
                                func()
                            })
                            console.log("Request completed");
                        }
                    });
                }