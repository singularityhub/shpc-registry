---
layout: container
name:  "quay.io/biocontainers/sage-proteomics"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sage-proteomics/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sage-proteomics/container.yaml"
updated_at: "2025-03-14 03:44:01.126775"
latest: "0.14.7--hc1c3326_2"
container_url: "https://biocontainers.pro/tools/sage-proteomics"
aliases:
 - "sage"
versions:
 - "0.8.1--hec16e2b_0"
 - "0.9.4--hec16e2b_0"
 - "0.10.0--hec16e2b_0"
 - "0.12.0--hec16e2b_1"
 - "0.11.2--hec16e2b_0"
 - "0.13.1--h031d066_2"
 - "0.12.0--h031d066_2"
 - "0.13.3--h031d066_0"
 - "0.13.4--h031d066_0"
 - "0.14.0--h031d066_0"
 - "0.14.3--h031d066_0"
 - "0.14.4--h031d066_0"
 - "0.14.5--h031d066_0"
 - "0.14.6--h031d066_0"
 - "0.14.7--hc1c3326_2"
description: "singularity registry hpc automated addition for sage-proteomics"
config: {"url": "https://biocontainers.pro/tools/sage-proteomics", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for sage-proteomics", "latest": {"0.14.7--hc1c3326_2": "sha256:cca3d95195925ea21c62a1bdd61812248d65f841b3bb00b6cf4a1b6083fd6586"}, "tags": {"0.8.1--hec16e2b_0": "sha256:c66ead864888868623284914f811e4c4c2894a8bb7bb6d55f55bb5aae15dcf6f", "0.9.4--hec16e2b_0": "sha256:ec89353ebcdda930283732d7bf904bc5d624a2f864672ea24d467066afaa8087", "0.10.0--hec16e2b_0": "sha256:6c3566fa2397f6207eea2789c1d6b5264f31bea18653e9def0c5ae1c090c30dc", "0.12.0--hec16e2b_1": "sha256:f4aff128364a8c0c318596f1c1c3c31ab59d5b2d9088f8553362954e33c35c38", "0.11.2--hec16e2b_0": "sha256:00037d543207ec084b4e858b49607811adcb1d694b8099c62fb9df63b4159fc3", "0.13.1--h031d066_2": "sha256:a9353047698f34b19f0f5b69d279e02dde8b8da986f0b47445727a352c72af44", "0.12.0--h031d066_2": "sha256:bf70218d2aeda12c75d91f1d1e0073bb2612c83160f0c82e491da19c9cc3ae92", "0.13.3--h031d066_0": "sha256:6c51bb044ab6966ae09047f536e04017b6a9a01b0d304500de4347d3c00d0715", "0.13.4--h031d066_0": "sha256:de2181bc412001c4ec8e8565d104a3d1ea4a20efe0817d801f02f4d77adead15", "0.14.0--h031d066_0": "sha256:3d53cca352e16935def040797f19dffbe69b754d22d6639353765587f3e0e5e2", "0.14.3--h031d066_0": "sha256:d8d6e58529b71dd653fda74b3cdd0b9e39a2e6fa81cf91bc39d1654d98d8d4a2", "0.14.4--h031d066_0": "sha256:d76b6cd9e74861b7f82c46de360489adcafb71214dc953fa0be178c50eba1cdf", "0.14.5--h031d066_0": "sha256:c25316faea9193e520b68702c00ea214467e9f5205b8bce7023667b55d25d34e", "0.14.6--h031d066_0": "sha256:af71eb315c227c996437a7d1cfedbb5555aebaabdf48559830761e42aa2462a0", "0.14.7--hc1c3326_2": "sha256:cca3d95195925ea21c62a1bdd61812248d65f841b3bb00b6cf4a1b6083fd6586"}, "docker": "quay.io/biocontainers/sage-proteomics", "aliases": {"sage": "/usr/local/bin/sage"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sage-proteomics.
singularity registry hpc automated addition for sage-proteomics
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sage-proteomics
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sage-proteomics:0.14.7--hc1c3326_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sage-proteomics/0.14.7--hc1c3326_2
$ module help quay.io/biocontainers/sage-proteomics/0.14.7--hc1c3326_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sage-proteomics-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sage-proteomics-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sage-proteomics-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sage-proteomics-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sage-proteomics-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sage-proteomics-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sage

```bash
$ singularity exec <container> /usr/local/bin/sage
$ podman run --it --rm --entrypoint /usr/local/bin/sage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sage   -v ${PWD} -w ${PWD} <container> -c " $@"
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