---
layout: container
name:  "quay.io/biocontainers/bioconductor-mirmine"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mirmine/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mirmine/container.yaml"
updated_at: "2024-08-31 03:18:15.341603"
latest: "1.22.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mirmine"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_0"
 - "1.20.0--r42hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r41hdfd78af_0"
 - "1.12.0--r40hdfd78af_1"
 - "1.10.0--r40_0"
 - "1.22.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mirmine"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mirmine", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mirmine", "latest": {"1.22.0--r43hdfd78af_0": "sha256:c7f505967751241062cbe037ea5ec0d5b2554e52c3397d96a673075b3048ca29"}, "tags": {"1.8.0--r36_0": "sha256:08897886a402b80df3daa6d404ff72a3124d6dd403fe2982b521cc3c907cf2e9", "1.20.0--r42hdfd78af_0": "sha256:72a15669da0d9b58311955d5eee51a94c3a508ff82b4d60139df10d670d52311", "1.16.0--r41hdfd78af_0": "sha256:d1b23439077ae4211f04f1039c5d175db018f85833ddab03dd31c50e2cfed1fd", "1.14.0--r41hdfd78af_0": "sha256:26b45887b113dd50507aa9992d0d222b08071c9a0b42b52b912d94731241f6c7", "1.12.0--r40hdfd78af_1": "sha256:a45b215b01e5c96c9627b4ee25f7eff1923b1cb1e4290d38a7d91ba8bcedb82e", "1.10.0--r40_0": "sha256:fa3136b866bfd01acccb520413b4acee836897a360b4e900d2213a6c6d9a029a", "1.22.0--r43hdfd78af_0": "sha256:c7f505967751241062cbe037ea5ec0d5b2554e52c3397d96a673075b3048ca29"}, "docker": "quay.io/biocontainers/bioconductor-mirmine", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mirmine.
shpc-registry automated BioContainers addition for bioconductor-mirmine
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mirmine
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mirmine:1.22.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mirmine/1.22.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mirmine/1.22.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mirmine-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mirmine-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mirmine-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mirmine-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mirmine-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mirmine-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gio-launch-desktop

```bash
$ singularity exec <container> /usr/local/bin/gio-launch-desktop
$ podman run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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