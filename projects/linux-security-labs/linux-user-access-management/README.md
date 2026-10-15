# Linux User & Access Management Lab

This lab came from a university simulation focused on user administration and access control in Ubuntu.

## What I worked on

- Creating individual Linux users with home directories
- Reviewing user entries in `/etc/passwd`
- Creating and managing groups
- Adding users to specific groups
- Testing privileged actions with `su` and `sudo`
- Reviewing active sessions with `who` and `w`
- Configuring password expiration with `chage`
- Removing temporary accounts and groups when they were no longer needed

## Security concepts practiced

The activity focused on why individual accounts are better than shared generic accounts. Using personal accounts improves traceability because administrative actions can be linked to a specific user.

I also practiced using groups to assign access in a more organized way instead of configuring permissions user by user.

The privilege section showed why `sudo` is preferable to sharing the root password. Each administrator can use their own account while privileged actions remain easier to audit.

## Session review

I used `who` and `w` to review active users and basic system activity. In a real investigation, an unknown user or an unexpected process such as `nmap` could be a reason to investigate further.

## Password policy

For the lab, password expiration was configured with `chage` using a 45-day maximum age and a 5-day warning period.

## Cleanup

At the end of the activity, the temporary users and group were removed and `/etc/passwd` and `/etc/group` were checked to confirm the cleanup.

## Evidence

The original activity contains Ubuntu terminal screenshots. For the portfolio I keep selected screenshots with personal system identifiers censored.

Screenshots will be stored in the `screenshots` folder.

## Project context

This was completed as part of the Basic Operating Systems course at Universidad Fidélitas. The portfolio version keeps the Linux administration and security-related parts of the activity.
