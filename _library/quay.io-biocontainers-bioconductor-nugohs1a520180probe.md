---
layout: container
name:  "quay.io/biocontainers/bioconductor-nugohs1a520180probe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-nugohs1a520180probe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-nugohs1a520180probe/container.yaml"
updated_at: "2024-03-05 02:44:52.046461"
latest: "3.4.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-nugohs1a520180probe"

versions:
 - "3.4.0--r41hdfd78af_9"
 - "3.4.0--r42hdfd78af_10"
 - "3.4.0--r43hdfd78af_11"
 - "3.4.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-nugohs1a520180probe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-nugohs1a520180probe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-nugohs1a520180probe", "latest": {"3.4.0--r43hdfd78af_12": "sha256:6e06a555077979d201efa1b9200e0f2643e18d1a8fea40221fd65184fca4bed5"}, "tags": {"3.4.0--r41hdfd78af_9": "sha256:4ac09f89bb885dce5dcdf59fd84f252344c192fba9bb2ee7f06566b3893aad0e", "3.4.0--r42hdfd78af_10": "sha256:d714add69f9f21d82efb3f9a2d9d41f94c003c0cc143f7fca25e0e986a99d3e1", "3.4.0--r43hdfd78af_11": "sha256:9c8854b4edeb7513b92588815eeb35b779e9dbea9fc8e2662866be90950545f3", "3.4.0--r43hdfd78af_12": "sha256:6e06a555077979d201efa1b9200e0f2643e18d1a8fea40221fd65184fca4bed5"}, "docker": "quay.io/biocontainers/bioconductor-nugohs1a520180probe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-nugohs1a520180probe.
shpc-registry automated BioContainers addition for bioconductor-nugohs1a520180probe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-nugohs1a520180probe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-nugohs1a520180probe:3.4.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-nugohs1a520180probe/3.4.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-nugohs1a520180probe/3.4.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-nugohs1a520180probe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-nugohs1a520180probe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-nugohs1a520180probe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-nugohs1a520180probe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-nugohs1a520180probe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-nugohs1a520180probe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-nugohs1a520180probe

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