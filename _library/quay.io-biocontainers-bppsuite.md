---
layout: container
name:  "quay.io/biocontainers/bppsuite"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bppsuite/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bppsuite/container.yaml"
updated_at: "2026-08-31 08:57:02.294561"
latest: "3.0.0--hd63eeec_0"
container_url: "https://biocontainers.pro/tools/bppsuite"
aliases:
 - "bppalnscore"
 - "bppancestor"
 - "bppbranchlik"
 - "bppconsense"
 - "bppdist"
 - "bppmixedlikelihoods"
 - "bppml"
 - "bpppars"
 - "bpppopstats"
 - "bppreroot"
 - "bppseqgen"
 - "bppseqman"
 - "bpptreedraw"
versions:
 - "3.0.0--hd63eeec_0"
description: "singularity registry hpc automated addition for bppsuite"
config: {"url": "https://biocontainers.pro/tools/bppsuite", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bppsuite", "latest": {"3.0.0--hd63eeec_0": "sha256:ca18e348a3c969f5f1aeb7057af262745e97923a0ead92d4e1140fa38708b1a6"}, "tags": {"3.0.0--hd63eeec_0": "sha256:ca18e348a3c969f5f1aeb7057af262745e97923a0ead92d4e1140fa38708b1a6"}, "docker": "quay.io/biocontainers/bppsuite", "aliases": {"bppalnscore": "/usr/local/bin/bppalnscore", "bppancestor": "/usr/local/bin/bppancestor", "bppbranchlik": "/usr/local/bin/bppbranchlik", "bppconsense": "/usr/local/bin/bppconsense", "bppdist": "/usr/local/bin/bppdist", "bppmixedlikelihoods": "/usr/local/bin/bppmixedlikelihoods", "bppml": "/usr/local/bin/bppml", "bpppars": "/usr/local/bin/bpppars", "bpppopstats": "/usr/local/bin/bpppopstats", "bppreroot": "/usr/local/bin/bppreroot", "bppseqgen": "/usr/local/bin/bppseqgen", "bppseqman": "/usr/local/bin/bppseqman", "bpptreedraw": "/usr/local/bin/bpptreedraw"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bppsuite.
singularity registry hpc automated addition for bppsuite
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bppsuite
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bppsuite:3.0.0--hd63eeec_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bppsuite/3.0.0--hd63eeec_0
$ module help quay.io/biocontainers/bppsuite/3.0.0--hd63eeec_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bppsuite-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bppsuite-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bppsuite-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bppsuite-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bppsuite-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bppsuite-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bppalnscore

```bash
$ singularity exec <container> /usr/local/bin/bppalnscore
$ podman run --it --rm --entrypoint /usr/local/bin/bppalnscore   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bppalnscore   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bppancestor

```bash
$ singularity exec <container> /usr/local/bin/bppancestor
$ podman run --it --rm --entrypoint /usr/local/bin/bppancestor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bppancestor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bppbranchlik

```bash
$ singularity exec <container> /usr/local/bin/bppbranchlik
$ podman run --it --rm --entrypoint /usr/local/bin/bppbranchlik   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bppbranchlik   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bppconsense

```bash
$ singularity exec <container> /usr/local/bin/bppconsense
$ podman run --it --rm --entrypoint /usr/local/bin/bppconsense   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bppconsense   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bppdist

```bash
$ singularity exec <container> /usr/local/bin/bppdist
$ podman run --it --rm --entrypoint /usr/local/bin/bppdist   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bppdist   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bppmixedlikelihoods

```bash
$ singularity exec <container> /usr/local/bin/bppmixedlikelihoods
$ podman run --it --rm --entrypoint /usr/local/bin/bppmixedlikelihoods   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bppmixedlikelihoods   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bppml

```bash
$ singularity exec <container> /usr/local/bin/bppml
$ podman run --it --rm --entrypoint /usr/local/bin/bppml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bppml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bpppars

```bash
$ singularity exec <container> /usr/local/bin/bpppars
$ podman run --it --rm --entrypoint /usr/local/bin/bpppars   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bpppars   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bpppopstats

```bash
$ singularity exec <container> /usr/local/bin/bpppopstats
$ podman run --it --rm --entrypoint /usr/local/bin/bpppopstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bpppopstats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bppreroot

```bash
$ singularity exec <container> /usr/local/bin/bppreroot
$ podman run --it --rm --entrypoint /usr/local/bin/bppreroot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bppreroot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bppseqgen

```bash
$ singularity exec <container> /usr/local/bin/bppseqgen
$ podman run --it --rm --entrypoint /usr/local/bin/bppseqgen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bppseqgen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bppseqman

```bash
$ singularity exec <container> /usr/local/bin/bppseqman
$ podman run --it --rm --entrypoint /usr/local/bin/bppseqman   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bppseqman   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bpptreedraw

```bash
$ singularity exec <container> /usr/local/bin/bpptreedraw
$ podman run --it --rm --entrypoint /usr/local/bin/bpptreedraw   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bpptreedraw   -v ${PWD} -w ${PWD} <container> -c " $@"
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