---
layout: container
name:  "quay.io/biocontainers/labrat"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/labrat/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/labrat/container.yaml"
updated_at: "2025-08-24 03:25:11.077871"
latest: "0.3.0--pyhdfd78af_1"
container_url: "https://biocontainers.pro/tools/labrat"
aliases:
 - "LABRAT.py"
 - "LABRAT_danRer.py"
 - "LABRAT_dm6annotation.py"
 - "LABRAT_rn6annotation.py"
 - "LABRATsc.py"
 - "salmon"
 - "gffutils-cli"
 - "activate-global-python-argcomplete"
 - "python-argcomplete-check-easy-install-script"
 - "python-argcomplete-tcsh"
 - "register-python-argcomplete"
 - "faidx"
 - "f2py3.9"
 - "2to3-3.9"
 - "idle3.9"
versions:
 - "0.3.0--pyhdfd78af_1"
description: "shpc-registry automated BioContainers addition for labrat"
config: {"url": "https://biocontainers.pro/tools/labrat", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for labrat", "latest": {"0.3.0--pyhdfd78af_1": "sha256:e2784b8b5a0ab77fc72669d9d0c189605d16eac085cc57dff6713dbd417296c4"}, "tags": {"0.3.0--pyhdfd78af_1": "sha256:e2784b8b5a0ab77fc72669d9d0c189605d16eac085cc57dff6713dbd417296c4"}, "docker": "quay.io/biocontainers/labrat", "aliases": {"LABRAT.py": "/usr/local/bin/LABRAT.py", "LABRAT_danRer.py": "/usr/local/bin/LABRAT_danRer.py", "LABRAT_dm6annotation.py": "/usr/local/bin/LABRAT_dm6annotation.py", "LABRAT_rn6annotation.py": "/usr/local/bin/LABRAT_rn6annotation.py", "LABRATsc.py": "/usr/local/bin/LABRATsc.py", "salmon": "/usr/local/bin/salmon", "gffutils-cli": "/usr/local/bin/gffutils-cli", "activate-global-python-argcomplete": "/usr/local/bin/activate-global-python-argcomplete", "python-argcomplete-check-easy-install-script": "/usr/local/bin/python-argcomplete-check-easy-install-script", "python-argcomplete-tcsh": "/usr/local/bin/python-argcomplete-tcsh", "register-python-argcomplete": "/usr/local/bin/register-python-argcomplete", "faidx": "/usr/local/bin/faidx", "f2py3.9": "/usr/local/bin/f2py3.9", "2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9"}}
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


#### salmon

```bash
$ singularity exec <container> /usr/local/bin/salmon
$ podman run --it --rm --entrypoint /usr/local/bin/salmon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/salmon   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gffutils-cli

```bash
$ singularity exec <container> /usr/local/bin/gffutils-cli
$ podman run --it --rm --entrypoint /usr/local/bin/gffutils-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gffutils-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### activate-global-python-argcomplete

```bash
$ singularity exec <container> /usr/local/bin/activate-global-python-argcomplete
$ podman run --it --rm --entrypoint /usr/local/bin/activate-global-python-argcomplete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/activate-global-python-argcomplete   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python-argcomplete-check-easy-install-script

```bash
$ singularity exec <container> /usr/local/bin/python-argcomplete-check-easy-install-script
$ podman run --it --rm --entrypoint /usr/local/bin/python-argcomplete-check-easy-install-script   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python-argcomplete-check-easy-install-script   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python-argcomplete-tcsh

```bash
$ singularity exec <container> /usr/local/bin/python-argcomplete-tcsh
$ podman run --it --rm --entrypoint /usr/local/bin/python-argcomplete-tcsh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python-argcomplete-tcsh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### register-python-argcomplete

```bash
$ singularity exec <container> /usr/local/bin/register-python-argcomplete
$ podman run --it --rm --entrypoint /usr/local/bin/register-python-argcomplete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/register-python-argcomplete   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### faidx

```bash
$ singularity exec <container> /usr/local/bin/faidx
$ podman run --it --rm --entrypoint /usr/local/bin/faidx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/faidx   -v ${PWD} -w ${PWD} <container> -c " $@"
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