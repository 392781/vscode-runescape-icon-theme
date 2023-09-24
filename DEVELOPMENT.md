# Development Instructions

## Making changes to icons

1. Build the development container.
2. Make changes to `src/icons.json`
    - `iconDefinitions` link an icon definition to an icon location
    - `fileExtensions` link an ending extension to an icon definition
    - `fileNames` link a whole file name to an icon definition
3. Testing icons can be done by hitting "Run" -> "Run without debugging".  When asked, navigate and select the `test/` folder to be your workspace.  `test/` contains all the various supported extensions.  Depending on the icon change, you may need to reload the window (`ctrl-r`) for the change to appear.
4. (For Ron only) Once you're happy with your changes and everything is looking good, you're ready to publish!

## Publishing (For Ron only)

1. Begin by modifying `CHANGELOG.md`.  Add a new entry with a major/minor/patch update.  Describe the changes, save the file.
2. Stage and commit all the changes. *DO NOT PUSH YET*.
3. Run `vsce ls` to view the items that will be published.  The only items that should be contained are:
    - `assets/**`
    - `CHANGELOG.md`
    - `icons/**`
    - `LICENSE`
    - `package.json`
    - `README.md`
    - `src/extension.js`
    - `src/icons.json`

    If **anything else** is in this list, remove it by adding an entry to `.vscodeignore` (the ignore file for `vsce` publishing).
4. Run `vsce publish <version>` where you can replace `<version>` with a specific version number (e.g. `1.1.1`) or one of the 3 keywords: `major`, `minor`, `patch` indicating the version bump size.
5. Double check the status of the git repository and push all the changes!
