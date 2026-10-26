---
domain: web, ios
part: checklists
summary: UI quality checks for apps and websites
adapt: Parts A-C are shared; D and the phone test are iOS; E is web.
---

# UI quality checklist (apps and websites)

Things that make a product feel unfinished or untrustworthy, grouped by area, plus a ten-minute phone test and the tools that help. Part A comes from a list that circulates among developers who build apps quickly with AI help; Parts B to E come from checklists used on a real app (accessibility, honest design, platform guidelines). Nothing here is Apple policy unless it says so, but reviewers and users notice these things.

Last verified: 2026-10-18.

## Part A: the 20 "looks unfinished" checks

| # | Check | What to look for |
|---|---|---|
| 1 | Empty states | Every list and screen has a friendly message when there is no data |
| 2 | Visual hierarchy | Primary, secondary and destructive buttons look different (not all the same blue) |
| 3 | Error messages | Specific messages (offline, timeout, session ended, validation), not "Something went wrong" everywhere |
| 4 | Loading | Every request has a timeout; a failed load shows a retry, never an endless spinner |
| 5 | Keyboard | The keyboard never covers the field being typed in; scrolling or tapping outside dismisses it |
| 6 | Navigation | Back button and swipe-back work on every screen |
| 7 | Dark mode | No white flash or unreadable text; the launch screen follows the system |
| 8 | Touch targets | Tappable areas are at least about 44 points |
| 9 | Safe areas | Nothing sits under the notch, Dynamic Island or home indicator |
| 10 | Placeholder text | No "lorem ipsum", "TODO", sample names or dummy data |
| 11 | Language | All text is translated in every language you ship |
| 12 | Dates and numbers | Use the system formatters so language and region are respected |
| 13 | Confirmation | Destructive actions ask first (delete, log out of all devices) |
| 14 | Haptics | Light feedback on important successes and errors |
| 15 | Animation | Screens and state changes transition instead of jumping |
| 16 | Permission reasons | Each permission has a clear, specific purpose string |
| 17 | Permission timing | Asked when the feature is used, never all at launch |
| 18 | Account deletion | Reachable in the app and really deletes the account |
| 19 | App icon | A custom icon, not the template |
| 20 | Testing | Someone has really used the app from a clean install on a real device |

## Part B: accessibility

**Image descriptions (the app equivalent of alt text)**
- [ ] Meaningful images (photos, avatars, badge icons) have an accessibility label.
- [ ] Decorative images are hidden from VoiceOver.
- [ ] Icon-only buttons (toolbar items, map controls, close buttons) have labels.
- [ ] Map pins and clusters read well aloud ("Robin, seen 3 May").
- [ ] Labels are translated in every language.

**Contrast and colour**
- [ ] Text and controls meet WCAG AA: **4.5:1** for normal text, **3:1** for large text and controls. Check light mode, dark mode, and text over images, maps and glass or blur effects.
- [ ] "Increase Contrast" and "Reduce Transparency" are supported; blurred or glass surfaces stay readable.
- [ ] Colour is never the only way to show information (a status also has text or an icon).
- [ ] Use semantic system colours and fix contrast in the colour assets or theme, not screen by screen.

**VoiceOver, text size, input and motion**
- [ ] The whole app works with VoiceOver in a logical reading order; related elements are grouped.
- [ ] Text scales with Dynamic Type up to the accessibility sizes without being cut off or overlapping (use text styles, not fixed point sizes).
- [ ] Custom gestures (swipe to delete, long press) have an accessible alternative (a context menu, an action, or a visible button).
- [ ] Tap targets are at least 44×44 points.
- [ ] Full Keyboard Access works in the main flows (sign up, log in, the main task).
- [ ] Animations respect "Reduce Motion".
- [ ] In the store listing, claim only the accessibility features you have really tested.

## Part C: honest design (no dark patterns)

