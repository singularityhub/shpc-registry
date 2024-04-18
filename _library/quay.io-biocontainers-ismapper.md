---
layout: container
name:  "quay.io/biocontainers/ismapper"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ismapper/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ismapper/container.yaml"
updated_at: "2024-04-18 03:04:45.528679"
latest: "2.0.2--pyhdfd78af_1"
container_url: "https://biocontainers.pro/tools/ismapper"
aliases:
 - "compiled_table.py"
 - "create_output.py"
 - "ismap"
 - "ismap.py"
 - "mapping_to_query.py"
 - "mapping_to_ref.py"
 - "read_grouping.py"
 - "run_commands.py"
 - "CA.pm"
 - "cacert.pem"
 - "index-themes"
 - "fetch-extras"
 - "go.mod"
 - "go.sum"
 - "hlp-xtract.txt"
 - "index-extras"
 - "pm-collect"
 - "readme.pdf"
versions:
 - "2.0.2--pyhdfd78af_1"
description: "shpc-registry automated BioContainers addition for ismapper"
config: {"url": "https://biocontainers.pro/tools/ismapper", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ismapper", "latest": {"2.0.2--pyhdfd78af_1": "sha256:0e7fb587312e2bb4f8e5b1f400c52a143f7bf36e63ee3fc1824a1604c191dae7"}, "tags": {"2.0.2--pyhdfd78af_1": "sha256:0e7fb587312e2bb4f8e5b1f400c52a143f7bf36e63ee3fc1824a1604c191dae7"}, "docker": "quay.io/biocontainers/ismapper", "aliases": {"compiled_table.py": "/usr/local/bin/compiled_table.py", "create_output.py": "/usr/local/bin/create_output.py", "ismap": "/usr/local/bin/ismap", "ismap.py": "/usr/local/bin/ismap.py", "mapping_to_query.py": "/usr/local/bin/mapping_to_query.py", "mapping_to_ref.py": "/usr/local/bin/mapping_to_ref.py", "read_grouping.py": "/usr/local/bin/read_grouping.py", "run_commands.py": "/usr/local/bin/run_commands.py", "CA.pm": "/usr/local/bin/CA.pm", "cacert.pem": "/usr/local/bin/cacert.pem", "index-themes": "/usr/local/bin/index-themes", "fetch-extras": "/usr/local/bin/fetch-extras", "go.mod": "/usr/local/bin/go.mod", "go.sum": "/usr/local/bin/go.sum", "hlp-xtract.txt": "/usr/local/bin/hlp-xtract.txt", "index-extras": "/usr/local/bin/index-extras", "pm-collect": "/usr/local/bin/pm-collect", "readme.pdf": "/usr/local/bin/readme.pdf"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ismapper.
shpc-registry automated BioContainers addition for ismapper
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ismapper
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ismapper:2.0.2--pyhdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ismapper/2.0.2--pyhdfd78af_1
$ module help quay.io/biocontainers/ismapper/2.0.2--pyhdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ismapper-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ismapper-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ismapper-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ismapper-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ismapper-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ismapper-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### compiled_table.py

```bash
$ singularity exec <container> /usr/local/bin/compiled_table.py
$ podman run --it --rm --entrypoint /usr/local/bin/compiled_table.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compiled_table.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### create_output.py

```bash
$ singularity exec <container> /usr/local/bin/create_output.py
$ podman run --it --rm --entrypoint /usr/local/bin/create_output.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/create_output.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ismap

```bash
$ singularity exec <container> /usr/local/bin/ismap
$ podman run --it --rm --entrypoint /usr/local/bin/ismap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ismap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ismap.py

```bash
$ singularity exec <container> /usr/local/bin/ismap.py
$ podman run --it --rm --entrypoint /usr/local/bin/ismap.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ismap.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mapping_to_query.py

```bash
$ singularity exec <container> /usr/local/bin/mapping_to_query.py
$ podman run --it --rm --entrypoint /usr/local/bin/mapping_to_query.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mapping_to_query.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mapping_to_ref.py

```bash
$ singularity exec <container> /usr/local/bin/mapping_to_ref.py
$ podman run --it --rm --entrypoint /usr/local/bin/mapping_to_ref.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mapping_to_ref.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### read_grouping.py

```bash
$ singularity exec <container> /usr/local/bin/read_grouping.py
$ podman run --it --rm --entrypoint /usr/local/bin/read_grouping.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/read_grouping.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_commands.py

```bash
$ singularity exec <container> /usr/local/bin/run_commands.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_commands.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_commands.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CA.pm

```bash
$ singularity exec <container> /usr/local/bin/CA.pm
$ podman run --it --rm --entrypoint /usr/local/bin/CA.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CA.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cacert.pem

```bash
$ singularity exec <container> /usr/local/bin/cacert.pem
$ podman run --it --rm --entrypoint /usr/local/bin/cacert.pem   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cacert.pem   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### index-themes

```bash
$ singularity exec <container> /usr/local/bin/index-themes
$ podman run --it --rm --entrypoint /usr/local/bin/index-themes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/index-themes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fetch-extras

```bash
$ singularity exec <container> /usr/local/bin/fetch-extras
$ podman run --it --rm --entrypoint /usr/local/bin/fetch-extras   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fetch-extras   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### go.mod

```bash
$ singularity exec <container> /usr/local/bin/go.mod
$ podman run --it --rm --entrypoint /usr/local/bin/go.mod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/go.mod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### go.sum

```bash
$ singularity exec <container> /usr/local/bin/go.sum
$ podman run --it --rm --entrypoint /usr/local/bin/go.sum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/go.sum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hlp-xtract.txt

```bash
$ singularity exec <container> /usr/local/bin/hlp-xtract.txt
$ podman run --it --rm --entrypoint /usr/local/bin/hlp-xtract.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hlp-xtract.txt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### index-extras

```bash
$ singularity exec <container> /usr/local/bin/index-extras
$ podman run --it --rm --entrypoint /usr/local/bin/index-extras   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/index-extras   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pm-collect

```bash
$ singularity exec <container> /usr/local/bin/pm-collect
$ podman run --it --rm --entrypoint /usr/local/bin/pm-collect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pm-collect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### readme.pdf

```bash
$ singularity exec <container> /usr/local/bin/readme.pdf
$ podman run --it --rm --entrypoint /usr/local/bin/readme.pdf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/readme.pdf   -v ${PWD} -w ${PWD} <container> -c " $@"
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