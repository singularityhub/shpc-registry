---
layout: container
name:  "quay.io/biocontainers/soapec"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/soapec/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/soapec/container.yaml"
updated_at: "2024-04-30 03:09:11.270038"
latest: "2.03--hdcf5f25_8"
container_url: "https://biocontainers.pro/tools/soapec"
aliases:
 - "Corrector_AR"
 - "Corrector_HA"
 - "KmerFreq_AR"
 - "KmerFreq_HA"
versions:
 - "2.03--hd03093a_6"
 - "2.03--hdcf5f25_8"
description: "shpc-registry automated BioContainers addition for soapec"
config: {"url": "https://biocontainers.pro/tools/soapec", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for soapec", "latest": {"2.03--hdcf5f25_8": "sha256:86ece8e8d978baba633b36314e24a9e890059815225e7d1a6b3f8439a240ca08"}, "tags": {"2.03--hd03093a_6": "sha256:b7d7a98d8d124e7aa81a6090b1bdd690dfcd97c77af989622c3abe37542e9ad6", "2.03--hdcf5f25_8": "sha256:86ece8e8d978baba633b36314e24a9e890059815225e7d1a6b3f8439a240ca08"}, "docker": "quay.io/biocontainers/soapec", "aliases": {"Corrector_AR": "/usr/local/bin/Corrector_AR", "Corrector_HA": "/usr/local/bin/Corrector_HA", "KmerFreq_AR": "/usr/local/bin/KmerFreq_AR", "KmerFreq_HA": "/usr/local/bin/KmerFreq_HA"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/soapec.
shpc-registry automated BioContainers addition for soapec
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/soapec
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/soapec:2.03--hdcf5f25_8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/soapec/2.03--hdcf5f25_8
$ module help quay.io/biocontainers/soapec/2.03--hdcf5f25_8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### soapec-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### soapec-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### soapec-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### soapec-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### soapec-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### soapec-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Corrector_AR

```bash
$ singularity exec <container> /usr/local/bin/Corrector_AR
$ podman run --it --rm --entrypoint /usr/local/bin/Corrector_AR   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Corrector_AR   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Corrector_HA

```bash
$ singularity exec <container> /usr/local/bin/Corrector_HA
$ podman run --it --rm --entrypoint /usr/local/bin/Corrector_HA   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Corrector_HA   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### KmerFreq_AR

```bash
$ singularity exec <container> /usr/local/bin/KmerFreq_AR
$ podman run --it --rm --entrypoint /usr/local/bin/KmerFreq_AR   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/KmerFreq_AR   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### KmerFreq_HA

```bash
$ singularity exec <container> /usr/local/bin/KmerFreq_HA
$ podman run --it --rm --entrypoint /usr/local/bin/KmerFreq_HA   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/KmerFreq_HA   -v ${PWD} -w ${PWD} <container> -c " $@"
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