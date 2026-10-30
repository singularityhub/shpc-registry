---
layout: container
name:  "quay.io/biocontainers/fair-bioheaders"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fair-bioheaders/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fair-bioheaders/container.yaml"
updated_at: "2026-10-30 08:22:49.402243"
latest: "0.5.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/fair-bioheaders"
aliases:
 - "bioheaders"
 - "fhr-convert"
 - "fhr-fasta-combine"
 - "fhr-fasta-strip"
 - "fhr-fasta-validate"
 - "fhr-gfa-combine"
 - "fhr-gfa-strip"
 - "fhr-gfa-validate"
 - "fhr-validate"
 - "idle3.15"
 - "pydoc3.15"
 - "python3.15"
 - "python3.15-config"
 - "jsonpointer"
 - "idna"
 - "jsonschema"
versions:
 - "0.5.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for fair-bioheaders"
config: {"url": "https://biocontainers.pro/tools/fair-bioheaders", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for fair-bioheaders", "latest": {"0.5.0--pyhdfd78af_0": "sha256:c0ad46ee4496801b584430a04cb6db5e73d1ee0ae1b9134f04bfef87185ef0d4"}, "tags": {"0.5.0--pyhdfd78af_0": "sha256:c0ad46ee4496801b584430a04cb6db5e73d1ee0ae1b9134f04bfef87185ef0d4"}, "docker": "quay.io/biocontainers/fair-bioheaders", "aliases": {"bioheaders": "/usr/local/bin/bioheaders", "fhr-convert": "/usr/local/bin/fhr-convert", "fhr-fasta-combine": "/usr/local/bin/fhr-fasta-combine", "fhr-fasta-strip": "/usr/local/bin/fhr-fasta-strip", "fhr-fasta-validate": "/usr/local/bin/fhr-fasta-validate", "fhr-gfa-combine": "/usr/local/bin/fhr-gfa-combine", "fhr-gfa-strip": "/usr/local/bin/fhr-gfa-strip", "fhr-gfa-validate": "/usr/local/bin/fhr-gfa-validate", "fhr-validate": "/usr/local/bin/fhr-validate", "idle3.15": "/usr/local/bin/idle3.15", "pydoc3.15": "/usr/local/bin/pydoc3.15", "python3.15": "/usr/local/bin/python3.15", "python3.15-config": "/usr/local/bin/python3.15-config", "jsonpointer": "/usr/local/bin/jsonpointer", "idna": "/usr/local/bin/idna", "jsonschema": "/usr/local/bin/jsonschema"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fair-bioheaders.
singularity registry hpc automated addition for fair-bioheaders
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fair-bioheaders
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fair-bioheaders:0.5.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fair-bioheaders/0.5.0--pyhdfd78af_0
$ module help quay.io/biocontainers/fair-bioheaders/0.5.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fair-bioheaders-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fair-bioheaders-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fair-bioheaders-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fair-bioheaders-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fair-bioheaders-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fair-bioheaders-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bioheaders

```bash
$ singularity exec <container> /usr/local/bin/bioheaders
$ podman run --it --rm --entrypoint /usr/local/bin/bioheaders   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bioheaders   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fhr-convert

```bash
$ singularity exec <container> /usr/local/bin/fhr-convert
$ podman run --it --rm --entrypoint /usr/local/bin/fhr-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fhr-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fhr-fasta-combine

```bash
$ singularity exec <container> /usr/local/bin/fhr-fasta-combine
$ podman run --it --rm --entrypoint /usr/local/bin/fhr-fasta-combine   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fhr-fasta-combine   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fhr-fasta-strip

```bash
$ singularity exec <container> /usr/local/bin/fhr-fasta-strip
$ podman run --it --rm --entrypoint /usr/local/bin/fhr-fasta-strip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fhr-fasta-strip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fhr-fasta-validate

```bash
$ singularity exec <container> /usr/local/bin/fhr-fasta-validate
$ podman run --it --rm --entrypoint /usr/local/bin/fhr-fasta-validate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fhr-fasta-validate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fhr-gfa-combine

```bash
$ singularity exec <container> /usr/local/bin/fhr-gfa-combine
$ podman run --it --rm --entrypoint /usr/local/bin/fhr-gfa-combine   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fhr-gfa-combine   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fhr-gfa-strip

```bash
$ singularity exec <container> /usr/local/bin/fhr-gfa-strip
$ podman run --it --rm --entrypoint /usr/local/bin/fhr-gfa-strip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fhr-gfa-strip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fhr-gfa-validate

```bash
$ singularity exec <container> /usr/local/bin/fhr-gfa-validate
$ podman run --it --rm --entrypoint /usr/local/bin/fhr-gfa-validate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fhr-gfa-validate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fhr-validate

```bash
$ singularity exec <container> /usr/local/bin/fhr-validate
$ podman run --it --rm --entrypoint /usr/local/bin/fhr-validate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fhr-validate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.15

```bash
$ singularity exec <container> /usr/local/bin/idle3.15
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.15   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.15   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.15

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.15
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.15   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.15   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.15

```bash
$ singularity exec <container> /usr/local/bin/python3.15
$ podman run --it --rm --entrypoint /usr/local/bin/python3.15   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.15   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.15-config

```bash
$ singularity exec <container> /usr/local/bin/python3.15-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.15-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.15-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jsonpointer

```bash
$ singularity exec <container> /usr/local/bin/jsonpointer
$ podman run --it --rm --entrypoint /usr/local/bin/jsonpointer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jsonpointer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idna

```bash
$ singularity exec <container> /usr/local/bin/idna
$ podman run --it --rm --entrypoint /usr/local/bin/idna   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idna   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jsonschema

```bash
$ singularity exec <container> /usr/local/bin/jsonschema
$ podman run --it --rm --entrypoint /usr/local/bin/jsonschema   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jsonschema   -v ${PWD} -w ${PWD} <container> -c " $@"
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