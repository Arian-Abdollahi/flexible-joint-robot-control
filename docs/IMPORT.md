# Complete the flexible-joint project import

A Git-ready 55-file ZIP has been prepared from the supplied flexible-joint control materials. Only experiments **5–8** are included, covering lead, lag, lead–lag and state-feedback controllers. The ball-and-beam materials from Report 4 were **not** included.

## Upload once using GitHub

1. Download **`flexible-joint-robot-control-GitHub-upload.zip`** from the ChatGPT conversation. This cleaned archive excludes generated Python bytecode files.
2. Open the [import branch](https://github.com/Arian-Abdollahi/flexible-joint-robot-control/tree/import/flexible-joint-experiments).
3. Choose **Add file → Upload files**.
4. Upload **the ZIP itself** to the repository **root** (do not extract it); do **not** upload a `.bundle` file or any of the original RAR archives.
5. Click **Commit changes** to `import/flexible-joint-experiments`, not `main`.
6. Review [Import verified flexible-joint archive](https://github.com/Arian-Abdollahi/flexible-joint-robot-control/actions) in GitHub Actions. The importer checks SHA256, all expected paths, and Simulink ZIP integrity, removes the temporary ZIP, runs six source tests, then commits the project into the same branch.
7. Review the [Pull Request](https://github.com/Arian-Abdollahi/flexible-joint-robot-control/pulls) and the final integrity-check results before merging.

The expected ZIP SHA256 is:

```text
9ebabe8e10d0222563009676fc1f18ff7a482535462f3fd67c89d80b8892fde8
```

The ZIP filename can change, but **its bytes must not**. Only one root-level ZIP should be uploaded.

## Project contents and caveats

- 4 original report PDFs, 3 Simulink `.slx` models, 5 MATLAB scripts, saved figures/`.mat` data, and LaTeX report sources.
- Structural checks can verify file integrity but **cannot certify controller performance**; no MATLAB simulation was rerun.
- Original report credits are preserved. The repository is kept private initially because the source reports may include contributor details.
- No ball-and-beam source files are included. Do not merge the PR while the ZIP and extracted contents are still missing.
