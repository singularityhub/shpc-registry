---
layout: container
name:  "quay.io/biocontainers/bioconductor-mbqn"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mbqn/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mbqn/container.yaml"
updated_at: "2026-02-02 04:53:07.021486"
latest: "2.18.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mbqn"

versions:
 - "2.5.0--r41hdfd78af_0"
 - "2.10.0--r42hdfd78af_0"
 - "2.12.0--r43hdfd78af_0"
 - "2.14.0--r43hdfd78af_0"
 - "2.18.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mbqn"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mbqn", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mbqn", "latest": {"2.18.0--r44hdfd78af_0": "sha256:6afc8294bf4d536e569dc4f731b3441fc4e87883154ce5c00c73fcec48b217f0"}, "tags": {"2.5.0--r41hdfd78af_0": "sha256:d2473e5f1d979813f1d49070d05f11ef8308d8e102a2ebb2ee9318f5e728c091", "2.10.0--r42hdfd78af_0": "sha256:512ef5a81193eeab3c9be471c23be9d776dd016db34d54629bae66f867cf5e29", "2.12.0--r43hdfd78af_0": "sha256:9288787b6453aa8276fca52264817174562fc8cc233fbf51e1508e0e2147b65c", "2.14.0--r43hdfd78af_0": "sha256:da6f02237abc4cf2f9bd5a0f577d3b1696d220aff85bf80380ea3a4470ce513e", "2.18.0--r44hdfd78af_0": "sha256:6afc8294bf4d536e569dc4f731b3441fc4e87883154ce5c00c73fcec48b217f0"}, "docker": "quay.io/biocontainers/bioconductor-mbqn"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mbqn.
shpc-registry automated BioContainers addition for bioconductor-mbqn
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mbqn
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mbqn:2.18.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mbqn/2.18.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mbqn/2.18.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mbqn-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mbqn-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mbqn-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mbqn-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mbqn-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mbqn-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mbqn

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