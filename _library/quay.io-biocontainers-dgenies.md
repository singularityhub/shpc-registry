---
layout: container
name:  "quay.io/biocontainers/dgenies"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dgenies/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/dgenies/container.yaml"
updated_at: "2024-04-22 02:28:57.481630"
latest: "1.5.0--pyhdfd78af_1"
container_url: "https://biocontainers.pro/tools/dgenies"
aliases:
 - "dgenies"
 - "pbr"
 - "flask"
 - "igzip"
 - "pbunzip2"
 - "pbzcat"
 - "pbzip2"
 - "pigz"
 - "unpigz"
 - "markdown_py"
 - "fonttools"
versions:
 - "1.4.0--pyhdfd78af_0"
 - "1.5.0--pyhdfd78af_0"
 - "1.5.0--pyhdfd78af_1"
description: "shpc-registry automated BioContainers addition for dgenies"
config: {"url": "https://biocontainers.pro/tools/dgenies", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for dgenies", "latest": {"1.5.0--pyhdfd78af_1": "sha256:29113b613f8e359402b077b16822202681c8dad5ce87f675875ae0216d854d28"}, "tags": {"1.4.0--pyhdfd78af_0": "sha256:92b1753c5363f783f3d0bff390d2d14094a8852f3bb08c8be76b1cbf0bb14989", "1.5.0--pyhdfd78af_0": "sha256:3dd27df4cd4a089b624cc3ad2f2b814c02e8ce296d1c036418e4e8eddd5d0c85", "1.5.0--pyhdfd78af_1": "sha256:29113b613f8e359402b077b16822202681c8dad5ce87f675875ae0216d854d28"}, "docker": "quay.io/biocontainers/dgenies", "aliases": {"dgenies": "/usr/local/bin/dgenies", "pbr": "/usr/local/bin/pbr", "flask": "/usr/local/bin/flask", "igzip": "/usr/local/bin/igzip", "pbunzip2": "/usr/local/bin/pbunzip2", "pbzcat": "/usr/local/bin/pbzcat", "pbzip2": "/usr/local/bin/pbzip2", "pigz": "/usr/local/bin/pigz", "unpigz": "/usr/local/bin/unpigz", "markdown_py": "/usr/local/bin/markdown_py", "fonttools": "/usr/local/bin/fonttools"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dgenies.
shpc-registry automated BioContainers addition for dgenies
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dgenies
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dgenies:1.5.0--pyhdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dgenies/1.5.0--pyhdfd78af_1
$ module help quay.io/biocontainers/dgenies/1.5.0--pyhdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dgenies-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dgenies-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dgenies-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dgenies-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dgenies-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dgenies-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dgenies

```bash
$ singularity exec <container> /usr/local/bin/dgenies
$ podman run --it --rm --entrypoint /usr/local/bin/dgenies   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dgenies   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbr

```bash
$ singularity exec <container> /usr/local/bin/pbr
$ podman run --it --rm --entrypoint /usr/local/bin/pbr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flask

```bash
$ singularity exec <container> /usr/local/bin/flask
$ podman run --it --rm --entrypoint /usr/local/bin/flask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### igzip

```bash
$ singularity exec <container> /usr/local/bin/igzip
$ podman run --it --rm --entrypoint /usr/local/bin/igzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/igzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbunzip2

```bash
$ singularity exec <container> /usr/local/bin/pbunzip2
$ podman run --it --rm --entrypoint /usr/local/bin/pbunzip2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbunzip2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbzcat

```bash
$ singularity exec <container> /usr/local/bin/pbzcat
$ podman run --it --rm --entrypoint /usr/local/bin/pbzcat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbzcat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbzip2

```bash
$ singularity exec <container> /usr/local/bin/pbzip2
$ podman run --it --rm --entrypoint /usr/local/bin/pbzip2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbzip2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pigz

```bash
$ singularity exec <container> /usr/local/bin/pigz
$ podman run --it --rm --entrypoint /usr/local/bin/pigz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pigz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unpigz

```bash
$ singularity exec <container> /usr/local/bin/unpigz
$ podman run --it --rm --entrypoint /usr/local/bin/unpigz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unpigz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### markdown_py

```bash
$ singularity exec <container> /usr/local/bin/markdown_py
$ podman run --it --rm --entrypoint /usr/local/bin/markdown_py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/markdown_py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fonttools

```bash
$ singularity exec <container> /usr/local/bin/fonttools
$ podman run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fonttools   -v ${PWD} -w ${PWD} <container> -c " $@"
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