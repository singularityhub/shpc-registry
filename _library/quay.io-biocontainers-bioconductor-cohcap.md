---
layout: container
name:  "quay.io/biocontainers/bioconductor-cohcap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cohcap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cohcap/container.yaml"
updated_at: "2024-03-06 02:51:17.555615"
latest: "1.48.0--pl5321r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cohcap"
aliases:
 - "perl5.32.1"
 - "streamzip"
versions:
 - "1.40.0--pl5321r41hc247a5b_3"
 - "1.44.0--pl5321r42hc247a5b_0"
 - "1.44.0--pl5321r42hf17093f_1"
 - "1.46.0--pl5321r43hf17093f_0"
 - "1.48.0--pl5321r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cohcap"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cohcap", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cohcap", "latest": {"1.48.0--pl5321r43hf17093f_0": "sha256:f768250c13c53736b79fa742380fddf810797a7aff1464d134426e56ab1aba16"}, "tags": {"1.40.0--pl5321r41hc247a5b_3": "sha256:19670a6ce08344aa0a468bd6ed81414dcb0e9bf130942ab7866626993f269a3b", "1.44.0--pl5321r42hc247a5b_0": "sha256:b46b84dd806fcb7247492a7146352025a8d4e859d7f2fb6e61f073e14cb047e3", "1.44.0--pl5321r42hf17093f_1": "sha256:cbb5e2a4c67ba3c2175b4dc3d762411c95ed6a072c8e3c63d8824de4c06a215a", "1.46.0--pl5321r43hf17093f_0": "sha256:7e76a5572e0ba46018a688fc3a938af7beaa29946aa0181c31246a12affb3021", "1.48.0--pl5321r43hf17093f_0": "sha256:f768250c13c53736b79fa742380fddf810797a7aff1464d134426e56ab1aba16"}, "docker": "quay.io/biocontainers/bioconductor-cohcap", "aliases": {"perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cohcap.
shpc-registry automated BioContainers addition for bioconductor-cohcap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cohcap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cohcap:1.48.0--pl5321r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cohcap/1.48.0--pl5321r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-cohcap/1.48.0--pl5321r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cohcap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cohcap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cohcap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cohcap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cohcap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cohcap-inspect-deffile:

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