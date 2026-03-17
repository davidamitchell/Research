# Transcript unavailable — QT7W_uHjqWE

Automated fetching failed. YouTube blocks transcript requests from GitHub Actions
IP ranges (AWS/GCP). This is a hard network-level restriction with no reliable
workaround from a cloud runner.

## How to add the transcript manually (GitHub website only — no IDE needed)

### Step 1 — Copy the transcript from YouTube
1. Open the video: <https://www.youtube.com/watch?v=QT7W_uHjqWE>
2. Click the **"⋮"** (three-dot) menu **below** the video player
3. Click **"Open transcript"**
4. In the transcript panel that opens on the right, click its own **"⋮"** →
   **"Toggle timestamps"** to remove the timestamps
5. Select all the text in the transcript panel and copy it

### Step 2 — Create the transcript file on GitHub
1. Go to: <https://github.com/davidamitchell/Research/new/main>
2. In the "Name your file…" box, type exactly:
   `Research/transcripts/QT7W_uHjqWE.txt`
3. Paste the copied transcript text into the editor
4. Scroll down, choose **"Commit directly to the `main` branch"**,
   and click **"Commit new file"**

### Step 3 — Ask @copilot to process it
Comment on the open pull request:

```
@copilot The transcript for QT7W_uHjqWE is now at Research/transcripts/QT7W_uHjqWE.txt —
please re-run the research synthesis using it.
```
