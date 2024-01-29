---
layout: container
name:  "quay.io/biocontainers/bioconductor-rtnduals"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rtnduals/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rtnduals/container.yaml"
updated_at: "2024-01-29 03:04:35.559987"
latest: "1.26.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rtnduals"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.1--r36_0"
 - "1.22.0--r42hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.1--r40hdfd78af_0"
 - "1.12.0--r40_0"
 - "1.24.0--r43hdfd78af_0"
 - "1.26.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rtnduals"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rtnduals", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rtnduals", "latest": {"1.26.0--r43hdfd78af_0": "sha256:bd17063c97c311990600e074e6469791db214d8a774738f7da5bb3a9859faed2"}, "tags": {"1.8.1--r36_0": "sha256:4839ee900f0e8e5a5ec9f65826b872ab04b5883f4c059173d45b61cabde4bed5", "1.22.0--r42hdfd78af_0": "sha256:3e252326bb97437998297cdb3efbb8d4b5f760b435379435d5d54f8a77abd517", "1.18.0--r41hdfd78af_0": "sha256:e6ff154e69a4b46ce09056a6b74fafae26acb428e5a83fb96cd221d97b35ee03", "1.16.0--r41hdfd78af_0": "sha256:c8c624fd60dbed6098e3e7196b02e95a40f3379f112d88f1fbf0d23017163e70", "1.14.1--r40hdfd78af_0": "sha256:b2eb842a8ab1dd445af6290d7a27bb8cd19a7ae9eb194ea23f79e634da1c8b2c", "1.12.0--r40_0": "sha256:582f4186e0757a534331e59f02125f4718078c442aadb645ea0932c2e6a65133", "1.24.0--r43hdfd78af_0": "sha256:b845008082a89915261e67f655184839e476ebf1567eee735fa37e3f1f2b80e7", "1.26.0--r43hdfd78af_0": "sha256:bd17063c97c311990600e074e6469791db214d8a774738f7da5bb3a9859faed2"}, "docker": "quay.io/biocontainers/bioconductor-rtnduals", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rtnduals.
shpc-registry automated BioContainers addition for bioconductor-rtnduals
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rtnduals
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rtnduals:1.26.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rtnduals/1.26.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rtnduals/1.26.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rtnduals-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rtnduals-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rtnduals-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rtnduals-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rtnduals-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rtnduals-inspect-deffile:

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