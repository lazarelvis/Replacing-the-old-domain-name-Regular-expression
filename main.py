#!/usr/bin/env python3

import re
import csv


def contains_domain(address, domain):
  """Returns True if the email address contains the given,domain,in the domain position, false if not."""
  domain_pattern = r'[\w\.-]+@'+domain+'$'
  if re.match(domain_pattern,address):
    return True
  return False


def replace_domain(address, old_domain, new_domain):
  """Replaces the old domain with the new domain in the received address."""
  old_domain_pattern = r'' + old_domain + '$'
  address = re.sub(old_domain_pattern, new_domain, address)
  return address

def main():
  """Processes the list of emails, replacing any instances of the old domain with the new domain."""
  old_domain, new_domain = 'abc.edu', 'xyz.edu'
  # path of the list user_emails.csv
  csv_file_location = '<csv_file_location>'
  # path for the resulting updated list within the variable report_file
  report_file = '<data-directory>' + '/updated_user_emails.csv'
  user_email_list = []
  old_domain_email_list = []
  new_domain_email_list = []

# data is read from the user_emails.csv file and passed to the user_data_list
  with open(csv_file_location, 'r') as f:
    user_data_list = list(csv.reader(f))
    user_email_list = [data[1].strip() for data in user_data_list[1:]]

# replace_domain will then take in the email addresses (with old domain) and replace them with the new domains
    for email_address in user_email_list:
      if contains_domain(email_address, old_domain):
        old_domain_email_list.append(email_address)
        replaced_email = replace_domain(email_address,old_domain,new_domain)
        new_domain_email_list.append(replaced_email)

# headers for our output file through the user_data_list, which contains all the data read from user_emails.csv file
    email_key = ' ' + 'Email Address'
    email_index = user_data_list[0].index(email_key)

# replace the email addresses within the user_data_list (which initially had all the user names and respective email addresses read from the user_emails.csv file) by iterating over the new_domain_email_list, and replacing the corresponding values in user_data_list
    for user in user_data_list[1:]:
      for old_domain, new_domain in zip(old_domain_email_list, new_domain_email_list):
        if user[email_index] == ' ' + old_domain:
          user[email_index] = ' ' + new_domain
  f.close()

# write the list to an output file within the variable report_file
  with open(report_file, 'w+') as output_file:
    writer = csv.writer(output_file)
    writer.writerows(user_data_list)
    output_file.close()

main()
