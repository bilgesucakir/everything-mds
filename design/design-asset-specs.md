# Design asset specs (iOS, App Store)

Pixel sizes and rules for the assets you make in a design tool. Apple changes these; every row marked **(check)** should be confirmed in App Store Connect before you spend hours designing. Last checked: 2026-10-18.

## App icon

- 1024×1024, no transparency, no rounded corners (iOS applies the mask).
- Use **Icon Composer** (`.icon` files) for layered icons with Dark and Tinted/Mono looks.
  - Default, Dark and Mono (tinted) are previewed in the bottom-right corner of Icon Composer.
  - **Different artwork for Default and Dark (two groups):**
    1. Make **two groups** in the layer list. Put the Default PNG in group 1 and the Dark PNG in group 2.
    2. Select the **Default** look (preview in the bottom-right corner). Set the group 1 PNG to **100% opacity** and the group 2 PNG to **0%**.
    3. Select the **Dark** look. Set the group 1 PNG to **0%** and the group 2 PNG to **100%**.
    4. Check the Default, Dark and Mono previews. This way each look can use a completely different PNG (for example a black bird for Default and a coloured bird for Dark).
    - Mono (tinted) can use its own opacity settings the same way.
    - Tip: give the files matching names (`name_default.png`, `name_dark.png`) so it is obvious which group holds which.
  - Large source images for layers: 3840×2160 is a safe size. Layers that are scaled up a lot get soft in large previews, but not on the home screen.
- Alternate icons (seasonal): add each `.icon` package to the target, and list the names in the build setting `ASSETCATALOG_COMPILER_ALTERNATE_APPICON_NAMES`. The package name is the icon's id.
- File names inside packages: use plain ASCII names (`halloween_default.png`), no spaces or accented letters.
- Keep one recognisable shape across variants so the app is easy to find on the Home Screen.

## Screenshots

- Required for at least the largest iPhone size; smaller sizes are scaled **(check)**.
- Accepted sizes for one slot (6.1/6.3 inch "medium"): 1179×2556, 1206×2622 and their landscape versions. 1320×2868 was rejected there with "File dimensions are invalid". Read the hint next to the upload box.
- PNG or JPEG, no transparency.
- **iPhone Duo (new device, announced October 2026):** App Store Connect now shows a banner "Preparing for iPhone Duo". Starting in **April 2027**, screenshots for iPhone Duo are **required for any app built with the iOS 27.1 SDK or later**. Apps built with older SDKs are not affected yet. The device shipped on 2026-10-23 per Apple's news. You can already upload Duo screenshots in App Store Connect. Plan for an extra set in each language, and check the exact pixel sizes in the upload box before designing **(check)**. Source: Apple developer news "Preparing for iPhone Duo" (2026-10-05) and the App Store Connect banner.
- Show the app in use, with fictional data. No prices, URLs, awards or other platforms' logos.
- Make a set for every language.
- Keep text short and large; headlines are read at thumbnail size.

## Product page header and search results asset (optional, newest OS only) **(check)**

| Asset | Image size | Notes |
|---|---|---|
| Product page header | 21:9, 3840×1646 | A banner above the icon and screenshots; image or video |
| Search results asset | 3:2, 1920×1280 up to 3840×2560 | Shown in search results instead of the default screenshots |
| One image for both | 16:9 PNG, 5244×2950 | The only size both accept; keep the subject in the centre |

- No transparency. Video: 5 to 30 seconds, muted, loops **(check)**.
- Rules (Guideline 2.3.14): about your app or brand, suitable for all ages, no unverifiable claims, no prices or discounts, no references to other apps meant to mislead.
- Keep icon, header and first screenshot telling the **same story** (same colours, same promise).
- Preview in App Store Connect before publishing.

## Other places images appear

- Website social preview: 1200×630.
- Favicon and touch icon: a square PNG at 180×180 for `apple-touch-icon`.
