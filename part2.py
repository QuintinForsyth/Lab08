import summonFile as s

def create_email(people):
  """
  makes emails for studentsand sends them back in a list
  """
  emails = []
  for person in people:
    emails.append(f"{person[2].lower()}{person[1][0]}@whatever.com")
  return emails
people = s.csv21list("people.csv")
  

emails = create_email(people)
for mails in emails:
  print(mails)