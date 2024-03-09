---
layout: container
name:  "quay.io/biocontainers/bioconductor-metacca"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-metacca/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-metacca/container.yaml"
updated_at: "2024-03-09 02:27:51.414894"
latest: "1.30.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-metacca"

versions:
 - "1.8.0--r351_0"
 - "1.26.0--r42hdfd78af_0"
 - "1.22.0--r41hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r40hdfd78af_1"
 - "1.16.0--r40_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.30.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-metacca"
config: {"url": "https://biocontainers.pro/tools/bioconductor-metacca", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-metacca", "latest": {"1.30.0--r43hdfd78af_0": "sha256:c9f4dd4459e980e33b57396f3aac5295982f2a2718334e058dd86af4a19fb22a"}, "tags": {"1.8.0--r351_0": "sha256:6273912a92ad87032f3bfd31f2c524db92abc8480e41fb81e992f46bf337f498", "1.26.0--r42hdfd78af_0": "sha256:cbe7e2a05c1f0bb663a9602630eb0aa5f7fd2a337daa56714cf8f4ae5a60f802", "1.22.0--r41hdfd78af_0": "sha256:88391b3865a6695963ddfd47f4175adf441f85bcb6381ca2c86d6af2e5da7175", "1.20.0--r41hdfd78af_0": "sha256:c956b1d216d44aa0443c5b463664791a5c1317dbc903c3b8d3415e314147db6e", "1.18.0--r40hdfd78af_1": "sha256:eff8e114ebb9e62063d8c37976d62fc0ae17f6f6565c2e2d6269af94135fea32", "1.16.0--r40_0": "sha256:51068492e0b2be4de6e4c4011b5af7033a1d50fe491910bc8588398c76a649f0", "1.28.0--r43hdfd78af_0": "sha256:1175549748408ed786d12a89e3c630d87d65f11e2b66d6e280955b889dd7600c", "1.30.0--r43hdfd78af_0": "sha256:c9f4dd4459e980e33b57396f3aac5295982f2a2718334e058dd86af4a19fb22a"}, "docker": "quay.io/biocontainers/bioconductor-metacca"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-metacca.
shpc-registry automated BioContainers addition for bioconductor-metacca
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-metacca
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-metacca:1.30.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-metacca/1.30.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-metacca/1.30.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-metacca-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-metacca-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-metacca-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-metacca-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-metacca-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-metacca-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-metacca

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