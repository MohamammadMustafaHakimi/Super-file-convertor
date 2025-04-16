# import os
# import subprocess

# def fun(input_path, output_folder):
#     os.makedirs(output_folder, exist_ok=True)

#     subprocess.run(
#         [
#             'libreoffice',
#             '--headless',
#             '--convert-to',
#             'pdf',
#             input_path,
#             '--outdir',
#             output_folder
#         ],
#         check=True
#     )


# fun("./files/Movie_Data_Analysis_Project.docx", "generated_pdfs")

import os
import subprocess

def fun(input_path, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    # Get the base filename (without .docx)
    base_name = input_path.split("/")[-1][:-5]
    output_file = f"{base_name}.pdf"
    full_output_path = os.path.join(output_folder, output_file)

    # Check for existing files and modify name if needed
    counter = 1
    while os.path.exists(full_output_path):
        output_file = f"{base_name}({counter}).pdf"
        full_output_path = os.path.join(output_folder, output_file)
        counter += 1

    # Run the conversion
    subprocess.run(
        [
            'libreoffice',
            '--headless',
            '--convert-to',
            'pdf',
            input_path,
            '--outdir',
            output_folder
        ],
        check=True
    )

    # Rename if we need a numbered version
    if counter > 1:
        original_output = os.path.join(output_folder, f"{base_name}.pdf")
        os.rename(original_output, full_output_path)

fun("./files/Movie_Data_Analysis_Project.docx", "generated_pdfs")
