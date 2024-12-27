# Import library

import csv

import openai
import os
from dotenv import load_dotenv

load_dotenv()

# Accessing the OPENAI KEY
openai.api_key = os.getenv("OPENAI_API_KEY")


def get_completion(prompt):
    """
    Function to create response from OpenAI model
    """
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0,
    max_tokens=300,
    )

    return response["choices"][0]["text"]

def convert_result_to_csv(results):
    """
    Write response from get_completion function
    to CSV file
    """
    csv_path = 'src/extracted_address.csv'

    try:
        # Open the file in append mode if it exists, otherwise create it
        with open(csv_path, 'a' if os.path.exists(csv_path) else 'w') as file:
            csv_writer = csv.writer(file)
            if not os.path.exists(csv_path):
                csv_writer.writerow(['street1, sub-district, district, province, zip-code'])
            csv_writer.writerow([results])
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    # Test
    address_input = input("ระบุที่อยู่: ")
    prompt = """
  แยกข้อมูลที่อยู่ จากข้อความที่อยู่ในเครื่องหมาย backtics
โดยแยกข้อมูลออกเป็น (บ้านเลขที่, ตำบล, อำเภอ, จังหวัด, เลขไปรษณีย์)
หากไม่มีข้อมูลดังกล่าวให้ระบุ เป็น -

ข้อความ
```{address}```

แสดงผลในรูปแบบของ CSV format
        """


    prompt=prompt.format(address=address_input)
    print(prompt)

    response = get_completion(prompt)
    print(response)

    # convert response to csv format

    # Example
    # result = '41/101, นวมินทร์24, บึงกุ่ม, คลองกุ่ม, กทม., 74000'
    # convert_result_to_csv(result)
