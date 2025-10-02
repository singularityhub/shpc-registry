---
layout: container
name:  "quay.io/biocontainers/mutalyzer_hgvs_parser"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mutalyzer_hgvs_parser/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mutalyzer_hgvs_parser/container.yaml"
updated_at: "2025-10-02 03:34:30.027853"
latest: "0.3.8--pyh7e72e81_0"
container_url: "https://biocontainers.pro/tools/mutalyzer_hgvs_parser"
aliases:
 - "mutalyzer_hgvs_parser"
 - "idle3.13"
 - "pydoc3.13"
 - "python3.13"
 - "python3.13-config"
versions:
 - "0.3.8--pyh7e72e81_0"
description: "singularity registry hpc automated addition for mutalyzer_hgvs_parser"
config: {"url": "https://biocontainers.pro/tools/mutalyzer_hgvs_parser", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for mutalyzer_hgvs_parser", "latest": {"0.3.8--pyh7e72e81_0": "sha256:bcb7d0a1f7d1854cfc05ecf54fe59713505004e73b475d80087d9d02e714b9ef"}, "tags": {"0.3.8--pyh7e72e81_0": "sha256:bcb7d0a1f7d1854cfc05ecf54fe59713505004e73b475d80087d9d02e714b9ef"}, "docker": "quay.io/biocontainers/mutalyzer_hgvs_parser", "aliases": {"mutalyzer_hgvs_parser": "/usr/local/bin/mutalyzer_hgvs_parser", "idle3.13": "/usr/local/bin/idle3.13", "pydoc3.13": "/usr/local/bin/pydoc3.13", "python3.13": "/usr/local/bin/python3.13", "python3.13-config": "/usr/local/bin/python3.13-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mutalyzer_hgvs_parser.
singularity registry hpc automated addition for mutalyzer_hgvs_parser
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mutalyzer_hgvs_parser
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mutalyzer_hgvs_parser:0.3.8--pyh7e72e81_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mutalyzer_hgvs_parser/0.3.8--pyh7e72e81_0
$ module help quay.io/biocontainers/mutalyzer_hgvs_parser/0.3.8--pyh7e72e81_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mutalyzer_hgvs_parser-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mutalyzer_hgvs_parser-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mutalyzer_hgvs_parser-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mutalyzer_hgvs_parser-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mutalyzer_hgvs_parser-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mutalyzer_hgvs_parser-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mutalyzer_hgvs_parser

```bash
$ singularity exec <container> /usr/local/bin/mutalyzer_hgvs_parser
$ podman run --it --rm --entrypoint /usr/local/bin/mutalyzer_hgvs_parser   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mutalyzer_hgvs_parser   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.13

```bash
$ singularity exec <container> /usr/local/bin/idle3.13
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.13

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.13
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.13

```bash
$ singularity exec <container> /usr/local/bin/python3.13
$ podman run --it --rm --entrypoint /usr/local/bin/python3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.13-config

```bash
$ singularity exec <container> /usr/local/bin/python3.13-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.13-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.13-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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