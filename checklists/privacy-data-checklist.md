---
domain: general
part: checklists
summary: Data inventory, user rights, policy, store privacy answers
adapt: Skip 'Apple specifics' unless shipping on the App Store.
---

# Privacy and data checklist (apps with accounts)

Not legal advice. Laws that often apply: GDPR (EU), KVKK (Türkiye), CCPA (California), and children's rules (COPPA, age limits). Check what applies to your users.

## 1. Know your data

- [ ] A list ("data inventory") of every kind of data you collect: account (email, name, username), content (notes, photos), location, device, usage, diagnostics.
- [ ] For each: why you collect it, where it is stored, who else receives it, how long you keep it.
- [ ] A list of every **third-party service** that sees data: hosting, database, file storage, email sender, maps, analytics, crash reports, APIs you call.
- [ ] Data the user gives you vs data you derive (for example location from a photo).

## 2. User rights, built into the product

- [ ] **Account deletion** inside the app that removes the data (database, files, tokens), not only a "deactivate".
- [ ] A **data download** (export) of the user's data.
- [ ] A way to correct data (edit profile).
- [ ] Retention: say how long you keep data and what happens to backups.
- [ ] Age: how you handle users under the minimum age.

## 3. Documents

- [ ] A public **privacy policy** that matches the real behaviour, in the languages you ship; linked in the app (sign-up and settings) and in the store listing.
- [ ] Terms of use if you have accounts or user content; record which version each user accepted.
- [ ] A contact address for privacy requests that you monitor.
- [ ] Update the policy and the store privacy answers **together** whenever something changes.

## 4. Apple specifics
<!-- tags: domain=ios -->

- [ ] App Privacy ("nutrition label") answered per data type: linked to the user or not, used for tracking or not, purposes.
- [ ] Privacy manifest (`PrivacyInfo.xcprivacy`) matches the label; required-reason APIs have reasons.
- [ ] Permission purpose strings in every language.
- [ ] Analytics counts as data collection; "none" must really be none.

## 5. Third parties and content

- [ ] Each third-party service is named in the policy with what it receives.
- [ ] Images, sounds and data from other people: licence recorded, credit shown where required.
- [ ] If the app loads media straight from another site, that site sees the user's IP address; mention it.

## 6. Operations

- [ ] Backups: where, how often, how long kept, and whether deleted data leaves them.
- [ ] Access: who can read user data (admin panel, database), and are admin actions logged?
- [ ] No personal data in logs or error reports.
- [ ] A plan for a data breach: who you tell and how fast.
- [ ] Email limits and caps, so a bug or attack cannot send unlimited mail.
