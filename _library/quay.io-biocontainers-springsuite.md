---
layout: container
name:  "quay.io/biocontainers/springsuite"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/springsuite/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/springsuite/container.yaml"
updated_at: "2022-10-27 00:47:32.125806"
latest: "0.2--pyh5e36f6f_1"
container_url: "https://biocontainers.pro/tools/springsuite"
aliases:
 - "TMalign"
 - "TMscore"
 - "pulchra"
 - "spring_cross.py"
 - "spring_map.py"
 - "spring_mcc.py"
 - "spring_minz.py"
 - "spring_model.py"
 - "spring_model_all.py"
versions:
 - "0.2--pyh5e36f6f_1"
description: "shpc-registry automated BioContainers addition for springsuite"
config: {"url": "https://biocontainers.pro/tools/springsuite", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for springsuite", "latest": {"0.2--pyh5e36f6f_1": "sha256:b43399fac2da4a835668dbca5006a7040794f8996f8b4aa25f64de786b75ae2f"}, "tags": {"0.2--pyh5e36f6f_1": "sha256:b43399fac2da4a835668dbca5006a7040794f8996f8b4aa25f64de786b75ae2f"}, "docker": "quay.io/biocontainers/springsuite", "aliases": {"TMalign": "/usr/local/bin/TMalign", "TMscore": "/usr/local/bin/TMscore", "pulchra": "/usr/local/bin/pulchra", "spring_cross.py": "/usr/local/bin/spring_cross.py", "spring_map.py": "/usr/local/bin/spring_map.py", "spring_mcc.py": "/usr/local/bin/spring_mcc.py", "spring_minz.py": "/usr/local/bin/spring_minz.py", "spring_model.py": "/usr/local/bin/spring_model.py", "spring_model_all.py": "/usr/local/bin/spring_model_all.py"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/springsuite.
shpc-registry automated BioContainers addition for springsuite
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/springsuite
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/springsuite:0.2--pyh5e36f6f_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/springsuite/0.2--pyh5e36f6f_1
$ module help quay.io/biocontainers/springsuite/0.2--pyh5e36f6f_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### springsuite-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### springsuite-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### springsuite-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### springsuite-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### springsuite-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### springsuite-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### TMalign

```bash
$ singularity exec <container> /usr/local/bin/TMalign
$ podman run --it --rm --entrypoint /usr/local/bin/TMalign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/TMalign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### TMscore

```bash
$ singularity exec <container> /usr/local/bin/TMscore
$ podman run --it --rm --entrypoint /usr/local/bin/TMscore   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/TMscore   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pulchra

```bash
$ singularity exec <container> /usr/local/bin/pulchra
$ podman run --it --rm --entrypoint /usr/local/bin/pulchra   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pulchra   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spring_cross.py

```bash
$ singularity exec <container> /usr/local/bin/spring_cross.py
$ podman run --it --rm --entrypoint /usr/local/bin/spring_cross.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spring_cross.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spring_map.py

```bash
$ singularity exec <container> /usr/local/bin/spring_map.py
$ podman run --it --rm --entrypoint /usr/local/bin/spring_map.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spring_map.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spring_mcc.py

```bash
$ singularity exec <container> /usr/local/bin/spring_mcc.py
$ podman run --it --rm --entrypoint /usr/local/bin/spring_mcc.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spring_mcc.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spring_minz.py

```bash
$ singularity exec <container> /usr/local/bin/spring_minz.py
$ podman run --it --rm --entrypoint /usr/local/bin/spring_minz.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spring_minz.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spring_model.py

```bash
$ singularity exec <container> /usr/local/bin/spring_model.py
$ podman run --it --rm --entrypoint /usr/local/bin/spring_model.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spring_model.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spring_model_all.py

```bash
$ singularity exec <container> /usr/local/bin/spring_model_all.py
$ podman run --it --rm --entrypoint /usr/local/bin/spring_model_all.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spring_model_all.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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