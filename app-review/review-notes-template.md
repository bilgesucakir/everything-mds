---
domain: ios
part: templates
summary: App Review notes template and worked example
adapt: iOS only.
---

# App Review notes: template and example

Paste into **App Store Connect → App Review Information → Notes**. Apple asks for the same information when it sends a "Guideline 2.1 – Information Needed" message, and wants it in the Notes too. Keep the text specific; generic descriptions are rejected (Guideline 2.3.1(a)). The Notes field has a size limit (several thousand characters) **(check)**.

## Template

```
PURPOSE AND AUDIENCE
<What the app does, who it is for, what problem it solves.>

HOW TO SIGN IN AND TRY THE MAIN FEATURES
• Demo account: credentials are in the Sign-In fields (<n> sample items already added).
• <Feature 1>: where to tap, what to choose, what should happen.
• <Feature 2>: ...
• Registration: <steps; mention email verification and that the demo account does not need it>.
• Account deletion: <where it is, what it does>.
• Anything that needs a special device, location, email or code, and how to test it.

USER CONTENT, PAID CONTENT
• Is user content private or shared? If shared: filtering, reporting, blocking, contact.
• Purchases / subscriptions: none, or where they are.

EXTERNAL SERVICES USED
• Backend: <host>, database: <service>, file storage: <service>.
• Email: <service> (what it sends).
• Data and media: <providers, with credit and licence shown in the app>.
• Maps: <provider>. Analytics: none / <service>. Ads: none. AI services: none / <service>.

REGIONS
<Same in all regions, or what differs.> Languages: <list>.

REGULATED OR PROTECTED MATERIAL
<None, or the documents you attach.>

SUPPORT
<email>, <support page URL>
```

## Example (fictional app "Trailmark", a hiking diary)

```
PURPOSE AND AUDIENCE
Trailmark is a private hiking diary for iPhone. It is for hikers who want to remember
routes, photos and notes. Entries appear on the user's own map and list.

HOW TO SIGN IN AND TRY THE MAIN FEATURES
• Use the demo account in the Sign-In fields (8 hikes already added).
• Add a hike: Map tab > "+" > choose a photo, a place and a date > Save.
• Registration: Welcome > Create account. A verification link is emailed; the demo account needs no registration.
• Delete account: Profile > Settings > Delete Account (asks to confirm).

USER CONTENT, PAID CONTENT
• Entries and photos are private. There is no feed, sharing, comments or messaging, so there is nothing to report or block.
• No purchases, no subscriptions.

EXTERNAL SERVICES USED
• Own backend on <host>; database <service>; photos in <service>.
• Email: <service>, verification links only.
• Maps: Apple MapKit. No analytics, no ads, no AI service.

REGIONS
The same in all regions. English and German.

REGULATED OR PROTECTED MATERIAL
None.

SUPPORT
support@example.com, https://example.com/support
```

## Notes

- Also send the same text as your reply in the Resolution Center if Apple asked for information.
- If you add a screen recording, record it on a real device from the app launch through registration, the main flow and account deletion.
- On every release that adds a feature, describe the new feature in the notes.
