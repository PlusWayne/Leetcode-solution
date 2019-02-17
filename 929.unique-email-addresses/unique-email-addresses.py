class Solution:
    def numUniqueEmails(self, emails: 'List[str]') -> 'int':
        for i in range(len(emails)):
            split_email = emails[i].split('@')
            split_email[0] = split_email[0].replace('.','')
            if '+' in split_email[0]:
                nums = split_email[0].index('+')
                split_email[0] = split_email[0][0:nums]
            emails[i] = '@'.join(split_email)
        return len(set(emails))
