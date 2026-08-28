---
layout: container
name:  "quay.io/biocontainers/fungar"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fungar/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fungar/container.yaml"
updated_at: "2026-08-28 14:05:03.185356"
latest: "2.0.0--py314hdfd78af_1"
container_url: "https://biocontainers.pro/tools/fungar"
aliases:
 - "fungar"
 - "fungar_benchmark.py"
 - "fungar_report.py"
 - "diamond"
 - "idle3.14"
 - "pydoc3.14"
 - "python3.14"
 - "python3.14-config"
 - "numpy-config"
versions:
 - "2.0.0--py314hdfd78af_0"
 - "2.0.0--py314hdfd78af_1"
description: "singularity registry hpc automated addition for fungar"
config: {"url": "https://biocontainers.pro/tools/fungar", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for fungar", "latest": {"2.0.0--py314hdfd78af_1": "sha256:6e82b439282f7b1db4fe73ec34469243ebb1fe9888cab1c5cabeb971be598944"}, "tags": {"2.0.0--py314hdfd78af_0": "sha256:21e6b196ed2e40057b133d243922b1d4123a169db603a81883e816d89244694e", "2.0.0--py314hdfd78af_1": "sha256:6e82b439282f7b1db4fe73ec34469243ebb1fe9888cab1c5cabeb971be598944"}, "docker": "quay.io/biocontainers/fungar", "aliases": {"fungar": "/usr/local/bin/fungar", "fungar_benchmark.py": "/usr/local/bin/fungar_benchmark.py", "fungar_report.py": "/usr/local/bin/fungar_report.py", "diamond": "/usr/local/bin/diamond", "idle3.14": "/usr/local/bin/idle3.14", "pydoc3.14": "/usr/local/bin/pydoc3.14", "python3.14": "/usr/local/bin/python3.14", "python3.14-config": "/usr/local/bin/python3.14-config", "numpy-config": "/usr/local/bin/numpy-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fungar.
singularity registry hpc automated addition for fungar
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fungar
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fungar:2.0.0--py314hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fungar/2.0.0--py314hdfd78af_1
$ module help quay.io/biocontainers/fungar/2.0.0--py314hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fungar-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fungar-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fungar-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fungar-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fungar-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fungar-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fungar

```bash
$ singularity exec <container> /usr/local/bin/fungar
$ podman run --it --rm --entrypoint /usr/local/bin/fungar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fungar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fungar_benchmark.py

```bash
$ singularity exec <container> /usr/local/bin/fungar_benchmark.py
$ podman run --it --rm --entrypoint /usr/local/bin/fungar_benchmark.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fungar_benchmark.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fungar_report.py

```bash
$ singularity exec <container> /usr/local/bin/fungar_report.py
$ podman run --it --rm --entrypoint /usr/local/bin/fungar_report.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fungar_report.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### diamond

```bash
$ singularity exec <container> /usr/local/bin/diamond
$ podman run --it --rm --entrypoint /usr/local/bin/diamond   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/diamond   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.14

```bash
$ singularity exec <container> /usr/local/bin/idle3.14
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.14

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.14
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.14

```bash
$ singularity exec <container> /usr/local/bin/python3.14
$ podman run --it --rm --entrypoint /usr/local/bin/python3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.14-config

```bash
$ singularity exec <container> /usr/local/bin/python3.14-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.14-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.14-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### numpy-config

```bash
$ singularity exec <container> /usr/local/bin/numpy-config
$ podman run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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