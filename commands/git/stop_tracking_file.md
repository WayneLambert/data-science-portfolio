# Stop Tracking File

`.gitignore` will prevent untracked files from being added (without an add -f) to the set of files tracked by git, however git will continue to track any files that are already being tracked.

To stop tracking a file you need to remove it from the index. This can be achieved with this command.

`git rm --cached <filename>`

If you want to remove a whole folder, you need to remove all files in it recursively.

`git rm -r --cached <folder-name>`

The removal of the file from the head revision will happen on the next commit.

**WARNING:** While this will not remove the physical file from your local, it will remove the files from other developers machines on next git pull.

**Source:** <https://stackoverflow.com/questions/1274057/how-to-make-git-forget-about-a-file-that-was-tracked-but-is-now-in-gitignore>
