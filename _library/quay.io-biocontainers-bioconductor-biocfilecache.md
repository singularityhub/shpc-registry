---
layout: container
name:  "quay.io/biocontainers/bioconductor-biocfilecache"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-biocfilecache/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-biocfilecache/container.yaml"
updated_at: "2024-12-07 01:45:38.681258"
latest: "2.10.1--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-biocfilecache"

versions:
 - "2.2.0--r41hdfd78af_0"
 - "2.6.0--r42hdfd78af_0"
 - "2.8.0--r43hdfd78af_0"
 - "2.10.1--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-biocfilecache"
config: {"url": "https://biocontainers.pro/tools/bioconductor-biocfilecache", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-biocfilecache", "latest": {"2.10.1--r43hdfd78af_0": "sha256:6b528c0dc7d8e26fb9f2f8af2bf1b521ef9d7e177996bc9d41cd5a791b5d0ac0"}, "tags": {"2.2.0--r41hdfd78af_0": "sha256:d006b4aa631d00d582f6a6cd9a41a3b1f7e3c16fac781cfe22aa12cf251d4ca8", "2.6.0--r42hdfd78af_0": "sha256:4a0c4e3480ebb73ccdb66a15a901b55e38da1b99ebde10d9c0e1048c01aa3d97", "2.8.0--r43hdfd78af_0": "sha256:8a62f924269b0c19f028ce9e98d6ba9a831d205781489c3bf8485828028acbde", "2.10.1--r43hdfd78af_0": "sha256:6b528c0dc7d8e26fb9f2f8af2bf1b521ef9d7e177996bc9d41cd5a791b5d0ac0"}, "docker": "quay.io/biocontainers/bioconductor-biocfilecache"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-biocfilecache.
shpc-registry automated BioContainers addition for bioconductor-biocfilecache
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-biocfilecache
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-biocfilecache:2.10.1--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-biocfilecache/2.10.1--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-biocfilecache/2.10.1--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-biocfilecache-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biocfilecache-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biocfilecache-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-biocfilecache-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-biocfilecache-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-biocfilecache-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-biocfilecache

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