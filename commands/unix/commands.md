# Commands

### Perform Action on All Filenames Matching Given Pattern

```sh
find . -name "<pattern>" -type f -exec <action> {} \;

# Example makes all files called 'entrypoint.sh" executable
find . -name "entrypoint.sh" -type f -exec chmod +x {} \;
```
