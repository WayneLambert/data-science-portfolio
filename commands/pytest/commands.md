# PyTest Commands

A list of commands for PyTest. As usual, when developing within a docker container, precede the command with `docker-compose exec web` where web is the canonical name given to the service for my Django project.

## Testing Commands

### Collect a List of All Tests in the Project

```sh
docker-compose exec web pytest --collect-only
```

### Run an Individual Unit Test in Debug Mode

```sh
docker-compose exec web pytest <dir_name>::<class_name>::<func_name> --pdb
```

### Run an Individual Unit Test in Debug Mode (Stepping Through)

```sh
docker-compose exec web pytest <dir_name>::<class_name>::<func_name> --trace
```

### Run an Individual Unit Test in Debug Mode using iPDB

```sh
docker-compose exec web pytest <dir_name>::<class_name>::<func_name> --pdb --pdbcls=IPython.terminal.debugger:Pdb
```

### Run Additional Unit Tests Marked with a Given Marker

In this example, all tests with the `runslow` marker are included within the test run. These markers are configured in the top level `conftest.py`.

```sh
docker-compose exec web pytest <dir_name>::<class_name>::<func_name> --runslow
```

***

## Keyboard Shortcuts for PDB

- $ `l` = list
- $ `ll` = long list
- $ `s` = Step Into
- $ `c` = Continue
- $ `u` = Until (good to run to finish executing a loop)
- $ `h` = Help
- $ `n` = Next (you can also press `enter` to move through the test)
