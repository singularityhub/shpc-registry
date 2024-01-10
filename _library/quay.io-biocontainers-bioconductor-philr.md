---
layout: container
name:  "quay.io/biocontainers/bioconductor-philr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-philr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-philr/container.yaml"
updated_at: "2024-01-10 08:50:38.188084"
latest: "1.28.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-philr"
aliases:
 - "c89"
 - "c99"
versions:
 - "1.8.1--r351_0"
 - "1.24.0--r42hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.14.0--r40_0"
 - "1.26.0--r43hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-philr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-philr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-philr", "latest": {"1.28.0--r43hdfd78af_0": "sha256:dc81f155c6cdb65db7f8f113d1c1d4ad334388e9f93a78f38b028ae3ca78a506"}, "tags": {"1.8.1--r351_0": "sha256:7db4ce4b632748ac09df84f19a46d0bcc4105dd455323296ed1158bd2c486371", "1.24.0--r42hdfd78af_0": "sha256:aa5046a910e505a1462969230335026d5e9f40c058f9231102f37be2755013de", "1.20.0--r41hdfd78af_0": "sha256:9eac8d776b24670d21ed9bfdcf487efc5626acffb01374f8c5a7e2813c429433", "1.18.0--r41hdfd78af_0": "sha256:c37be7536d6b29f2718f09133e0b31642e982f071314c0390970669d2d1410b1", "1.16.0--r40hdfd78af_1": "sha256:fa0326b02a92ce777cc9c9c09f55e4871d20b857b52395828e8fb564d2508173", "1.14.0--r40_0": "sha256:e7300ac2a0e02192ac213f6b23b01e443bcf5311b95831cc1d812f25e45427fd", "1.26.0--r43hdfd78af_0": "sha256:69ed736bf49e7fb70ae9c2e8c28da1bfc9483187abdac42143b82997e59b017b", "1.28.0--r43hdfd78af_0": "sha256:dc81f155c6cdb65db7f8f113d1c1d4ad334388e9f93a78f38b028ae3ca78a506"}, "docker": "quay.io/biocontainers/bioconductor-philr", "aliases": {"c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-philr.
shpc-registry automated BioContainers addition for bioconductor-philr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-philr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-philr:1.28.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-philr/1.28.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-philr/1.28.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-philr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-philr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-philr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-philr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-philr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-philr-inspect-deffile:

```bash
$ singularity inspect -d <container>
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