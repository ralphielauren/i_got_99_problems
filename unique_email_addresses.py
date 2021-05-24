"""
UNIQUE EMAIL ADDRESSES
-----------------------
https://leetcode.com/problems/unique-email-addresses/

Given an array of strings emails where we send
one email to each email[i], return the number
of different addresses that actually receive mails.

Constraints:

1 <= emails.length <= 100
1 <= emails[i].length <= 100
email[i] consist of lowercase English letters, '+', '.' and '@'.
Each emails[i] contains exactly one '@' character.
All local and domain names are non-empty.
Local names do not start with a '+' character.

-- Every valid email consists of a local name and a domain name,
separated by the '@' sign. Besides lowercase letters, the
email may contain one or more '.' or '+'.

For example, in "alice@leetcode.com", "alice" is the local name,
and "leetcode.com" is the domain name.

-- If you add periods '.' between some characters in the local name
part of an email address, mail sent there will be forwarded to the
same address without dots in the local name. Note that this rule
does not apply to domain names.

For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward
to the same email address.

-- If you add a plus '+' in the local name, everything after the first
plus sign will be ignored. This allows certain emails to be filtered.
Note that this rule does not apply to domain names.

For example, "m.y+name@email.com" will be forwarded to "my@email.com".
It is possible to use both of these rules at the same time.
"""
from typing import List


class Solution:

    def num_unique_emails(self, emails: List[str]) -> int:

        assert 1 <= len(emails) <= 100

        seen_emails = set()
        for email in emails:

            assert email.islower()
            assert 1 <= len(email) <= 100
            assert email.count("@") == 1
            assert email[0] != "+"

            local_name = email.split("@")[0].replace(".", "").split("+")[0]
            domain_name = email.split("@")[1]

            assert local_name != ""
            assert domain_name != ""

            seen_emails.add(local_name + "@" + domain_name)

        return len(seen_emails)