- [ ] No confirmshaming ("No thanks, I don't like saving money").
- [ ] No fake countdowns, fake "only 2 left", or made-up activity counts.
- [ ] Logging out, deleting the account, cancelling and turning off notifications are as easy to find as signing up.
- [ ] No pre-prompts that push people to accept a permission or hide a "Not now" option.
- [ ] No nagging for ratings: use the system review prompt only, at a natural moment, and never reward ratings.
- [ ] No fake reviews, testimonials, star ratings or user counts; search the code and string files.
- [ ] No unsupported claims ("best", "#1", "guaranteed", "100% accurate", "identifies anything") in the app, onboarding, empty states, store text or screenshots.
- [ ] If there are purchases: prices shown from the store API, billing period and trial terms visible before buying, links to terms and privacy, and a Restore Purchases button. If there are none, say so.
- [ ] The app shows who made it and how to contact them (an About or Settings screen with the version).

## Part D: platform guidelines (Apple)
<!-- tags: domain=ios -->

- [ ] Use standard system components (navigation, tab bars, toolbars, lists, sheets, alerts, menus) before inventing your own.
- [ ] Follow the current Human Interface Guidelines for the OS version you target, including how materials and glass effects, tab bars, search and toolbars behave. The guidelines change every major release; check the "what changed" notes.
- [ ] Use the platform's accent and brand colour guidance; keep one accent colour for interactive elements.
- [ ] App icon: follow the current icon guidance (layers, light, dark and tinted looks).
- [ ] New device sizes (for example the foldable iPhone Duo) resize correctly if you build for the newest SDK.
- [ ] Before designing a screen or component, open the matching HIG page.

## Part E: websites
<!-- tags: domain=web -->

- [ ] Review the page against the Web Interface Guidelines (see tools below): semantics, labels, focus states, forms, images, motion, performance, dark mode.
- [ ] Choose a design direction on purpose (colours, typography, spacing) instead of a generic template; write it down in a `DESIGN.md`.
- [ ] Fonts: licence checked, self-hosted if possible, with characters for every language (see `design/fonts.md`).
- [ ] Works at phone width with no horizontal scroll; every page has a title, description and social preview image.
- [ ] Contrast, keyboard focus and "prefers-reduced-motion" tested.

## Ten-minute phone test
<!-- tags: domain=ios -->

1. **Airplane Mode:** open every tab; check for a clear message and a retry.
2. **Keyboard:** open the longest form and the notes field with the keyboard up.
3. **Dark mode:** switch, kill the app, reopen; look for a white flash.
4. **Large text:** set a big text size; open the main screens and forms.
5. **VoiceOver:** turn it on and move through one screen and one form.
6. **Swipe back** from every screen.
7. **Permissions:** deny each one and use the feature anyway.
8. **Slow network:** use Network Link Conditioner or move away from Wi-Fi.
9. **Fresh install:** delete the app, install, register, use the main flow, delete the account.
10. **Interrupt:** background the app mid-save and return.

Code can answer some points (search for hardcoded colours, placeholder strings, `ignoresSafeArea`, fixed font sizes, missing accessibility labels, number of translated strings). The rest needs a real device. Add automated UI tests for the flows that matter once the app is stable.

## Tools and skills that help
<!-- tags: domain=general -->

These are AI-assistant skills or reference collections. Install them as the project documents each one; check the licence before copying files into your own repository.

| Tool | Use it for | Link |
|---|---|---|
| **Apple Human Interface Guidelines** (and an `apple-hig` skill made from them) | Platform rules for iPhone design; a skill can hold the pages as markdown and be refreshed when Apple updates them | https://developer.apple.com/design/human-interface-guidelines/ |
| **Web Interface Guidelines** (`web-design-guidelines` skill, by Vercel) | Reviewing UI code for accessibility, forms, focus, motion, performance | https://github.com/vercel-labs/web-interface-guidelines |
| **awesome-design-md** (by VoltAgent, MIT) | 74 ready-made `DESIGN.md` references from well-known products (colours, type, spacing, components) to pick a direction or write your own `DESIGN.md` | https://github.com/VoltAgent/awesome-design-md |
| **design-taste-frontend** (by Leonxlnx, MIT) | A skill for landing pages, portfolios and redesigns that avoids generic template looks | repository link not verified; search for "tasteskill" by Leonxlnx |
| **frontend-design** (Anthropic plugin) | Guidance for distinctive, intentional visual design when building or reshaping a UI | bundled as an Anthropic plugin in Claude Code |

The GitHub links for the Web Interface Guidelines and awesome-design-md are built from the repository names in each skill's own metadata; open them once to confirm before sharing this file.
