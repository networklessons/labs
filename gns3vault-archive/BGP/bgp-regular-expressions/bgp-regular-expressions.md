# BGP Regular Expressions

## Scenario

As a trainee you are starting your network career at a big service provider. One of your tasks in the future will be to configure BGP connecting multiple AS'es to the service provider network. However you are still studying and BGP holds many secrets for you...one of them is how regular expressions work, time for some lab exercises!

This lab does not use GNS3 because I believe it's more fun to use a looking glass server, you will find the URL of a public route server at the bottom of this article.

## Goal

- Check out the URL at the bottom of this article, open it and scroll to the bottom. Find one of the public route servers and telnet into it.
- Use 'show ip bgp' just to take a look at some information in the routing table.
- See if you can create the following regular expressions to solve some questions, in this example I'm using AS 3491 but another AS you see with the 'show ip bgp' command is fine.
- Use the 'show ip bgp regexp' command to enter the regular expressions.
- Create a regular expression that only shows AS 3491.
- Create a regular expression that shows AS 3491 at the beginning, and everything behind it. For example:
  - 3491 5423 5431 5434
- Create a regular expression that shows all networks that originate in AS 3491
- Create a regular expression that only shows the locally originated networks.
- Create a regular expression that shows everything where AS 3491 is in the middle of the AS-PATH.
- Create a regular expression that shows all networks that are originated by your directly connected AS neighbors.

## IOS

None needed

## Topology

Check out of the following link for "looking glass" servers, these are routers you can telnet into and use 'show ip bgp' commands to practice with:

**<http://www.bgp4.as/looking-glasses>**

Scroll to the bottom for the 'telnet' access route servers.

## Video Solution

http://www.youtube.com/watch?v=HRkMjBS6XWs
