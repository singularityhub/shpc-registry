---
layout: container
name:  "quay.io/biocontainers/hmmer2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hmmer2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hmmer2/container.yaml"
updated_at: "2024-12-24 03:36:33.923170"
latest: "2.3.2--h031d066_9"
container_url: "https://biocontainers.pro/tools/hmmer2"
aliases:
 - "hmmalign2"
 - "hmmbuild2"
 - "hmmcalibrate2"
 - "hmmconvert2"
 - "hmmemit2"
 - "hmmfetch2"
 - "hmmindex2"
 - "hmmpfam2"
 - "hmmsearch2"
versions:
 - "2.3.2--hec16e2b_7"
 - "2.3.2--h031d066_9"
description: "shpc-registry automated BioContainers addition for hmmer2"
config: {"url": "https://biocontainers.pro/tools/hmmer2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for hmmer2", "latest": {"2.3.2--h031d066_9": "sha256:6569ab6291bdf274ee6e805e7a3e59b482a7db37f173c950832b45598e2e7bca"}, "tags": {"2.3.2--hec16e2b_7": "sha256:d60e6e1d1b1a464c63f6cf4f677200c1ff8cf9030ce6477214fae34ba42a56f4", "2.3.2--h031d066_9": "sha256:6569ab6291bdf274ee6e805e7a3e59b482a7db37f173c950832b45598e2e7bca"}, "docker": "quay.io/biocontainers/hmmer2", "aliases": {"hmmalign2": "/usr/local/bin/hmmalign2", "hmmbuild2": "/usr/local/bin/hmmbuild2", "hmmcalibrate2": "/usr/local/bin/hmmcalibrate2", "hmmconvert2": "/usr/local/bin/hmmconvert2", "hmmemit2": "/usr/local/bin/hmmemit2", "hmmfetch2": "/usr/local/bin/hmmfetch2", "hmmindex2": "/usr/local/bin/hmmindex2", "hmmpfam2": "/usr/local/bin/hmmpfam2", "hmmsearch2": "/usr/local/bin/hmmsearch2"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hmmer2.
shpc-registry automated BioContainers addition for hmmer2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hmmer2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hmmer2:2.3.2--h031d066_9
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hmmer2/2.3.2--h031d066_9
$ module help quay.io/biocontainers/hmmer2/2.3.2--h031d066_9
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hmmer2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hmmer2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hmmer2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hmmer2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hmmer2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hmmer2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### hmmalign2

```bash
$ singularity exec <container> /usr/local/bin/hmmalign2
$ podman run --it --rm --entrypoint /usr/local/bin/hmmalign2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmalign2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmbuild2

```bash
$ singularity exec <container> /usr/local/bin/hmmbuild2
$ podman run --it --rm --entrypoint /usr/local/bin/hmmbuild2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmbuild2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmcalibrate2

```bash
$ singularity exec <container> /usr/local/bin/hmmcalibrate2
$ podman run --it --rm --entrypoint /usr/local/bin/hmmcalibrate2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmcalibrate2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmconvert2

```bash
$ singularity exec <container> /usr/local/bin/hmmconvert2
$ podman run --it --rm --entrypoint /usr/local/bin/hmmconvert2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmconvert2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmemit2

```bash
$ singularity exec <container> /usr/local/bin/hmmemit2
$ podman run --it --rm --entrypoint /usr/local/bin/hmmemit2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmemit2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmfetch2

```bash
$ singularity exec <container> /usr/local/bin/hmmfetch2
$ podman run --it --rm --entrypoint /usr/local/bin/hmmfetch2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmfetch2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmindex2

```bash
$ singularity exec <container> /usr/local/bin/hmmindex2
$ podman run --it --rm --entrypoint /usr/local/bin/hmmindex2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmindex2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmpfam2

```bash
$ singularity exec <container> /usr/local/bin/hmmpfam2
$ podman run --it --rm --entrypoint /usr/local/bin/hmmpfam2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmpfam2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmsearch2

```bash
$ singularity exec <container> /usr/local/bin/hmmsearch2
$ podman run --it --rm --entrypoint /usr/local/bin/hmmsearch2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmsearch2   -v ${PWD} -w ${PWD} <container> -c " $@"
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