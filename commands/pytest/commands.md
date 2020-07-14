# PyTest Commands

A list of commands for PyTest. As usual, when developing within a docker container, precede the command with `docker-compose exec web` where web is the canonical name given to the service for my Django project.

## Testing Commands

### Collect a List of All Tests in the Project

$ `docker-compose exec web pytest --collect-only`

### Run an Individual Unit Test in Debug Mode

$ `docker-compose exec web pytest <dir_name>::<class_name>::<func_name> --pdb`

### Run an Individual Unit Test in Debug Mode (Stepping Through)

$ `docker-compose exec web pytest <dir_name>::<class_name>::<func_name> --trace`

## Keyboard Shortcuts

- $ `l` = list
- $ `ll` = long list
- $ `s` = Step Into
- $ `c` = Continue
- $ `u` = Until (good to run to finish executing a loop)
- $ `h` = Help
- $ `n` = Next (you can also press `enter` to move through the test)
