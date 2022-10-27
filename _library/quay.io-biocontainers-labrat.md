---
layout: container
name:  "quay.io/biocontainers/labrat"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/labrat/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/labrat/container.yaml"
updated_at: "2022-10-27 00:57:07.746825"
latest: "0.3.0--pyhdfd78af_1"
container_url: "https://biocontainers.pro/tools/labrat"
aliases:
 - "LABRAT.py"
 - "LABRAT_danRer.py"
 - "LABRAT_dm6annotation.py"
 - "LABRAT_rn6annotation.py"
 - "LABRATsc.py"
versions:
 - "0.3.0--pyhdfd78af_1"
description: "shpc-registry automated BioContainers addition for labrat"
config: {"url": "https://biocontainers.pro/tools/labrat", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for labrat", "latest": {"0.3.0--pyhdfd78af_1": "sha256:e2784b8b5a0ab77fc72669d9d0c189605d16eac085cc57dff6713dbd417296c4"}, "tags": {"0.3.0--pyhdfd78af_1": "sha256:e2784b8b5a0ab77fc72669d9d0c189605d16eac085cc57dff6713dbd417296c4"}, "docker": "quay.io/biocontainers/labrat", "aliases": {"LABRAT.py": "/usr/local/bin/LABRAT.py", "LABRAT_danRer.py": "/usr/local/bin/LABRAT_danRer.py", "LABRAT_dm6annotation.py": "/usr/local/bin/LABRAT_dm6annotation.py", "LABRAT_rn6annotation.py": "/usr/local/bin/LABRAT_rn6annotation.py", "LABRATsc.py": "/usr/local/bin/LABRATsc.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/labrat.
shpc-registry automated BioContainers addition for labrat
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/labrat
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/labrat:0.3.0--pyhdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/labrat/0.3.0--pyhdfd78af_1
$ module help quay.io/biocontainers/labrat/0.3.0--pyhdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### labrat-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### labrat-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### labrat-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### labrat-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### labrat-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### labrat-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### LABRAT.py

```bash
$ singularity exec <container> /usr/local/bin/LABRAT.py
$ podman run --it --rm --entrypoint /usr/local/bin/LABRAT.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LABRAT.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### LABRAT_danRer.py

```bash
$ singularity exec <container> /usr/local/bin/LABRAT_danRer.py
$ podman run --it --rm --entrypoint /usr/local/bin/LABRAT_danRer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LABRAT_danRer.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### LABRAT_dm6annotation.py

```bash
$ singularity exec <container> /usr/local/bin/LABRAT_dm6annotation.py
$ podman run --it --rm --entrypoint /usr/local/bin/LABRAT_dm6annotation.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LABRAT_dm6annotation.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### LABRAT_rn6annotation.py

```bash
$ singularity exec <container> /usr/local/bin/LABRAT_rn6annotation.py
$ podman run --it --rm --entrypoint /usr/local/bin/LABRAT_rn6annotation.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LABRAT_rn6annotation.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### LABRATsc.py

```bash
$ singularity exec <container> /usr/local/bin/LABRATsc.py
$ podman run --it --rm --entrypoint /usr/local/bin/LABRATsc.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/LABRATsc.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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