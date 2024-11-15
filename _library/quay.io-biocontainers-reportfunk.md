---
layout: container
name:  "quay.io/biocontainers/reportfunk"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/reportfunk/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/reportfunk/container.yaml"
updated_at: "2024-11-15 02:24:58.314883"
latest: "1.0.1--pyh3252c3a_0"
container_url: "https://biocontainers.pro/tools/reportfunk"
aliases:
 - "baltic.py"
 - "class_definitions.py"
 - "custom_logger.py"
 - "io_functions.py"
 - "log_handler_handle.py"
 - "parsing_functions.py"
 - "prep_data_functions.py"
 - "report_functions.py"
 - "reportfunk"
 - "table_functions.py"
 - "time_functions.py"
 - "tree_functions.py"
 - "f2py3.9"
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
 - "jpgicc"
 - "linkicc"
 - "psicc"
 - "tificc"
 - "transicc"
versions:
 - "1.0.1--pyh3252c3a_0"
description: "singularity registry hpc automated addition for reportfunk"
config: {"url": "https://biocontainers.pro/tools/reportfunk", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for reportfunk", "latest": {"1.0.1--pyh3252c3a_0": "sha256:76450575c0e2c63fade50c722bd3f32efd712903265c3fd9ce73825e0a259293"}, "tags": {"1.0.1--pyh3252c3a_0": "sha256:76450575c0e2c63fade50c722bd3f32efd712903265c3fd9ce73825e0a259293"}, "docker": "quay.io/biocontainers/reportfunk", "aliases": {"baltic.py": "/usr/local/bin/baltic.py", "class_definitions.py": "/usr/local/bin/class_definitions.py", "custom_logger.py": "/usr/local/bin/custom_logger.py", "io_functions.py": "/usr/local/bin/io_functions.py", "log_handler_handle.py": "/usr/local/bin/log_handler_handle.py", "parsing_functions.py": "/usr/local/bin/parsing_functions.py", "prep_data_functions.py": "/usr/local/bin/prep_data_functions.py", "report_functions.py": "/usr/local/bin/report_functions.py", "reportfunk": "/usr/local/bin/reportfunk", "table_functions.py": "/usr/local/bin/table_functions.py", "time_functions.py": "/usr/local/bin/time_functions.py", "tree_functions.py": "/usr/local/bin/tree_functions.py", "f2py3.9": "/usr/local/bin/f2py3.9", "2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config", "jpgicc": "/usr/local/bin/jpgicc", "linkicc": "/usr/local/bin/linkicc", "psicc": "/usr/local/bin/psicc", "tificc": "/usr/local/bin/tificc", "transicc": "/usr/local/bin/transicc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/reportfunk.
singularity registry hpc automated addition for reportfunk
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/reportfunk
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/reportfunk:1.0.1--pyh3252c3a_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/reportfunk/1.0.1--pyh3252c3a_0
$ module help quay.io/biocontainers/reportfunk/1.0.1--pyh3252c3a_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### reportfunk-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### reportfunk-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### reportfunk-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### reportfunk-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### reportfunk-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### reportfunk-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### baltic.py

```bash
$ singularity exec <container> /usr/local/bin/baltic.py
$ podman run --it --rm --entrypoint /usr/local/bin/baltic.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/baltic.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### class_definitions.py

```bash
$ singularity exec <container> /usr/local/bin/class_definitions.py
$ podman run --it --rm --entrypoint /usr/local/bin/class_definitions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/class_definitions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### custom_logger.py

```bash
$ singularity exec <container> /usr/local/bin/custom_logger.py
$ podman run --it --rm --entrypoint /usr/local/bin/custom_logger.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/custom_logger.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### io_functions.py

```bash
$ singularity exec <container> /usr/local/bin/io_functions.py
$ podman run --it --rm --entrypoint /usr/local/bin/io_functions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/io_functions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### log_handler_handle.py

```bash
$ singularity exec <container> /usr/local/bin/log_handler_handle.py
$ podman run --it --rm --entrypoint /usr/local/bin/log_handler_handle.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/log_handler_handle.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### parsing_functions.py

```bash
$ singularity exec <container> /usr/local/bin/parsing_functions.py
$ podman run --it --rm --entrypoint /usr/local/bin/parsing_functions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/parsing_functions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prep_data_functions.py

```bash
$ singularity exec <container> /usr/local/bin/prep_data_functions.py
$ podman run --it --rm --entrypoint /usr/local/bin/prep_data_functions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prep_data_functions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### report_functions.py

```bash
$ singularity exec <container> /usr/local/bin/report_functions.py
$ podman run --it --rm --entrypoint /usr/local/bin/report_functions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/report_functions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### reportfunk

```bash
$ singularity exec <container> /usr/local/bin/reportfunk
$ podman run --it --rm --entrypoint /usr/local/bin/reportfunk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/reportfunk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### table_functions.py

```bash
$ singularity exec <container> /usr/local/bin/table_functions.py
$ podman run --it --rm --entrypoint /usr/local/bin/table_functions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/table_functions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### time_functions.py

```bash
$ singularity exec <container> /usr/local/bin/time_functions.py
$ podman run --it --rm --entrypoint /usr/local/bin/time_functions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/time_functions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tree_functions.py

```bash
$ singularity exec <container> /usr/local/bin/tree_functions.py
$ podman run --it --rm --entrypoint /usr/local/bin/tree_functions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tree_functions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.9

```bash
$ singularity exec <container> /usr/local/bin/f2py3.9
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.9

```bash
$ singularity exec <container> /usr/local/bin/idle3.9
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.9

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.9
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9

```bash
$ singularity exec <container> /usr/local/bin/python3.9
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.9-config

```bash
$ singularity exec <container> /usr/local/bin/python3.9-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.9-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jpgicc

```bash
$ singularity exec <container> /usr/local/bin/jpgicc
$ podman run --it --rm --entrypoint /usr/local/bin/jpgicc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jpgicc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### linkicc

```bash
$ singularity exec <container> /usr/local/bin/linkicc
$ podman run --it --rm --entrypoint /usr/local/bin/linkicc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/linkicc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psicc

```bash
$ singularity exec <container> /usr/local/bin/psicc
$ podman run --it --rm --entrypoint /usr/local/bin/psicc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psicc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tificc

```bash
$ singularity exec <container> /usr/local/bin/tificc
$ podman run --it --rm --entrypoint /usr/local/bin/tificc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tificc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### transicc

```bash
$ singularity exec <container> /usr/local/bin/transicc
$ podman run --it --rm --entrypoint /usr/local/bin/transicc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/transicc   -v ${PWD} -w ${PWD} <container> -c " $@"
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. An environment file in the
module folder will also be bound. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For anycommands above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)
 - PODMAN_OPTS: to define custom options for podman or docker
 - PODMAN_COMMAND_OPTS: to define custom options for the command

<br>

### Install

You can install shpc locally (for yourself or your user base) as follows:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc
$ pip install -e .
```

Have any questions, or want to request a new module or version? [ask for help!](https://github.com/singularityhub/singularity-hpc/issues)