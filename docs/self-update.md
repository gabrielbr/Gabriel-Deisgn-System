# Self-update

Every app updates itself the same way: it notices a new release when you open it, shows what's new,
and installs it with one tap after Android's own confirmation. This is PulseLoop's update feature,
made the standard for every app, with GMind's download checks added.

Status: ✅ PulseLoop (`com.pulseloop.update`) · 🟡 GVoice, GMind, GMoney, GHealth, GDesk
(`br.gabriel.ui.update` in the kit).

## What the person sees

1. **They open the app.** If a newer release is out, a sheet rises:
   **"Update available · {version}"**, the release notes under it, **Update · {size}** (the
   screen's one primary action; the size so nobody spends mobile data unknowingly) and **Later**.
2. **Update.** If Android hasn't yet let this app install apps, the app opens that setting first;
   they allow it, come back and tap Update again. Then the sheet shows **"Downloading… 41%"**, and
   in the Views kit the frame's line stands at 41% (the frame is the loading line for waits the
   person asked for). While it downloads, Later becomes **Cancel**, which stops the download and
   deletes the part; tapping outside or Back does nothing, so it can't vanish by accident. A big
   download (GMind's is hundreds of MB) must never trap the person.
3. **Android asks** "Do you want to update this app?". Nothing installs without that confirmation.
4. **Later** hides the sheet for that version until the app is next started from cold. A manual
   check always shows it.

**About** (or Settings → About) carries, in this order:

| Row | Content |
|---|---|
| Version | "{App} v{versionName} ({versionCode})" |
| Check for updates | A secondary button. Checking: "Checking…". Then one line: "You're on the latest version ({version})", or "Couldn't check for updates ({reason}). Try again.", or the update sheet. |
| Source, Licence | As the app has them. |

A debug or side-built copy can't update itself (its signing key differs), so instead of the button
it says "Self-update works in the release build only ({versionName} / {applicationId})."

## The rules

- **When it checks.** On every return to the foreground, cold start included, at most **once every
  15 minutes**. Repeat checks send `If-None-Match` with the last `ETag`; a `304` re-reads the cached
  release, so a release dismissed earlier is offered again next session. The manual check skips the
  15 minutes and the cache. A background job may refresh the cache; only the foreground shows UI.
- **What counts as newer.** The latest non-draft, non-prerelease release. With a tag
  `v{name}+{code}` (PulseLoop), compare the version code; with `v{x.y.z}` (the G apps, which share
  one version), compare x.y.z with the installed version name. Never offer an older or equal version.
- **Which file.** The app's own APK in the release's assets: PulseLoop the universal APK (else the
  device's ABI, else the first); the G apps by name prefix (`GVoice-…-arm64-v8a.apk`, `GMind-`,
  `GMoney-`, `GHealth-`, `GDesk-`). A release without one is "no update", never an error to show.
- **Checks before install, all required:**
  1. Over HTTPS only, and redirected to HTTPS only.
  2. The whole file arrived (the bytes match the asset's size). A short file is a failed download.
  3. Its **SHA-256 matches `SHA256SUMS.txt`** published in the same release. No published sum, no
     install. Every release workflow publishes that file.
  4. It is the same package and is signed with the installed app's key.
- **Honest failures.** "Couldn't check" is never shown as "up to date". Offline, rate-limited, or a
  bad reply each say so, with Try again. A failed download says so; the file is deleted.
- **One at a time.** One download per app process. A second tap while one runs does nothing.
- **Privacy.** The check is a plain unauthenticated request to GitHub's public API with the app's name
  as User-Agent. It sends nothing about the person or their data.
- **Permissions it needs:** `INTERNET` and `REQUEST_INSTALL_PACKAGES`. Each app's APK test allows
  both and says why.

## Words

Sentence case, verb first, no engine or vendor names beyond "GitHub" in a failure reason.

| English | Português (Brasil) |
|---|---|
| Update available · {0} | Atualização disponível · {0} |
| Update · {0} | Atualizar · {0} |
| Cancel | Cancelar |
| Later | Mais tarde |
| Downloading… {0}% | Baixando… {0}% |
| Check for updates | Procurar atualizações |
| Checking… | Procurando… |
| You're on the latest version ({0}). | Você está na versão mais recente ({0}). |
| Couldn't check for updates ({0}). Try again. | Não foi possível procurar atualizações ({0}). Tente de novo. |
| Download failed. Try again. | O download falhou. Tente de novo. |
| The download didn't match the release's checksum, so it wasn't installed. | O download não confere com a soma de verificação da versão, então não foi instalado. |
| Allow installs from this app, then tap Update again. | Permita instalações deste app e toque em Atualizar de novo. |
| Self-update works in the release build only ({0} / {1}). | A atualização automática só funciona na versão de lançamento ({0} / {1}). |
| Version | Versão |
| A new version is available. | Uma nova versão está disponível. |

## How it's built

### Compose (PulseLoop) ✅

`update/UpdateChecker.kt` (check, throttle, ETag, evaluate, download), `update/ApkInstaller.kt`,
`update/UpdateUi.kt` (`UpdateDialog`, `CheckForUpdatesButton`); the foreground check lives in
`PulseLoopApp` (ON_START observer, dismissed version kept with `rememberSaveable`); About in
`SettingsSubScreens.kt`. Text goes through `tr()`.

### Views kit (GVoice, GMind, GMoney, GHealth, GDesk) 🟡

`br.gabriel.ui.update` in `ui-kit`: `SelfUpdate` (the same rules, for the calling app's own
package), `Ui.updateSheet` (the sheet, with the frame's progress line) and `Ui.checkForUpdates` (the
About row). Each app calls `SelfUpdate.onForeground(activity)` from its launcher activity's
`onResume` and adds the About row. Installing goes through Android's `PackageInstaller`; its answer
comes back to a non-exported activity of the kit, so no app grows a receiver or a provider.

GMind keeps one extra job: installing GMoney, GHealth and GDesk the first time, from its invite
(`UpdatesActivity`). Updating each installed app is that app's own job.
