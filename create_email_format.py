# Create email format using full name and string methods


full_name = input("enter your full name: ")

company_name = input("enter your company name: ")

splitted_full_name = full_name.split()

joined_full_name = ".".join(splitted_full_name)

splitted_company_name = company_name.split()
joined_company_name = "".join(splitted_company_name)

predicted_email = f"{joined_full_name}@{joined_company_name}.com.au".lower()

print(predicted_email)