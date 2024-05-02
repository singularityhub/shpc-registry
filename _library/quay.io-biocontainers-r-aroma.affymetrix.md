---
layout: container
name:  "quay.io/biocontainers/r-aroma.affymetrix"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-aroma.affymetrix/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-aroma.affymetrix/container.yaml"
updated_at: "2024-05-02 02:53:01.028946"
latest: "3.2.2--r43h3121a25_0"
container_url: "https://biocontainers.pro/tools/r-aroma.affymetrix"

versions:
 - "3.2.1--r41h3121a25_0"
 - "3.2.1--r42h3121a25_2"
 - "3.2.1--r43h3121a25_3"
 - "3.2.2--r43h3121a25_0"
description: "shpc-registry automated BioContainers addition for r-aroma.affymetrix"
config: {"url": "https://biocontainers.pro/tools/r-aroma.affymetrix", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-aroma.affymetrix", "latest": {"3.2.2--r43h3121a25_0": "sha256:c14775b1559f59950bffdd1664d8d124edbc36e1740a66da3092137e862d600e"}, "tags": {"3.2.1--r41h3121a25_0": "sha256:76b1894c7ec98b34149cee0aab1ab85d3ecc860d3a52624e6224c1562862d042", "3.2.1--r42h3121a25_2": "sha256:4db647fc87345805362c2f03faf6c021481bca10c9132e3dd75314caa2d45f70", "3.2.1--r43h3121a25_3": "sha256:06268d32e53d72b71f66f3efa2202559d96bf57bc44bbd81b6563aa0221ea87f", "3.2.2--r43h3121a25_0": "sha256:c14775b1559f59950bffdd1664d8d124edbc36e1740a66da3092137e862d600e"}, "docker": "quay.io/biocontainers/r-aroma.affymetrix"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-aroma.affymetrix.
shpc-registry automated BioContainers addition for r-aroma.affymetrix
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-aroma.affymetrix
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-aroma.affymetrix:3.2.2--r43h3121a25_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-aroma.affymetrix/3.2.2--r43h3121a25_0
$ module help quay.io/biocontainers/r-aroma.affymetrix/3.2.2--r43h3121a25_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-aroma.affymetrix-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-aroma.affymetrix-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-aroma.affymetrix-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-aroma.affymetrix-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-aroma.affymetrix-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-aroma.affymetrix-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-aroma.affymetrix

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