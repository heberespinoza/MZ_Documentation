import sys
import os
import inspect
import traceback
import importlib.util


def file_paths(directory):
    results = []
    for root, dirs, files in os.walk(directory):
        for name in files:
            if name.endswith(".py") and not name.endswith("__.py"):
                module_path = os.path.join(root, name)
                module_name = os.path.basename(module_path)
                results.append((module_name, module_path))
    return results


def paths_results(file_and_path, session, core_db, dwdb):
    summary = []
    results = []
    for module_name, module_path in file_and_path:
        spec = importlib.util.spec_from_file_location(module_name, module_path)
        foo = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = foo
        spec.loader.exec_module(foo)

        module_functions = [function_name for function_name in dir(foo) if callable(getattr(foo, function_name))]

        # for function_name in module_functions:
        #     module_function = getattr(foo, function_name)
        #     result = module_function(*args, **kwargs)  # Pass the parameter value to the function
        #     summary_str = f"Imported {module_function}"
        #     summary.append(summary_str)  # Store the result in the list
        #     results.append(result)

        for function_name in module_functions:
            module_function = getattr(foo, function_name)
            summary_str = f"Imported {function_name}"
            if "session" in module_function.__code__.co_varnames:
                result = module_function(session, core_db, dwdb)  # Pass session along with other parameters
                summary.append(summary_str)
            else:
                result = module_function(core_db, dwdb)  # Pass parameters excluding session
                summary.append(summary_str)

            results.append(result)

    print(summary)
    return results





# import sys
# import os
# import inspect
# import traceback
# import importlib.util
#
#
# def file_paths(directory):
#     results = []
#     for root, dirs, files in os.walk(directory):
#         for name in files:
#             if name.endswith(".py") and not name.endswith("__.py"):
#                 module_path = os.path.join(root, name)
#                 module_name = os.path.basename(module_path)
#                 results.append((module_name, module_path))
#     return results
#
#
# def execute_sp_folder(file_and_path, session):
#     summary = []
#     results = []
#     for module_name, module_path in file_and_path:
#         spec = importlib.util.spec_from_file_location(module_name, module_path)
#         foo = importlib.util.module_from_spec(spec)
#         sys.modules[module_name] = foo
#         spec.loader.exec_module(foo)
#
#         module_functions = [function_name for function_name in dir(foo) if callable(getattr(foo, function_name))]
#
#         for function_name in module_functions:
#             module_function = getattr(foo, function_name)
#             summary_str = f"Imported {function_name}"
#             if "session" in module_function.__code__.co_varnames:
#                 result = module_function(session)
#                 summary.append(summary_str)
#             # else:
#             #     result = module_function(database, schema)  # Pass parameters excluding session
#             #     summary.append(summary_str)
#
#             results.append(result)
#
#     print(summary)
#     return results
#
#
