---
layout: container
name:  "quay.io/biocontainers/bioconductor-ntw"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ntw/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ntw/container.yaml"
updated_at: "2024-04-19 02:52:03.742806"
latest: "crane ls quay.io/biocontainers/bioconductor-ntw: unsupported status code 504; body: <html>"
container_url: "https://biocontainers.pro/tools/bioconductor-ntw"

versions:
 - "1.44.0--r41hdfd78af_0"
 - "1.48.0--r42hdfd78af_0"
 - "crane ls quay.io/biocontainers/bioconductor-ntw: unsupported status code 504; body: <html>"
 - "<body>"
 - "<center><h1>504 Gateway Time-out</h1></center>"
 - "</body>"
 - "</html>"
 - "1.50.0--r43hdfd78af_0"
 - "1.52.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ntw"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ntw", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ntw", "latest": {"crane ls quay.io/biocontainers/bioconductor-ntw: unsupported status code 504; body: <html>": "crane digest quay.io/biocontainers/bioconductor-ntw:crane ls quay.io/biocontainers/bioconductor-ntw: unsupported status code 504; body: <html>: parsing reference \"quay.io/biocontainers/bioconductor-ntw:crane ls quay.io/biocontainers/bioconductor-ntw: unsupported status code 504; body: <html>\": could not parse reference"}, "tags": {"1.44.0--r41hdfd78af_0": "sha256:016cc04957306b27520229f84aed35683fd8438166e6eb16691185f01eb1e5fa", "1.48.0--r42hdfd78af_0": "sha256:daa8182dfbe2ac0578c44eead0781ca1d48953c4afee6aa0ff989dc355de2574", "crane ls quay.io/biocontainers/bioconductor-ntw: unsupported status code 504; body: <html>": "crane digest quay.io/biocontainers/bioconductor-ntw:crane ls quay.io/biocontainers/bioconductor-ntw: unsupported status code 504; body: <html>: parsing reference \"quay.io/biocontainers/bioconductor-ntw:crane ls quay.io/biocontainers/bioconductor-ntw: unsupported status code 504; body: <html>\": could not parse reference", "<body>": "crane digest quay.io/biocontainers/bioconductor-ntw:<body>: parsing reference \"quay.io/biocontainers/bioconductor-ntw:<body>\": could not parse reference", "<center><h1>504 Gateway Time-out</h1></center>": "crane digest quay.io/biocontainers/bioconductor-ntw:<center><h1>504 Gateway Time-out</h1></center>: parsing reference \"quay.io/biocontainers/bioconductor-ntw:<center><h1>504 Gateway Time-out</h1></center>\": could not parse reference", "</body>": "crane digest quay.io/biocontainers/bioconductor-ntw:</body>: parsing reference \"quay.io/biocontainers/bioconductor-ntw:</body>\": could not parse reference", "</html>": "crane digest quay.io/biocontainers/bioconductor-ntw:</html>: parsing reference \"quay.io/biocontainers/bioconductor-ntw:</html>\": could not parse reference", "1.50.0--r43hdfd78af_0": "sha256:bbc13a763c5dfd39d2530c966c78ee26a3938b1374ad0e7a3b772b161784756b", "1.52.0--r43hdfd78af_0": "sha256:f70e30279b16eb1026bd5ba6dbd4b3d465e0a9bbe1e236e920c45ee3dbc71005"}, "docker": "quay.io/biocontainers/bioconductor-ntw"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ntw.
shpc-registry automated BioContainers addition for bioconductor-ntw
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ntw
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ntw:crane ls quay.io/biocontainers/bioconductor-ntw: unsupported status code 504; body: <html>
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ntw/crane ls quay.io/biocontainers/bioconductor-ntw: unsupported status code 504; body: <html>
$ module help quay.io/biocontainers/bioconductor-ntw/crane ls quay.io/biocontainers/bioconductor-ntw: unsupported status code 504; body: <html>
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ntw-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ntw-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ntw-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ntw-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ntw-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ntw-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ntw

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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