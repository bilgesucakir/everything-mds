---
domain: ios
part: checklists
summary: What to verify before, during and after App Store review
adapt: iOS only.
---

# App Store review checklist (iOS)

A practical checklist for getting a first iOS app through App Review. Written after shipping a first version and answering a "Guideline 2.1 – Information Needed" request.

- **Last verified:** 2026-10-18 against the App Review Guidelines revision of **2026-10-16** (the newest on Apple's developer news page that day; guidelines 1.2, 2.3.14 and 2.5.19 were added or changed in it). Apple changes the rules and the App Store Connect screens often, so before each submission check https://developer.apple.com/news/ for a newer revision. Treat anything below as a starting point and check the sources at the end.
- **Mark items** `[x]` when done. Items marked **(check)** change often, so confirm them in App Store Connect or Apple's docs.

---

## 0. Before you start (every submission)

- [ ] **Check whether there is a new release of the App Review Guidelines.** Open https://developer.apple.com/news/ and look for "Updated App Review Guidelines" newer than the revision this checklist was verified against (see "Last verified" above). If there is one, read what changed in https://developer.apple.com/app-store/review/guidelines/ and update the checklist items that are affected before you submit.
- [ ] Also check the same news page for a new Apple Developer Program License Agreement and for new minimum Xcode/SDK requirements.

## 1. Accounts and agreements

- [ ] Apple Developer Program membership is active.
- [ ] The latest Program License Agreement is accepted (App Store Connect shows a banner when a new one is waiting; releasing can be blocked until it is accepted).
- [ ] EU trader status (DSA) is declared (Business → Compliance) if the app is sold in the EU. **(check)**
- [ ] A contact email that you read exists and is the same everywhere (App Store listing, support page, privacy policy, review contact).

## 2. Build

- [ ] Built with the Xcode and SDK version Apple currently requires for new submissions. **(check)**
- [ ] Know which SDK you build with: moving to the iOS 27.1 SDK triggers the iPhone Duo screenshot requirement (from April 2027). **(check)**
- [ ] Every target (app, widgets, extensions) has the **same version and build number**.
- [ ] Build number is **higher than every build ever uploaded**, even rejected or unused ones.
- [ ] Release configuration archive, destination "Any iOS Device (arm64)", signed, uploaded through Organizer or Transporter.
- [ ] `ITSAppUsesNonExemptEncryption` is set (usually `NO` if you only use standard HTTPS), so the export question is not asked on every upload.
- [ ] Tested on a **real device** on the latest iOS, from a fresh install (not just the simulator).
- [ ] No crashes, no dead buttons, no placeholder text, no "coming soon" screens.
- [ ] Works on a slow or offline connection: clear message, no endless spinner.
- [ ] Works with permissions **denied** (a refused permission must not break the app).
- [ ] IPv6-only networks work (use host names, not IPv4 addresses).
- [ ] The backend the app talks to is **live and stays live** for the whole review. Do not deploy or change it while the app is in review.

## 3. Permissions and privacy in the app

- [ ] Every permission has a clear, specific purpose string (what and why), in each language you ship.
- [ ] Permissions are asked **in context** (when the user taps the feature), not all at launch.
- [ ] Photo access: prefer the system photo picker (no permission needed); ask only for what you really need.
- [ ] Privacy policy is linked **inside the app** and in App Store Connect, and the page is public and working.
- [ ] Privacy manifest (`PrivacyInfo.xcprivacy`) is in the app target and matches what the app really does; third-party SDKs ship their own.
- [ ] If sign-up exists: **in-app account deletion** that really deletes the account and its data (not "email us", not "deactivate").
- [ ] Optional but expected by users: a way to download their data.
- [ ] No tracking prompt unless you really track across apps.
- [ ] Ask for ratings only with Apple's own system prompt (it is shown a limited number of times per year); no custom "rate us" popups that steer people to give five stars. **(check the guideline number: sources disagree)**

## 4. Accounts and user content

- [ ] If an account is not needed for the core features, allow use without one; otherwise say in the review notes why it is needed.
- [ ] Sign in with Apple is offered **if** you offer another third-party login (Google, Facebook, ...). Plain email and password does not trigger it.
- [ ] **User-generated content** (anything other users can see): filtering, a report button, blocking, published contact details (Guideline 1.2). If content is private to each user, say so clearly in the review notes. The 2026-10-16 update also covers non-consensual intimate imagery, including AI-generated.
- [ ] No hidden, dormant or undocumented features (Guideline 2.5.19). Anything surprising (secret badges, easter eggs, remote-enabled features) is mentioned in the notes.
- [ ] Features that arrive after review (server-driven content, remote flags) do not change what the app does in a way App Review has not seen.

## 5. Third-party content

- [ ] You have the right to use every image, sound, text and data set. Keep a list of sources and licences.
- [ ] Creative Commons and similar licences: show the credit and licence in the app where required; respect NonCommercial, NoDerivatives and ShareAlike terms.
- [ ] Answer **Content Rights** in App Store Connect honestly (yes if the app uses third-party content).
- [ ] APIs you call have terms that allow your use; note keys and quotas.

## 6. App Store Connect listing

- [ ] Name, subtitle, keywords (no competitor names, no keyword stuffing), description (only features that exist), promotional text.
- [ ] Every localization you ship is complete (including keywords and screenshots).
- [ ] Support URL works and shows a way to contact you.
- [ ] Category, copyright line, price (free or paid), availability (countries). **(check countries)**
- [ ] Age rating questionnaire answered honestly. **(check)**
- [ ] App Privacy ("nutrition label") answered and consistent with the policy, the privacy manifest and the real behaviour. Analytics or crash reporting counts.
- [ ] Accessibility section: claim only what you have tested. Support is usually published only **after** the app has a released version.
- [ ] Screenshots show the **real app in use** (not only a splash or login screen), use fictional data, and use a size Apple accepts for the slot. **(check sizes; a rejected size shows "File dimensions are invalid")**
- [ ] **iPhone Duo screenshots** (new device): from April 2027 they are required for apps built with the iOS 27.1 SDK or later. If you build with that SDK, add a Duo set. **(check)**
- [ ] No pricing, URLs, awards or other platforms' logos in screenshots or creative assets (Guideline 2.3.14 for header and search assets).
- [ ] Optional creative assets (product page header, search results asset) are suitable for all ages. They need the newest OS to show, so treat them as optional.

## 7. App Review information

- [ ] **Demo account** with working credentials, already holding sample data. Keep it working during the review and change its password afterwards.
- [ ] If sign-up needs email verification, explain it, and make sure the demo account does not.
- [ ] **Review notes** (use the template below). Be specific; generic notes are rejected (Guideline 2.3.1(a)).
- [ ] Contact name, phone and email are filled in and monitored.
- [ ] Attach a **screen recording from a real device** when the flow is not obvious (sign-up, deletion, hardware or location features). File types allowed in the attachment field are listed in App Store Connect; use lowercase extensions (`.mp4`, not `.MP4`).
- [ ] Release option chosen (manual release is safest for a first version).

Use `review-notes-template.md` for the structure and a worked example. The step-by-step order of work is in `submission-playbook.md`.

## 8. If App Review asks for information (Guideline 2.1)

New developer accounts are often asked for more information. A good reply:

1. Answer **every numbered point** Apple lists, in the same order.
2. Reply in the Resolution Center **and** paste the same text into the Notes field.
3. Attach the screen recording to the reply (zip if you have more than one file).
4. Resubmit (button name varies: "Update Review" or "Resubmit to App Review").
5. Do **not** change the build, the demo account or the backend while you wait.

## 9. While waiting

- Status "Waiting for Review" can last days, especially after a resubmission or a guideline update. Typical is 24 to 48 hours, but it is not guaranteed.
- A red mark next to "App Review" in the sidebar usually flags a message thread, not a new problem. Read the thread.
- "Last updated by Apple" only means the system touched the record.
- Do not click "Remove from Review" or "Cancel Submission" unless you really mean to start over.
- After about three days with no change, contact Apple through "Contact Us" and ask for a status check. Use expedited review only for real emergencies.
- Use the time to prepare: release notes, site links, a list of things to test on the live listing.

## 10. After approval

- [ ] Release (if you chose manual), then check the live listing in the store.
- [ ] Install from the App Store on a clean device; sign up, use the main flow, delete the account.
- [ ] Publish accessibility support in App Store Connect if it is waiting for a released version.
- [ ] Change the demo account password.
- [ ] Put the store link on your website and README.
- [ ] Watch crash reports and reviews for the first days.
- [ ] Next release: describe new features **specifically** in the review notes; keep the privacy label and policy in sync.

## 11. Common rejection reasons (quick list)

| Guideline | Short version |
|---|---|
| 2.1 | Crashes, broken flows, missing demo account, information needed |
| 2.3.1(a) | New features not described in the notes; misleading marketing |
| 2.3.3 | Screenshots show only a splash or login screen |
| 2.5.19 | Hidden or undocumented features |
| 4.8 | Third-party login without an equivalent privacy-friendly option |
| 5.1.1 | Privacy policy missing, no account deletion, permissions not explained |
| 1.2 | User content without filtering, reporting, blocking and contact |

## Sources

- App Review Guidelines: https://developer.apple.com/app-store/review/guidelines/
- App Store Connect Help: https://developer.apple.com/help/app-store-connect/
- Apple developer news (guideline updates): https://developer.apple.com/news/
- Asset best practices: https://developer.apple.com/app-store/asset-best-practices/
