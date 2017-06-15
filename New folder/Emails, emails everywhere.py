counter=int(input())

emails={'lak':-1}
for i in range(counter):
    query=input()
    if 'store' in query:
        stored=[x for x in query.split(' ')]
        emails[stored[1]]=int(stored[2])
    else:
        getEmailsKey=[key for key,val in emails.items() if val==max(emails.values())]
        print(getEmailsKey[len(getEmailsKey)-1])



