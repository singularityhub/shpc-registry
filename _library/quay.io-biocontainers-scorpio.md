---
layout: container
name:  "quay.io/biocontainers/scorpio"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/scorpio/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/scorpio/container.yaml"
updated_at: "2025-07-01 04:31:03.731210"
latest: "0.3.19--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/scorpio"
aliases:
 - "constellations"
 - "extract_definitions.py"
 - "scorpio"
 - "type_constellations.py"
 - "f2py3.9"
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
 - "python3.9"
 - "python3.9-config"
versions:
 - "0.3.9--pyhdfd78af_0"
 - "0.3.17--pyhdfd78af_0"
 - "0.3.19--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for scorpio"
config: {"url": "https://biocontainers.pro/tools/scorpio", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for scorpio", "latest": {"0.3.19--pyhdfd78af_0": "sha256:15ccf565a44d1774db86dc3467698e78ae833cc61f9c395e7e175f7e037edf51"}, "tags": {"0.3.9--pyhdfd78af_0": "sha256:b8604db530f657839e7ac0d94f9cbfe3f66a59bec37852b2165d0229a95e0147", "0.3.17--pyhdfd78af_0": "sha256:dc262783561b5eda182d3c68bbdcfb6acae0a03c040d1c1971401a9cf5425fb4", "0.3.19--pyhdfd78af_0": "sha256:15ccf565a44d1774db86dc3467698e78ae833cc61f9c395e7e175f7e037edf51"}, "docker": "quay.io/biocontainers/scorpio", "aliases": {"constellations": "/usr/local/bin/constellations", "extract_definitions.py": "/usr/local/bin/extract_definitions.py", "scorpio": "/usr/local/bin/scorpio", "type_constellations.py": "/usr/local/bin/type_constellations.py", "f2py3.9": "/usr/local/bin/f2py3.9", "2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9", "python3.9": "/usr/local/bin/python3.9", "python3.9-config": "/usr/local/bin/python3.9-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/scorpio.
shpc-registry automated BioContainers addition for scorpio
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/scorpio
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/scorpio:0.3.19--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/scorpio/0.3.19--pyhdfd78af_0
$ module help quay.io/biocontainers/scorpio/0.3.19--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### scorpio-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### scorpio-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### scorpio-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### scorpio-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### scorpio-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### scorpio-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### constellations

```bash
$ singularity exec <container> /usr/local/bin/constellations
$ podman run --it --rm --entrypoint /usr/local/bin/constellations   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/constellations   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### extract_definitions.py

```bash
$ singularity exec <container> /usr/local/bin/extract_definitions.py
$ podman run --it --rm --entrypoint /usr/local/bin/extract_definitions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/extract_definitions.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scorpio

```bash
$ singularity exec <container> /usr/local/bin/scorpio
$ podman run --it --rm --entrypoint /usr/local/bin/scorpio   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scorpio   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### type_constellations.py

```bash
$ singularity exec <container> /usr/local/bin/type_constellations.py
$ podman run --it --rm --entrypoint /usr/local/bin/type_constellations.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/type_constellations.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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