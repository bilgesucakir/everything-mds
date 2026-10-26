---
domain: ios
part: playbooks
summary: Order of work for a first App Store submission
adapt: iOS only.
---

# App Store submission playbook (first release)

The order of work for shipping an iOS app, with the traps that cost time. Pair it with `app-store-review-checklist.md` (what to verify) and `review-notes-template.md`. Screen names and size limits change, so items marked **(check)** need confirming in App Store Connect.

## 0. Check for new rules

- Before you start, check https://developer.apple.com/news/ for a **new release of the App Review Guidelines** (and a new Program License Agreement or Xcode/SDK requirement). Compare it with the "Last verified" revision in `app-store-review-checklist.md` and update the checklist first.

## 1. Versions and build numbers

- The **version** (for example `1.0.0`) is what users see. The **build number** is a counter.
- A build number can **never be reused**, even for a build that was rejected or never selected. Xcode may renumber an archive you rebuild, so read the number in Organizer before you upload.
- All targets (app, widgets, extensions) must have the **same version and build number**.
- Changing the build after you submitted means removing the version from review. That puts you back in the queue. Avoid it.

## 2. Archive and upload

1. Choose the scheme and destination **Any iOS Device (arm64)**.
2. **Product → Archive**.
3. Organizer → select the archive → **Distribute App → App Store Connect → Upload**.
4. Wait for the processing email; the build shows up in App Store Connect after a few minutes.
5. Xcode may edit `Info.plist`, `project.pbxproj` or string catalogs on its own. Those edits are harmless; do not mix them into feature commits.

## 3. Create the version in App Store Connect

- Add the build (the "+" next to Build). It may show a warning icon first while it processes.
- Fill the listing for **each language** you ship: promotional text, description, keywords, support URL, screenshots.
- Choose **manual release** for a first version, so nothing goes live before you check it.
- Pricing, availability (countries), age rating, Content Rights, App Privacy, and Accessibility each have their own page. All must be complete before the "Add for Review" button works.

## 4. Screenshots

- Each device size has its own slot, and the accepted pixel sizes change **(check)**. In one case the "6.1/6.3 inch" slot accepted 1179×2556 and 1206×2622 (and their landscape versions) but rejected 1320×2868 with "File dimensions are invalid". Read the hint text next to the upload box before you design.
- Screenshots must show the app in use, with fictional data.
- Make them in each language you ship.
- From April 2027, **iPhone Duo** screenshots are required for apps built with the iOS 27.1 SDK or later; plan a set for them **(check)**.
- If you change a screenshot later, you can replace it without a new build.

## 5. App Privacy and accessibility

- Answer the privacy questions from what the app and every service it uses really collect, then compare with the privacy policy and the privacy manifest.
- Accessibility support can be drafted before release but is usually published **after** the app has a released version. Claim only what you tested.

## 6. Submit

- Add the demo account and notes (`review-notes-template.md`).
- Attach a screen recording from a real device if flows are not obvious.
- Press **Add for Review**, then **Submit to App Review**.
- Do not change the build, the demo account or the backend until you have a decision.

## 7. If Apple asks for information (Guideline 2.1)

1. Read the numbered list; answer each point in order.
2. Reply in the Resolution Center and paste the same text in the Notes field.
3. Attach the recording to the reply. The attachment field accepts a limited list of types, with **lowercase** extensions; if you have two videos, zip them.
4. Resubmit (**Update Review** or **Resubmit to App Review**, depending on the screen).
5. Check that the status says **Waiting for Review**. The submission row shows the date and "Last updated by Apple" after Apple's system touches it; that is normal.

## 8. Waiting, approval and release

- Waiting time varies from hours to several days. See the checklist section "While waiting".
- On approval: release manually, install from the store, test the main flow, publish accessibility support, change the demo account password, update your website and README with the store link.

## 9. Updates

- New version number, new unique build number, new "What's New" text (specific).
- Describe new features in the review notes. Keep the privacy label and policy in sync.
- Back-end changes the new build depends on must be live **before** you release.
