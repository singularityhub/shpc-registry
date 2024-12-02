---
layout: container
name:  "quay.io/biocontainers/bioconductor-modcon"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-modcon/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-modcon/container.yaml"
updated_at: "2024-12-02 03:52:05.650031"
latest: "1.10.0--pl5321r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-modcon"
aliases:
 - "perl5.32.1"
 - "streamzip"
versions:
 - "1.2.0--pl5321r41hdfd78af_0"
 - "1.6.0--pl5321r42hdfd78af_0"
 - "1.8.0--pl5321r43hdfd78af_0"
 - "1.10.0--pl5321r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-modcon"
config: {"url": "https://biocontainers.pro/tools/bioconductor-modcon", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-modcon", "latest": {"1.10.0--pl5321r43hdfd78af_0": "sha256:60c6e447e4004e323f994e09ed2d4ed1941ba0bd08573f86f380273516d84b60"}, "tags": {"1.2.0--pl5321r41hdfd78af_0": "sha256:79002c2588c382953e90830021d9f0c4ee7642c402c01a317fb796cd869dbf0f", "1.6.0--pl5321r42hdfd78af_0": "sha256:4eebebf930d8d55fe35cefd8a6688917f5e230ba305de85c68bd9b236e2eebc2", "1.8.0--pl5321r43hdfd78af_0": "sha256:9162602ff504a0e5c23b112c10d97ddea9a841cdf99f38e4fcc0e43110395b1d", "1.10.0--pl5321r43hdfd78af_0": "sha256:60c6e447e4004e323f994e09ed2d4ed1941ba0bd08573f86f380273516d84b60"}, "docker": "quay.io/biocontainers/bioconductor-modcon", "aliases": {"perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-modcon.
shpc-registry automated BioContainers addition for bioconductor-modcon
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-modcon
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-modcon:1.10.0--pl5321r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-modcon/1.10.0--pl5321r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-modcon/1.10.0--pl5321r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-modcon-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-modcon-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-modcon-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-modcon-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-modcon-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-modcon-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### perl5.32.1

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.1
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### streamzip

```bash
$ singularity exec <container> /usr/local/bin/streamzip
$ podman run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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